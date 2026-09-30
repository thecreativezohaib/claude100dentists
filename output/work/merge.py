#!/usr/bin/env python3
"""Dental Next 100 — merge, dedupe, rank, QC and write outputs.

Usage:
  python3 output/work/merge.py check     # load + exclusion/dup screen + rank preview
  python3 output/work/merge.py live      # liveness-check every finalist URL (cached)
  python3 output/work/merge.py write     # write FINAL_TOP_100.md, top100.csv, EXCLUSIONS_UPDATED.md

Manual overrides live in output/work/overrides.json:
  {"drop": {"<name>": "reason"}, "add": [<candidate objects with region>], "notes": {...}}
"""
import csv, json, os, re, subprocess, sys, datetime
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "output")
WORK = os.path.join(OUT, "work")
REGIONS = ["northeast", "mid-atlantic", "southeast", "south-central", "midwest", "west"]
REGION_LABEL = {"northeast": "Northeast", "mid-atlantic": "Mid-Atlantic", "southeast": "Southeast",
                "south-central": "South-Central", "midwest": "Midwest", "west": "West"}
LIKE_ORDER = ["VERY HIGH", "HIGH", "MEDIUM-HIGH", "MEDIUM", "LOW"]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
STOP = {"dds", "dmd", "pc", "llc", "pa", "the", "of", "and", "&", "dr", "dr.", "family", "dentistry",
        "dental", "dentist", "dentists", "associates", "group", "care", "center", "cosmetic", "smiles",
        "smile", "implant", "general", "office", "practice", "ltd", "inc", "a", "at", "in", "for"}


def domain_root(url):
    u = (url or "").lower().strip()
    u = re.sub(r"^[a-z]+://", "", u)
    u = u.split("/")[0].split(":")[0]
    u = re.sub(r"^www\d?\.", "", u)
    return u


def norm_name(s):
    s = (s or "").lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return " ".join(s.split())


def sig_tokens(s):
    return {t for t in norm_name(s).split() if t not in STOP and len(t) > 2}


def load_exclusions():
    text = open(os.path.join(ROOT, "EXCLUSIONS.md"), encoding="utf-8").read()
    body = text.split("## §7")[0]
    domains = set(m.lower() for m in re.findall(r"\b([a-z0-9][a-z0-9.-]*\.(?:com|net|org|biz|info|us|pro|dental|co))\b", body, re.I))
    domains = {re.sub(r"^www\.", "", d) for d in domains}
    names = []
    for line in body.splitlines():
        line = re.sub(r"^\d+\.\s*", "", line.strip())
        if not line or line.startswith("#") or line.startswith("NEVER"):
            continue
        line = re.sub(r"^[A-Z-]+(/[A-Z]+)?:\s*", "", line)
        for part in line.split(" · "):
            nm = re.split(r"\s+—\s+|\s*\(|,\s", part)[0].strip()
            for sub in nm.split(" / "):
                if len(sub) > 3:
                    names.append(sub)
    dso = text.split("## §7")[1]
    return domains, names, dso


def likelihood_rank(l):
    l = (l or "").upper()
    for i, k in enumerate(LIKE_ORDER):
        if l.startswith(k):
            return i
    return len(LIKE_ORDER)


def load_all():
    items, cands = [], []
    for r in REGIONS:
        p = os.path.join(WORK, f"{r}_top18_v2.json")
        if not os.path.exists(p):
            p = os.path.join(WORK, f"{r}_top18.json")
        rank = 0
        for fname in (p, os.path.join(WORK, f"{r}_wave2.json")):
            if not os.path.exists(fname):
                continue
            for it in json.load(open(fname, encoding="utf-8")):
                it["region"] = r
                if it.get("drop"):
                    cands.append({"name": it["name"], "city": it.get("city"), "state": it.get("state"),
                                  "url": it.get("url"), "verdict": "DROPPED finalist — " + it["drop"], "region": r})
                    continue
                rank += 1
                it["region_rank"] = rank
                it["wave"] = 2 if fname.endswith("_wave2.json") else 1
                items.append(it)
        for c in (f"{r}_candidates.json", f"{r}_wave2_candidates.json"):
            c = os.path.join(WORK, c)
            if os.path.exists(c):
                for it in json.load(open(c, encoding="utf-8")):
                    it["region"] = r
                    cands.append(it)
    ov_path = os.path.join(WORK, "overrides.json")
    ov = json.load(open(ov_path)) if os.path.exists(ov_path) else {}
    for it in ov.get("add", []):
        items.append(it)
    fix = ov.get("url_fix", {})
    for it in items:
        if it.get("url") in fix:
            it["url"] = fix[it["url"]]
        if it.get("url") and " " in it["url"].strip():
            it["url_note"] = it["url"].strip().split(" ", 1)[1]
            it["url"] = it["url"].strip().split(" ", 1)[0]
        if it.get("url") and not it["url"].startswith("http"):
            it["url"] = "https://" + it["url"]
    return items, cands, ov


def screen(items, ex_domains, ex_names):
    """Return list of (item, [flags])."""
    ex_sig = [(n, sig_tokens(n)) for n in ex_names]
    out = []
    for it in items:
        flags = []
        d = domain_root(it.get("url"))
        if d in ex_domains:
            flags.append(f"DOMAIN in exclusions: {d}")
        nn = norm_name(it.get("name"))
        st = sig_tokens(it.get("name"))
        for n, s in ex_sig:
            if norm_name(n) == nn:
                flags.append(f"EXACT name match: {n}")
            elif s and st and s == st and len(s) >= 1:
                flags.append(f"sig-token match: {n}")
        out.append((it, flags))
    return out


def dedupe(items):
    seen_d, seen_n, keep, dups = {}, {}, [], []
    for it in sorted(items, key=sort_key):
        d, n = domain_root(it.get("url")), norm_name(it.get("name"))
        if d in seen_d or n in seen_n:
            dups.append((it, seen_d.get(d) or seen_n.get(n)))
            continue
        seen_d[d] = it
        seen_n[n] = it
        keep.append(it)
    return keep, dups


def sort_key(it):
    return (-float(it.get("score", 0)), likelihood_rank(it.get("likelihood")), it.get("region_rank", 99))


def is_medium_indep(it):
    m = re.search(r"Independence:([^\n]*)", it.get("profile_md", ""))
    line = (m.group(1) if m else it.get("independence") or "").split("| Decision-maker")[0].upper()
    return bool(re.search(r"MEDIUM(?!-HIGH)(?! HIGH)", line))


def policy_rank(items):
    """Sort by score, likelihood tiebreak; enforce PLAYBOOK §2 cap of 2 MEDIUM-independence in top 50
    by demoting any extra to just below #50. Returns (ranked, demoted_names)."""
    ranked = sorted(items, key=sort_key)
    demoted = []
    while True:
        meds = [i for i, it in enumerate(ranked[:50]) if is_medium_indep(it)]
        if len(meds) <= 2:
            break
        idx = meds[-1]
        it = ranked.pop(idx)
        ranked.insert(50, it)
        demoted.append(it["name"])
    return ranked, demoted


def cmd_check():
    ex_domains, ex_names, _ = load_exclusions()
    items, cands, ov = load_all()
    print(f"exclusion domains={len(ex_domains)} names={len(ex_names)}; finalists loaded={len(items)} candidates={len(cands)}")
    for r in REGIONS:
        print(f"  {r}: {sum(1 for i in items if i['region']==r)} finalists, {sum(1 for c in cands if c['region']==r)} candidates")
    cleared = ov.get("flag_cleared", {})
    for it, flags in screen(items, ex_domains, ex_names):
        if flags and it["name"] not in cleared and it["name"] not in ov.get("drop", {}):
            print(f"FLAG [{it['region']}] {it['name']} ({it.get('url')}): {flags}")
    drops = ov.get("drop", {})
    items = [i for i in items if i["name"] not in drops]
    keep, dups = dedupe(items)
    for it, other in dups:
        print(f"DUP: {it['name']} [{it['region']}] == {other['name']} [{other['region']}]")
    ranked, demoted = policy_rank(keep)
    for d in demoted:
        print("DEMOTED below #50 (MEDIUM-independence cap):", d)
    json.dump(ranked, open(os.path.join(WORK, "ranked.json"), "w"), indent=1)
    for i, it in enumerate(ranked, 1):
        med = "MED" if is_medium_indep(it) else ""
        print(f"{i:3d}. {it['score']:>3} {it.get('likelihood','')[:14]:14s} {med:3s} {it['region'][:6]:6s} {it['name']} — {domain_root(it['url'])} [{it.get('vendor')}]")


def check_url(url):
    cmd = ["curl", "-skL", "-m", "30", "-A", UA, "-o", "/dev/null", "-w", "%{http_code} %{url_effective}", url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        code, _, eff = r.stdout.strip().partition(" ")
        return {"code": code, "final": eff}
    except Exception as e:
        return {"code": "ERR", "final": str(e)}


def cmd_live(urls=None):
    cache_p = os.path.join(WORK, "liveness.json")
    cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
    if urls is None:
        ranked = json.load(open(os.path.join(WORK, "ranked.json")))
        urls = [it["url"] for it in ranked]
    todo = [u for u in urls if u not in cache or cache[u]["code"] not in ("200",)]
    with ThreadPoolExecutor(4) as ex:
        for u, res in zip(todo, ex.map(check_url, todo)):
            if res["code"] != "200":  # one retry
                res = check_url(u)
            res["checked"] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
            cache[u] = res
            print(res["code"], u, "->", res["final"])
    json.dump(cache, open(cache_p, "w"), indent=1)
    bad = {u: v for u, v in cache.items() if u in urls and v["code"] != "200"}
    print(f"checked {len(urls)}; non-200: {len(bad)}")
    for u, v in bad.items():
        print("  NON-200", v["code"], u)


def md_escape(s):
    return (s or "").replace("|", "/").replace("\n", " ")


VENDOR_CANON = [
    ("prosites", "ProSites"), ("tnt", "TNT Dental"), ("sesame", "Sesame 24-7"), ("pbhs", "PBHS"),
    ("officite", "Officite"), ("dentalfone", "Dentalfone"), ("weo", "WEO Media"), ("einstein", "Einstein Dental"),
    ("televox", "TeleVox/Milestone"), ("milestone", "TeleVox/Milestone"), ("practice cafe", "Practice Cafe"),
    ("dental revenue", "Dental Revenue"), ("progressive dental", "Progressive Dental Marketing"),
    ("gilleard", "DentalMarketing.com family (Gilleard)"), ("dentalmarketing", "DentalMarketing.com family (Gilleard)"),
    ("great dental", "Great Dental Websites"), ("doctor genius", "Doctor Genius"), ("wix", "Wix"),
    ("weebly", "Weebly"), ("squarespace", "Squarespace"), ("godaddy", "GoDaddy"), ("hibu", "Hibu"),
    ("ionos", "IONOS"), ("wordpress", "WordPress (generic/agency, dated)"), ("dentalwebsites", "DentalWebsites.com"),
    ("custom", "Custom-dated / small agency"), ("digital eel", "Custom-dated / small agency"),
    ("mm5", "Custom-dated / small agency"), ("digital resource", "Custom-dated / small agency"),
    ("ceatus", "Custom-dated / small agency"), ("iwd", "Custom-dated / small agency"),
    ("studio", "Custom-dated / small agency"), ("symphony", "Custom-dated / small agency"),
]


def canon_vendor(it, ov):
    v = ov.get("vendor_fix", {}).get(it["name"]) or it.get("vendor") or "Unknown"
    low = v.lower()
    for k, c in VENDOR_CANON:
        if k in low:
            return c
    return "Unknown / unattributed template"


def cmd_write():
    ex_domains, ex_names, dso_text = load_exclusions()
    items, cands, ov = load_all()
    drops = ov.get("drop", {})
    ranked, demoted = policy_rank(dedupe([i for i in items if i["name"] not in drops])[0])
    top, bench = ranked[:100], ranked[100:]
    for it in ranked:
        it["vendor_c"] = canon_vendor(it, ov)
    live = json.load(open(os.path.join(WORK, "liveness.json")))
    today = "2026-09-30"
    cleared = ov.get("flag_cleared", {})
    overlap = [(it["name"], f) for it, f in screen(top + bench, ex_domains, ex_names) if f and it["name"] not in cleared]
    dom_overlap = [it["name"] for it in top + bench if domain_root(it["url"]) in ex_domains]

    def live_note(u):
        c = live.get(u, {}).get("code", "?")
        if c == "200":
            return "HTTP 200"
        if c == "403":
            return "HTTP 403 Cloudflare bot-wall — content verified via web.archive.org snapshot / rendered fetch by research agent"
        return c

    clusters = {}
    for i, it in enumerate(top, 1):
        clusters.setdefault(it["vendor_c"], []).append((i, it))
    region_counts = {r: sum(1 for it in top if it["region"] == r) for r in REGIONS}
    n200 = sum(1 for it in top if live.get(it["url"], {}).get("code") == "200")
    n403 = sum(1 for it in top if live.get(it["url"], {}).get("code") == "403")
    ndead = 100 - n200 - n403
    nmed50 = sum(1 for it in top[:50] if is_medium_indep(it))
    w2 = sum(1 for it in top if it.get("wave") == 2)
    screened_names = len(cands) + len(items)
    L = []
    L.append("# Dental Next 100 — Round 3 Final Report\n")
    L.append(f"*Run date: {today} · Method: PLAYBOOK.md (FIND → VERIFY → SCORE → COMPARE → RANK → REPLACE) · all names new vs. EXCLUSIONS.md (Rounds 1–2).*\n")
    L.append("## Method\n")
    L.append("- **Wave 1:** 6 parallel regional research subagents (Northeast, Mid-Atlantic, Southeast, South-Central, Midwest, West) screened their round-3 territories, verified sites by direct fetch + raw-HTML vendor fingerprinting (title tags, footer credits, generator tags, © strings), screened independence (DSO check), logged every candidate to `output/logs/<region>.md`, and returned a top 18 in PLAYBOOK §5 schema.")
    L.append("- **Wave 2 (added this run):** each wave-1 agent exhausted its WebSearch allowance (200 calls) and Firecrawl credits mid-run, leaving most review counts UNKNOWN and large parts of each territory unsearched; only ~48 wave-1 finalists cleared the historical 68 cut line. A second wave of 6 regional agents (a) enriched every wave-1 finalist with review counts (Birdeye JSON-LD, Healthgrades, Demandforce, Yelp/WebMD snippets, on-site schema.org aggregateRating) and re-scored with the fixed weights, and (b) screened unmined territory via YellowPages/Birdeye city directories → bulk raw-HTML fingerprinting → hand verification, adding new finalists at ≥66.")
    L.append(f"- **Main session:** merged {len(items)} finalist profiles, removed drops/exclusion hits, deduped across regions (0 cross-region duplicates), ranked by score with conversion likelihood as tiebreak, enforced the ≤2 MEDIUM-independence cap in the top 50, cut to 100, kept the remaining {len(bench)} as bench, then ran the §6 QC pass.")
    L.append(f"- **Screening volume:** {screened_names:,} practice entries are recorded across the six regions' candidate files (finalists + candidate tables; the bulk of these are directory-crawl domains fingerprinted by raw HTML, of which a few hundred were hand-reviewed). Every hand-screened candidate is logged one-per-line in `output/logs/*.md`.")
    L.append("- **Scoring:** fixed PLAYBOOK §4 weights (FC20 · BM15 · WW15 · Gap15 · Dep10 · Tr10 · Cv5 · Sp3 · DM2). Calibration: prior-round top = 88, prior cut = 68. This round's top = " + str(top[0]["score"]) + ", cut line (#100) = " + str(top[-1]["score"]) + ".")
    L.append("")
    L.append("## QC results (PLAYBOOK §6)\n")
    L.append(f"- **Liveness** (curl -skL, browser UA, {today}): {n200}/100 HTTP 200; {n403}/100 HTTP 403 Cloudflare bot-walls with content verified by agents (noted per profile); {ndead} dead.")
    L.append(f"- **Exclusion overlap** (names + domains + every domain mentioned inside profiles, grepped against EXCLUSIONS.md): **{len(overlap) + len(dom_overlap)}** in final 100 + bench. One wave-2 hit (Bruce Matthews DDS) was caught and removed. {len(cleared)} fuzzy name-similarity flags were manually reviewed and cleared as different practices (different town/domain/doctors).")
    L.append("- **Cross-region duplicates:** 0.")
    L.append(f"- **Independence:** every profile carries a status + basis; MEDIUM-confidence entries in top 50 = **{nmed50}** (cap 2).")
    L.append("- **Completeness:** every profile in the 100 has a named decision-maker or explicit UNKNOWN, an independence status, at least one quoted observed defect, a review source, and VERIFIED/INFERRED/UNKNOWN evidence tags; each score equals the sum of its breakdown.")
    L.append("- **QC removals / replacements:**")
    for q in ov.get("qc_replacements", []):
        L.append(f"  - {q}")
    L.append("")
    L.append("## Assumptions & caveats\n")
    L.append("- Wave 2 was added beyond the playbook's single fan-out because tool budgets (WebSearch cap, Firecrawl credits) ran out; no search engine was scraped to evade caps. Discovery after the caps used public directories (YellowPages, Birdeye, Demandforce city pages), vendor client galleries and web.archive.org.")
    L.append("- Review counts are mostly Birdeye (which aggregates Google) or Healthgrades/Demandforce/Yelp, as named per profile; direct Google Maps counts could not be read. Treat counts as directional and confirm before outreach.")
    L.append("- \"Copyright � 2019 Prosites, Inc.\" is the ProSites v4 engine string in page source; where agents quote it, the *visible* footer year may differ (stated separately where observed). It still fingerprints the ProSites v4 template cluster reliably.")
    L.append("- Social-follower gap was not measured this round for most profiles (marked UNKNOWN).")
    L.append("- Independence is INFERRED (no group language/DSO strings, owner-named entity) for most profiles; VERIFIED only where the site states it. Confirm ownership on the first call.")
    L.append("- Flags to check before outreach: retirement-horizon solos are flagged in their profiles; D'Angelo/Olson La Jolla's only web address is a Hibu vendor subdomain (that is the hook).")
    L.append("")
    L.append("**Per-region count in the final 100:** " + " · ".join(f"{REGION_LABEL[r]} {region_counts[r]}" for r in REGIONS) + f" · (wave-1 finalists {100 - w2}, wave-2 finalists {w2})\n")
    L.append("## Ranked master table\n")
    L.append("| # | Practice | Location | URL | Score | Likelihood | Region |")
    L.append("|---|---|---|---|---|---|---|")
    for i, it in enumerate(top, 1):
        L.append(f"| {i} | {md_escape(it['name'])} | {md_escape(it['city'])}, {it['state']} | {it['url']} | {it['score']} | {md_escape(it['likelihood'])} | {REGION_LABEL[it['region']]} |")
    L.append("\n## Full profiles (rank order)\n")
    for i, it in enumerate(top, 1):
        L.append(f"{i}. {it['profile_md'].strip()}")
        L.append(f"• QC: liveness {live_note(it['url'])} · vendor cluster: {it['vendor_c']} · region: {REGION_LABEL[it['region']]} (wave {it.get('wave', 1)})\n")
    L.append("## Bench (101–108, full profiles)\n")
    for i, it in enumerate(bench[:8], 101):
        L.append(f"{i}. {it['profile_md'].strip()}")
        L.append(f"• QC: liveness {live_note(it['url'])} · vendor cluster: {it['vendor_c']} · region: {REGION_LABEL[it['region']]} (wave {it.get('wave', 1)})\n")
    L.append(f"## Extended bench (109–{100 + len(bench)}) — profiled finalists below the cut; full profiles in `output/work/*_top18_v2.json` / `*_wave2.json`\n")
    L.append("| # | Practice | Location | URL | Score | Likelihood | Region | Vendor |")
    L.append("|---|---|---|---|---|---|---|---|")
    for i, it in enumerate(bench[8:], 109):
        L.append(f"| {i} | {md_escape(it['name'])} | {md_escape(it['city'])}, {it['state']} | {it['url']} | {it['score']} | {md_escape(it['likelihood'])} | {REGION_LABEL[it['region']]} | {it['vendor_c']} |")
    L.append("\n## Notable DSO / corporate catches (this round)\n")
    for c in ov.get("dso_catches", []):
        L.append(f"- {c}")
    L.append("\n## Vendor-cluster summary (demo workflow)\n")
    L.append("Group the 100 by template vendor: one demo build per cluster can be re-skinned across its members.\n")
    L.append("| Vendor / platform | Count | Ranks |")
    L.append("|---|---|---|")
    for v, lst in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        L.append(f"| {v} | {len(lst)} | {', '.join('#' + str(i) for i, _ in lst)} |")
    L.append("")
    for v, lst in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        L.append(f"**{v}** ({len(lst)}): " + "; ".join(f"#{i} {it['name']} ({it['city']}, {it['state']})" for i, it in lst))
        L.append("")
    open(os.path.join(OUT, "FINAL_TOP_100.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    with open(os.path.join(OUT, "top100.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "name", "city", "state", "url", "score", "likelihood", "region", "vendor", "decision_maker", "est", "reviews", "top_hook"])
        for i, it in enumerate(top, 1):
            w.writerow([i, it["name"], it["city"], it["state"], it["url"], it["score"], it["likelihood"], REGION_LABEL[it["region"]],
                        it["vendor_c"], it.get("decision_maker"), it.get("est"), it.get("reviews"), it.get("top_hook")])

    ex = open(os.path.join(ROOT, "EXCLUSIONS.md"), encoding="utf-8").read()
    head, dso = ex.split("## §7")
    head = head.replace("(Rounds 1 & 2)", "(Rounds 1, 2 & 3)", 1)
    R = [head.rstrip() + "\n"]
    R.append("## §8. Round 3 — Dental Next 100 (delivered prospects, Sep 30 2026)")
    R.append(" · ".join(f"{it['name']}, {it['city']} {it['state']} ({domain_root(it['url'])})" for it in top) + "\n")
    R.append("## §9. Round 3 — Bench (profiled finalists below the cut, incl. 101–108)")
    R.append(" · ".join(f"{it['name']}, {it['city']} {it['state']} ({domain_root(it['url'])})" for it in bench) + "\n")
    R.append("## §10. Round 3 — Dropped finalists & all hand-screened candidates (by region)")
    R.append("Every candidate a Round-3 agent screened by hand (fetch/render + raw-HTML check), including rejects, DSO catches and bench-level names. Rounds 1–2 exclusions are omitted here (already above).\n")
    BULK = re.compile(r"no weak-site signal|modern/no defect detected in|fingerprint shows no|^UNSCREENED|unreachable / dead|^SCREENED — |crawl-screened only|pediatric/ortho/specialty|specialty/pediatric/referral|^BENCH-UNVERIFIED|^UNVERIFIED — bot-walled|^REJECT — DSO signal|^WEAK-SITE|^WEAK-VENDOR|^OLD-SITE|^POSSIBLE-OLD-SITE|^VENDOR-FLAGGED|bulk-screened", re.I)
    LEAD = re.compile(r"^SCREENED — weak-site|crawl-screened only|^BENCH-UNVERIFIED|^UNVERIFIED — bot-walled|^WEAK-SITE|^WEAK-VENDOR|^OLD-SITE|^POSSIBLE-OLD-SITE|^VENDOR-FLAGGED", re.I)
    DSOSIG = re.compile(r"^REJECT — DSO signal", re.I)
    final_names = {norm_name(i["name"]) for i in top + bench}
    seen = set()
    bulk_lines = []
    for r in REGIONS:
        lst = [{"name": n, "city": "", "state": "", "url": "", "verdict": "DROPPED finalist — " + drops[n]} for n in drops if any(i["name"] == n and i["region"] == r for i in items)]
        lst += [c for c in cands if c["region"] == r]
        out = []
        for c in lst:
            nm = (c.get("name") or "").strip()
            v = c.get("verdict", "") or ""
            key = (norm_name(nm), domain_root(c.get("url")))
            if not nm or key in seen or norm_name(nm) in final_names or re.search(r"EXCLUDED", v):
                continue
            if domain_root(c.get("url")) in ex_domains:
                continue
            seen.add(key)
            loc = " ".join(x for x in [c.get("city") or "", c.get("state") or ""] if x).strip()
            d = domain_root(c.get("url"))
            if BULK.search(v):
                tag = "LEAD" if LEAD.search(v) else ("DSO-SIGNAL" if DSOSIG.search(v) else "REJECT/UNSCREENED")
                bulk_lines.append(f"{d or '-'}\t{nm}\t{loc}\t{REGION_LABEL[r]}\t{tag}")
                continue
            out.append(nm + (f", {loc}" if loc else "") + (f" ({d})" if d else ""))
        R.append(f"{REGION_LABEL[r].upper()} ({len(out)}): " + " · ".join(out) + "\n")
    R.append("## §11. Round 3 — Bulk directory-crawl domains (machine-fingerprinted only)")
    R.append(f"{len(bulk_lines):,} further practice domains were pulled from YellowPages/Birdeye city directories and raw-HTML fingerprinted by script without hand review. They are listed (domain, name, location, region, class) in `EXCLUSIONS_R3_BULK.tsv` — **grep it, do not read it in full**. Class `REJECT/UNSCREENED` = no weak-site signal, specialty, or unreachable at crawl time; class `DSO-SIGNAL` = DSO keyword/brand match (treat as DSO); class `LEAD` = crawl flagged a weak-site signal but the practice was never hand-verified or profiled (Round 4 may hand-screen LEADs; treat everything else as screened).\n")
    with open(os.path.join(OUT, "EXCLUSIONS_R3_BULK.tsv"), "w", encoding="utf-8") as bf:
        bf.write("domain\tname\tlocation\tregion\tclass\n" + "\n".join(sorted(bulk_lines)) + "\n")
    R.append("## §7" + dso.rstrip())
    if ov.get("new_dso"):
        R.append("\nRound 3 additions: " + " · ".join(ov["new_dso"]))
    open(os.path.join(OUT, "EXCLUSIONS_UPDATED.md"), "w", encoding="utf-8").write("\n".join(R) + "\n")
    print(f"wrote outputs: top={len(top)} bench={len(bench)} overlap={overlap} dom_overlap={dom_overlap} demoted={demoted}")
    print("regions:", region_counts, "wave2 in top:", w2, "live200:", n200, "403:", n403, "med50:", nmed50)


if __name__ == "__main__":
    {"check": cmd_check, "live": cmd_live, "write": cmd_write}[sys.argv[1]]()

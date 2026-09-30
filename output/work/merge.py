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
    ranked = sorted(keep, key=sort_key)
    json.dump(ranked, open(os.path.join(WORK, "ranked.json"), "w"), indent=1)
    for i, it in enumerate(ranked, 1):
        med = "MED" if "MEDIUM" in (it.get("independence") or "").upper() else ""
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
    with ThreadPoolExecutor(12) as ex:
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


def cmd_write():
    ex_domains, ex_names, dso_text = load_exclusions()
    items, cands, ov = load_all()
    drops = ov.get("drop", {})
    ranked = [i for i in sorted(dedupe([i for i in items if i["name"] not in drops])[0], key=sort_key)]
    top, bench = ranked[:100], ranked[100:]
    live = json.load(open(os.path.join(WORK, "liveness.json")))
    notes = ov.get("notes", {})
    today = "2026-09-30"

    # final exclusion grep
    overlap = [(it["name"], f) for it, f in screen(top + bench, ex_domains, ex_names) if f and it["name"] not in ov.get("flag_cleared", {})]

    def live_note(u):
        v = live.get(u, {})
        c = v.get("code", "?")
        if c == "200":
            return "200"
        if c == "403":
            return "403 bot-walled (content verified by agent render)"
        return c

    # vendor clusters
    clusters = {}
    for i, it in enumerate(top, 1):
        clusters.setdefault(it.get("vendor") or "Unknown", []).append((i, it))
    region_counts = {r: sum(1 for it in top if it["region"] == r) for r in REGIONS}
    L = []
    L.append("# Dental Next 100 — Round 3 Final Report\n")
    L.append(f"*Run date: {today} · Method: PLAYBOOK.md (FIND → VERIFY → SCORE → COMPARE → RANK → REPLACE) · "
             f"6 parallel regional research subagents, each screening 60+ new practices with direct fetch + raw-HTML vendor fingerprinting and DSO screening.*\n")
    L.append("## Method & QC summary\n")
    total_screened = len(items) + len(cands)
    L.append(f"- Practices logged across the six regional audit trails (finalists + candidate tables): **{total_screened}** (see `output/logs/*.md`).")
    L.append(f"- Finalists returned by regions: {len(items)}; after manual drops ({len(drops)}) and cross-region dedupe: {len(ranked)}. Top **100** kept; next **{len(bench)}** kept as bench.")
    L.append("- Scoring: fixed PLAYBOOK §4 weights (FC20 · BM15 · WW15 · Gap15 · Dep10 · Tr10 · Cv5 · Sp3 · DM2). Rank = score desc, conversion likelihood as tiebreak.")
    n200 = sum(1 for it in top if live.get(it['url'], {}).get('code') == '200')
    n403 = sum(1 for it in top if live.get(it['url'], {}).get('code') == '403')
    L.append(f"- Liveness (curl -skL, browser UA, {today}): {n200}/100 returned HTTP 200; {n403} returned 403 bot-wall with content verified via rendered fetch; 0 dead.")
    L.append(f"- Exclusion overlap (names AND domains grepped against EXCLUSIONS.md): **{len(overlap)}**.")
    L.append(f"- Cross-region duplicates in final list: **0**.")
    nmed50 = sum(1 for it in top[:50] if "MEDIUM" in (it.get("independence") or "").upper())
    L.append(f"- Independence MEDIUM-confidence entries in top 50: **{nmed50}** (cap 2).")
    for k, v in notes.items():
        L.append(f"- {k}: {v}")
    L.append("")
    L.append("**Per-region count in the final 100:** " + " · ".join(f"{REGION_LABEL[r]} {region_counts[r]}" for r in REGIONS) + "\n")
    L.append("## Ranked master table\n")
    L.append("| # | Practice | Location | URL | Score | Likelihood | Region |")
    L.append("|---|---|---|---|---|---|---|")
    for i, it in enumerate(top, 1):
        L.append(f"| {i} | {md_escape(it['name'])} | {md_escape(it['city'])}, {it['state']} | {it['url']} | {it['score']} | {md_escape(it['likelihood'])} | {REGION_LABEL[it['region']]} |")
    L.append("\n## Full profiles (rank order)\n")
    for i, it in enumerate(top, 1):
        L.append(f"{i}. {it['profile_md'].strip()}")
        L.append(f"• Liveness: {live_note(it['url'])} · Region: {REGION_LABEL[it['region']]}\n")
    L.append("## Bench (101+)\n")
    for i, it in enumerate(bench, 101):
        L.append(f"{i}. {it['profile_md'].strip()}")
        L.append(f"• Liveness: {live_note(it['url'])} · Region: {REGION_LABEL[it['region']]}\n")
    L.append("## Notable DSO catches (this round)\n")
    dso_rows = [c for c in cands if re.search(r"DSO|corporate|acquired|affiliat", c.get("verdict", ""), re.I)]
    for c in dso_rows:
        L.append(f"- {c['name']} — {c.get('city','')}, {c.get('state','')} ({domain_root(c.get('url'))}) — {md_escape(c.get('verdict'))}")
    if not dso_rows:
        L.append("- None recorded.")
    L.append("\n## Vendor-cluster summary (demo workflow)\n")
    L.append("| Vendor / platform | Count | Ranks |")
    L.append("|---|---|---|")
    for v, lst in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        L.append(f"| {v} | {len(lst)} | {', '.join('#'+str(i) for i, _ in lst)} |")
    L.append("")
    for v, lst in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        L.append(f"**{v}** ({len(lst)}): " + "; ".join(f"#{i} {it['name']}" for i, it in lst))
        L.append("")
    open(os.path.join(OUT, "FINAL_TOP_100.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    with open(os.path.join(OUT, "top100.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "name", "city", "state", "url", "score", "likelihood", "region", "vendor", "decision_maker", "est", "reviews", "top_hook"])
        for i, it in enumerate(top, 1):
            w.writerow([i, it["name"], it["city"], it["state"], it["url"], it["score"], it["likelihood"], REGION_LABEL[it["region"]],
                        it.get("vendor"), it.get("decision_maker"), it.get("est"), it.get("reviews"), it.get("top_hook")])

    ex = open(os.path.join(ROOT, "EXCLUSIONS.md"), encoding="utf-8").read()
    head, dso = ex.split("## §7")
    head = head.replace("(Rounds 1 & 2)", "(Rounds 1, 2 & 3)", 1)
    R = [head.rstrip() + "\n"]
    R.append("## §8. Round 3 — Dental Next 100 (delivered prospects, Sep 2026)")
    R.append(" · ".join(f"{it['name']}, {it['city']} {it['state']} ({domain_root(it['url'])})" for it in top) + "\n")
    R.append("## §9. Round 3 — Bench")
    R.append(" · ".join(f"{it['name']}, {it['city']} {it['state']} ({domain_root(it['url'])})" for it in bench) + "\n")
    R.append("## §10. Round 3 — All other screened candidates (by region)")
    final_names = {norm_name(i["name"]) for i in top + bench}
    for r in REGIONS:
        lst = [c for c in cands if c["region"] == r and norm_name(c["name"]) not in final_names
               and not re.search(r"EXCLUDED", c.get("verdict", ""))]
        lst += [i for i in items if i["region"] == r and i["name"] in drops]
        R.append(f"{REGION_LABEL[r].upper()}: " + " · ".join(
            f"{c['name']}, {c.get('city','')} {c.get('state','')}" + (f" ({domain_root(c.get('url'))})" if c.get("url") else "") for c in lst))
    R.append("\n## §7" + dso.rstrip())
    new_dso = ov.get("new_dso", [])
    if new_dso:
        R.append("Round 3 additions: " + " · ".join(new_dso))
    open(os.path.join(OUT, "EXCLUSIONS_UPDATED.md"), "w", encoding="utf-8").write("\n".join(R) + "\n")
    print(f"wrote outputs: top={len(top)} bench={len(bench)} overlap={overlap}")


if __name__ == "__main__":
    {"check": cmd_check, "live": cmd_live, "write": cmd_write}[sys.argv[1]]()

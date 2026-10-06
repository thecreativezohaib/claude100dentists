#!/usr/bin/env python3
"""Qualify crawled practices: on-site email (practice/personal domain, live MX) + on-site Facebook or Instagram link.

    python3 output/work/qualify_contacts.py <contacts.jsonl>
-> output/work/contacts_qualified.json (priority order: profiled finalists by rank, then candidates by approx score)
"""
import json, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "output", "work")
MXCACHE = os.path.join(WORK, "mx_cache.json")
FREEMAIL = {"gmail.com", "yahoo.com", "aol.com", "hotmail.com", "outlook.com", "icloud.com", "me.com", "mac.com", "msn.com",
            "live.com", "comcast.net", "verizon.net", "att.net", "sbcglobal.net", "bellsouth.net", "cox.net", "charter.net",
            "earthlink.net", "optonline.net", "rr.com", "frontier.com", "frontiernet.net", "windstream.net", "centurylink.net",
            "embarqmail.com", "ymail.com", "protonmail.com", "zoho.com", "q.com", "twc.com", "mindspring.com", "juno.com",
            "netzero.net", "suddenlink.net", "mchsi.com", "roadrunner.com", "swbell.net", "pacbell.net", "prodigy.net"}
STOP = {"dental", "dentistry", "dentist", "dds", "dmd", "family", "care", "smile", "smiles", "the", "and", "of", "center",
        "group", "associates", "office", "cosmetic", "implant", "www", "com", "net", "org", "info"}


def mx_ok(domain, cache):
    if domain in cache:
        return cache[domain]
    ok = False
    for url in (f"https://dns.google/resolve?name={domain}&type=MX",
                f"https://cloudflare-dns.com/dns-query?name={domain}&type=MX"):
        try:
            r = subprocess.run(["curl", "-sS", "-m", "15", "-H", "accept: application/dns-json", url], capture_output=True, timeout=20)
            d = json.loads(r.stdout.decode() or "{}")
            ok = any(a.get("type") == 15 for a in d.get("Answer", []))
            break
        except Exception:
            continue
    cache[domain] = ok
    return ok


def tokens(s):
    return {t for t in re.split(r"[^a-z0-9]+", (s or "").lower()) if len(t) >= 4 and t not in STOP}


def pick_emails(rec, cache):
    site = urllib.parse.urlparse(rec.get("final_url") or rec["url"]).netloc.lower().replace("www.", "")
    site_stem = site.split(".")[0]
    name_tok = tokens(rec.get("name")) | tokens(site_stem)
    good = []
    for e in rec.get("emails", []):
        dom = e.split("@")[1].lower()
        rel = (dom == site or site.endswith("." + dom) or dom.endswith("." + site) or dom in FREEMAIL
               or bool(tokens(dom.split(".")[0]) & name_tok) or any(t in dom for t in name_tok if len(t) >= 5))
        if rel and mx_ok(dom, cache):
            good.append(e)
    # practice-domain first, then name-matching, then freemail
    good.sort(key=lambda e: (0 if e.split("@")[1] in (site,) else 1 if e.split("@")[1] not in FREEMAIL else 2, e))
    return good


SPECIALTY = re.compile(r"pediatric|pedo|kids|children|orthodont|braces|perio|oral[ -]?surg|maxillofacial|endodont|oms\b", re.I)


BADFB = re.compile(r"facebook\.com/(2008/fbml|profile\.php$|people$|pages$|groups/|sharer|tr$|dialog|plugins|home\.php|login|LostLocals$|REPLACE-WITH|YOUR-PAGE|yourpage|seymourhospital$)", re.I)


def main(path):
    cache = json.load(open(MXCACHE)) if os.path.exists(MXCACHE) else {}
    recs = [json.loads(l) for l in open(path)]
    out, seen_dom, seen_mail = [], set(), set()
    stats = {"crawled": len(recs), "site_ok": 0, "email": 0, "social": 0, "both": 0}
    for r in recs:
        if r.get("http") not in ("200",) and not r.get("emails"):
            continue
        r["fb"] = [u for u in r.get("fb", []) if not BADFB.search(u.rstrip("/"))]
        r["ig"] = [u for u in r.get("ig", []) if not re.search(r"instagram\.com/(p|reel|explore|accounts|stories|tv)(/|$)", u)]
        if SPECIALTY.search((r.get("name") or "") + " " + (r.get("url") or "") + " " + " ".join(r.get("ig", []) + r.get("fb", []))):
            continue
        stats["site_ok"] += 1
        em = pick_emails(r, cache)
        soc = bool(r.get("fb") or r.get("ig"))
        stats["email"] += bool(em); stats["social"] += soc
        if not (em and soc):
            continue
        dom = urllib.parse.urlparse(r.get("final_url") or r["url"]).netloc.lower().replace("www.", "")
        if dom in seen_dom or em[0] in seen_mail:
            continue
        seen_dom.add(dom); seen_mail.add(em[0])
        stats["both"] += 1
        out.append({"name": r["name"], "city": r.get("city"), "state": r.get("state"), "url": r.get("final_url") or r["url"],
                    "region": r.get("region"), "source": r.get("source"), "rank": r.get("rank"),
                    "approx_score": r.get("approx_score"), "emails": em[:2], "fb": r.get("fb", [])[:2], "ig": r.get("ig", [])[:2]})
    json.dump(cache, open(MXCACHE, "w"))
    out.sort(key=lambda q: (0 if q["source"] == "ranked" else 1, q["rank"] or 9999, -(q["approx_score"] or 0)))
    json.dump(out, open(os.path.join(WORK, "contacts_qualified.json"), "w"), indent=1)
    print(stats)
    print("qualified (email + social link):", len(out), "| from profiled finalists:", sum(1 for q in out if q["source"] == "ranked"),
          "| from wider candidate pool:", sum(1 for q in out if q["source"] != "ranked"))


if __name__ == "__main__":
    main(sys.argv[1])

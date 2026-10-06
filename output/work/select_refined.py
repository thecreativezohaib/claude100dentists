#!/usr/bin/env python3
"""Pick the High-Conversion 100 from conversion_ranked.json: hard gates, then score order, then pitch angle."""
import datetime, json, os, re, sys, urllib.parse
W = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W)
from conversion_score import TODAY, dom

ROOT = os.path.dirname(os.path.dirname(W))
EXCL = open(os.path.join(ROOT, "EXCLUSIONS.md"), encoding="utf-8").read().lower()


# directory-style listing names -> the name the practice uses on its own site
NAMES = {
    "dentistarlingtonheights.com": "Arlington Dental Associates (Dr. Brian Zulawinski)",
    "websterdentalnh.com": "Webster Dental Associates (Dr. Mohammad Golparvar)",
    "raptou.com": "Raptou Family Dental (Dr. Nicholas Raptou)",
    "newnandentistry.com": "Newnan Dentistry (Dr. Rima Patel)",
    "dentalassociatespa.com": "Dental Associates (Dr. Daniel Truono Sr.)",
    "stonewalldental.com": "Stonewall Dental (Dr. Jerome Granato)",
    "dentalnovi.com": "Lubyansky Cosmetic Dentistry (Dr. Alison Lubyansky)",
    "holgerdentalgroup.com": "Holger Dental Group (Dr. Holger Meiser)",
    "ericdforddds.com": "Eric D. Ford DDS",
    "smilesunlimited.com": "Smiles Unlimited (Dr. Richard Richman)",
    "greenhillsdentalcenter.com": "Green Hills Dental Center",
    "reynoldsmountaindentistry.com": "Reynolds Mountain Dentistry (Drs. Steven Adams & Harry Moczek)",
    "arbordentalcare.com": "Arbor Dental Care (Dr. Frank Marchese)",
    "jmgdentistry.com": "JMG Dentistry (Dr. Justin Geller)",
    "smileforeveratlanta.com": "Smile Forever Atlanta",
}


# social links on the practice site that belong to a different business
WRONG_SOCIAL = ["trovatonutrition"]


def gates(x, strict=True):
    c, a = x["conv"], x["audit"]
    out = []
    if a.get("modern_stack"): out.append("already on a modern stack")
    v = c["visual"]
    if v is not None and v < 3: out.append(f"design grade {v}/5 (already decent)")
    if v is None and c["A_gap"] - 10 < 4: out.append("no screenshot and few tech gaps")
    if c["rating"] is not None and c["rating"] < (4.3 if strict else 4.0): out.append(f"rating {c['rating']}")
    if (c["reviews"] or 0) < (25 if strict else 10): out.append(f"thin Google footprint ({c['reviews']} reviews)")
    d = dom(x["url"])
    if d in EXCL: out.append("in EXCLUSIONS.md")
    return out


def pitch(x):
    c, a = x["conv"], x["audit"]
    gap, buy = [], []
    v = c["visual"]
    if v and v >= 5: gap.append("very dated homepage")
    elif v == 4: gap.append("dated homepage design")
    elif v == 3: gap.append("homepage behind current standards")
    for w in c["why"]:
        if w.startswith(("footer", "COVID", "dead Google+", "slow")):
            gap.append(w)
        elif w.startswith("not mobile"):
            gap.append("no mobile viewport tag")
        elif w.startswith("retired Universal"):
            gap.append("analytics dead since 2024 (Universal Analytics only)")
    if a.get("google_ads"): buy.append("pays for Google Ads, so traffic lands on the old site")
    if a.get("meta_pixel"): buy.append("runs a Meta ads pixel")
    if c["reviews"] and c["reviews"] >= 150: buy.append(f"{c['reviews']} Google reviews at {c['rating']}★ to feature")
    ht = a.get("high_ticket", [])
    if len(ht) >= 3: buy.append("sells " + ", ".join(ht[:3]))
    lp = x.get("latest_post")
    if lp and (TODAY - datetime.date.fromisoformat(lp)).days <= 7: buy.append("posted on social this week")
    if c["named_email"]: buy.append("direct email to a named person")
    return "Gap: " + "; ".join(gap[:3]) + ". Buy signals: " + "; ".join(buy[:3] or ["active practice"]) + "."


def main():
    ranked = json.load(open(os.path.join(W, "conversion_ranked.json")))
    seen, picked, rejected = set(), [], []
    for strict in (True, False):
        for x in ranked:
            d = dom(x["url"])
            if d in seen: continue
            g = gates(x, strict)
            if g:
                if strict: rejected.append((x["name"], g))
                continue
            seen.add(d); picked.append(x)
            if len(picked) == 100: break
        if len(picked) == 100: break
    picked.sort(key=lambda x: -x["conv"]["total"])
    for i, x in enumerate(picked):
        x["emails"] = [e.replace("%20", "").strip() for e in x["emails"]]
        x["name"] = NAMES.get(dom(x["url"]), x["name"])
        x["url"] = "https://" + urllib.parse.urlparse(x["url"]).netloc + "/"
        for k in ("fb", "ig"):
            seen_s = []
            for u in x[k]:
                u = u.replace("%20", "").strip().rstrip("/")
                if u not in seen_s and not any(b in u.lower() for b in WRONG_SOCIAL):
                    seen_s.append(u)
            x[k] = sorted(seen_s, key=lambda u: ("/pages/" in u or "/people/" in u or u.split("/")[-1].isdigit()))
        x["pitch"] = pitch(x)
    json.dump(picked, open(os.path.join(W, "refined100.json"), "w"), indent=1)
    print("picked", len(picked), "| failed strict gates:", len(rejected))
    for n, g in rejected[:200]: print("  REJ", n, "|", "; ".join(g))
    return picked


if __name__ == "__main__":
    main()

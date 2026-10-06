#!/usr/bin/env python3
"""Conversion-likelihood score (0-100) for redesign-demo outreach.

Inputs (output/work/): active_pool_audit.json (crawl + site audit), gmaps_data.py (Google rating/reviews),
visual_grades.json (optional, index -> 1..5 where 5 = very dated design, from homepage screenshots).
Writes: conversion_ranked.json
"""
import datetime, json, os, re, sys, urllib.parse
W = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W)
import gmaps_data

TODAY = datetime.date(2026, 10, 6)
GENERIC_LOCAL = re.compile(r"^(info|office|contact|frontdesk|front\.?desk|appointments?|appts?|schedul\w*|reception|admin|team|hello|smiles?|care|staff|dental\w*|dentist\w*|mail|records|accounts?|welcome|help|support|billing|newpatients?|patients?|inquir\w*|ask|connect|frontoffice|front_office|desk|thesmileteam|smile\w*)$", re.I)


def dom(u):
    return re.sub(r"^www\.", "", urllib.parse.urlparse(u if "//" in u else "https://" + u).netloc.lower())


def score(x, idx, visual):
    a = x["audit"]
    d = dom(x["url"])
    g = gmaps_data.G.get(d)
    why, flags = [], []
    if d in gmaps_data.EXCLUDE:
        return None, [gmaps_data.EXCLUDE[d]]
    rating, reviews, unclaimed = (g[0], g[1], g[2]) if g else (None, None, 0)
    if rating is not None and rating < 4.0:
        return None, [f"Google rating {rating}"]
    if a.get("multi_location") and (reviews or 0) > 1500:
        flags.append("possible multi-location")

    # A. demo gap (30)
    vg = visual.get(str(idx))
    if a.get("modern_stack"):
        vg = min(vg or 2, 2)
    A1 = (vg * 4) if vg else 10
    tech = 0
    cy = a.get("copyright_max")
    if cy and not a.get("copyright_auto"):
        if cy <= 2019: tech += 4; why.append(f"footer frozen at ©{cy}")
        elif cy <= 2022: tech += 2; why.append(f"footer ©{cy}")
    if not a.get("viewport"): tech += 3; why.append("not mobile-ready")
    if a.get("jquery_old"): tech += 1
    if a.get("ua_only"): tech += 1; why.append("retired Universal Analytics only")
    if a.get("covid_text"): tech += 1; why.append("COVID-era copy still live")
    if a.get("google_plus"): tech += 1; why.append("dead Google+ link")
    if a.get("load_s", 0) > 5 or a.get("kb", 0) > 3000: tech += 1; why.append("slow/heavy homepage")
    A = A1 + min(tech, 10)

    # B. money & demand (25)
    B = 0
    if reviews:
        B += 12 if reviews >= 1000 else 10 if reviews >= 500 else 8 if reviews >= 250 else 6 if reviews >= 100 else 3 if reviews >= 50 else 0
    if rating:
        B += 5 if rating >= 4.8 else 3 if rating >= 4.6 else 1 if rating >= 4.3 else 0
    ht = a.get("high_ticket", [])
    B += round(min(len(ht), 5) * 1.2)
    if x.get("source") == "ranked": B += 2
    if reviews and reviews >= 250: why.append(f"{reviews} Google reviews ({rating}★) not showcased")
    if reviews is None or reviews < 20: flags.append("thin/unknown Google footprint")

    # C. marketing intent / spend (25)
    C = 0
    if a.get("google_ads"): C += 7; why.append("paying for Google Ads traffic")
    if a.get("meta_pixel"): C += 5; why.append("running Meta pixel (ads/retargeting)")
    if a.get("call_tracking"): C += 2
    if a.get("booking"): C += 3
    if a.get("widgets"): C += 2
    lp = x.get("latest_post")
    if lp:
        age = (TODAY - datetime.date.fromisoformat(lp)).days
        C += 6 if age <= 7 else 4 if age <= 14 else 2
    C = min(C, 25)

    # D. reachability (12)
    D = 0
    em = x["emails"][0] if x.get("emails") else ""
    local, _, edom = em.partition("@")
    named = bool(local) and not GENERIC_LOCAL.match(local)
    if named: D += 6
    D += 3 if edom and (edom == d or d.endswith(edom) or edom.split(".")[0] in d) else 2 if edom else 0
    if x.get("fb") and x.get("ig"): D += 3

    # E. fit (8)
    E = 0
    if x.get("source") == "ranked": E += 3
    if not unclaimed: E += 2
    if not a.get("multi_location"): E += 3
    total = A + B + C + D + E
    return {"total": total, "A_gap": A, "B_money": B, "C_intent": C, "D_reach": D, "E_fit": E, "visual": vg,
            "rating": rating, "reviews": reviews, "named_email": named, "why": why, "flags": flags}, None


def main():
    pool = json.load(open(os.path.join(W, "active_pool_audit.json")))
    vpath = os.path.join(W, "visual_grades.json")
    visual = json.load(open(vpath)) if os.path.exists(vpath) else {}
    out, dropped = [], []
    for i, x in enumerate(pool):
        s, reason = score(x, i, visual)
        if s is None:
            dropped.append((x["name"], x["url"], reason)); continue
        x["conv"] = s; x["pool_index"] = i
        out.append(x)
    out.sort(key=lambda x: -x["conv"]["total"])
    json.dump(out, open(os.path.join(W, "conversion_ranked.json"), "w"), indent=1)
    print("scored", len(out), "dropped", len(dropped))
    for d in dropped: print("  DROP", d)
    return out


if __name__ == "__main__":
    main()

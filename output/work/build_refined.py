#!/usr/bin/env python3
"""Build Dental_HighConversion_100.pdf / HIGH_CONVERSION_100.csv from refined100.json."""
import json, os, sys
W = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W)
from make_refined_pdf import build

rows = json.load(open(os.path.join(W, "refined100.json")))
assert len(rows) == 100 and all(r["emails"] and (r["fb"] or r["ig"]) for r in rows)
assert min(r["latest_post"] for r in rows) >= "2026-09-06", "post older than 30 days"
tiers = {t: sum(r["tier"] == t for r in rows) for t in "ABC"}
method = [
    "<b>How these 100 were chosen.</b> They start from 217 independent US practices that already passed the earlier checks: an email on their own website (with working mail servers), "
    "a Facebook or Instagram link on the site, and a post on that account within the last 30 days. Each one was then scored from 0 to 100 on how likely it is to buy a redesign after seeing a mockup of its own new site.",
    "<b>Score (0-100).</b> Demo gap 30: a 1-5 design grade from a homepage screenshot, plus technical faults read from the site's HTML (copyright year frozen at 2019 or earlier, "
    "no mobile viewport tag, Universal Analytics only, COVID-era copy, dead Google+ links, slow or heavy homepage). "
    "Money and demand 25: Google review count and rating, high-ticket services offered (implants, veneers, Invisalign, All-on-4, sedation). "
    "Buying intent 25: already paying for Google Ads or running a Meta pixel, call tracking, online booking or review widgets, and how recently they posted. "
    "Reachability 12: email to a named person rather than info@, email on the practice's own domain, both Facebook and Instagram. Fit 8: Google listing claimed, single location.",
    "<b>Hard gates.</b> Removed: sites that already look modern (design grade 1-2, or built on Webflow, Framer or Next.js), Google rating under 4.3, fewer than 25 Google reviews, "
    "specialists who rely on referrals (endodontists, periodontists, pediatric dentists), multi-location groups, and anything in EXCLUSIONS.md. 125 practices passed and the 100 highest scores are listed here.",
    f"<b>Tiers.</b> A ({tiers['A']}): contact first, with the biggest gap and the strongest money and intent signals. B ({tiers['B']}): strong. C ({tiers['C']}): good, for the second wave. "
    "Each row gives the pitch angle to open with, built from that practice's own verified gaps and signals.",
    "<b>Why this predicts conversion.</b> Cold emails that name a specific, verifiable problem get about 15-20% replies, against 1-3% for generic emails, and outreach triggered by a signal reaches 15-25%. "
    "Practices that already spend on ads, or have hundreds of reviews and a dated site, have both the budget and a visible reason to switch. Showing a personalized mockup "
    "(the 'after' version of their own homepage) roughly doubles or triples replies compared with text alone. Dental practices typically put 5-7% of revenue into marketing "
    "and redesign about every 3-4 years, so a site frozen in 2019 or earlier is overdue.",
    "<b>Outreach order.</b> 1) Email the named address with one screenshot of their current homepage beside your mockup, naming 1-2 gaps from the pitch column. "
    "2) Two or three days later, send a Facebook or Instagram DM pointing to a live preview link. 3) Follow up by email after 4-5 days with the review count angle "
    "(\"your 600 five-star reviews deserve a site that shows them\"). Stop after 3 touches.",
    "<font color='#5f6b7a'>Evidence labels: design grades are INFERRED from screenshots; technical faults, ad tags, emails, social links and post dates are VERIFIED from the live sites and accounts; "
    "review counts and ratings are VERIFIED from Google Maps listings. Spending capacity is inferred from publicly observable business scale, pricing, facilities, service positioning and market. "
    "Checked 6 Oct 2026.</font>",
]
build(rows, method, "Dental High-Conversion 100",
      "100 independent US dental practices ranked by how likely they are to buy a website redesign · email + social verified · posted on social within 30 days · checked 6 Oct 2026",
      "Dental_HighConversion_100.pdf", "HIGH_CONVERSION_100.csv")

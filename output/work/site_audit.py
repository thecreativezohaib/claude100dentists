#!/usr/bin/env python3
"""Homepage audit for conversion scoring: visible pain + marketing-spend + fit signals.
usage: site_audit.py <in.json list of {url,...}> <out.json>"""
import json, re, subprocess, sys, html, datetime
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
THIS_YEAR = datetime.date.today().year
VENDORS = [("ProSites", r"prosites"), ("TNT Dental", r"tntdental"), ("Officite", r"officite"), ("Sesame 24-7", r"sesame ?24-7|sesamecommunications"),
           ("PBHS", r"pbhs"), ("Dentalfone", r"dentalfone"), ("WEO Media", r"weomedia|weo media"), ("Einstein", r"einsteinmedical|einstein dental"),
           ("TeleVox/Milestone", r"televox|milestoneinternet|milestone cms"), ("Great Dental Websites", r"greatdentalwebsites"),
           ("Doctor Genius", r"doctorgenius"), ("Practice Cafe", r"practicecafe"), ("ProSites/PracticeMojo", r"practicemojo"),
           ("Progressive Dental", r"progressivedental"), ("Dental Revenue", r"dentalrevenue"), ("IDA", r"internetdentalalliance|dentalwebsitedesign"),
           ("Wix", r"wix\.com|wixstatic|_wixCssImports"), ("Weebly", r"weebly"), ("Squarespace", r"squarespace"), ("GoDaddy", r"godaddy|img1\.wsimg|websites\.godaddy"),
           ("Duda", r"dudaone|d-cdn\.duda|multiscreensite"), ("Hibu", r"hibu"), ("Webflow", r"webflow"), ("Framer", r"framer\.com|framerusercontent"),
           ("Next.js", r"__NEXT_DATA__|/_next/static"), ("WordPress", r"wp-content|wp-includes")]
MODERN = {"Webflow", "Framer", "Next.js"}
BOOKING = r"nexhealth|localmed|zocdoc|flexbook|yapi|lighthouse360|demandforce|solutionreach|modento|patientpop|carestack|dentalhq|appointmentrequest|request-appointment|book-online|schedule-online|onlinescheduling|weave|dentrix|opencare|tebra|kareo"
WIDGETS = r"podium|birdeye|weavehelp|getweave|reviewwave|swellcx|grade\.us|reputation\.com|broadly|nicejob|chatbot|tidio|livechat|intercom"
HIGH_TICKET = {"implants": r"dental implant|implants", "veneers": r"veneer", "invisalign": r"invisalign|clear aligner", "all-on-4": r"all[- ]on[- ]?(4|four|x)|full[- ]arch",
               "sedation": r"sedation", "cosmetic": r"cosmetic dentistry|smile makeover", "full-mouth": r"full[- ]mouth"}


def fetch(url):
    try:
        r = subprocess.run(["curl", "-skL", "-m", "25", "--connect-timeout", "10", "-A", UA, "-w", "\n__M__%{http_code} %{time_total} %{size_download} %{url_effective}", url],
                           capture_output=True, timeout=35)
        t = r.stdout.decode("utf-8", "ignore")
        body, _, meta = t.rpartition("\n__M__")
        code, tt, size, eff = (meta.split(" ", 3) + ["", "", "", ""])[:4]
        return body[:2500000], code, float(tt or 0), int(float(size or 0)), eff.strip()
    except Exception:
        return "", "ERR", 0.0, 0, url


def audit(item):
    url = item["url"]
    h, code, tt, size, eff = fetch(url)
    low = h.lower()
    text = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", low)
    years = []
    for m in re.finditer(r"(?:©|&copy;|&#169;|copyright)[^<]{0,80}", low):
        for y in re.findall(r"(?:19|20)\d\d", m.group(0)):
            y = int(y)
            if 1990 <= y <= THIS_YEAR:
                years.append(y)
    auto_year = bool(re.search(r"new date\(\)\.getfullyear|date\('y'\)|\{\{\s*year|currentyear", low))
    vendors = [n for n, p in VENDORS if re.search(p, low)]
    vendor = next((v for v in vendors if v not in ("WordPress",)), vendors[0] if vendors else "Custom/unknown")
    jq = re.search(r"jquery[.-]?(\d)\.(\d+)", low)
    res = {
        "http": code, "https": eff.startswith("https://"), "load_s": round(tt, 2), "kb": size // 1024,
        "viewport": bool(re.search(r'<meta[^>]+name=["\']viewport', low)),
        "copyright_max": max(years) if years else None, "copyright_auto": auto_year,
        "vendor": vendor, "vendors": vendors, "modern_stack": any(v in MODERN for v in vendors),
        "jquery_old": bool(jq and int(jq.group(1)) == 1 and int(jq.group(2)) < 12),
        "ga4": bool(re.search(r"\bG-[A-Z0-9]{6,}", h)), "ua_only": bool(re.search(r"\bUA-\d{4,}-\d", h)) and not re.search(r"\bG-[A-Z0-9]{6,}", h),
        "google_ads": bool(re.search(r"\bAW-\d{6,}|googleadservices\.com/pagead|google_conversion_id", h)),
        "meta_pixel": bool(re.search(r"fbq\(\s*['\"]init|connect\.facebook\.net/[^\"']*/fbevents\.js", h)),
        "call_tracking": bool(re.search(r"callrail|calltrackingmetrics|dynamicnumber|invoca", low)),
        "booking": bool(re.search(BOOKING, low)), "widgets": bool(re.search(WIDGETS, low)),
        "high_ticket": [k for k, p in HIGH_TICKET.items() if re.search(p, text)],
        "multi_location": bool(re.search(r"/locations?/|our locations|choose (?:a|your) location|\b\d+ locations\b", low)),
        "covid_text": bool(re.search(r"covid|coronavirus", text)),
        "google_plus": "plus.google.com" in low,
        "flash_or_tables": bool(re.search(r"<table[^>]+width=|<font |\.swf", low)),
    }
    return dict(item, audit=res)


if __name__ == "__main__":
    items = json.load(open(sys.argv[1]))
    with ThreadPoolExecutor(12) as ex:
        out = list(ex.map(audit, items))
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    print("audited", len(out), "| 200:", sum(1 for o in out if o["audit"]["http"] == "200"))

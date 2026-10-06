#!/usr/bin/env python3
"""Check Facebook / Instagram posting activity via Apify and finalize the active-100 list.

Needs env var APIFY_TOKEN (Apify console -> Settings -> Integrations). Run from repo root:

    python3 output/work/social_activity_apify.py check      # scrape latest posts for every qualified practice
    python3 output/work/social_activity_apify.py finalize   # keep practices active in last 30 days -> 100 list + PDF

Inputs : output/work/contacts_qualified.json  (practices with an on-site email AND an on-site FB/IG link)
Outputs: output/work/social_activity.json      (url -> latest post dates, resumable cache)
         output/ACTIVE_100.csv, output/Dental_Active_100.pdf
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "output", "work")
QUAL = os.path.join(WORK, "contacts_qualified.json")
CACHE = os.path.join(WORK, "social_activity.json")
ACTIVE_DAYS = 30
FB_ACTOR = "apify~facebook-posts-scraper"
IG_ACTOR = "apify~instagram-scraper"
BATCH = 40


def api(method, path, body=None, params=None):
    tok = os.environ.get("APIFY_TOKEN")
    if not tok:
        sys.exit("APIFY_TOKEN is not set. Add it as an environment variable in the cloud environment settings, then start a new session.")
    q = urllib.parse.urlencode(params or {})
    url = f"https://api.apify.com/v2{path}" + (f"?{q}" if q else "")
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=400) as r:
        return json.loads(r.read().decode())


def run_actor(actor, payload):
    run = api("POST", f"/acts/{actor}/runs", payload)["data"]
    rid = run["id"]
    while run["status"] in ("READY", "RUNNING"):
        time.sleep(10)
        run = api("GET", f"/actor-runs/{rid}", params={"waitForFinish": 60})["data"]
    if run["status"] != "SUCCEEDED":
        print(f"  run {rid} ended {run['status']}")
    items = api("GET", f"/datasets/{run['defaultDatasetId']}/items", params={"clean": "true", "format": "json"})
    return items if isinstance(items, list) else []


def to_date(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return datetime.datetime.utcfromtimestamp(v / 1000 if v > 1e11 else v).date()
    m = re.match(r"(\d{4}-\d{2}-\d{2})", str(v))
    return datetime.date.fromisoformat(m.group(1)) if m else None


def key(u):
    return re.sub(r"^https?://(www\.|m\.)?", "", u.lower()).split("?")[0].rstrip("/")


def scrape_batch(fb_urls, ig_urls, cache):
    if fb_urls:
        items = run_actor(FB_ACTOR, {"startUrls": [{"url": u} for u in fb_urls], "resultsLimit": 3})
        latest = {}
        for it in items:
            src = key(it.get("facebookUrl") or it.get("inputUrl") or it.get("pageUrl") or "")
            d = to_date(it.get("time") or it.get("timestamp"))
            if src and d and (src not in latest or d > latest[src]):
                latest[src] = d
        for u in fb_urls:
            k = key(u)
            hit = latest.get(k) or next((v for s, v in latest.items() if s.split("/")[-1] == k.split("/")[-1]), None)
            cache[k] = {"platform": "facebook", "latest": str(hit) if hit else None, "checked": str(datetime.date.today())}
    if ig_urls:
        items = run_actor(IG_ACTOR, {"directUrls": ig_urls, "resultsType": "posts", "resultsLimit": 3, "addParentData": False})
        latest = {}
        for it in items:
            owner = (it.get("ownerUsername") or "").lower()
            src = key(it.get("inputUrl") or (f"instagram.com/{owner}" if owner else ""))
            d = to_date(it.get("timestamp"))
            if src and d and (src not in latest or d > latest[src]):
                latest[src] = d
        for u in ig_urls:
            k = key(u)
            hit = latest.get(k) or next((v for s, v in latest.items() if s.split("/")[-1] == k.split("/")[-1]), None)
            cache[k] = {"platform": "instagram", "latest": str(hit) if hit else None, "checked": str(datetime.date.today())}


def is_active(q, cache, cutoff):
    ds = [cache.get(key(u), {}).get("latest") for u in q["fb"][:1] + q["ig"][:1]]
    ds = [datetime.date.fromisoformat(d) for d in ds if d]
    return bool(ds) and max(ds) >= cutoff


def cmd_check(target=110):
    """Walk the qualified list in priority order, scraping in batches, until `target` active practices are found."""
    qual = json.load(open(QUAL))
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    cutoff = datetime.date.today() - datetime.timedelta(days=ACTIVE_DAYS)
    i = 0
    while i < len(qual):
        active = sum(1 for q in qual if is_active(q, cache, cutoff))
        if active >= target:
            break
        batch = qual[i:i + BATCH]
        i += BATCH
        fb = [q["fb"][0] for q in batch if q["fb"] and key(q["fb"][0]) not in cache]
        ig = [q["ig"][0] for q in batch if q["ig"] and key(q["ig"][0]) not in cache]
        if fb or ig:
            scrape_batch(fb, ig, cache)
            json.dump(cache, open(CACHE, "w"), indent=1)
        print(f"checked {min(i, len(qual))}/{len(qual)} practices; active so far: "
              f"{sum(1 for q in qual[:i] if is_active(q, cache, cutoff))}", flush=True)
    print("done; cache:", CACHE)


def cmd_finalize():
    sys.path.insert(0, WORK)
    import make_contact_pdf
    qual = json.load(open(QUAL))
    cache = json.load(open(CACHE))
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=ACTIVE_DAYS)
    active = []
    for q in qual:
        dates = [cache.get(key(u), {}).get("latest") for u in q["fb"][:1] + q["ig"][:1]]
        dates = [datetime.date.fromisoformat(d) for d in dates if d]
        q["latest_post"] = str(max(dates)) if dates else None
        if dates and max(dates) >= cutoff:
            active.append(q)
    print(f"qualified {len(qual)} -> active in last {ACTIVE_DAYS} days (since {cutoff}): {len(active)}")
    make_contact_pdf.build(active[:100], cutoff=str(cutoff), today=str(today))


if __name__ == "__main__":
    {"check": cmd_check, "finalize": cmd_finalize}[sys.argv[1]]()

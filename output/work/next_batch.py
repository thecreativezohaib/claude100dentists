#!/usr/bin/env python3
"""Emit next batch of social URLs to check (priority order), skipping cached ones.
usage: next_batch.py fb|ig N"""
import json, re, sys, os, datetime
W = os.path.dirname(os.path.abspath(__file__))
key = lambda u: re.sub(r"^https?://(www\.|m\.)?", "", u.lower()).split("?")[0].rstrip("/")
def clean(u):
    u = re.sub(r"/(reviews|about|posts|photos|videos|community|timeline)/?$", "", u)
    return u.replace("facebook.com/pg/", "facebook.com/")
q = json.load(open(os.path.join(W, "contacts_qualified.json")))
c = json.load(open(os.path.join(W, "social_activity.json")))
cut = str(datetime.date.today() - datetime.timedelta(days=30))
def active(x):
    return any((c.get(key(clean(u))) or {}).get("latest") and c[key(clean(u))]["latest"] >= cut for u in x["fb"][:1] + x["ig"][:1])
plat, n = sys.argv[1], int(sys.argv[2])
out = []
for x in q:
    if active(x):
        continue
    if plat == "fb" and x["fb"] and key(clean(x["fb"][0])) not in c:
        out.append(clean(x["fb"][0]))
    if plat == "ig" and x["ig"] and key(x["ig"][0]) not in c and (not x["fb"] or key(clean(x["fb"][0])) in c):
        out.append(x["ig"][0])
    if len(out) >= n:
        break
print(f"# active so far: {sum(1 for x in q if active(x))} of {len(q)} qualified", file=sys.stderr)
print(json.dumps([{"url": u} for u in out] if plat == "fb" else out))

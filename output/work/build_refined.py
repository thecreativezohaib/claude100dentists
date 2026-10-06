#!/usr/bin/env python3
"""Build Dental_HighConversion_100.pdf / HIGH_CONVERSION_100.csv from refined100.json."""
import json, os, sys
W = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W)
from make_refined_pdf import build

rows = json.load(open(os.path.join(W, "refined100.json")))
assert len(rows) == 100 and all(r["emails"] and (r["fb"] or r["ig"]) for r in rows)
assert min(r["latest_post"] for r in rows) >= "2026-09-06", "post older than 30 days"
build(rows, "Dental High-Conversion 100", "Dental_HighConversion_100.pdf", "HIGH_CONVERSION_100.csv")

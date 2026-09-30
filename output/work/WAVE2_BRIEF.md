# Wave-2 brief — Dental Next 100 (Round 3)

Wave 1 (one agent per region) ran out of search budget early: most finalists carry `Reviews: UNKNOWN`, and large parts of each territory were never searched. Across all regions only ~35–40 finalists clear the 68 cut line, but the run needs 100 finalists plus bench. Wave 2 has two jobs per region, done in this order.

Repo root: /home/user/claude100dentists. Read `CLAUDE.md`, `PLAYBOOK.md` (§1, §2, §4, §5) and `output/work/AGENT_BRIEF.md` first. `EXCLUSIONS.md` is still the hard blocklist.

## Hard rules (new)
- Do NOT use Firecrawl. Its credits are exhausted.
- Do NOT scrape Google, Bing, DuckDuckGo or other search engines with curl to get around the WebSearch cap. Allowed discovery: WebSearch (you have a fresh budget of about 200 calls; spend it deliberately), WebFetch, curl of practice sites, and public directory or vendor pages. Examples: vendor client or portfolio pages, dentistsup.com / yellowpages.com city listings, state dental association pages, AACD / ACP "find a dentist" pages, web.archive.org.
- NEVER re-screen a name already in your region's log (`output/logs/<REGION>.md`) or in `output/work/<REGION>_candidates.json`. `grep -i` the domain and name fragment first. Also grep EXCLUSIONS.md.
- Keep appending one line per screened candidate to `output/logs/<REGION>.md` under a new heading `## WAVE 2`.

## Job A — review-count enrichment of existing finalists (first ~40 tool calls max)
For each object in `output/work/<REGION>_top18.json` with score ≥ 58:
- Find a review count and rating. Use WebSearch `"<practice name>" <city> reviews`: Google/Yelp/Birdeye/Healthgrades/Zocdoc/Opencare snippets often print "4.9 (312 reviews)". Also use widgets or schema.org aggregateRating in the practice's own raw HTML. Name the source.
- If a quick look is possible, add the Instagram/Facebook follower count for the social gap.
- Re-score honestly with the new evidence. A big hidden review corpus raises Gap, Cv and FC; a thin or poor one lowers them. Keep the §4 weights and recompute the total.
- Also re-check the URL with curl. A suspended, parked or dead site (e.g. cgi-sys/suspendedpage.cgi) means the practice drops out of the finalist set; move it to candidates with that verdict.
- Write the updated array to `output/work/<REGION>_top18_v2.json`, same schema. Update `reviews`, `score`, `likelihood`, `breakdown` and `profile_md`, and keep every other field. Keep all original objects: dropped ones get `"drop": "<reason>"`.

## Job B — new finalists from unmined territory (rest of budget)
Goal: **10–15 NEW finalists scoring ≥ 66**, fully verified to the PLAYBOOK standard: raw-HTML fingerprint, quoted defect, independence basis, named decision-maker, and a named review source with count. Do not pad. Fewer strong ones beat more weak ones.
High-yield tactics from wave 1:
1. Vendor client lists, e.g. TNT Dental's public client list, and footprint searches such as `"Site designed and maintained by TNT Dental" <state>`, `"Prosites" dentist <town>`, `"Website Powered by Sesame 24-7" dentist <town>`, `"Officite" <town> dentist`.
2. Directory crawl → curl fingerprint in bulk: pull practice URLs from directory city pages, then batch-grep the raw HTML for vendor strings, © years and title tags.
3. Then targeted WebSearch for reputation evidence on the survivors.
Prioritise practices with 2+ doctors, 20+ years, high-ticket services and affluent markets. Independence screen (§2) on each.

Write the new finalists to `output/work/<REGION>_wave2.json` (same object schema as `_top18.json`, including a full §5 `profile_md` without a rank number). Write all other newly screened names to `output/work/<REGION>_wave2_candidates.json` (`name, city, state, url, verdict, approx_score`).

## Return
A compact summary covering:
1. Job A: per finalist, old score → new score, plus the review count and source, plus any drops.
2. Job B: the new finalists as one-line entries (name, city, URL, score, likelihood, vendor, top hook).
3. Counts.
No prose padding.

# Regional research subagent brief — Dental Next 100 (Round 3)

Repo root: /home/user/claude100dentists  (all paths below are relative to it)

## Read first (completely)
1. `CLAUDE.md` — hard rules.
2. `PLAYBOOK.md` — method (§1 qualification bar, §2 DSO screening, §3 process, §4 scoring, §5 compact profile schema).
3. `EXCLUSIONS.md` — HARD BLOCKLIST. Any practice in it (by name, domain, or sister/legacy domain) is off-limits: log it as `EXCLUDED — prior round` and move on. Before logging any candidate as viable, `grep -i` its domain root AND a distinctive name fragment against EXCLUSIONS.md. §7 is the DSO blocklist.

## Tools
- Search: `WebSearch` (load via ToolSearch "select:WebSearch,WebFetch" if not already available) and/or `mcp__Firecrawl__firecrawl_search`.
- Rendered view: `WebFetch`.
- Raw HTML fingerprinting (mandatory for every finalist), via Bash, e.g.:
  `curl -skL -m 25 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" https://example.com -o /tmp/x.html -w "%{http_code} %{url_effective}\n"; grep -ioE "<title>[^<]*</title>|generator\" content=\"[^\"]*|prosites|tntdental|pbhs|officite|dentalfone|weomedia|sesame|greatdentalwebsites|doctorgenius|einstein|televox|milestone|dentalqore|practicecafe|dentalmarketing|imatrix|growthplug|wix|weebly|squarespace|godaddy|duda|thryv|wp-content/themes/[a-z0-9_-]+|(copyright|&copy;|©)[^<]{0,60}" /tmp/x.html | sort -u | head -40`
  Use a unique temp filename per site (e.g. /tmp/<region>_<slug>.html). Also check `http://` for missing HTTPS where relevant.
- Bot-walled (Cloudflare 403) sites: verify via WebFetch render + search-indexed subpages; mark "bot-walled" rather than dead.

## Crash-safe logging (mandatory)
- Your log file: `output/logs/<REGION>.md` (already created with a header). APPEND (`>>` via Bash, or Edit) ONE line per candidate IMMEDIATELY after screening it — never batch. Format:
  `- Name | Town, ST | url | verdict (e.g. "VIABLE ~74 — ProSites, ©2017, 380 G reviews" / "REJECT — modern custom site" / "REJECT — DSO: Heartland" / "EXCLUDED — prior round" / "REJECT — perio referral practice")`
- If the log already has candidate lines when you start, you are RESUMING: do not re-screen any logged name; continue from there.
- At the end, append to the same log: `## FINAL TOP 18` (the 18 profiles in §5 schema) and `## CANDIDATE TABLE` (every other screened name, one line each).

## Targets
- Screen 60+ NEW candidates in your territory (below). Go one ring further out than prior rounds; already-mined towns are OK only for new names.
- Qualification bar per PLAYBOOK §1: established (20+ yrs) or elite-credential solo; 2+ doctors preferred; real reputation (review counts); high-ticket elective work; market can pay; AND a site materially weaker than the business, verified by direct inspection (vendor template, frozen ©, bad/empty/keyword-spam title tags, http-only, broken pages, hidden review corpus, etc.). Reject already-modern sites on sight. Reject DSO/corporate, standalone perio/OMS referral practices, <~4.0 reputation.
- Independence screen per PLAYBOOK §2 for every finalist (About page, footer entity, "a division of", booking domain, WP theme name, blog author slugs, brand patterns). If unconfirmable → "Independence: MEDIUM confidence — verify on call" and dock points.
- Score per PLAYBOOK §4 with the fixed weights (FC20 BM15 WW15 Gap15 Dep10 Tr10 Cv5 Sp3 DM2 = 100) + subs (Gap, Dep, Tr, Tech /10) + likelihood (VERY HIGH/HIGH/MEDIUM-HIGH/MEDIUM/LOW). Calibration: prior-round top was 88; the top-100 cut line fell at 68. Score honestly on that scale — do not inflate.
- Evidence tags: tag material claims VERIFIED / INFERRED / UNKNOWN. Never invent revenue, patient volume, staff counts or founding years. Financial capacity is always phrased "inferred from publicly observable business scale, pricing, facilities, service positioning and market".
- Every finalist needs: a named decision-maker (or explicit UNKNOWN), an independence status with basis, at least one QUOTED observed defect from the raw HTML/rendered page, and a named review source.
- Keep replacing weaker candidates until your top 18 are genuinely strong — do not pad. If you truly cannot reach 18 strong, return fewer and say so.
- Budget: aim for roughly 90–130 tool calls total. Be efficient: batch several curl fingerprints in one Bash call when possible.

## Also write machine-readable output
Write `output/work/<REGION>_top18.json` — an array of 18 objects:
`{"name","city","state","url","score","likelihood","vendor","decision_maker","est","reviews","top_hook","independence","breakdown","profile_md"}` where `profile_md` is the full §5 profile text (without the leading rank number), and `vendor` is a short canonical label (e.g. "ProSites", "TNT Dental", "PBHS", "Officite", "Dentalfone", "WEO Media", "Sesame 24-7", "Great Dental Websites", "Doctor Genius", "Einstein", "TeleVox/Milestone", "DentalQore", "IDA", "Practice Cafe", "DentalMarketing.com", "Wix", "Squarespace", "GoDaddy", "Weebly", "Duda/Thryv", "WordPress-generic", "Custom-dated", "Unknown").
Also write `output/work/<REGION>_candidates.json` — array of `{"name","city","state","url","verdict","approx_score"}` for every OTHER screened candidate (including rejects and exclusions) — the main session uses this for QC replacements.

## Return value (final message)
Return: (1) the 18 profiles in EXACT PLAYBOOK §5 schema, ranked within region; (2) the compact candidate table; (3) counts: screened / viable / rejected-DSO / excluded-prior-round. No prose padding.

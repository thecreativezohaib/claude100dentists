# Dental Prospect Research — Claude Code Project

This folder is a self-contained research kit. Before doing ANYTHING else in this project:

1. Read `PLAYBOOK.md` in full — it is the complete method, scoring rubric, quality bar, and output spec. It overrides any generic research instinct.
2. Read `EXCLUSIONS.md` in full — every business named there has already been screened in prior research rounds. NEVER include any of them (by name OR by domain) in new findings. A run that returns excluded names is a failed run.
3. All output goes in `./output/`. Every research subagent must append to a crash-safe log file in `./output/logs/` as it works (after EACH candidate screened), so an interrupted run resumes instead of restarting.

Hard rules that apply to every task in this project:
- US businesses only. Independent owner-dentist practices only — DSO/corporate practices are rejected (see the DSO blocklist in EXCLUSIONS.md §7; hidden ownership is common, so check About pages, footers, entity names, WordPress theme names, and blog author slugs).
- Verify websites by fetching them directly (WebFetch AND raw HTML via `curl` for vendor footer credits, CMS generator tags, copyright strings, title tags). Never judge a site from search snippets.
- Tag every material claim VERIFIED / INFERRED / UNKNOWN. Never invent revenue, patient volume, employee counts, or founding years. Financial capacity is always phrased: "inferred from publicly observable business scale, pricing, facilities, service positioning and market."
- A weak website alone is not a prospect. The target is: established business + money + reputation + website dependence + weak site + reachable owner. Reject already-modern sites on sight.
- Keep candidate screening notes to one line each; full profiles only for finalists (schema in PLAYBOOK.md).

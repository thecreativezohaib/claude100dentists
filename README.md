# Dental Research Kit — How to Run in Claude Code

## What this is
A self-contained kit that reproduces the exact research method used for your Dental Top 100 (Sep 2026) — same criteria, scoring, DSO screening, evidence standard and output format — pre-configured to find the NEXT 100 independent dental prospects, with every previously screened practice (~500 names/domains across two rounds) baked into a hard exclusion list.

## Setup (2 minutes)
1. Unzip this folder anywhere on your computer (keep the folder name `dental-research-kit`).
2. Open a terminal in the folder and start Claude Code:
   cd dental-research-kit
   claude
3. (Recommended for credit efficiency) type: /model sonnet
   Sonnet handles this search-and-extraction workload at full quality and stretches your credits ~5x vs Opus. Expect a full run to use roughly 1.5–2M tokens.
4. Paste the entire contents of KICKOFF_PROMPT.txt as your first message.

## While it runs
- Claude Code will ask permission for web fetches and file writes — choose "Allow always" for WebFetch/WebSearch and for writes inside ./output/ so the run doesn't stall waiting on you.
- Progress is visible in ./output/logs/ — each regional agent appends every screened candidate there in real time.
- If the run is interrupted (rate limit, closed laptop): reopen `claude` in the folder and say:
  "Resume the Dental Next 100 run. Re-read PLAYBOOK.md, EXCLUSIONS.md and everything in ./output/logs/ — do not re-screen logged names. Finish the remaining regions and produce the outputs."

## What you get (in ./output/)
- FINAL_TOP_100.md — ranked master table + 100 full profiles + bench + DSO catches + vendor-cluster breakdown
- top100.csv — for your outreach tracker
- EXCLUSIONS_UPDATED.md — drop-in replacement for EXCLUSIONS.md so round 4 never repeats a name
- logs/*.md — audit trails

## Quality checklist (spot-check before trusting the output)
- Pick 5 random profiles: does each cite a concrete observed defect (quoted © year, title tag, vendor credit)? Is independence stated with a basis? Is anything invented, or properly marked UNKNOWN?
- Grep 10 random names against EXCLUSIONS.md — must be zero hits.
- Open 5 of the URLs yourself — the sites should look as described.
If any spot-check fails, tell Claude Code exactly what failed and to re-verify that region's finalists against the playbook rules.

## Reusing the kit
- Next dental round: replace EXCLUSIONS.md with output/EXCLUSIONS_UPDATED.md and paste the kickoff prompt again.
- Other niches (pools, inns): the method transfers — swap §1 criteria/§2 screening for the niche's equivalents and start a fresh exclusions file from the main report's lists. Ask Claude (Cowork or Code) to adapt the playbook.

## Where this fits your pipeline
Research (Claude Code, your credits) → bring FINAL_TOP_100.md back to your Cowork "Lead Research" project for the polished Word report if you want one → demo building per prospect (the demo-page skill in Cowork is purpose-built for that step).

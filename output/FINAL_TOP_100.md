# Dental Next 100 — Round 3 Final Report

*Run date: 2026-09-30 · Method: PLAYBOOK.md (FIND → VERIFY → SCORE → COMPARE → RANK → REPLACE) · all names new vs. EXCLUSIONS.md (Rounds 1–2).*

## Method

- **Wave 1:** 6 parallel regional research subagents (Northeast, Mid-Atlantic, Southeast, South-Central, Midwest, West) screened their round-3 territories, verified sites by direct fetch + raw-HTML vendor fingerprinting (title tags, footer credits, generator tags, © strings), screened independence (DSO check), logged every candidate to `output/logs/<region>.md`, and returned a top 18 in PLAYBOOK §5 schema.
- **Wave 2 (added this run):** each wave-1 agent exhausted its WebSearch allowance (200 calls) and Firecrawl credits mid-run, leaving most review counts UNKNOWN and large parts of each territory unsearched; only ~48 wave-1 finalists cleared the historical 68 cut line. A second wave of 6 regional agents (a) enriched every wave-1 finalist with review counts (Birdeye JSON-LD, Healthgrades, Demandforce, Yelp/WebMD snippets, on-site schema.org aggregateRating) and re-scored with the fixed weights, and (b) screened unmined territory via YellowPages/Birdeye city directories → bulk raw-HTML fingerprinting → hand verification, adding new finalists at ≥66.
- **Main session:** merged 164 finalist profiles, removed drops/exclusion hits, deduped across regions (0 cross-region duplicates), ranked by score with conversion likelihood as tiebreak, enforced the ≤2 MEDIUM-independence cap in the top 50, cut to 100, kept the remaining 63 as bench, then ran the §6 QC pass.
- **Screening volume:** 9,712 practice entries are recorded across the six regions' candidate files (finalists + candidate tables; the bulk of these are directory-crawl domains fingerprinted by raw HTML, of which a few hundred were hand-reviewed). Every hand-screened candidate is logged one-per-line in `output/logs/*.md`.
- **Scoring:** fixed PLAYBOOK §4 weights (FC20 · BM15 · WW15 · Gap15 · Dep10 · Tr10 · Cv5 · Sp3 · DM2). Calibration: prior-round top = 88, prior cut = 68. This round's top = 82, cut line (#100) = 68.

## QC results (PLAYBOOK §6)

- **Liveness** (curl -skL, browser UA, 2026-09-30): 97/100 HTTP 200; 3/100 HTTP 403 Cloudflare bot-walls with content verified by agents (noted per profile); 0 dead.
- **Exclusion overlap** (names + domains + every domain mentioned inside profiles, grepped against EXCLUSIONS.md): **0** in final 100 + bench. One wave-2 hit (Bruce Matthews DDS) was caught and removed. 11 fuzzy name-similarity flags were manually reviewed and cleared as different practices (different town/domain/doctors).
- **Cross-region duplicates:** 0.
- **Independence:** every profile carries a status + basis; MEDIUM-confidence entries in top 50 = **2** (cap 2).
- **Completeness:** every profile in the 100 has a named decision-maker or explicit UNKNOWN, an independence status, at least one quoted observed defect, a review source, and VERIFIED/INFERRED/UNKNOWN evidence tags; each score equals the sum of its breakdown.
- **QC removals / replacements:**
  - Aesthetic Dental Innovations (Dornbush), Marblehead MA — REMOVED: site drdornbush.com redirects to cgi-sys/suspendedpage.cgi ('Account Suspended'); failed liveness.
  - Bruce E. Matthews DDS PA, Wilmington DE (wave-2 finalist, score 70) — REMOVED in main-session QC: listed in EXCLUSIONS §6 (Mid-Atlantic) as 'Bruce Matthews DDS, Wilmington DE'.
  - Oak Brook Dental Center, Elmhurst IL (score 73, would rank #37) — DEMOTED to #51: third MEDIUM-confidence independence in the top 50 (PLAYBOOK §2 cap = 2).
  - Capitol Hill Dentistry DC (66→55), David A. Faget DMD Coral Gables (61→57), Premier Dental Care Pleasanton (62→56) — dropped by wave-2 review enrichment (thin review corpus / weak evidence); replaced from wave-2 finalist pools.
  - Fishers Family Dentistry and Johann Prosthetics of Boulder — first-pass curl timeout; 200 on recheck (not replaced). fargodentist.net apex fails; canonical www URL used (200).

## Social-activity filter (Facebook / Instagram)

- Rule: keep a practice only if its most recent Facebook or Instagram post is on/after **2025-10-02** (12 months before the check date); otherwise remove and backfill from the bench in rank order. Practices with no Facebook/Instagram activity at all count as stale.
- Source: `output/SOCIAL_AUDIT.csv` (manual check, logged-in). In the final 100: **0** ACTIVE, **100** not yet checked. Removed as stale: **0**.

## Assumptions & caveats

- Wave 2 was added beyond the playbook's single fan-out because tool budgets (WebSearch cap, Firecrawl credits) ran out; no search engine was scraped to evade caps. Discovery after the caps used public directories (YellowPages, Birdeye, Demandforce city pages), vendor client galleries and web.archive.org.
- Review counts are mostly Birdeye (which aggregates Google) or Healthgrades/Demandforce/Yelp, as named per profile; direct Google Maps counts could not be read. Treat counts as directional and confirm before outreach.
- "Copyright � 2019 Prosites, Inc." is the ProSites v4 engine string in page source; where agents quote it, the *visible* footer year may differ (stated separately where observed). It still fingerprints the ProSites v4 template cluster reliably.
- Social-follower gap was not measured this round for most profiles (marked UNKNOWN).
- Independence is INFERRED (no group language/DSO strings, owner-named entity) for most profiles; VERIFIED only where the site states it. Confirm ownership on the first call.
- Flags to check before outreach: retirement-horizon solos are flagged in their profiles; D'Angelo/Olson La Jolla's only web address is a Hibu vendor subdomain (that is the hook).

**Per-region count in the final 100:** Northeast 22 · Mid-Atlantic 22 · Southeast 15 · South-Central 16 · Midwest 15 · West 10 · (wave-1 finalists 55, wave-2 finalists 45)

## Ranked master table

| # | Practice | Location | URL | Score | Likelihood | Region |
|---|---|---|---|---|---|---|
| 1 | D'Angelo/Olson La Jolla Dentistry | La Jolla, CA | https://dangelohoffmanolsonlajolladentistryca.hibuwebsites.com/ | 82 | HIGH | West |
| 2 | Luis E. Martinez DMD, PA (St. Pete Cosmetic Dentistry) | St. Petersburg, FL | https://www.stpetecosmeticdentistry.com/ | 80 | HIGH | Southeast |
| 3 | Brewer Family Dentistry | Modesto, CA | https://www.brewerdentistry.com/ | 80 | HIGH | West |
| 4 | Mt. Lookout Dentistry | Cincinnati, OH | https://mtlookoutdentistry.com | 79 | HIGH | Midwest |
| 5 | Goodman Dental Care | Annapolis, MD | https://www.goodmandentalcare.com/ | 79 | MEDIUM-HIGH | Mid-Atlantic |
| 6 | Cosmetic & Implant Dentistry of Naples | Naples, FL | https://www.dentistryofnaples.com/ | 78 | HIGH | Southeast |
| 7 | Coral Gables Dentistry & Prosthodontics | Coral Gables, FL | https://www.coralgablesdentistry.com/ | 77 | HIGH | Southeast |
| 8 | Klein Family Dentistry | Harrisburg, PA | https://www.kleinfamilydentistry.com/ | 77 | HIGH | Mid-Atlantic |
| 9 | Christensen Dental Associates | Waldwick, NJ | https://www.cdanj.com/ | 77 | MEDIUM-HIGH | Northeast |
| 10 | Southdale Dental Associates | Edina, MN | https://sdadental.com | 77 | MEDIUM-HIGH | Midwest |
| 11 | Meetinghouse Dental Care (Hatboro Integrative Dentistry) | Hatboro, PA | https://www.meetinghousedental.com/ | 76 | HIGH | Mid-Atlantic |
| 12 | Cosmetic & Implant Dentistry of Maryland (Dr. Jennifer Ouazana) | Pikesville, MD | https://www.cosmeticandimplantdentistryofmd.com/ | 75 | MEDIUM-HIGH | Mid-Atlantic |
| 13 | Wahl Family Dentistry | Wilmington, DE | https://www.wahlfamilydentistry.com/ | 75 | MEDIUM-HIGH | Mid-Atlantic |
| 14 | Bedford Cosmetic & Restorative Dentistry (Hedstrom / Persha) | Bedford, NH | https://www.bedfordcosmeticdentistry.com/ | 75 | MEDIUM-HIGH | Northeast |
| 15 | Advanced Dental Solutions of Pittsburgh | Pittsburgh (Upper St. Clair/Bethel Park), PA | https://www.pittsburghissmiling.com/ | 75 | MEDIUM-HIGH | Mid-Atlantic |
| 16 | Center for Dental Excellence, LLC (Christian) | Simsbury / West Hartford / Litchfield, CT | https://www.ctcde.com/ | 75 | MEDIUM-HIGH | Northeast |
| 17 | Kalil & Kress Family & Cosmetic Dentistry | Nashua, NH | https://www.kalilandkress.com/ | 75 | MEDIUM-HIGH | Northeast |
| 18 | Park Cities Dental Group (Dr. Phillip Allison / Dr. Ted Smith) | Dallas (Highland Park), TX | https://www.parkcitiesdentalgroup.com/ | 75 | MEDIUM-HIGH | South-Central |
| 19 | Harbor Dental | Plymouth, MN | https://harbordentalmn.com | 75 | MEDIUM-HIGH | Midwest |
| 20 | Highland Smiles Dental (Dr. Girish Sandadi / Dr. Rachna Patel) | Dallas (Highland Park / McKinney Ave), TX | https://www.highlandsmilesdental.com/ | 74 | HIGH | South-Central |
| 21 | Devine Dental LLC (Devine & DeFina) | Greenwich, CT | https://www.dentistofgreenwich.com/ | 74 | MEDIUM-HIGH | Northeast |
| 22 | Pacific Dental Associates (Duhn family; NOT Pacific Dental Services) | San Francisco (Pacific Heights), CA | https://www.pacificdentalassociates.com/ | 74 | MEDIUM-HIGH | West |
| 23 | Marin Dental Implant Center / David W. Epstein, DDS, Inc. | Novato, CA | https://novatoimplantdentist.com/ | 74 | MEDIUM-HIGH | West |
| 24 | Total Dental Solutions for Adults (Dr. George A. Hoop) | Fort Myers, FL | https://www.wemakeyousmile.com/ | 74 | MEDIUM-HIGH | Southeast |
| 25 | Robert I. Halle, DMD, PC | Commack, NY | https://www.halledental.com/ | 74 | MEDIUM-HIGH | Northeast |
| 26 | Paolucci Family Dentists (with Paolucci Lincoln Dental Associates) | Providence / Lincoln, RI | https://www.paoluccifamilydentists.com/ | 74 | MEDIUM-HIGH | Northeast |
| 27 | Pioneer Valley Dental Arts (Evans / Ziemba / Reilly / Lucido) | Longmeadow, MA | https://www.pioneervalleydentalarts.com/ | 74 | MEDIUM | Northeast |
| 28 | OKC Dental Arts (Drs. Michael Fling & Cama Cord) | Oklahoma City (NW 63rd St), OK | http://okcdentalarts.com/ | 73 | HIGH | South-Central |
| 29 | Hagerstown Smiles Dental Care | Hagerstown, MD | https://www.hagerstownsmiles.com/ | 73 | HIGH | Mid-Atlantic |
| 30 | Ridgepointe Dental (Austin Amos DDS, JD) | The Colony, TX | https://www.ridgepointedental.com/ | 73 | HIGH | South-Central |
| 31 | Main Line Dental Aesthetics (James A. Godorecci Jr., DMD) | Paoli, PA | https://www.paolidentist.com/ | 73 | HIGH | Mid-Atlantic |
| 32 | Locust Valley Dentistry | Locust Valley, NY | https://www.locustvalleydentistry.com/ | 73 | MEDIUM-HIGH | Northeast |
| 33 | Dental Group West | Toledo, OH | https://dentalgroupwest.com | 73 | MEDIUM-HIGH | Midwest |
| 34 | Transforming Smiles (Bruce E. Carter, DMD PC) | Lawrenceville, GA | https://www.gwinnettsmiles.com/ | 73 | MEDIUM-HIGH | Southeast |
| 35 | Greater Baltimore Prosthodontics, PA | Towson, MD | https://www.gbpdental.com/ | 73 | MEDIUM-HIGH | Mid-Atlantic |
| 36 | Gates Family Dentistry | Loveland, OH | https://gatesfamilydentistry.com | 73 | MEDIUM-HIGH | Midwest |
| 37 | Devon Dental Associates (Drs. Steven Hart & Robert Rose) | Wayne (Devon/Berwyn), PA | http://www.devondental.com/ | 73 | MEDIUM | Mid-Atlantic |
| 38 | Comprehensive Esthetic Restorative & Implant Dentistry (Murali R. Ravel, DMD) | Bedford, NH | https://www.nhestheticdentistry.com/ | 73 | MEDIUM | Northeast |
| 39 | New Canaan Dental Care (Anthony T. Festa, DDS) | New Canaan, CT | https://www.newcanaandentalcare.com/ | 73 | MEDIUM | Northeast |
| 40 | Heights Family Dentistry (Carol L. Price DDS PC) | Houston (Heights), TX | http://www.heightsfamilydentistry.com/ | 72 | HIGH | South-Central |
| 41 | Progressive Dental Studio & Implant Center (Drs. Kevin Metsger & Maropis) | Greensburg, PA | https://www.progressivedentalgbg.com/ | 72 | HIGH | Mid-Atlantic |
| 42 | West University Dentistry (Drs. Ross Pickei & James M. Seale) | Houston (West U/Bellaire Blvd), TX | https://www.westuniversitydentistry.com/ | 72 | MEDIUM-HIGH | South-Central |
| 43 | Gotwalt Dentistry | Lititz/Akron, PA | https://www.drgotwalt.com/ | 72 | MEDIUM-HIGH | Mid-Atlantic |
| 44 | Aesthetic Image Dentistry (Debra Duryea, DMD) | Mendham, NJ | https://www.aestheticimagedentistry.com/ | 72 | MEDIUM-HIGH | Northeast |
| 45 | Vason Family Dentistry of Buckhead | Atlanta (Buckhead), GA | https://www.drvason.com/ | 72 | MEDIUM-HIGH | Southeast |
| 46 | Fox Chapel Advanced Dental Care (Dr. J. Kevin Pawlowicz) | Pittsburgh (Fox Chapel), PA | https://www.foxchapeldentistry.com/ | 72 | MEDIUM-HIGH | Mid-Atlantic |
| 47 | Heck Family Dentistry of Lawrence (Dr. Brian Heck + 3 dentists) | Lawrence, KS | https://www.heckfamilydentistry.com/ | 72 | MEDIUM-HIGH | South-Central |
| 48 | Garden Oaks Family & Cosmetic Dentistry (Drs. Patrick Ruehle & Erika Eide) | Denton, TX | https://www.gardenoaksfamilydental.com/ | 72 | MEDIUM-HIGH | South-Central |
| 49 | Stephen J. Rothman, DMD & Cammarano, DMD | Woodbridge, CT | https://rothmandentist.com/ | 72 | MEDIUM-HIGH | Northeast |
| 50 | Canyon Golf Family Dentistry (Dr. Bryan E. Soto) | San Antonio (Stone Oak), TX | https://www.familydentiststoneoak.com/ | 72 | MEDIUM-HIGH | South-Central |
| 51 | Oak Brook Dental Center | Elmhurst, IL | https://oakbrookdentalcenter.com | 73 | MEDIUM-HIGH | Midwest |
| 52 | North Shore Prosthodontic Associates | Manhasset / Woodbury, NY | https://www.nspali.com/ | 72 | MEDIUM | Northeast |
| 53 | Beliveau Dental (E. Charles Beliveau, DDS, PLLC) | North Andover, MA | https://www.beliveaudental.com/ | 71 | MEDIUM-HIGH | Northeast |
| 54 | Fox Valley Dental Associates (Tami Zuck DDS) | Crystal Lake, IL | https://foxvalleydentalcl.com | 71 | MEDIUM-HIGH | Midwest |
| 55 | Baltimore Dental Arts (Drs. Kevin Murphy, Devon Conklin, Charles & Melody Ward) | Baltimore, MD | https://www.baltimoredentalarts.com/ | 71 | MEDIUM-HIGH | Mid-Atlantic |
| 56 | Maras Dentistry (William H. Maras, DDS, PA) | Palm Beach Gardens, FL | https://www.marasdentistry.com/ | 71 | MEDIUM-HIGH | Southeast |
| 57 | Fishers Family Dentistry | Fishers, IN | https://fishersfamilydentistry.com | 71 | MEDIUM-HIGH | Midwest |
| 58 | Oak Canyon Dentistry (Dr. Steven Haase) | Bee Cave (Austin), TX | https://www.oakcanyondentistry.com/ | 71 | MEDIUM-HIGH | South-Central |
| 59 | Montrose DDS (Drs. Samuel Carrell & Austin Faulk) | Houston (Montrose), TX | https://montrosedds.com/ | 71 | MEDIUM-HIGH | South-Central |
| 60 | Smiles by Martin (Dr. Greg Martin - third generation) | Grapevine, TX | https://www.smilesbymartin.com/ | 71 | MEDIUM-HIGH | South-Central |
| 61 | Progressive Dentistry (Steven M. Levy, DMD) | Merrick, NY | https://www.merrickdentistry.com/ | 71 | MEDIUM | Northeast |
| 62 | Thomsen Dental Group | West Omaha, NE | https://thomsendental.com | 70 | MEDIUM-HIGH | Midwest |
| 63 | Donna L. Kiesel DDS PA | Coppell, TX | https://www.drdonnakiesel.com/ | 70 | MEDIUM-HIGH | South-Central |
| 64 | Byerly Family Dentistry | Montgomery (Cincinnati), OH | https://byerlydental.com | 70 | MEDIUM-HIGH | Midwest |
| 65 | Wallingford Station Family Dental | Wallingford (Media), PA | https://www.wallingforddental.com/ | 70 | MEDIUM-HIGH | Mid-Atlantic |
| 66 | Midtown Dental Sacramento | Sacramento, CA | https://www.midtowndentalsacramento.com/ | 70 | MEDIUM-HIGH | West |
| 67 | Johann Prosthetics of Boulder (Andrew R. Johann DDS MS PC) | Boulder, CO | https://www.andrewjohannddsmspc.com/ | 70 | MEDIUM-HIGH | West |
| 68 | Baccellieri Family Dentistry (Dr. Carl Baccellieri Jr.) | Kennett Square, PA | https://bfdentistry.com/ | 70 | MEDIUM-HIGH | Mid-Atlantic |
| 69 | March Dentistry | Upper Arlington (Columbus), OH | https://marchdentistry.com | 70 | MEDIUM-HIGH | Midwest |
| 70 | Todd Phelan DDS (Drs. S. Todd Phelan & Tyler Gossett) | Rogers, AR | https://www.nwadentist.com/ | 70 | MEDIUM-HIGH | South-Central |
| 71 | Thomas J. Emmer, DDS, PA (Prosthodontist) | Morristown, NJ | https://www.tjemmer.com/ | 70 | MEDIUM | Northeast |
| 72 | Moulton Dentistry of Hoover | Hoover (Birmingham), AL | https://www.moultondentistry.com/ | 70 | MEDIUM | Southeast |
| 73 | Portland Dental Health Care & Implant Center | Portland, ME | https://www.portlandmainedental.com/ | 70 | MEDIUM | Northeast |
| 74 | Ross & Sourlis Family Dentistry of Rock Hill (domain: Coombs and Ross legacy) | Rock Hill, SC | https://www.crsmile.com/ | 70 | MEDIUM | Southeast |
| 75 | Perry Hall Smiles (Caroline F. Owens, DDS, PA) | Perry Hall (Baltimore), MD | http://www.perryhallsmiles.com/ | 69 | MEDIUM-HIGH | Mid-Atlantic |
| 76 | Always Great Smiles (Drs. Pecora & Langner) | Glen Ellyn, IL | https://alwaysgreatsmiles.com | 69 | MEDIUM-HIGH | Midwest |
| 77 | Schilling Farms Dental (Drs. Midyett & Prine) | Collierville (Memphis), TN | https://www.schillingfarmsdental.com/ | 69 | MEDIUM-HIGH | Southeast |
| 78 | Dental Arts of Delaware (Drs. Gregg Fink & Christopher Appleman) | Newark, DE | https://dentalartsofdelaware.com/ | 69 | MEDIUM-HIGH | Mid-Atlantic |
| 79 | CMB Family Dentistry (Drs. David Brown & Josh Alter) | Broomall, PA | https://www.cmbdental.com/ | 69 | MEDIUM-HIGH | Mid-Atlantic |
| 80 | Cinco Meadows Dental (Dr. Brian Williams) | Katy (Cinco Ranch), TX | https://www.cincomeadowsdental.com/ | 69 | MEDIUM-HIGH | South-Central |
| 81 | Dr. Rosenbaum & Associates | Modesto, CA | https://www.docsforteeth.com/ | 69 | MEDIUM | West |
| 82 | Pelandale Dental Care (Dr. Param Gill) | Modesto, CA | https://www.pelandaledental.com/ | 69 | MEDIUM | West |
| 83 | Annapolis Dental Associates | Annapolis, MD | https://www.annapolisdentalassociates.net/ | 69 | MEDIUM | Mid-Atlantic |
| 84 | James A. Vito, DMD (Prosthodontics & Periodontics) | Wayne, PA | https://www.jamesvito.com/ | 69 | MEDIUM | Mid-Atlantic |
| 85 | Serafin Family Dentistry | Carlisle, PA | https://www.serafinfamilydentistry.com/ | 69 | MEDIUM | Mid-Atlantic |
| 86 | Allison Family & Cosmetic Dentistry (F. Vincent Allison III, DDS, PA) | Durham, NC | https://www.allisonfamilydentistry.com/ | 69 | MEDIUM | Southeast |
| 87 | Iglesias Dental Group (formerly Walter K. Kulick, DMD, PA) | Coral Springs, FL | https://www.dentistrycoralsprings.com/ | 69 | MEDIUM | Southeast |
| 88 | DeMartin Dental Associates | Fairfield, CT | https://www.demartindental.com/ | 69 | MEDIUM | Northeast |
| 89 | Egidio Dental Care (Aaron J. Egidio, DDS) | Madison, CT | https://www.egidiodentalcare.com/ | 69 | MEDIUM | Northeast |
| 90 | Blossfeld Family Dentistry (Dr. Carol M. Blossfeld) | Edmond / Oklahoma City, OK | https://www.drblossfeld.com/ | 69 | MEDIUM | South-Central |
| 91 | Perfect Smiles Dental Care | Lenexa, KS | https://perfectsmilesdentalcare.com | 68 | MEDIUM-HIGH | Midwest |
| 92 | Somerset Hills Family Dentist (Joseph M. Micale, DMD, PA) | Basking Ridge, NJ | https://www.somersethillsfamilydentist.com/ | 68 | MEDIUM-HIGH | Northeast |
| 93 | North Macon Dental Associates | Macon, GA | https://www.northmacondentalassociates.com/ | 68 | MEDIUM-HIGH | Southeast |
| 94 | Passidomo Cosmetic & Family Dentistry (Dr. Passidomo & Dr. Brij Patel) | Centerville (Dayton), OH | https://dpsmilecenter.com | 68 | MEDIUM-HIGH | Midwest |
| 95 | Michael A. MacInnes, DDS, PLLC | Sammamish, WA | https://www.macinnesdentistry.com/ | 68 | MEDIUM-HIGH | West |
| 96 | Kahala Smile Professionals, LLC (Drs. Candace & Robert Wada) | Honolulu (Kahala), HI | https://www.kahalasmileprofessionals.com/ | 68 | MEDIUM-HIGH | West |
| 97 | Lee Dental Care | Fort Myers, FL | https://www.leedental.net/ | 68 | MEDIUM-HIGH | Southeast |
| 98 | Delmar Dental Medicine (Thomas H. Abele, DMD, FAGD) | Delmar, NY | https://delmardental.com/ | 68 | MEDIUM | Northeast |
| 99 | Family Smile Dentistry (Drs. Foroughi & Jarquin) | Lakewood Ranch (Bradenton), FL | https://familysmiledentistry.com/ | 68 | MEDIUM | Southeast |
| 100 | Jonson Dental Care (George P. Jonson DDS) | Kettering (Dayton), OH | https://jonsondentalcare.com | 68 | MEDIUM | Midwest |

## Full profiles (rank order)

1. D'Angelo/Olson La Jolla Dentistry — La Jolla, CA — https://dangelohoffmanolsonlajolladentistryca.hibuwebsites.com/ — 82/100 — HIGH (medium-high confidence)
• Est/Doctors: Est. 1990 (self-stated; VERIFIED on site) | 2 doctors | Reviews: Birdeye 5.0 (304 reviews) + Yelp ~80 reviews (D'Angelo/Olson/Hoffman DDS listing, May 2026); NONE surfaced on the practice's own site (reviews page renders empty). Source: reviews.birdeye.com, yelp.com via WebSearch 2026-09-30
• Site (observed): Hibu-built (VERIFIED: hibu-runtime.css, hibustudio.com and AudioEye overlay in source). Canonical/og:url is the vendor subdomain itself, i.e. 'https://dangelohoffmanolsonlajolladentistryca.hibuwebsites.com/' - no owned domain seen (INFERRED: no custom domain is in use). Title tag 'D'Angelo/Olson La Jolla Dentistry San Diego, CA' (no service keywords). /reviews page ships with no testimonial content; /hibu-video-splash page live. Legacy 'Hoffman' partner name still embedded in the URL slug.
• Social gap: Facebook, Instagram and Yelp links in footer; follower counts UNKNOWN.
• Breakdown: FC17/20 BM13/15 WW14/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap9 Dep8 Tr8 Tech8
• Independence: INFERRED - self-described 'local, family-, and woman-owned'; two named owner-dentists; no group/DSO language on home/about/team pages; no DSO name matches EXCLUSIONS §7. | Decision-maker: Dr. Joseph D'Angelo and Dr. Ashley Olson (co-leads; VERIFIED on site)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — La Jolla ZIP/positioning, veneers+implants+sedation menu, 2 doctors, 7am-5pm hours (tier: upper-mid) | Digital spend: Hibu subscription (redirect target), AudioEye accessibility overlay
• Hooks: 'Your website lives on hibuwebsites.com - you do not own your web address.' / Reviews page loads empty while 15 straight years of 'Best in La Jolla' go unshown.
• Pitch/offer: Own-domain premium rebuild that migrates them off Hibu and surfaces the awards/reviews - $8-12k standard.
• Wave-2 update (2026-09-30): 80 -> 82. Review corpus now VERIFIED at 380+ across Birdeye+Yelp while own reviews page is empty, which raises Gap/FC. Site re-checked with curl: live, still served from the hibuwebsites.com vendor subdomain.
• Sources: Site raw HTML + WebFetch of /, /about, /reviews (2026-09-30); EXCLUSIONS grep clear
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Hibu · region: West (wave 1)

2. Luis E. Martinez DMD, PA (St. Pete Cosmetic Dentistry) — St. Petersburg, FL — https://www.stpetecosmeticdentistry.com/ — 80/100 — HIGH (confidence: MEDIUM-HIGH)
• Est/Doctors: Est. UNKNOWN; solo; FACD logo displayed (VERIFIED, render) | Dr. Martinez UF College of Dentistry grad 1985; "over 35 years" (Healthgrades bio; practice founding year INFERRED) | Reviews: Birdeye 1,018 reviews / 5.0 stars (search snippet, birdeye.com); Healthgrades 390 reviews; Yelp 13 reviews. Own homepage (18KB, ©2014) shows no counts [WAVE 2]
• Site (observed): 18KB single-page-style template with jQuery carousel ("#myCarousel" interval 4000, "#topCarousel" interval 5000). Footer: "© 2014 All Rights Reserved by Luis E. Martinez, D.M.D., P.A. … Website Redesigned, Hosted, and Promoted by Digital Eel, Inc." Title: "St Petersburg Dentist and Florida Cosmetic Dentistry in Tampa Bay FL" (keyword-stuffed). Nav items: Home / Office Tour / Meet the Team / Services / Masterpieces/Gallery / Reviews / Newsletter.
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC13/20 BM13/15 WW13/15 Gap14/15 Dep8/10 Tr9/10 Cv5/5 Sp3/3 DM2/2 | Gap 9 Dep 8 Tr 9 Tech 9
• Independence: VERIFIED (solo) — professional-association entity in footer and personal branding; no group language | Decision-maker: Dr. Luis E. Martinez, DMD (owner — VERIFIED via "© Luis E. Martinez, D.M.D., P.A.")
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Solo cosmetic/aesthetic practice (veneers, smile makeovers, FACD) in St. Petersburg — Mid-High | Digital spend: Digital Eel, Inc. (design + hosting + promotion; observed)
• Hooks: 1) Site last redesigned 2014 (© 2014) while the practice pitches 'among the top 1% of dentists' for aesthetics. 2) 'Masterpieces/Gallery' page sitting behind a 2014 carousel.
• Pitch/offer: Cosmetic gallery-led redesign — $5–8k (solo) up to $8k
• Sources: stpetecosmeticdentistry.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Southeast (wave 1)

3. Brewer Family Dentistry — Modesto, CA — https://www.brewerdentistry.com/ — 80/100 — HIGH (medium confidence)
• Est/Doctors: Since 1979 (VERIFIED: 'Since 1979, Brewer Family Dentistry has proudly served'); founded by Dr. Keith Brewer, now second generation | 2 doctors | Reviews: Birdeye 4.9 (597 reviews) + a second platform 5.0 (329 reviews) + Yelp 34 + BBB Accredited since 9/2010; own /patient-reviews/ page shows first-name quotes with no rating or count. Source: reviews.birdeye.com, yelp.com, bbb.org via WebSearch
• Site (observed): Progressive Dental Marketing template (VERIFIED footer: '© 2018 Brewer Family Dentistry | Dental Website by Progressive Dental Marketing | Privacy Policy'; theme 'varsity'; 'dentalmarketing' asset marker). Copy is internally inconsistent: 'Serving Modesto, CA for Over 40 Years' vs 'more than 37 years ago'. /patient-reviews/ page shows only first-name quotes with no rating or count.
• Social gap: UNKNOWN
• Breakdown: FC14/20 BM14/15 WW12/15 Gap14/15 Dep9/10 Tr8/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap9 Dep9 Tr8 Tech8
• Independence: INFERRED - family-owned second-generation practice, no group language; Modesto is not a known DSO stronghold for this brand. | Decision-maker: Dr. Dean Brewer (DDS Loma Linda; California Implant Institute surgical fellowship) and Dr. Amanda Brewer (DDS Loma Linda)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — CEREC, Galileos CBCT, laser, All-on-4 menu, two doctors (tier: mid; Central Valley market) | Digital spend: agency-maintained site (Progressive Dental Marketing), Google/Yelp presence
• Hooks: 'Your footer is frozen at 2018 and says 37 years in one place and 40 in another.' / All-on-4 + CBCT is high-ticket work sitting on a template page.
• Pitch/offer: Premium multi-generation practice rebuild; $8-10k standard.
• Wave-2 update (2026-09-30): 73 -> 80. Biggest upgrade: ~900+ verified reviews invisible on a (c)2018 DentalMarketing.com template. Live, curl 200.
• Sources: Raw HTML, WebFetch /, /meet-our-doctors/, /patient-reviews/
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Progressive Dental Marketing · region: West (wave 1)

4. Mt. Lookout Dentistry — Cincinnati, OH — mtlookoutdentistry.com — 79/100 — HIGH (medium)
• Est/Doctors: 'Looking Out for Cincinnati Smiles Since 1956' (VERIFIED, site); Gosnell: UK / Louisville dental school, GPR 2008, local study clubs incl. Spear Education; Pankey Institute + SPEAR affiliation shown (VERIFIED on render) | Reviews: ~3,350-3,570 reviews, 4.9-5.0 (Birdeye listings reviews.birdeye.com/mt-lookout-dentistry-155338424065279 = 3,353; -155338441138064 = 3,571; two listings, possibly overlapping); Facebook 96% recommend on 23 reviews (WebSearch snippets). Homepage raw HTML shows only a generic 'Reviews' block, no visible count (curl). [Wave-2 enrichment]
• Site (observed): Officite platform — rendered footer "© 2022 MH SUB I, LLC DBA Officite | Web Design by LanternSol"; raw HTML contains unpopulated placeholder copy under the DOCTORS and FOUNDERS headings: "Lorem ipsum dolor sit amet, consectetuer adipiscing" (VERIFIED, curl); <title> "Mt. Lookout Dentistry | Dentist In Cincinnati, OH"
• Social gap: UNKNOWN (not checked)
• Breakdown: FC14/20 BM14/15 WW12/15 Gap14/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM1/2 | Subs: Gap9 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED — local brand with 70-yr history; no DSO strings; footer entity is the web vendor (Officite), not a practice owner; ownership transition to Dr. Gosnell possible — verify on call | Decision-maker: Dr. Ben T. Gosnell (VERIFIED as named dentist; ownership UNKNOWN); Dr. Croop also named
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — Pankey/Spear-trained restorative practice in Mt. Lookout/Hyde Park corridor | Digital spend: Officite subscription, PatientFi financing, PatientConnect365
• Hooks: 1) 'Lorem ipsum' placeholder text is live under the DOCTORS and FOUNDERS headings of a practice founded in 1956 2) Pankey + Spear credentials are not carried by the design
• Pitch/offer: Heritage + restorative-credential redesign to replace Officite. $8–12k
• Sources: mtlookoutdentistry.com raw HTML + render
• Wave-2 re-score: 71 -> 79. Review corpus of 3,000+ is huge and not surfaced on the 'Lorem ipsum' Officite homepage: strongest Gap in the region.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Officite · region: Midwest (wave 1)

5. Goodman Dental Care — Annapolis, MD — https://www.goodmandentalcare.com/ — 79/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: ~40 yrs, three-generation family practice (site: 'nearly 40 years'; testimonial family 'visiting Goodman Dental Care since 1985') [VERIFIED on site]; 3 dentists: A. Gary Goodman DDS, Jeremy Goodman DDS, Shoshana Garfield DDS; affiliations shown: Pankey Institute, Seattle Study Club, Spear, AAID, ADA [VERIFIED on site] | Reviews: 449 reviews, 5.0 (Birdeye, search snippet 2026-09-30); Healthgrades 143 (Dr. A. Gary Goodman) + 104 (Dr. Jeremy Goodman); Yelp 11. Site homepage does not surface the count [VERIFIED via search]
• Site (observed): TNT Dental template. Footer verbatim: "©2019 Goodman Dental Care | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental". Title tag verbatim: "Dentist in Annapolis, MD | Dentist Near Me | Cost of Dentistry in Annapolis | Dental Office Near Me | Goodman Dental Care" (keyword-stuffed). Retired Universal Analytics tag UA-22571916-1 still in source; 4 of 29 images have no alt text. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Site links Facebook, Instagram, YouTube [VERIFIED]; posting activity UNKNOWN. Pankey/Spear-level case work is not surfaced on the homepage [INFERRED from page content].
• Breakdown: FC15/20 BM13/15 WW12/15 Gap13/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM2/2 | Gap8 Dep8 Tr8 Tech9 (/10)
• Independence: VERIFIED (site self-description: independent family practice across three generations; single office; no group/entity language in footer or booking links) | Decision-maker: Dr. A. Gary Goodman (senior/founder generation; ownership split INFERRED); sons/daughters-in-practice Dr. Jeremy Goodman
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Annapolis waterfront/Anne Arundel market, E4D same-day crowns, implants and implant dentures, veneers, sedation, Botox/fillers -> upper-mid tier | Digital spend: TNT Dental hosting/maintenance subscription; CareCredit financing; Google Maps profile
• Hooks: 1) Footer still reads "©2019" and the title tag says "Dentist Near Me | Cost of Dentistry in Annapolis" on a 3-generation, Pankey/Spear-trained practice. 2) ~40-year / three-generation milestone is a natural moment for a redesign.
• Pitch/offer: Premium homepage rebuild leading with the Pankey/Spear comprehensive-care story, smile gallery and generational brand; keep existing booking/financing links. $8-12k (3-doctor standard).
• Sources: goodmandentalcare.com raw HTML + rendered fetch (2026-09-30); Google Maps place link on site
• Wave-2 note: score 77 -> 79 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Mid-Atlantic (wave 1)

6. Cosmetic & Implant Dentistry of Naples — Naples, FL — https://www.dentistryofnaples.com/ — 78/100 — HIGH (confidence: MEDIUM-HIGH)
• Est/Doctors: Est. 1977 (INFERRED — search-indexed practice bio, not on-page); 2 doctors (VERIFIED, site); Dr. Stanosheck AACD member (INFERRED, directory snippet) | Reviews: 709 patient reviews on PatientConnect365 profile (platform not specified; VERIFIED via fetch); Yelp 19 reviews (search snippet); Facebook 94% recommend / 20 reviews; 709 vs on-page zero counts = large hidden corpus [WAVE 2]
• Site (observed): MM5 Digital Marketing build. Footer (rendered): "© ~ Comestic & Implant Denistry of Naples All rights reserved." — year missing, 'Cosmetic' and 'Dentistry' misspelled. Award badge: "Choice awards 2020 — Award Winner 12 Years Running" (5+ years stale). Site is bot-walled (Cloudflare-style "One moment, please..." loader) — mark bot-walled, not dead.
• Social gap: Not assessed (no search tool available) — UNKNOWN
• Breakdown: FC16/20 BM14/15 WW11/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Gap 8 Dep 8 Tr 8 Tech 8
• Independence: INFERRED — two named owner-doctors, no group/'division of' language, footer credit only to MM5 Digital Marketing; no DSO markers found (bot-walled: raw HTML not retrievable, verified via rendered fetch only) | Decision-maker: Drs. William N. Sullivan & Christopher Stanosheck (owner status INFERRED)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Naples FL (wealthy market) + implants/cosmetic/veneers positioning + two-doctor 40-year-plus practice — Mid-High to High | Digital spend: MM5 Digital Marketing (observed footer credit) — retainer/hosting likely redirectable
• Hooks: 1) Footer literally says "Comestic & Implant Denistry" on a Naples cosmetic-implant practice. 2) Still advertising a "Choice Awards 2020" badge in 2026.
• Pitch/offer: Naples implant/cosmetic flagship redesign — $8–12k
• Sources: dentistryofnaples.com (rendered fetch); search-indexed practice bio (est. 1977); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Southeast (wave 1)

7. Coral Gables Dentistry & Prosthodontics — Coral Gables, FL — https://www.coralgablesdentistry.com/ — 77/100 — HIGH (confidence: MEDIUM-HIGH)
• Est/Doctors: "Well over thirty years" (INFERRED — directory snippet, not on-page); 2 prosthodontists incl. Dr. Cristina Osorio (VERIFIED, site) | Dr. Davila = Diplomate ABP & Fellow of the Academy of Prosthodontics (directory snippet) | Reviews: 706 patient reviews on PatientConnect365 profile (search snippet; platform not specified); Yelp 54 reviews (search snippet); Healthgrades thin (Dr. Davila 5 reviews, 4.2 recommend); own /for-patients/reviews page prints NO counts or ratings (VERIFIED via fetch) [WAVE 2]
• Site (observed): Digital Resource (yourdigitalresource.com) build, 41KB page. Footer (rendered): "Copyright Coral Gables Dentistry # - All Rights Reserved" (unfilled '#'). Raw HTML carries a legacy notice: "Internet Explorer. To view our site accurately, we highly recommend you…". Title: "Best Dentist in Coral Gables | Coral Gables Dentistry" (generic superlative, no specialty).
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC16/20 BM13/15 WW11/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Gap 8 Dep 8 Tr 8 Tech 8
• Independence: INFERRED — no group/DSO language; footer credit only "Designed and Maintained by: Digital Resource"; distinct from excluded Abadin Dental / Morales (Coral Gables) practices | Decision-maker: Dr. Laura J. Davila (board-certified prosthodontist) — owner status INFERRED
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Board-certified prosthodontist pair; All-on-Four, laser suite (SmoothLase/NightLase), sedation, Botox — Coral Gables affluent market — High | Digital spend: Digital Resource (hosting/maintenance credit observed)
• Hooks: 1) Board-certified prosthodontists whose footer still shows a literal '#' copyright and IE-era compat code. 2) Title says 'Best Dentist' — nowhere says 'prosthodontist'.
• Pitch/offer: Prosthodontic/All-on-4 flagship redesign — $8–12k
• Sources: coralgablesdentistry.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Southeast (wave 1)

8. Klein Family Dentistry — Harrisburg, PA — https://www.kleinfamilydentistry.com/ — 77/100 — HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: 'A Harrisburg staple to local families since 1979'; 'Locally-Owned & Operated' [VERIFIED on site]; Dr. Gary M. Klein DDS (owner, son of founder Dr. Joel S. Klein) + Dr. Miller (and associate reviewed as Dr. Franklin-Pitts); exact roster 2-3 [VERIFIED on site, count INFERRED] | Reviews: 512 reviews, 4.9 (Birdeye); dentascore.com aggregator 433; Facebook 96% recommend / 36; Yelp listed (search snippet 2026-09-30). Homepage shows only a small carousel [VERIFIED]
• Site (observed): TNT Dental. Footer verbatim: "Copyright © 2017 Klein Family Dental | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental"; review strip uses a dead 'Google Plus' logo (assets/images/reviews-google.png, alt 'Google Plus logo'); title "Dentist Harrisburg | Klein Family Dentistry | Dental Implants"; UA-103004655-1 legacy tag. Site markets All-on-4, cone-beam scanning, 3D printing, soft-tissue laser that the template does not showcase. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook and Yelp links only [VERIFIED]; no Instagram.
• Breakdown: FC13/20 BM13/15 WW12/15 Gap13/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM2/2 | Gap8 Dep8 Tr8 Tech9 (/10)
• Independence: VERIFIED (site: 'Locally-Owned & Operated'; family succession Joel -> Gary Klein; single office) | Decision-maker: Dr. Gary M. Klein DDS (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Harrisburg suburban market; All-on-4, implants (site claims 97% success), CBCT, 3D printing, laser, sleep apnea -> mid tier | Digital spend: TNT Dental subscription; CareCredit; Google Analytics
• Hooks: 1) Review strip still uses a 'Google Plus' logo (Google+ shut down in 2019) and the footer is frozen at ©2017. 2) Generational handoff (Joel -> Gary Klein) + 45-year mark in 2024 already passed.
• Pitch/offer: Implant/All-on-4 focused redesign with proper review surfacing; keep TNT-hosted forms until cut-over. $8-12k.
• Sources: kleinfamilydentistry.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 74 -> 77 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Mid-Atlantic (wave 1)

9. Christensen Dental Associates — Waldwick, NJ — https://www.cdanj.com/ — 77/100 — MEDIUM-HIGH(medium)
• Est/Doctors: Dr. Christensen practicing privately since 1998 (VERIFIED, bio); 3 doctors (Christensen, Ryan Burke, Leeda Bassam) | Reviews: Google 4.9 (count not shown); Birdeye 115 reviews 4.9; Healthgrades 65 reviews (Dr. David Christensen); site shows only 14 curated testimonials (VERIFIED via snippets)
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved" while the page footer also says "©2026 Christensen Dental Associates" (two conflicting years); homepage title "Dentist in Waldwick, NJ | Christensen Dental Associates" is a generic vendor pattern; 121KB template; site sells "in-house dental lab / All-On-X" capability the template barely showcases
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC16/20 BM12/15 WW12/15 Gap13/15 Dep8/10 Tr7/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap9 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED — bio names owner-dentist and two associates; no group language or DSO strings in raw HTML | Decision-maker: Dr. Christensen (owner; first name UNKNOWN on fetched page)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (Bergen County; in-house lab, CEREC since 2008, 3D printing, All-On-X manufacturing for other dentists) | Digital spend: ProSites subscription; laser (Biolase Waterlase page) and CEREC investments
• Hooks: 1) Dr. Christensen was associate team dentist for the NY Giants, NJ Devils and NJ Nets and runs an in-house lab that makes All-On-X prosthetics for other dentists — none of it headlines a ProSites template 2) Footer carries the mojibake "Copyright � 2019 Prosites" next to "©2026"
• Pitch/offer: Full-arch/All-on-X and digital-dentistry showcase redesign — $8–12k standard tier.
• Sources: Live fetch cdanj.com (homepage, /our-practice/meet-the-doctors/meet-dr-christensen/, /our-practice/read-our-reviews/) | Wave-2 review enrichment (2026-09-30): Birdeye 115 reviews, Healthgrades 65; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

10. Southdale Dental Associates — Edina, MN — sdadental.com — 77/100 — MEDIUM-HIGH (medium)
• Est/Doctors: 'CELEBRATING 50 YEARS IN EDINA, MINNESOTA' / 'more than 50 years' and 'second and third generations of the same families' (VERIFIED, site); 6 dentists (VERIFIED); Dr. Mehta is FICOI (implants) (VERIFIED) | Reviews: 1,140 reviews, 5-star aggregate, 98.9% would refer (Demandforce local.demandforce.com/b/sdadental, VERIFIED via fetch; patients listed as customers since 1999). Not surfaced on the homepage (one lone testimonial).
• Site (observed): Wix DIY build — raw HTML <meta generator> 'Wix.com Website Builder' + static.wixstatic assets; a header social icon links to "https://www.facebook.com/wix" (the real page "https://www.facebook.com/SOUTHDALEDENTAL" is a second link); homepage is one scroll with six bios and one testimonial and no services copy at all (no implants/cosmetic/sedation mention despite an FICOI doctor); <title> "Edina Minnesota Dentist | Southdale Dental Associates | Edina" (Edina repeated); Wix residue text 'top of page … bottom of page'; footer "©2026 by Southdale Dental Associates" (VERIFIED raw HTML + WebFetch render)
• Social gap: UNKNOWN (only a Facebook link present; follower count not checked)
• Breakdown: FC15/20 BM14/15 WW12/15 Gap13/15 Dep8/10 Tr9/10 Cv3/5 Sp2/3 DM1/2 | Subs: Gap8 Dep7 Tr9 Tech9 (/10)
• Independence: INFERRED — 'Southdale Dental Associates' single suite (7373 France Ave S, Ste 600), no DSO/group strings in raw HTML, info@sdadental.com; six-doctor 'Associates' entity: confirm ownership/entity on call (MEDIUM-HIGH confidence) | Decision-maker: UNKNOWN principal — six dentists named on the site (VERIFIED): Thomas P. Telander DDS (listed first; 30+ yrs), Kyle Gearhart, Lara Bainer, Sachin R. Mehta DDS FICOI (20 yrs), James Healy, Jason Pendleton; no owner named
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — six-dentist, 50-yr practice in Edina/Southdale medical corridor (affluent Twin Cities inner-ring suburb) | Digital spend: Wix subscription (redirect target); Demandforce (reviews)
• Hooks: 1) 'Celebrating 50 years' and 1,140 Demandforce reviews sit behind a single-scroll Wix page with no services 2) The header Facebook icon still points to facebook.com/wix
• Pitch/offer: Heritage + six-doctor showcase site with services/implant pages, keep Demandforce; replace Wix. $12–15k (multi-doctor flagship)
• Sources: sdadental.com raw HTML + WebFetch render; local.demandforce.com/b/sdadental
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Wix · region: Midwest (wave 2)

11. Meetinghouse Dental Care (Hatboro Integrative Dentistry) — Hatboro, PA — https://www.meetinghousedental.com/ — 76/100 — HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Founder Dr. Lou Trovato (DDS, FAGD, FICOI; now retired) - founding year UNKNOWN; long-running biologic/whole-body practice [VERIFIED on site]; Dr. Wendy Beratan DMD, Dr. Matthew He DMD, Dr. David Klass DMD (all AIAOMT/SMART); Dr. Anthony Trovato PhD nutritionist [VERIFIED on site] | Reviews: 921 reviews (Birdeye); Facebook 224 reviews / 100% recommend; BBB A+, in business since 1984 (search snippets 2026-09-30); Yelp 22. Homepage shows awards, not the corpus [VERIFIED]
• Site (observed): ProSites. Footer verbatim: "Site Developed by ProSites.com"; source comment "Copyright � 2019 Prosites, Inc." (mojibake); title " Hatboro Integrative Dentistry | Hatboro Whole-Body Dentistry | Meetinghouse Dental Care " (three brand names); UA-30546800-1 retired Analytics. Site lists CEREC, 3D cone beam, ozone therapy, PRF, ceramic implants but reads as a generic stock-photo template. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook and Instagram links present [VERIFIED]; activity UNKNOWN. Opencare profile present.
• Breakdown: FC14/20 BM11/15 WW11/15 Gap14/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM2/2 | Gap9 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (self-described private-practice general dentists; no group language) - verify on call | Decision-maker: Dr. Wendy Beratan DMD (probable successor lead; owner UNKNOWN)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Hatboro/Montgomery County; cash-pay biologic dentistry (ceramic implants, ozone, PRF, amalgam-safe removal) -> mid-upper tier niche | Digital spend: ProSites subscription; Opencare listing
• Hooks: 1) Founder retirement = brand reset moment for a three-name title tag. 2) Cash-pay biologic niche that the template presents like a generic office.
• Pitch/offer: Niche-authority redesign (biologic/ceramic implant story); $8-12k.
• Sources: meetinghousedental.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 71 -> 76 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

12. Cosmetic & Implant Dentistry of Maryland (Dr. Jennifer Ouazana) — Pikesville, MD — https://www.cosmeticandimplantdentistryofmd.com/ — 75/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Practice 'first established by our prior owner in 1965' [VERIFIED on site]; current owner-dentist Dr. Jennifer Ouazana (tenure UNKNOWN); prior owner appears to be Howard Rothschild DDS (second domain howardrothschilddds.com) [INFERRED]; 1 owner-dentist (Dr. Jennifer Ouazana DDS); AACD membership displayed [VERIFIED on site] | Reviews: Google/Birdeye count still UNKNOWN after search (Healthgrades group listing + Fresha exist; est. 1965 per site/search snippet); homepage only says 'Connect with us and leave a review!' - corpus unmeasured, Gap trimmed
• Site (observed): ProSites template. Footer verbatim: "Dental Websites powered by ProSites"; source comment "Prosites Web Engine Technology Version 4.0 Copyright � 2019 Prosites, Inc." (mojibake); title " Dentist in Pikesville | Cosmetic & Implant Dentistry of Maryland "; jQuery 1.9.1; TWO live domains serve the identical page (cosmeticandimplantdentistryofmd.com and howardrothschilddds.com; the old-owner domain has a TLS name-mismatch and redirects only over http). [VERIFIED raw HTML + curl, 2026-09-30]
• Social gap: Site links Facebook, YouTube, Twitter, Yelp [VERIFIED]; activity UNKNOWN. Site describes CEREC Primescan, 3D CBCT guided surgery, 'Teeth-in-a-Day', DURAthin veneers (capex signals) that the dated template undersells [VERIFIED on site].
• Breakdown: FC15/20 BM11/15 WW13/15 Gap9/15 Dep9/10 Tr9/10 Cv4/5 Sp3/3 DM2/2 | Gap7 Dep9 Tr9 Tech9 (/10)
• Independence: INFERRED (single-owner practice; entity name is generic; no group/'division of' language; no group booking domain) - verify on call | Decision-maker: Dr. Jennifer Ouazana DDS (owner-dentist)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Pikesville/NW Baltimore County affluent market; CEREC Primescan, CBCT, Teeth-in-a-Day, minimal-prep veneers, Botox -> upper-mid tier for a solo | Digital spend: ProSites subscription (two domains being paid/kept alive); Google Analytics UA tag in source
• Hooks: 1) Two competing live domains (the previous owner's name still serves the identical site, with a broken certificate). 2) New-owner practice with CEREC Primescan/CBCT capex whose site still looks 'early 2010s'.
• Pitch/offer: Owner-rebrand redesign: one domain, cosmetic/implant story, before-after gallery; keep existing scheduling. $6-9k (solo, high-ticket).
• Sources: cosmeticandimplantdentistryofmd.com and howardrothschilddds.com raw HTML/curl; rendered fetch (2026-09-30)
• Wave-2 note: score 76 -> 75 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

13. Wahl Family Dentistry — Wilmington, DE — https://www.wahlfamilydentistry.com/ — 75/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Founded 1949 by Dr. Mervin H. Wahl; children and grandchildren now practice [VERIFIED on site]; 4 dentists: Michael Wahl DDS, Yaella Aronhime DMD, Suraj Patel DMD, Zachary Pettoruto DMD; Drs. Wahl and Aronhime named Top Dentists by Delaware Today [VERIFIED on site] | Reviews: 302 reviews, 4.7 (Birdeye); aggregator 195 verified 4.7; Yelp 24; Healthgrades 10 (Dr. Wahl); practice history since 1949 per search snippet; homepage footer '2016' [VERIFIED]
• Site (observed): TNT Dental. Footer verbatim: "© 2016 Wahl Family Dentistry | Sitemap | Site designed and maintained by TNT Dental"; legacy table/font markup; 24 of 26 images have no alt text; UA-38644436-1 retired Analytics tag; title "Dentist Wilmington | General Dentistry | Wahl Family Dentistry". [VERIFIED raw HTML, 2026-09-30]
• Social gap: Only a YouTube link found in source [VERIFIED]; no Facebook/Instagram links.
• Breakdown: FC13/20 BM14/15 WW12/15 Gap12/15 Dep7/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Gap8 Dep7 Tr8 Tech9 (/10)
• Independence: VERIFIED (site: family-operated across founder's children and grandchildren; single Concord Pike office) | Decision-maker: Dr. Michael Wahl DDS (family principal; ownership split INFERRED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — 2003 Concord Pike, Wilmington (Brandywine-adjacent), 4 dentists, cosmetic/restorative mix -> mid tier | Digital spend: TNT Dental subscription; CareCredit; Google Analytics
• Hooks: 1) ©2016 footer on a practice founded 1949 (nearly a 75-year brand). 2) Two Delaware Today Top Dentists but no proof shown above the fold.
• Pitch/offer: Heritage-brand redesign (1949 to third generation) with team + awards; $8-12k (4-doctor standard).
• Sources: wahlfamilydentistry.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 74 -> 75 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Mid-Atlantic (wave 1)

14. Bedford Cosmetic & Restorative Dentistry (Hedstrom / Persha) — Bedford, NH — https://www.bedfordcosmeticdentistry.com/ — 75/100 — MEDIUM-HIGH(medium)
• Est/Doctors: Hedstrom opened private practice in Bedford 1987, 33+ yrs per bio (VERIFIED); 2 doctors | Reviews: Birdeye 374 reviews / 5.0 (Birdeye Bedford NH directory JSON-LD, VERIFIED) invisible on the homepage; Healthgrades 1 review for Dr. Hedstrom ('awesome dental care for over 25 years'); Yelp/Facebook listings exist; site has reviews.html
• Site (observed): TNT Dental; footer "©Copyright 2016, Bedford Cosmetic & Restorative Dentistry | Site designed and maintained by TNT Dental"; 17KB homepage; homepage copy still says "Dr. Hedstrom and his Bedford, NH dental team" while nav says "Meet Dr. Persha" (stale handoff copy); 360 NH-101 shared building with a second practice
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC13/20 BM13/15 WW12/15 Gap13/15 Dep8/10 Tr7/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap9 Dep7 Tr9 Tech9 (/10)
• Independence: INFERRED — bios name founder and successor; no group language or DSO strings | Decision-maker: Joseph Hedstrom, DDS (founder, opened 1987) — successor Alokh Persha, DDS
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2-3 (Bedford/Manchester NH; implants, cosmetic, sleep apnea) | Digital spend: TNT Dental subscription
• Hooks: 1) Generational handoff visible in the site itself: nav "Meet Dr. Persha" but body copy "Dr. Hedstrom and his team" 2) ©2016 footer on a 10-year-old TNT template
• Pitch/offer: Handoff-positioning redesign for the new owner — $8–12k standard tier.
• Sources: Live fetch bedfordcosmeticdentistry.com (home, meet-dr-hedstrom.html, meet-dr-persha.html) | Wave-2 review enrichment (2026-09-30): Healthgrades, Yelp/Facebook listings; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Northeast (wave 1)

15. Advanced Dental Solutions of Pittsburgh — Pittsburgh (Upper St. Clair/Bethel Park), PA — https://www.pittsburghissmiling.com/ — 75/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: UNKNOWN founding year; Dr. Rairigh graduated WVU dentistry 2004 (Dawson Academy trained) [VERIFIED on site]; 3 dentists: Dr. Dan Rairigh DDS (Midwest Implant Institute; Dawson), Dr. Josh Culver DDS, Dr. Dakota Goodrum [VERIFIED on site] | Reviews: Birdeye 1,658 reviews, 4.9 (second Birdeye page shows 944; aggregator 1,565+); Yelp 10; BBB profile (search snippets 2026-09-30). Homepage carries a reviews page but the corpus is not headline-visible [VERIFIED]
• Site (observed): TNT Dental. Title verbatim: "Dentist Pittsburgh, PA | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Advanced Dental Solutions of Pittsburgh"; footer "© Advanced Dental Solutions of Pittsburgh | Sitemap | Site designed and maintained by TNT Dental | Privacy Policy" (no year); jQuery 1.11.3. Site markets CEREC, All-on-4, sedation, full-mouth reconstruction. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook, YouTube, Yelp links [VERIFIED].
• Breakdown: FC14/20 BM11/15 WW10/15 Gap14/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM2/2 | Gap9 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (owner-dentist bio, single office at 1395 McLaughlin Run Rd; generic brand name 'Advanced Dental Solutions' - MEDIUM-HIGH confidence, verify on call) | Decision-maker: Dr. Dan Rairigh DDS
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Upper St. Clair/South Hills affluent suburb, CEREC, CBCT-adjacent implant services, All-on-4, sedation, full-mouth -> mid-upper tier | Digital spend: TNT Dental subscription; MetLife/UPMC insurance landing pages
• Hooks: 1) Six-segment keyword title including 'Cost of Dental Care'. 2) All-on-4/full-mouth capability is buried under insurance landing pages.
• Pitch/offer: Implant/full-mouth-led redesign; $8-12k.
• Sources: pittsburghissmiling.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 67 -> 75 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Mid-Atlantic (wave 1)

16. Center for Dental Excellence, LLC (Christian) - Simsbury / West Hartford / Litchfield, CT - https://www.ctcde.com/ - 75/100 - MEDIUM-HIGH (medium)
• Est/Doctors: Serving the Farmington Valley 'for over 50 years' (VERIFIED, ctcde.com copy via search); 3+ doctors (L. Christian DMD, M. Christian DMD FACP, Bruce M. Nghiem DMD); 3 offices (Simsbury, West Hartford, Litchfield) | Reviews: Birdeye 390 reviews / 4.9 (Birdeye Simsbury directory JSON-LD, 2026-09-30; Yelp and BBB listings also exist)
• Site (observed): PBHS (footer 'Dental Website Design by PBHS (c) 2026', wp-content/themes/2112-template; live site is Cloudflare-walled to scripts, so read from web.archive.org snapshot 2026-04-20 + WebFetch of search-indexed pages); homepage <title> "Center For Dental Excellence in Simsbury and West Hartford CT" while body says "now has three locations ... Simsbury, West Hartford, and Litchfield"; boilerplate copy "can literally redesign your smile"; no visible review count despite 390 on Birdeye
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC16/20 BM14/15 WW10/15 Gap12/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech7 (/10)
• Independence: INFERRED - 'Center for Dental Excellence, LLC' (BBB lists as LLC/prosthodontist); father-and-son owner-dentists named (Lawrence and Michael Christian); no group/DSO language or DSO strings in archived raw HTML | Decision-maker: Michael A. Christian, DMD, FACP (board-certified prosthodontist) / Lawrence S. Christian, DMD
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 1-2 (Simsbury/West Hartford/Litchfield; prosthodontics, implants, full-mouth work; 3 offices; 3+ doctors) | Digital spend: PBHS subscription (template site, 2021-era design)
• Hooks: 1) Board-certified prosthodontist credential ("one of only fourteen private-practice Board Certified Prosthodontists in Connecticut") is buried in a stock PBHS template 2) Title tag omits the Litchfield office the body copy announces; 390 Birdeye reviews invisible on the homepage
• Pitch/offer: Group-flagship redesign built around the prosthodontic credential, case gallery and 3-office structure - $12-15k group-flagship tier
• Sources: ctcde.com (archive.org snapshot 2026-04-20; WebFetch/search-indexed pages); Birdeye Simsbury CT directory JSON-LD; BBB profile
• QC: liveness HTTP 403 Cloudflare bot-wall — content verified via web.archive.org snapshot / rendered fetch by research agent · social activity NOT YET CHECKED · vendor cluster: PBHS · region: Northeast (wave 2)

17. Kalil & Kress Family & Cosmetic Dentistry - Nashua, NH - https://www.kalilandkress.com/ - 75/100 - MEDIUM-HIGH (medium)
• Est/Doctors: Since 1990 (VERIFIED, homepage 'Since 1990, the team at Kalil & Kress ...'); 4 doctors; single office 303 Amherst St | Reviews: Birdeye 840 reviews / 4.9 (Birdeye Nashua directory JSON-LD, 2026-09-30); homepage only shows a handful of quotes + 'Leave a review on Google'
• Site (observed): Sesame 24-7 (footer "Website Powered by Sesame 24-7(TM) | Site Map | Privacy Policy"); 21,862-byte homepage; caption "Retired office dog, Teddy"; stock-style imagery; deep menu (Meet 4 doctors + Team + Office Tour + Testimonials...); title "Kalil & Kress Family & Cosmetic Dentistry | Nashua, NH" (no service keywords)
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC12/20 BM14/15 WW12/15 Gap12/15 Dep8/10 Tr8/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr9 Tech8 (/10)
• Independence: INFERRED - four named family/partner doctors, single office, no group language, no DSO strings in raw HTML; WebFetch reading of About text = privately owned partnership | Decision-maker: Owner-dentist partners Donna Kalil, Beth Kress, Michelle Kalil, Andrew Kalil (which one signs contracts UNKNOWN - verify on call)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 3 (Nashua NH; family/cosmetic mix, laser dentistry, 3D printing, sedation; 4 doctors, 35 years) | Digital spend: Sesame 24-7 subscription (patient-communication + site bundle - redirectable budget)
• Hooks: 1) Four partner-dentists and 840 Birdeye reviews served by a default Sesame template 2) 35-year 'since 1990' story, laser dentistry and 3D printing not showcased; homepage leads with an office-dog caption
• Pitch/offer: Standard practice redesign: outcomes gallery, doctor-led story, review integration - $8-12k standard tier
• Sources: kalilandkress.com (curl raw HTML + WebFetch); Birdeye Nashua NH directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Northeast (wave 2)

18. Park Cities Dental Group (Dr. Phillip Allison / Dr. Ted Smith) - Dallas (Highland Park), TX - https://www.parkcitiesdentalgroup.com/ - 75/100 - MEDIUM-HIGH (medium confidence - owner not stated on page)
• Est/Doctors: 1982 (VERIFIED - homepage 'ESTABLISHED IN 1982') | Drs. Phillip Allison, DDS and Ted Smith, DDS, FICOI (Pankey Institute post-doc, Misch Institute training) - VERIFIED on /about-pcdg/ | Reviews: Birdeye 4.9 (546 reviews; JSON-LD aggregateRating, 2026-09-30); Dr. Ted Smith separate Birdeye profile 4.8 (25)
• Site (observed, raw HTML 2026-09-30): Avada/Elementor WordPress 6.8.10: homepage HTML is 1.62 MB for only ~1,750 characters of visible copy; footer reads 'Copyright 2007 - 2025© Park Cities Dental Group.' (stale, reversed (c)); a stray post byline prints on the live page: 'Home Phillip Allison 2025-02-05T07:22:21+00:00'; a SiteGround JS captcha ('You are being redirected... Javascript is required') intermittently intercepts non-browser clients (INFERRED crawl/SEO risk). Only 4 service blurbs ('Learn More' stubs).
• Social gap: UNKNOWN (no social links in homepage HTML)
• Breakdown: FC15/20 BM13/15 WW10/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech7 (/10)
• Independence: INFERRED - named doctors, 'Established in 1982', no DSO/affiliate strings in HTML scan, own domain/email | Decision-maker: Dr. Phillip Allison (INFERRED - YP listing + homepage byline; confirm owner vs. Dr. Ted Smith on call)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - 3110 Webb Ave Ste 300 (Highland Park/Knox area) with 'complimentary valet parking'; implants, Zoom, Invisalign, iTero, sedation = high tier | Digital spend: Custom WordPress build (Avada); Birdeye review profile (INFERRED from 546-review corpus)
• Hooks: (1) 'Your footer says Copyright 2007 - 2025 and the homepage prints a raw timestamp byline - on a practice with 546 five-star reviews since 1982.' (2) '1.6 MB of page for four one-line service blurbs - none of your Pankey/Misch-level implant credentials are on the homepage.'
• Pitch/offer: Flagship Highland Park implant/cosmetic homepage that puts Pankey/FICOI credentials and the 546-review corpus up front; keep existing forms; $10-12k (standard) - up to $12-15k if two-doctor group confirmed.
• Sources: curl of homepage + /about-pcdg/ (2026-09-30); reviews.birdeye.com Park Cities Dental Group (JSON-LD); YellowPages Highland Park listing; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: South-Central (wave 2)

19. Harbor Dental — Plymouth, MN — harbordentalmn.com — 75/100 — MEDIUM-HIGH (medium)
• Est/Doctors: 'more than 30 years' serving Plymouth (Demandforce profile text, VERIFIED); 'Awarded Top Dentist Every Year Since 2006' by Mpls.St.Paul Magazine (VERIFIED, /about-us/awards/); 4 dentists; implants, Invisalign, veneers, sedation-free family scope listed | Reviews: 2,941 reviews, 5-star aggregate, 99.4% would refer (Demandforce local.demandforce.com/b/harbordentalmn, VERIFIED via fetch; customers since 1995 shown). The homepage carries only a 'Patient Reviews' menu link.
• Site (observed): ProSites litesite — raw HTML footer "Copyright � 2019 Prosites, Inc.  All Rights Reserved." (mojibake + frozen 2019) and asset path styles.prosites.com/litesite; <title> "Family Dental Care in Plymouth, MN | Harbor Dental"; menu is a 40-link ProSites procedure tree (Panoramic X-rays, Dental Videos, Cherry Payment Plans) (VERIFIED curl)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC15/20 BM13/15 WW10/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM1/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — legal entity 'Harbor Dental, PA', single address (3001 Harbor Ln N), phrase 'big practice capabilities with small practice values'; no DSO strings in raw HTML; confirm owner on call (MEDIUM-HIGH confidence) | Decision-maker: UNKNOWN principal — four dentists named (VERIFIED): Dr. Barry Panning (DDS 2000, listed first), Dr. Nicole Haus, Dr. Travis Wildenberg, Dr. Callan Bock
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — four-dentist practice, Plymouth MN (affluent NW Twin Cities suburb), 30+ yrs | Digital spend: ProSites subscription (redirect target); Demandforce; Cherry financing; collectcheckout pay link
• Hooks: 1) Voted Top Dentist by Mpls.St.Paul Magazine every year since 2006 yet footer still reads 'Copyright � 2019 Prosites' 2) 2,941 Demandforce reviews are one menu click away, not on the page
• Pitch/offer: Award- and review-forward relaunch of a 4-dentist practice; keep Cherry/pay links; leave ProSites. $10–14k
• Sources: harbordentalmn.com raw HTML + /about-us/the-dentists/ + /about-us/awards/; local.demandforce.com/b/harbordentalmn
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 2)

20. Highland Smiles Dental (Dr. Girish Sandadi / Dr. Rachna Patel) - Dallas (Highland Park / McKinney Ave), TX - https://www.highlandsmilesdental.com/ - 74/100 - HIGH (medium confidence - founding year UNKNOWN)
• Est/Doctors: UNKNOWN (founding year not on site) | Dr. Girish Sandadi, DDS (US Army Reserve since 2009) + Dr. Rachna Patel, DMD (Baylor 2008) - 2 doctors VERIFIED | Reviews: Birdeye 4.8 (1,991 reviews; JSON-LD aggregateRating, 2026-09-30); directory snippet cites 1,548 patient reviews for Dr. Sandadi
• Site (observed, raw HTML 2026-09-30): TNT Dental template: footer '(c) 2018 Highland Smiles Dental | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental' and '<!-- TNT Dental Content Management System -->' (VERIFIED raw HTML); legacy Universal Analytics ID UA-133108731-1 still loaded; Google Maps embed stamped Dec-2018 (4v1544134232876); title is generic 'Dentist Highland Park | Cosmetic Dentistry | Highland Smiles Dental'. /reviews.html is a 17 KB page that does not surface the ~2,000-review corpus.
• Social gap: Facebook page facebook.com/HighlandSmilesDental (follower count UNKNOWN - login-walled)
• Breakdown: FC15/20 BM11/15 WW10/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap9 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - owner-doctor narrative ('too many dental offices put profits over people'), own patient portal, no group/DSO strings in HTML | Decision-maker: Dr. Girish Sandadi, DDS (owner per directory listing - INFERRED; About page centres him)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - 4925 McKinney Ave (Knox-Henderson/Highland Park edge); implants incl. All-On-4, veneers, SureSmile, Zoom, sedation; ~2,000 reviews implies very high patient throughput = high tier | Digital spend: TNT Dental (VERIFIED footer), Google Analytics UA + GA4, Facebook page
• Hooks: (1) 'About 2,000 five-star reviews and the footer still says (c) 2018.' (2) 'You are one of the most-reviewed practices in Highland Park but the homepage is a stock TNT template with a 2018 map embed.'
• Pitch/offer: Premium Highland Park implant + cosmetic homepage that foregrounds the review volume; keep existing portal; $10-12k.
• Sources: curl + raw HTML (2026-09-30); reviews.birdeye.com Highland Smiles Dental JSON-LD; /meet-the-dentists.html; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 2)

21. Devine Dental LLC (Devine & DeFina) — Greenwich, CT — https://www.dentistofgreenwich.com/ — 74/100 — MEDIUM-HIGH(medium)
• Est/Doctors: In practice since 1977; current Greenwich location since 1990 (VERIFIED, About page); 2 doctors | Reviews: Thin public corpus: Birdeye 15 + 9 reviews (two listings, ~5.0); Healthgrades 11 reviews (4.6/5 recommend); RateMDs 4.5/5; Yelp listing exists with a few complaints about 'unnecessary procedures'; no Google count retrievable (VERIFIED via WebSearch snippets, 2026-09)
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved" (mojibake, frozen); homepage <title> "Cosmetic Dentistry Greenwich | Welcome | Devine Dental LLC" (generic "Welcome" filler); http:// URL does not redirect to https (http://www.dentistofgreenwich.com/ stays http); 78KB template page for a Pankey-lineage Greenwich practice
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC16/20 BM14/15 WW11/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap7 Dep7 Tr9 Tech8 (/10)
• Independence: INFERRED — About page names two owner-dentists (Devine, DeFina); legal name Devine Dental LLC; no group/DSO language, no DSO strings in raw HTML; booking/portal domain not identified | Decision-maker: Barbara J. Devine, DMD, MAGD (owner) / Vincent B. DeFina, DMD, FAGD
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 1 (Greenwich 06830 market; comprehensive/Pankey-style care; two senior doctors) | Digital spend: ProSites subscription (2019-era template)
• Hooks: 1) Both doctors are Pankey Institute alumni; Dr. Devine "has been part of the Visiting Faculty at the Pankey Institute since 1996" yet the site title says just "Welcome" 2) Footer still reads "Copyright � 2019 Prosites, Inc." and the http:// address does not force https
• Pitch/offer: Comprehensive-dentistry flagship redesign that leads with Pankey credentials and case gallery — $12–15k group-flagship tier. Retirement-horizon flag (in practice since 1977): probe succession before pitching.
• Sources: Live fetch of dentistofgreenwich.com (homepage raw HTML + /our-practice/meet-the-doctors/); YellowPages Greenwich listing | Wave-2 review enrichment (2026-09-30): Healthgrades, RateMDs, Yelp snippets; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

22. Pacific Dental Associates (Duhn family; NOT Pacific Dental Services) — San Francisco (Pacific Heights), CA — https://www.pacificdentalassociates.com/ — 74/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: Serving Pacific Heights since 1984 (VERIFIED on site, 'Established in 1984') | 3 doctors + in-house prosthodontics/perio/OMS listed | Reviews: Birdeye 49 reviews; Yelp 28 (practice listing) + 32 (Stafford Duhn DDS listing) = ~109 across platforms; Google count not retrievable. One Yelp reviewer calls it 'wildly overpriced' (unmanaged? no reply seen). Third dentist Anisha Kahai DDS also listed. Source: birdeye.com, yelp.com via WebSearch
• Site (observed): ProSites (VERIFIED: HTML comment 'Prosites Web Engine Technology Version 4.0' in source; ProSites asset structure). Homepage <title> is the generic 'Dentist in Pacific Heights, San Francisco' (no practice name). Doctor names and credentials are buried two clicks deep at /about/meet-the-doctors/. Hero states '35 Years of Quality Dental Care' while body says 'over 30 years' - inconsistent. Only 3 testimonials, no star/count widget.
• Social gap: Facebook profile exists (profile.php?id=100069121071001 - un-vanity URL); activity level UNKNOWN.
• Breakdown: FC16/20 BM13/15 WW11/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp1/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech8
• Independence: INFERRED - Duhn family name on bios; no PDS branding ('Dentists of ...'/'Modern Dentistry'); no ownership or group language; name resembles PDS but domain, address (2100 Webster St #325) and staffing are local. Verify on call. | Decision-maker: Dr. Stafford Duhn (DDS, FICD, FPFA - senior partner); Dr. Christopher Duhn (DDS, FACP, board-certified prosthodontist, joined ~2020)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Pacific Heights address, prosthodontist + perio + OMS under one roof, UOP faculty ties (tier: upper) | Digital spend: ProSites subscription, Matomo analytics
• Hooks: 'Your homepage does not show a single doctor's name or credential - Dr. C. Duhn is a board-certified prosthodontist and UOP faculty.' / Generational handoff (Stafford 1984 grad to Christopher) is a natural rebrand moment.
• Pitch/offer: Credential-forward Pacific Heights rebuild keeping their existing booking; $8-12k standard.
• Wave-2 update (2026-09-30): 76 -> 74. Reputation corpus is real but modest (~110), so Gap trimmed 12->11 and score 76->74. Live; ProSites 'Copyright � 2019 Prosites, Inc.' still in footer.
• Sources: Raw HTML curl (200, ProSites engine comment), WebFetch home + /about/meet-the-doctors/
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: West (wave 1)

23. Marin Dental Implant Center / David W. Epstein, DDS, Inc. — Novato, CA — https://novatoimplantdentist.com/ — 74/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: 'placed and restored over 20,000 implants in the last 30 years' (self-stated; INFERRED ~30 yrs in practice) | ABOI/ID Diplomate per second site | 1 doctor | Reviews: Yelp 47 reviews (David W Epstein DDS, Aug 2026); Google count not retrievable. Source: yelp.com via WebSearch
• Site (observed): Two competing live domains for one practice (VERIFIED): novatoimplantdentist.com (GoDaddy Website Builder 8.0 generator; footer 'Copyright © 2019 Marin Dental Implant Center - All Rights Reserved'; <title> is just 'Marin Dental Implant Center') and davidepsteindds.com (Wix; title 'David Epstein, DDS | Full Dental Implant Specialist | Novato, Marin County, California, United States'). The GoDaddy site's header CTA links to davidepsteindds.com/contact-novato-dentist.
• Social gap: UNKNOWN
• Breakdown: FC14/20 BM12/15 WW13/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp1/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech9
• Independence: VERIFIED - single-doctor practice under David W. Epstein, DDS, Inc.; no group language. | Decision-maker: David W. Epstein, DDS (owner, solo; VERIFIED - 'One Doctor. One Location.')
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Marin County market, in-house 3D CT + digital impressions + prosthetic lab; but 'All PPO Dental Insurance Accepted' tempers ticket (tier: mid-upper) | Digital spend: GoDaddy builder + Wix subscription (two)
• Hooks: 'You are paying for two websites and neither shows your Diplomate credential above the fold.' / 20,000 implants / 30 years is not mentioned in either page title.
• Pitch/offer: Consolidate two domains into one premium implant-authority site; $5-8k solo.
• Wave-2 update (2026-09-30): 75 -> 74. Practice actually runs FOUR web properties: novatoimplantdentist.com (GoDaddy builder, (c)2019), davidepsteindds.com (Wix), marindentalimplants.com (Wix, (c) 2025) - so the pitch is consolidation of a sprawl, not a single frozen site. Live.
• Sources: curl fingerprints of both domains; WebFetch novatoimplantdentist.com
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: GoDaddy · region: West (wave 1)

24. Total Dental Solutions for Adults (Dr. George A. Hoop) — Fort Myers, FL — https://www.wemakeyousmile.com/ — 74/100 — MEDIUM-HIGH (confidence: MEDIUM-HIGH)
• Est/Doctors: In private practice since 1991 (VERIFIED, site); Emory DDS; ICOI, Misch, Pikos, Pankey memberships (VERIFIED, site); adults-only practice | 3 providers listed: Drs. Hoop, Chouraqui, Streater; sister TNT domain wemakeyousmilenaples.com (North Naples) suggests 2nd office - verify | Reviews: Aggregate "4.9 stars" per directory listings; no verifiable review COUNT found (Healthgrades group page has reviews, Yelp has photos only, BBB listed) - UNKNOWN count [WAVE 2]
• Site (observed): TNT Dental. <title>Dentist</title> (one word). Footer: "©2020 Total Dental Solutions for Adults" and TNT Dental design credit. Rendered page shows a dead internal link (dental-crowns-bridges.html). JSON-LD: "description": "Dentist in Fort Myers, FL.", 12630 Whitehall Dr., Fort Myers 33907.
• Social gap: Facebook (facebook.com/totaldentalsolutionsforadults) and YouTube channel exist (VERIFIED links); activity UNKNOWN
• Breakdown: FC15/20 BM12/15 WW12/15 Gap11/15 Dep7/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Gap 7 Dep 7 Tr 8 Tech 9
• Independence: INFERRED — 'Dr. Hoop's practice', founder in structured data, footer entity is the practice itself; only vendor is TNT Dental. (Note: patients call him 'periodontist and dentist' — services include crowns, Invisalign, emergencies, full-mouth reconstruction, so treated as general/implant practice, not a standalone perio referral office — confirm on call.) | Decision-maker: Dr. George A. Hoop, DDS (founder — VERIFIED via JSON-LD "founder")
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Implants, dentures, full-mouth reconstruction with Misch/Pikos/Pankey training — SW Florida retiree/implant market — Mid-High | Digital spend: TNT Dental subscription (observed) — redirectable
• Hooks: 1) Homepage title is literally "Dentist". 2) 35 years in practice and Pankey/Misch/Pikos-trained, but the site is stamped ©2020 with a dead crowns/bridges link.
• Pitch/offer: Implant/full-mouth reconstruction redesign — $8–12k
• Sources: wemakeyousmile.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 1)

25. Robert I. Halle, DMD, PC — Commack, NY — https://www.halledental.com/ — 74/100 — MEDIUM-HIGH(low-medium)
• Est/Doctors: 'Decades of experience' (homepage; exact year UNKNOWN); solo PC | Reviews: Very large corpus: Demandforce 1,317 reviews / 5.0 (100% would refer) (VERIFIED via WebFetch, shared listing with former partner Richard Tesser DMD); Healthgrades patient-experience ratings based on 103 reviews; Yelp listing; site has /read-our-reviews/ page
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; title " Dentist in Commack, NY | Robert I. Halle, DMD, PC " (leading/trailing whitespace, generic pattern); 109KB template; lists Medit i900 digital impressions and CEREC but as small nav items
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM12/15 WW11/15 Gap14/15 Dep8/10 Tr6/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap9 Dep6 Tr8 Tech8 (/10)
• Independence: INFERRED — 'Robert I. Halle, DMD, PC' solo; no group language | Decision-maker: Robert I. Halle, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2-3 (Suffolk County; CEREC, Medit scanner) | Digital spend: ProSites subscription
• Hooks: 1) CEREC + Medit i900 buried in nav on a 2019 ProSites template 2) Mojibake copyright footer 3) Practice relocated to a newly constructed Commack office in Oct 2023 (search snippet) yet the site is still ProSites-2019 while a 1,300-review Demandforce corpus is invisible on the homepage
• Pitch/offer: Solo redesign — $5–8k solo tier.
• Sources: Live fetch halledental.com (home, meet-the-doctors) | Wave-2 review enrichment (2026-09-30): Demandforce 1,317, Healthgrades 103; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

26. Paolucci Family Dentists (with Paolucci Lincoln Dental Associates) - Providence / Lincoln, RI - https://www.paoluccifamilydentists.com/ - 74/100 - MEDIUM-HIGH (medium)
• Est/Doctors: 'Since opening our doors in 1957' (VERIFIED, homepage); 6 doctors named incl. a periodontist and board-certified endodontist (Paolucci, Mohamed, Cathcart, Mirucki, Govostes, Evans); Providence + Lincoln offices | Reviews: Birdeye 1,571 reviews / 4.9 (Providence listing) and 1,903 / 4.9 (Lincoln Dental Associates: Mark Paolucci DMD listing) (Birdeye directory JSON-LD, 2026-09-30); homepage banner claims only 'Over 600 Five-Star Reviews!'
• Site (observed): Sesame 24-7 (footer "Website Powered by Sesame 24-7 (TM) | Site Map | Back to Top"); 42,792-byte template homepage; stale review claim "Over 600 Five-Star Reviews!"; second live domain lincolndentalassociatesri.com (title "Paolucci Lincoln Dental Associates | Dentist Lincoln RI", 21KB Sesame) = two competing domains for one family; nav 'Special Promotions' / 'Book Appointment' banner
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC14/20 BM14/15 WW10/15 Gap12/15 Dep8/10 Tr8/10 Cv5/5 Sp2/3 DM1/2 | Subs: Gap9 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED (MEDIUM-HIGH) - family-named practice since 1957, no group/DSO language or DSO strings in raw HTML; two separate Paolucci domains/entities so ownership split between Providence and Lincoln is not confirmed - verify on call | Decision-maker: Anthony D. Paolucci, DMD (Providence) / Mark L. Paolucci, DMD (Lincoln Dental Associates) - which one controls marketing UNKNOWN
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2-3 (Providence/Lincoln RI; multi-specialty, 6+ doctors, 65-year brand; volume/insurance-leaning positioning) | Digital spend: Two Sesame 24-7 subscriptions (one per domain)
• Hooks: 1) Stale '600 reviews' banner vs 3,400+ real reviews across two Birdeye listings 2) Two separate Sesame sites for one 1957 family brand - consolidation pitch
• Pitch/offer: Group-flagship: consolidate two sites into one brand with doctor/specialist directory + review integration - $12-15k group tier
• Sources: paoluccifamilydentists.com and lincolndentalassociatesri.com (curl raw HTML); Birdeye Providence RI + Lincoln RI directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Northeast (wave 2)

27. Pioneer Valley Dental Arts (Evans / Ziemba / Reilly / Lucido) — Longmeadow, MA — https://www.pioneervalleydentalarts.com/ — 74/100 — MEDIUM(medium)
• Est/Doctors: Dr. Evans in private practice since 1985 (VERIFIED, bio); 4 doctors named (Evans, Ziemba, Reilly, Lucido) | Reviews: Birdeye 285 reviews / 4.9; Dentascore 149 reviews; BBB, Yelp, Nextdoor listings; 4 doctors incl. AACD-accredited Dr. Evans (VERIFIED via snippets)
• Site (observed): Dental Revenue template (WP Engine, theme folder "ziemba"); footer "Copyright 2018, All Rights Reserved" and "Dental Marketing by Dental Revenue"; title "Dentist Longmeadow MA | Cosmetic Dentistry | Dental Implants"; 87KB generic nav-heavy homepage
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC15/20 BM13/15 WW9/15 Gap12/15 Dep8/10 Tr8/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — theme named for owner Ziemba; four named DMDs with bios; no group language or DSO strings | Decision-maker: Mark Evans, DMD (senior partner; AACD accreditation candidate, AAID); Dr. Ziemba
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (Longmeadow affluent suburb; implants, veneers, sedation, orthodontics in-house) | Digital spend: Dental Revenue marketing + WP Engine hosting
• Hooks: 1) Theme folder literally named "ziemba" and a ©2018 footer on a four-doctor practice 2) Dr. Evans is an AACD accreditation candidate + AAID member since 1985 — not visible on the homepage
• Pitch/offer: Multi-doctor group redesign — $8–12k standard tier; Dental Revenue contract redirect.
• Sources: Live fetch pioneervalleydentalarts.com (home + /longmeadow-ma-dentist-dr-mark-evans/) | Wave-2 review enrichment (2026-09-30): Birdeye 285, Dentascore 149; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Dental Revenue · region: Northeast (wave 1)

28. OKC Dental Arts (Drs. Michael Fling & Cama Cord) — Oklahoma City (NW 63rd St), OK — http://okcdentalarts.com/ — 73/100 — HIGH (medium confidence)
• Est/Doctors: Dr. Michael Fling (40+ yrs in dentistry, began as lab technician — VERIFIED) + Dr. Cama Cord (OU College of Dentistry — VERIFIED); practice est. UNKNOWN | Reviews: Birdeye 4.9 (431 reviews); Facebook 100% recommend (89 reviews); Dentascore 272; BBB profile; Yelp only 11 - web-search snippets 2026-09-30
• Site (observed): served on plain http://okcdentalarts.com (VERIFIED, curl 200 on http); page <h1> is 'Patient Reviews'; markup uses Bootstrap 3 'glyphicon' classes (2011-2016 lib); footer '© OKC Dental Arts. All rights reserved.' with 'Website Design & Marketing by Optima' and assets from optimasites.cloudfront (VERIFIED).
• Social gap: UNKNOWN.
• Breakdown: FC14/20 BM13/15 WW12/15 Gap12/15 Dep7/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — no DSO/group language; grep of HTML clean | Decision-maker: Dr. Fling / Dr. Cord (UNKNOWN which holds equity)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — NW OKC (73116, Nichols Hills-adjacent), implants/Botox/Invisalign/TMJ menu = mid tier | Digital spend: Optima marketing/hosting subscription (VERIFIED footer)
• Hooks: (1) "A 40-year veteran and an OU-trained associate/partner — the site is still an http-only Bootstrap-3-era page." (2) "Your H1 is 'Patient Reviews'."
• Pitch/offer: Two-doctor credibility-forward redesign keeping existing booking; redirect Optima spend; $8–11k.
• Sources: http://okcdentalarts.com/ (curl + WebFetch).
• Wave-2 update (2026-09-30): score 69 -> 73. Reviews found: Birdeye 431 @4.9 - large corpus vs an Optima-platform site. URL live (200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: South-Central (wave 1)

29. Hagerstown Smiles Dental Care — Hagerstown, MD — https://www.hagerstownsmiles.com/ — 73/100 — HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Founded 1986 by J. Bruce Burley DDS FAGD (now retired, fills in) [VERIFIED on site]; Dr. J. Brandon Burley DDS, Dr. Brandy Behrens DDS, Dr. Kyle Briggs DDS (+ founder) [VERIFIED on site] | Reviews: Site claim '1000+ Google Reviews' [VERIFIED in raw HTML]; Birdeye 180 reviews, 4.9; Yelp 12 (search 2026-09-30). Practice since 1986 (Dr. J. Bruce Burley)
• Site (observed): ProSites. Footer: "2026 Hagerstown Smiles Dental Care" + "Dental Website Design Powered by ProSites"; source comment "Copyright � 2019 Prosites, Inc." (mojibake); UA-72590405-1 retired Analytics; boilerplate meta description ('are a group of dentists dedicated to...'). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook and TikTok links present [VERIFIED].
• Breakdown: FC10/20 BM12/15 WW11/15 Gap14/15 Dep8/10 Tr8/10 Cv5/5 Sp3/3 DM2/2 | Gap9 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (founder-family practice; no group language) | Decision-maker: Dr. J. Brandon Burley DDS (second-generation lead; owner status INFERRED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Hagerstown/Washington County mid-tier market, implants + sedation + cosmetic, 3 active dentists -> lower-mid tier | Digital spend: ProSites subscription; Google review link; patient payment portal
• Hooks: 1) '1000+ Google Reviews' is a plain text link on a ProSites page. 2) Founder Bruce Burley retired; second-generation Burley now leads.
• Pitch/offer: Review-corpus-led redesign; $6-9k.
• Sources: hagerstownsmiles.com raw HTML + rendered fetch of home and /meet-the-doctors (2026-09-30)
• Wave-2 note: score 70 -> 73 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

30. Ridgepointe Dental (Austin Amos DDS, JD) — The Colony, TX — https://www.ridgepointedental.com/ — 73/100 — HIGH (medium confidence)
• Est/Doctors: 1979 | Dr. Austin Amos, DDS, JD | Reviews: Birdeye 4.9 (905 reviews; earlier snippet 904); Yelp 27; BestProsInTown 79 - verified via Birdeye JSON-LD reviewCount 905
• Site (observed): 'Copyright © 2017 Ridgepointe Dental | Privacy Policy | Sitemap | Site designed and maintained by TNT Dental' (VERIFIED); text still says 'nearly 40 years' (stale).
• Social gap: UNKNOWN. • Breakdown: FC13/20 BM14/15 WW11/15 Gap13/15 Dep8/10 Tr7/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap9 Dep8 Tr7 Tech7 (/10)
• Independence: INFERRED | Decision-maker: Dr. Amos
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Main St, The Colony (Frisco-adjacent), implants/All-on-4/Invisalign = mid tier | Digital spend: TNT
• Hooks: (1) '~40 years' text is itself out of date. (2) 47th anniversary approaching.
• Pitch/offer: $6–8k.
• Sources: https://www.ridgepointedental.com/ (curl + WebFetch).
• Wave-2 update (2026-09-30): score 59 -> 73. Reviews found: Birdeye 905 @4.9 (JSON-LD) - large corpus vs a TNT site with 'Copyright (c) 2017'; est. 1979. URL live (200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 1)

31. Main Line Dental Aesthetics (James A. Godorecci Jr., DMD) — Paoli, PA — https://www.paolidentist.com/ — 73/100 — HIGH (HIGH confidence on site/reviews; MEDIUM on ownership scale)
• Est/Doctors: Practice acquired by Dr. Godorecci in 2010; 30+ yrs in practice (Penn Dental 1993) [VERIFIED on site]; 1 principal dentist (Dr. Godorecci, Penn Dental 1993, former Penn clinical instructor; AACD member; Invisalign, E4D/CEREC); staff tenure 20+ yrs (office manager) [VERIFIED on site] | Reviews: Birdeye 585 reviews, 4.9 (Birdeye Paoli listing, crawl 2026-09-30; search snippet 565); Yelp listing; Healthgrades 5 (Dr. Godorecci)
• Site (observed): ProSites template. Title verbatim: "Dentist in Paoli, PA | Main Line Dental Aesthetics". Footer verbatim: "Site Developed by ProSites.com". Page source carries the ProSites legal block "Copyright � 2019 Prosites, Inc." (mojibake). Reviews sit on a separate 'Reviews' page; the homepage does not surface the 585-review corpus. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook link on site [VERIFIED]; follower counts UNKNOWN. 585 Birdeye reviews are not surfaced on the homepage [VERIFIED].
• Breakdown: FC14/20 BM11/15 WW11/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (owner-dentist bio: 'acquired Main Line Dental Aesthetics in 2010'; single office at 91 Chestnut Rd; no group/entity language on About, footer or booking) - HIGH confidence, verify on call | Decision-maker: Dr. James A. Godorecci Jr., DMD (owner since 2010)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Main Line/Paoli affluent market; CEREC/E4D same-day crowns, veneers, implants, sleep-apnea appliances, laser; solo owner -> upper-mid tier | Digital spend: ProSites subscription; online appointment request; Invisalign provider
• Hooks: 1) 585 Birdeye reviews (4.9) sit off the homepage on a ProSites template whose title is a generic 'Dentist in Paoli, PA'. 2) Owner-dentist since 2010 - a 16-year mark with AACD/E4D credentials that the template never showcases.
• Pitch/offer: Premium homepage that leads with smile-gallery/CEREC/AACD credentials and surfaces the 585-review proof; keep existing booking. $5-8k (solo owner).
• Sources: paolidentist.com raw HTML + WebFetch (2026-09-30); reviews.birdeye.com/d/dental/paoli-pa (crawl 2026-09-30); Healthgrades; WebSearch
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 2)

32. Locust Valley Dentistry — Locust Valley, NY — https://www.locustvalleydentistry.com/ — 73/100 — MEDIUM-HIGH(medium)
• Est/Doctors: Opened 1995 as Locust Valley Dentistry (VERIFIED, homepage); 2+ doctors visible | Reviews: Birdeye 78 reviews / 5.0; Yelp listing present (count not retrieved); site has a patient-reviews page (VERIFIED via snippet)
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved" (mojibake); homepage title "Welcome | Locust Valley, NY | Locust Valley Dentistry" (generic Welcome); 125KB template; implant, Invisalign and veneer pages but no visual case work above the fold
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC16/20 BM11/15 WW11/15 Gap12/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — two named DMDs; opened as independent 'Locust Valley Dentistry' in 1995; no DSO language | Decision-maker: Dr. Schmitz, DMD (first name UNKNOWN) — with Erika Schweighardt, DMD
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 1 (North Shore Gold Coast market; implants/cosmetic emphasis) | Digital spend: ProSites subscription
• Hooks: 1) "We opened our doors as Locust Valley Dentistry in 1995" — 30-year anniversary just passed on a 2019 ProSites template 2) Title tag literally begins "Welcome |"
• Pitch/offer: Gold Coast premium redesign — $8–12k standard tier.
• Sources: Live fetch locustvalleydentistry.com (raw HTML + meet-the-doctors); YellowPages Oyster Bay listing | Wave-2 review enrichment (2026-09-30): Birdeye 71 reviews; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

33. Dental Group West — Toledo, OH — dentalgroupwest.com — 73/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Founding year UNKNOWN (site has an 'Our History' page not captured); 3 dentists listed (VERIFIED); recent-associate announcement 'Dental Group West Welcomes Dr. Quinn Crago' (VERIFIED) | Reviews: 4.7 on 126 reviews (Birdeye, reviews.birdeye.com/dental-group-west-154301912); est. 1969 per directory snippet (INFERRED); doctors named in listings: Thomas, Weisenburger, Poole, Aridi, Crago; some negative TMJ review noted. [Wave-2 enrichment]
• Site (observed): TNT Dental — footer credit tntdental.com; dead Google+ link in raw HTML "plus.google.com/116880711539601348852/"; <title> "Dentist Toledo, OH | Accepting New Patients | Dental Group West"; separate 'Dentist Near Ottawa Hills' landing page; menu lists Full Mouth Reconstruction, Porcelain Veneers, Sedation, Implants, Invisalign (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC14/20 BM12/15 WW12/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM1/2 | Subs: Gap7 Dep7 Tr8 Tech8 (/10)
• Independence: MEDIUM confidence — verify on call: generic 'Dental Group West' brand name (group-style pattern) but three named dentists and no DSO/parent language in HTML; ownership entity not confirmed | Decision-maker: UNKNOWN (dentists: Dr. Tracy Poole, Dr. Quinn Crago (new associate), Dr. Richard Thomas; principal not stated on pages read)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — 3-dentist full-scope practice serving Ottawa Hills/West Toledo (affluent pocket) | Digital spend: TNT Dental (redirect target)
• Hooks: 1) Live dead-Google+ link (plus.google.com/1168…) in a 3-dentist practice's HTML 2) 'Accepting New Patients' in the title tag — the homepage's main SEO string is a status line, not a value proposition
• Pitch/offer: Multi-doctor full-mouth-reconstruction/cosmetic positioning site, keep patient-pay links. $8–12k
• Sources: dentalgroupwest.com raw HTML + rendered nav
• Wave-2 re-score: 70 -> 73. Est. 1969 and 3-5 doctors raise Business Maturity; 126 Birdeye reviews moderate.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Midwest (wave 1)

34. Transforming Smiles (Bruce E. Carter, DMD PC) — Lawrenceville, GA — https://www.gwinnettsmiles.com/ — 73/100 — MEDIUM-HIGH (confidence: MEDIUM)
• Est/Doctors: Dr. Carter 'practicing in this field since 1985 – well over 30 years' (VERIFIED, site About page); 'Best of Gwinnett County since 2002' and Chamber 'Physician of the Year' 2014 (site claims); 2 named doctors, 1 office (751 Old Norcross Rd) | Reviews: 'Over 500 5-Star Reviews On Google' (VERIFIED on-page text; Google count not independently confirmed); Healthgrades Dr. Carter 4.8 / 20 ratings (Healthgrades directory)
• Site (observed): TNT Dental template. Homepage <title>: "Dentist Lawrenceville, GA | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Transforming Smiles" (keyword-spam). Footer: "© Transforming Smiles | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental". Legacy Universal Analytics tag UA-50318718-1 still in source. 58KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC11/20 BM13/15 WW13/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap 7 Dep 8 Tr 8 Tech 9 (/10)
• Independence: INFERRED — entity 'Transforming Smiles - Bruce E. Carter, DMD PC', single office, no group/'division of' language, no booking-domain or theme markers | Decision-maker: Dr. Shariq Zafrani, DMD (operating dentist, probable successor) and founder Dr. Bruce E. Carter, DMD, FAGD (owner status INFERRED)
• FinCap: Lawrenceville/Gwinnett suburban, full-mouth reconstruction + veneers + implants offered; two-doctor tenure practice — Mid | Digital spend: TNT Dental (footer credit, retainer/hosting likely redirectable)
• Hooks: 1) Title tag literally reads 'Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care'. 2) 40-year founder plus successor doctor and 500+ Google reviews sit behind a stock TNT template.
• Pitch/offer: Generational-handoff flagship refresh for a Gwinnett cosmetic/restorative practice — $8–12k
• Sources: gwinnettsmiles.com raw HTML (curl) + about-our-dental-practice.html; WebFetch homepage; Healthgrades usearch (Carter); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 2)

35. Greater Baltimore Prosthodontics, PA — Towson, MD — https://www.gbpdental.com/ — 73/100 — MEDIUM-HIGH (MEDIUM: principal/owner not identified; site is more current than most vendor shells)
• Est/Doctors: '30+ years experience' (site) [VERIFIED on site]; founding year UNKNOWN; 6 dentists incl. prosthodontists: Arash M. Rostami DDS MS DICOI, Michael P. Linnan DDS, Maya M. Brooks DMD, Pegah Ghiasi DDS MS, Tareq Haddad DDS, W. Maxwell Wahle DDS MS FACP; 'Top dentists - Baltimore Magazine' (site claim) [VERIFIED on site] | Reviews: Birdeye 1,070 reviews, 5.0 (crawl 2026-09-30; search snippet shows 813); Yelp 16; Nextdoor and Facebook pages exist
• Site (observed): Dentalfone template. Title verbatim: "Greater Baltimore Prosthodontics, PA – Welcome To Our Site" (placeholder-style title; meta description "Welcome to Our Towson, MD office We love serving patients in the Towson or Baltimore area"). Footer verbatim: "DESIGN AND CONTENT © 2013- 2026 BY DENTALFONE". Homepage shows seven testimonials, not the ~1,000-review corpus. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook page (gbpdental) exists; counts UNKNOWN.
• Breakdown: FC15/20 BM14/15 WW9/15 Gap12/15 Dep8/10 Tr7/10 Cv4/5 Sp3/3 DM1/2 | Subs: Gap8 Dep8 Tr7 Tech8 (/10)
• Independence: INFERRED (PA of named prosthodontists/general dentists; Towson office; no group or DSO language on site) - MEDIUM confidence, verify on call | Decision-maker: UNKNOWN principal (six-doctor prosthodontic PA; Drs. Michael P. Linnan and Arash M. Rostami are the names most cited in reviews)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Towson/Baltimore County; prosthodontic + implant + full-arch and on-site lab work; six-doctor specialty group -> upper tier | Digital spend: Dentalfone design+content subscription (2013-2026 credit); on-site lab
• Hooks: 1) Six-doctor prosthodontic group whose homepage title is literally 'Welcome To Our Site' despite ~1,000 five-star reviews. 2) Complex-case (implant/full-arch) specialty positioned on a stock Dentalfone shell.
• Pitch/offer: Specialty-grade rebrand: case galleries for full-arch/veneer, doctor pages, review wall. $12-15k (group flagship).
• Sources: gbpdental.com raw HTML + WebFetch (2026-09-30); reviews.birdeye.com/d/dental/towson-md; WebSearch
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Dentalfone · region: Mid-Atlantic (wave 2)

36. Gates Family Dentistry — Loveland, OH — gatesfamilydentistry.com — 73/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Founded 1979 by Dr. John P. Gates; 'over 40 years'; father-to-son handoff after 2016 retirement (VERIFIED, site); '2 dentists, 3 dental hygienists, 4 dental assistants, and 3 administrative assistants' (VERIFIED) | Reviews: 1,994 reviews, 5-star aggregate, 99.2% would refer (Demandforce local.demandforce.com/b/gatesfamilydentistry, VERIFIED via fetch; customers since 1992 shown).
• Site (observed): ProSites — raw HTML footer "Copyright � 2019 Prosites, Inc.  All Rights Reserved." (mojibake, frozen 2019); <title> "Loveland Dentist | Dr Gregory Gates | Dr Robert Capozza | Gates Family Dentistry | Loveland OH 45140" (ZIP + two doctor names in the title); practice email gatesfamilydentistry@gmail.com; direct curl to the home URL intermittently times out (VERIFIED curl)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC12/20 BM13/15 WW11/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — family-founded single office (3249 West US 22 & 3), gmail address, no DSO strings in raw HTML; owner-successor language on About page | Decision-maker: Dr. Gregory Gates, DDS (VERIFIED, site: continuing father's vision after Dr. John P. Gates retired in 2016); Dr. Robert Capozza also named
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — two-dentist, 12-person team, Loveland OH (affluent NE Cincinnati exurb), 47 yrs | Digital spend: ProSites subscription (redirect target); Demandforce
• Hooks: 1) A 1979 founder-to-son practice with ~2,000 reviews on a 'Copyright � 2019 Prosites' template 2) ZIP code and two doctor names stuffed into the title tag
• Pitch/offer: Second-generation relaunch (heritage story + smile gallery), keep Demandforce. $8–12k
• Sources: gatesfamilydentistry.com raw HTML; local.demandforce.com/b/gatesfamilydentistry
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 2)

37. Devon Dental Associates (Drs. Steven Hart & Robert Rose) — Wayne (Devon/Berwyn), PA — http://www.devondental.com/ — 73/100 — MEDIUM (review enrichment wave 2, 2026-09-30)
• Est/Doctors: 'Since 1985' [VERIFIED on site]; 2 dentists: Dr. Steven Hart, Dr. Robert Rose ('dentists who practice together') [VERIFIED on site] | Reviews: 4.9/5 from 62 reviews (aggregator citing verified reviews, search snippet 2026-09-30); Yelp 17 (practice page) - mid-sized corpus, none shown on the 7.9KB homepage [VERIFIED]
• Site (observed): Sesame 24-7 ('Website Powered by Sesame 24-7'). The site FORCES plain http: https://www.devondental.com/ answers 301 -> http://devondental.com/ -> http://www.devondental.com/ ('Not Secure'); no viewport meta tag (not mobile-optimized); page is 7.7 KB with legacy _gaq/UA-20458549-1 Analytics; stale banner "We have officially moved into our new office at 995 Old Eagle School Road, suite 305"; .php URLs (office-location.php). Title: "Dentist Wayne PA | Devon Dental Associates". [VERIFIED raw HTML + curl, 2026-09-30]
• Social gap: Only a Facebook widget is present [VERIFIED]; no Instagram/YouTube. Gap in visible brand vs. a Main Line address.
• Breakdown: FC14/20 BM12/15 WW14/15 Gap9/15 Dep8/10 Tr9/10 Cv3/5 Sp2/3 DM2/2 | Gap8 Dep8 Tr9 Tech9 (/10)
• Independence: INFERRED (two-dentist partnership; no group language; footer only vendor credit) - verify on call | Decision-maker: Dr. Steven Hart / Dr. Robert Rose (owner split UNKNOWN)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Devon/Berwyn Main Line professional-office address (Old Eagle School Rd), new 'state of the art' facility -> upper-mid tier | Digital spend: Sesame 24-7 subscription; patient/doctor login portals; legacy Google Analytics
• Hooks: 1) The homepage is served over http only ('Not Secure') and has no mobile viewport - a Main Line practice a patient reaches on a phone. 2) Still shows a 'we have officially moved' announcement.
• Pitch/offer: Mobile-first, HTTPS premium rebuild for a 40-year Main Line practice; keep existing patient login links. $6-9k.
• Sources: devondental.com raw HTML + curl redirect check (2026-09-30)
• Wave-2 note: score 76 -> 73 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Mid-Atlantic (wave 1)

38. Comprehensive Esthetic Restorative & Implant Dentistry (Murali R. Ravel, DMD) — Bedford, NH — https://www.nhestheticdentistry.com/ — 73/100 — MEDIUM(low-medium)
• Est/Doctors: UNKNOWN (founding year not stated on fetched pages); doctors: Ravel + team | Reviews: Healthgrades 111 reviews / 4.7 (89% five-star) for Dr. Ravel; site has testimonials page; Yelp listing present (VERIFIED via WebFetch of Healthgrades)
• Site (observed): Sesame 24-7 ("Website Powered by Sesame 24-7™" footer, no copyright line); 18KB homepage; title is the practice name string "Comprehensive Esthetic Restorative & Implant Dentistry | Dentist Bedford NH"; page advertises CBCT (Galileos), CEREC, laser, full-mouth reconstruction with template-grade presentation
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM11/15 WW11/15 Gap12/15 Dep8/10 Tr8/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED — 'Welcome to the practice of Murali R. Ravel, DMD'; no group language | Decision-maker: Murali R. Ravel, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (technology stack: Galileos CBCT, CEREC CAD/CAM, laser, rotary endo, full-mouth reconstruction) | Digital spend: Sesame 24-7 subscription
• Hooks: 1) CBCT + CEREC + laser + full-mouth reconstruction are listed as plain nav items on a Sesame template 2) No copyright line at all in the footer
• Pitch/offer: Technology-forward implant/esthetic redesign — $8–12k standard tier.
• Sources: Live fetch nhestheticdentistry.com (home, meet-dr-murali-ravel) | Wave-2 review enrichment (2026-09-30): Healthgrades 111 reviews, 4.7; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Northeast (wave 1)

39. New Canaan Dental Care (Anthony T. Festa, DDS) - New Canaan, CT - https://www.newcanaandentalcare.com/ - 73/100 - MEDIUM (medium)
• Est/Doctors: 'After 32 years on South Avenue' - practice recently moved to a new Pine Street office (VERIFIED, homepage news); solo; 'Voted Connecticut's topDentists 2025' (homepage) | Reviews: Birdeye 184 reviews / 4.9 (Birdeye New Canaan directory JSON-LD, 2026-09-30; still lists the old 116 South Ave address)
• Site (observed): ProSites ("Site Developed by ProSites.com"); title includes ZIP "New Canaan CT 06840"; <link rel="canonical" href="http://www.newcanaandentalcare.com/" /> (canonical is plain http); second live domain http://newcanaancosmeticdentist.com/ serves the identical 77,842-byte page over plain http = two competing domains for one practice; homepage still carries the office-move news item
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC14/20 BM14/15 WW11/15 Gap11/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - solo owner-dentist named in title/bio; no group language or DSO strings in raw HTML | Decision-maker: Anthony T. Festa, DDS (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 1 (New Canaan 06840; sedation, veneers, makeovers; new office build-out) | Digital spend: ProSites subscription + second domain
• Hooks: 1) New office after 32 years is a natural re-launch moment 2) Two live domains (one plain http, canonical http) split SEO for a topDentists-listed practice; retirement-horizon flag - probe succession
• Pitch/offer: Solo relaunch tied to the new office - $5-8k solo tier (upper end for New Canaan)
• Sources: newcanaandentalcare.com + newcanaancosmeticdentist.com (curl raw HTML); Birdeye New Canaan CT directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 2)

40. Heights Family Dentistry (Carol L. Price DDS PC) — Houston (Heights), TX — http://www.heightsfamilydentistry.com/ — 72/100 — HIGH (medium confidence — tenure and reviews UNKNOWN)
• Est/Doctors: UNKNOWN est. (site says 'experienced'; do not assume) | Dr. Carol L. Price, DDS, PC (VERIFIED solo owner) | Reviews: Birdeye 4.8 (146 reviews); Chamber of Commerce 4.9 (110 reviewers) - web-search snippets 2026-09-30; practice now shown as Drs. Carol L. Price and Eileen Kwee (2 doctors)
• Site (observed, raw HTML 2026-09-30): homepage <title> is EMPTY (VERIFIED); no meta description; loads 'js/jquery-migrate-1.2.1.js', 'js/camera.js' (2013-era slider stack) and a bootstrap 3 + Font Awesome 4.4 CDN; mixed http asset references; homepage still carries a live Covid-19 screening questionnaire ('If you have a fever, sore throat… tested positive for Covid-19 in the last 14 days') plus a stray 'Weather Update' banner (VERIFIED). Privacy-banner script from thedoctorsinternet.net (legacy vendor).
• Social gap: UNKNOWN (not checked; Instagram/Facebook not retrievable) — INFERRED gap from the new-building announcement vs. a site that cannot even name itself in search.
• Breakdown: FC14/20 BM11/15 WW14/15 Gap11/15 Dep7/10 Tr9/10 Cv3/5 Sp1/3 DM2/2 | Subs: Gap8 Dep7 Tr9 Tech9 (/10)
• Independence: INFERRED — no About-page group language, footer entity 'Carol L. Price, DDS, PC', no DSO strings in HTML | Decision-maker: Dr. Carol L. Price (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Heights/Houston inner-loop market, new commercial building under construction on adjacent lot (VERIFIED site announcement) = mid-high tier | Digital spend: thedoctorsinternet.net privacy-banner (legacy vendor relationship, INFERRED)
• Hooks: (1) "Google can't read your homepage title — it's empty." (2) "You're opening a new building; the site still shows a Covid questionnaire and a 2013 slider."
• Pitch/offer: New-building-launch homepage refresh with real office/team photography; existing scheduling stays; $8–10k (solo).
• Sources: http://www.heightsfamilydentistry.com/ (curl + WebFetch); EXCLUSIONS grep clean.
• Wave-2 update (2026-09-30): score 70 -> 72. Reviews found: Birdeye 146 @4.8 + 110 Chamber @4.9 all invisible behind an empty <title>; second doctor (Kwee) on directory listings. URL live (200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: South-Central (wave 1)

41. Progressive Dental Studio & Implant Center (Drs. Kevin Metsger & Maropis) — Greensburg, PA — https://www.progressivedentalgbg.com/ — 72/100 — HIGH (MEDIUM-HIGH: est. year from doctor bio)
• Est/Doctors: Dr. Metsger 'over 30 years' in Greensburg (Pitt Dental 1986) [VERIFIED on site]; 2 dentists: L. Kevin Metsger DMD (ADIA member, implants) and Dr. Maropis (Pitt 2014) [VERIFIED on site] | Reviews: Birdeye 1,588 reviews, 4.9 (Progressive Dental Studio listing) PLUS a second Birdeye listing for Dr. Metsger with 700 reviews, 4.9 (crawl 2026-09-30)
• Site (observed): ProSites template. Title verbatim: "Progressive Dental Studio & Implant Center" (homepage meta: "Welcome to our Welcome page. Contact Progressive Dental Studio & Implant Center today..." - ProSites placeholder copy). Source carries "Copyright � 2019 Prosites, Inc.". Legacy domain metsgerdental.com still resolves and redirects to progressivedentalgbg.com (domain rename). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Site links Facebook/reviews page [VERIFIED]; follower counts UNKNOWN. 2,288 combined Birdeye reviews (two listings) vs a placeholder-copy homepage.
• Breakdown: FC11/20 BM12/15 WW11/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM1/2 | Subs: Gap9 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (two named owner/associate dentists, single Greensburg office at 520 Pellis Rd; brand shares a word with 'Progressive Dental' vendor/marketing names but no group language found) - MEDIUM-HIGH confidence, verify on call | Decision-maker: Dr. L. Kevin Metsger, DMD (senior partner; Pitt Dental 1986)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Greensburg/Westmoreland County; 'Implant Center' positioning, implants, cosmetic; 2 docs, 2,000+ reviews imply high patient flow -> mid tier | Digital spend: ProSites subscription; two Birdeye listings
• Hooks: 1) ~2,300 Birdeye reviews across two listings while the homepage meta still says 'Welcome to our Welcome page'. 2) 'Implant Center' in the name but the ProSites shell shows no implant case work; Dr. Metsger at 30+ years is a natural moment to hand the brand to Dr. Maropis.
• Pitch/offer: Implant-led rebuild with case gallery and review wall; retire the second domain. $8-12k.
• Sources: progressivedentalgbg.com raw HTML + meet-the-doctors page (2026-09-30); reviews.birdeye.com/d/dental/greensburg-pa
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 2)

42. West University Dentistry (Drs. Ross Pickei & James M. Seale) — Houston (West U/Bellaire Blvd), TX — https://www.westuniversitydentistry.com/ — 72/100 — MEDIUM-HIGH (medium confidence — tenure UNKNOWN)
• Est/Doctors: UNKNOWN est. ('For years…'); Drs. Ross Pickei & James M. Seale (VERIFIED names) | Reviews: 4.9 rating on 91 reviews (directory snippet; platform not named - Google/Yelp mix, verify); est. 1972 by Dr. James Seale; Dr. Ross Pickei purchased practice July 2021 (directory snippet)
• Site (observed): footer 'Copyright � 2019 Prosites, Inc. All Rights Reserved.' (mojibake, frozen) and ProSites vendor strings; jQuery 1.x era scripts; only 3 <img> tags on the homepage; generic title 'Dentist in Houston, TX | Family & Cosmetic Dentistry' (VERIFIED raw HTML).
• Social gap: UNKNOWN.
• Breakdown: FC15/20 BM12/15 WW12/15 Gap11/15 Dep7/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED — no DSO language; MB2/Lovett names screened in territory: page mentions neither (Lovett West U is a separate listing) | Decision-maker: Dr. Ross Pickei (INFERRED lead)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — West University/Bellaire Blvd, affluent inner-loop, services incl. sedation, dental lasers, full mouth rehabilitation, oral surgery/endo on menu = high tier | Digital spend: ProSites subscription (VERIFIED)
• Hooks: (1) "'Copyright � 2019 Prosites' — in West U, your homepage looks seven years old." (2) "You list full-mouth rehab and sedation; the page shows 3 images."
• Pitch/offer: Premium West-U-grade redesign migrating off ProSites; $10–12k.
• Sources: https://www.westuniversitydentistry.com/ (curl + WebFetch).
• Wave-2 update (2026-09-30): score 67 -> 72. Est. 1972 (founder Seale), Pickei bought July 2021 = ownership-transition timing hook; 91 reviews @4.9. 'Mb2' string in wave-1 was a base64 false positive (re-checked, none as a word). URL live (200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: South-Central (wave 1)

43. Gotwalt Dentistry — Lititz/Akron, PA — https://www.drgotwalt.com/ — 72/100 — MEDIUM-HIGH (MEDIUM confidence)
• Est/Doctors: 'Over 30 years' (Dr. John Gotwalt); '35+ years combined experience' [VERIFIED on site]; 3 dentists: John T. Gotwalt DDS MAGD, Sara J. Gotwalt DMD FAGD, Stephanie Berg Stephens DMD FAGD [VERIFIED on site] | Reviews: Site schema.org aggregateRating 5.0 / 350 reviews [VERIFIED in raw HTML]; Birdeye 459 reviews, 5.0 (Sara J. Gotwalt DMD listing); Yelp 24 (search 2026-09-30)
• Site (observed): Dental Revenue template. Footer verbatim: "Copyright 2018, All Rights Reserved" + Dental Revenue credit; two conflicting title tags in source ("Lititz PA Dentist – Dr. John Gotwalt" and "Dentist in Lititz, PA | Gotwalt Dentistry"); 2014-era Font Awesome 4.2.0 via bootstrapcdn. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Only a Facebook link found in source [VERIFIED]; site-level review claim 350+ is not tied to a widget.
• Breakdown: FC11/20 BM13/15 WW11/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED (husband-and-wife/associate practice; no group language) | Decision-maker: Dr. John T. Gotwalt DDS (principal); Dr. Sara J. Gotwalt DMD
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Lititz/Lancaster County (Akron, PA office at 112 S 7th St), 3 FAGD/MAGD dentists, implants/veneers/Invisalign -> mid tier | Digital spend: Dental Revenue marketing/hosting; online reviews management
• Hooks: 1) 350+ reviews claimed while the template footer is frozen at 2018. 2) Two competing title tags on the homepage.
• Pitch/offer: Review-led premium redesign for a 30-year Lancaster County practice; $8-12k.
• Sources: drgotwalt.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 71 -> 72 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Dental Revenue · region: Mid-Atlantic (wave 1)

44. Aesthetic Image Dentistry (Debra Duryea, DMD) — Mendham, NJ — https://www.aestheticimagedentistry.com/ — 72/100 — MEDIUM-HIGH(medium)
• Est/Doctors: In dentistry since 1980; DMD 1990 (FDU); solo (VERIFIED, bio) | Reviews: Very large corpus for a solo: Demandforce 852 reviews / 5.0 (100% would refer) (VERIFIED via WebFetch); Zocdoc 138 reviews / 4.92; Birdeye 35 reviews / 4.9
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; title "Mendham Dentist | Aesthetic Image Dentistry | Cosmetic Dentist Mendham, NJ 07945" (ZIP in title); nav lists legacy products "Empress Restorations", "Procera Crowns", "LUMINEERS"; http:// address does not redirect to https
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM11/15 WW11/15 Gap13/15 Dep7/10 Tr7/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap9 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — solo owner bio; no group language | Decision-maker: Debra Duryea, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (Mendham/Morris County affluent market; cosmetic, veneers) | Digital spend: ProSites; ZocDoc link
• Hooks: 1) Practice name is literally "Aesthetic Image" but the site still promotes Empress/Procera-era materials 2) ZIP code inside the title tag
• Pitch/offer: Solo cosmetic boutique redesign — $5–8k solo tier.
• Sources: Live fetch aestheticimagedentistry.com (home + meet-the-doctor) | Wave-2 review enrichment (2026-09-30): Demandforce 852, Zocdoc 138, Birdeye 35; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

45. Vason Family Dentistry of Buckhead — Atlanta (Buckhead), GA — https://www.drvason.com/ — 72/100 — MEDIUM-HIGH (confidence: MEDIUM)
• Est/Doctors: 'Serving Buckhead, Atlanta for 40+ Years … Originally opened by Dr. Vason's father, Dr. J. Hamilton Vason, Jr.' (VERIFIED, site); office 3193 Howell Mill Rd NW Ste 202; full-mouth reconstruction, implants, implant dentures listed | Reviews: Count UNKNOWN — site links 'Read More Reviews' and shows long-tenure testimonials ('patients for over 20 years'); Healthgrades shows no ratings for Dr. Vason (WebSearch quota exhausted, so no Google/Birdeye count)
• Site (observed): TNT Dental template. Homepage <title>: "Dentist Buckhead, Atlanta | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Vason Family Dentistry of Buckhead". Footer 'Site designed and maintained by TNT Dental'; 45KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC14/20 BM14/15 WW13/15 Gap6/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap 5 Dep 8 Tr 8 Tech 9 (/10)
• Independence: VERIFIED — family-legacy practice (father founded; site history page); no DSO/group markers; not in EXCLUSIONS.md | Decision-maker: Dr. Carlisle Vason, DMD (owner, second-generation — VERIFIED via site history)
• FinCap: Buckhead/Howell Mill address (very affluent market) + full-mouth/implant services + 40-year legacy — Mid-High | Digital spend: TNT Dental (retainer/hosting likely redirectable)
• Hooks: 1) Buckhead legacy practice (40+ years, second-generation) whose title tag reads 'Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care'. 2) Legacy/handoff story is buried in a stock template.
• Pitch/offer: Buckhead legacy-practice flagship — $8–12k
• Sources: drvason.com raw HTML (curl); Healthgrades usearch (Vason, no ratings); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 2)

46. Fox Chapel Advanced Dental Care (Dr. J. Kevin Pawlowicz) — Pittsburgh (Fox Chapel), PA — https://www.foxchapeldentistry.com/ — 72/100 — MEDIUM-HIGH (MEDIUM: est. year not stated)
• Est/Doctors: 'Over 20 years' of practice per bio; founding year UNKNOWN [VERIFIED bio]; 1 principal dentist (AACD, Academy of Laser Dentistry, Academy of Computer Dentistry; adjunct faculty/mentor at the Scottsdale Center) plus in-house lab [VERIFIED on site] | Reviews: Birdeye 677 reviews, 4.9 (Fox Chapel Advanced Dental Care listing, crawl 2026-09-30)
• Site (observed): ProSites template. Title verbatim: "Fox Chapel Advanced Dental Care | Modern High-Tech Dentistry Pittsburgh". Footer verbatim: "Dental Website Powered by ProSites". Source carries "Copyright � 2019 Prosites, Inc." and retired Universal Analytics tag UA-9997448-1. Site markets CEREC, CBCT, in-house lab, veneers, Botox. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook/Instagram links UNKNOWN; 'Featured In' block without dated awards [VERIFIED].
• Breakdown: FC15/20 BM10/15 WW11/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (single owner-dentist bio; single office at 1347 Freeport Rd; no group language) - MEDIUM-HIGH confidence, verify on call | Decision-maker: Dr. J. Kevin Pawlowicz, DDS (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Fox Chapel is among Pittsburgh's wealthiest ZIPs; CEREC, CBCT, in-house lab, sedation-adjacent cosmetic menu -> upper tier | Digital spend: ProSites subscription; retired UA tag still firing
• Hooks: 1) 'Boutique dental retreat' positioning in one of Pittsburgh's richest ZIPs delivered on a ProSites shell with a retired UA-9997448-1 tag. 2) 677 Birdeye reviews and CBCT/in-house-lab capex not evidenced on the page.
• Pitch/offer: Boutique-retreat homepage: case gallery, in-house-lab story, review wall. $8-12k.
• Sources: foxchapeldentistry.com raw HTML + meet-our-team page (2026-09-30); reviews.birdeye.com/d/dental/pittsburgh-pa
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 2)

47. Heck Family Dentistry of Lawrence (Dr. Brian Heck + 3 dentists) - Lawrence, KS - https://www.heckfamilydentistry.com/ - 72/100 - MEDIUM-HIGH (medium confidence - founding year UNKNOWN)
• Est/Doctors: UNKNOWN (site text cites '50' in a years phrase - context UNVERIFIED; not used) | 4 dentists named on /meet-the-dentists.html: Drs. Ryan Brittingham, Brian Heck, Ahsan Iqbal + one more - VERIFIED; houses the 'Kansas Center for Sedation Dentistry' | Reviews: Birdeye 4.9 (757 reviews) + second Birdeye profile 4.8 (418) - JSON-LD / slug lookup 2026-09-30 (profiles may overlap)
• Site (observed, raw HTML 2026-09-30): TNT Dental template: footer '(c)2021 Heck Family Dentistry of Lawrence | Sitemap | Privacy Policy' and '<!-- TNT Dental Content Management System -->' (VERIFIED raw HTML); title 'Dentist in Lawrence, KS | Sedation & Same-Day Emergencies' (no brand, no implants/cosmetic); HubSpot form script (hbspt) bolted on; site now intermittently bot-walled (HTTP 403 on re-check; rendered fine earlier same day - treat as live/bot-walled); separate Instagram for the sedation center (kansascenter4sedationdentistry) vs. one sparse site.
• Social gap: Instagram @heckfamilydentistry and @kansascenter4sedationdentistry (followers UNKNOWN); Facebook HeckFamilyDentistryLawrence
• Breakdown: FC13/20 BM12/15 WW10/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - family-named 4-dentist practice, own sedation-center brand, no DSO strings (scan clean) | Decision-maker: Dr. Brian Heck, DDS (practice namesake; INFERRED owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - 4 dentists, IV sedation center, implants ('Sedation Dental Implants'), lasers, PRF; Lawrence (university town) market = mid-high tier | Digital spend: TNT Dental (VERIFIED), HubSpot forms (VERIFIED script), two Instagram accounts
• Hooks: (1) 'Your title tag says sedation and emergencies - nothing about implants or the Kansas Center for Sedation Dentistry that you run.' (2) 'Footer is (c)2021 with 1,100+ reviews across two profiles that the homepage never shows.'
• Pitch/offer: Two-brand architecture (family practice + Kansas Center for Sedation Dentistry) on one premium site; $8-12k.
• Sources: curl + raw HTML (2026-09-30); Birdeye profiles heck-family-dentistry-*; /meet-the-dentists.html; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 2)

48. Garden Oaks Family & Cosmetic Dentistry (Drs. Patrick Ruehle & Erika Eide) - Denton, TX - https://www.gardenoaksfamilydental.com/ - 72/100 - MEDIUM-HIGH (medium confidence)
• Est/Doctors: YellowPages: 43 years in business (directory, 2026-09-30); Dr. Ruehle '40+ years', FICOI (Misch), Diplomate ABDSM, Spear CEREC faculty - VERIFIED on /meet-dr-ruehle.html | Drs. Ruehle + Erika Eide | Reviews: Birdeye 5.0 (432 reviews; JSON-LD) + legacy Birdeye profile 5.0 (50), 2026-09-30
• Site (observed, raw HTML 2026-09-30): TNT Dental template; title 'Dentist Denton | Dentist Near Me | Garden Oaks Family & Cosmetic Dentistry' (keyword-spam pattern); footer '(c) Garden Oaks Family & Cosmetic Dentistry | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental' with NO copyright year; '<!-- TNT Dental Content Management System -->'; About page copy 'Privately Owned' is the only differentiator.
• Social gap: Instagram @dentondentist; Facebook GardenOaksFamilyDental (followers UNKNOWN)
• Breakdown: FC14/20 BM13/15 WW10/15 Gap12/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr7 Tech8 (/10)
• Independence: VERIFIED - About page 'Privately Owned... large corporations are taking over' statement; two named owner-doctors | Decision-maker: Dr. Patrick Ruehle (senior partner; 40+ years)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Lasers for ~20 yrs, CEREC, FICOI implants, dental sleep medicine diplomate; Denton (Teasley Ln, north Denton) = mid-high tier | Digital spend: TNT Dental (VERIFIED), Facebook/Instagram
• Hooks: (1) 'Your whole brand is "privately owned" but your title tag says "Dentist Near Me | Cost of Dental Care".' (2) 'A FICOI/ABDSM-credentialed 40-year practice with 480+ five-star reviews running on a generic TNT template.'
• Pitch/offer: Credential-led Denton homepage (implants, sleep, laser) with review wall; $8-12k.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /about-us.html, /meet-dr-ruehle.html; YellowPages Denton; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 2)

49. Stephen J. Rothman, DMD & Cammarano, DMD - Woodbridge, CT - https://rothmandentist.com/ - 72/100 - MEDIUM-HIGH (medium)
• Est/Doctors: 'Serving your family's dentistry needs for over 30 years'; staff 'average of 25 years' (VERIFIED, homepage); 2 doctors; 1 Bradley Rd Suite 905 | Reviews: Birdeye 632 reviews / 4.9 (Birdeye Woodbridge CT directory JSON-LD, 2026-09-30); homepage only asks 'Please review our dental services on Google'
• Site (observed): Hand-built site (index.php / services.php / new-patient.php, css/bootstrap.min.css, FontAwesome 4.4.0); 11,810-byte page with 4 images; footer "(c) 2021 Dr. Stephen Rothman DMD"; title "Dr. Stephen Rothman & Cammarano DMD | Woodbridge New Haven Dentist"; no meta description; copy "We accept most insurances - Mastercard, Visa, check or cash"
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC12/20 BM12/15 WW11/15 Gap13/15 Dep8/10 Tr8/10 Cv5/5 Sp1/3 DM2/2 | Subs: Gap9 Dep8 Tr9 Tech9 (/10)
• Independence: INFERRED - two named owner-dentists, no group language, no DSO strings in raw HTML, personal-name copyright | Decision-maker: Stephen J. Rothman, DMD (owner); Dr. Cammarano (first name UNKNOWN)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2-3 (Woodbridge/New Haven County; general family practice, insurance-friendly, 2 doctors, 30-year staff tenure) | Digital spend: None visible (no vendor credit); Birdeye listing active
• Hooks: 1) 632 reviews and a 25-year average staff tenure told in one paragraph on a 4-image PHP page 2) Frozen (c) 2021 footer and a title that drops the second doctor's first name
• Pitch/offer: Solo/duo redesign - review-led homepage, doctor pages, new-patient flow - $5-8k solo tier (top of range for 2 doctors)
• Sources: rothmandentist.com (curl raw HTML); Birdeye Woodbridge CT directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Northeast (wave 2)

50. Canyon Golf Family Dentistry (Dr. Bryan E. Soto) - San Antonio (Stone Oak), TX - https://www.familydentiststoneoak.com/ - 72/100 - MEDIUM-HIGH (medium confidence)
• Est/Doctors: YellowPages: 26 years in business (as 'Stone Oak Family Dentistry'; INFERRED same office) | Dr. Bryan Soto solo (UTHSCSA DDS; AOS member; Engle Institute implant training) - VERIFIED | Reviews: Birdeye 4.9 (486 reviews; JSON-LD, 2026-09-30)
• Site (observed, raw HTML 2026-09-30): Practice Cafe one-page template (14 KB): footer '(c) Copyright 2014 Bryan Soto, DDS, All Rights Reserved 20210 Stone Oak Pkwy' + 'Dental Marketing by Practice Cafe'; only Universal Analytics (ga('create','UA-47822853-17')) - retired tag; brand/domain mismatch: 'Canyon Golf Family Dentistry' vs. familydentiststoneoak.com; title 'Canyon Golf Family Dentistry: San Antonio Dentist'.
• Social gap: Facebook canyongolfdentistry (followers UNKNOWN)
• Breakdown: FC13/20 BM11/15 WW12/15 Gap12/15 Dep7/10 Tr9/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr9 Tech9 (/10)
• Independence: INFERRED - footer entity is the individual doctor; no DSO strings | Decision-maker: Dr. Bryan E. Soto, DDS (owner-doctor; footer entity 'Bryan Soto, DDS')
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Stone Oak Pkwy (affluent north SA), Invisalign/AOS orthodontic CE, implant training = mid-high tier | Digital spend: Practice Cafe (VERIFIED footer), Universal Analytics
• Hooks: (1) '486 five-star reviews and your footer still reads Copyright 2014.' (2) 'Your Analytics tag is the retired UA- property - you have not seen real traffic numbers since 2023.'
• Pitch/offer: Stone Oak premium homepage consolidating the brand/domain split; $6-9k solo.
• Sources: curl + raw HTML (2026-09-30); /team.php; Birdeye JSON-LD; YellowPages San Antonio; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Practice Cafe · region: South-Central (wave 2)

51. Oak Brook Dental Center — Elmhurst, IL — oakbrookdentalcenter.com — 73/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Dr. Karas 'practicing in the Oak Brook and Elmhurst areas since 1987' (39 yrs) with AAID-sponsored one-year implant course and consultant/teaching work (VERIFIED, site); 2–3 dentists | Reviews: 3,478 reviews, 5-star aggregate (Demandforce local.demandforce.com/b/oakbrookdentalcenter, VERIFIED via fetch). None surfaced on the 9-page static site.
• Site (observed): Static 9-page Bootstrap-3-era template — footer "© 2016 CGDesign" (frozen 2016; vendor credit link callawaygraphic.com); <title> "Oak Brook Dental Center in Elmhurst, IL"; contact email contact@obdent.com (a different domain from the site domain); Facebook link is the legacy "facebook.com/pages/Oak-Brook-Dental-Center/132869270063243" and a Twitter @OakBrookDental widget; homepage shows no doctor bios or credentials (WebFetch render) (VERIFIED raw HTML)
• Social gap: Legacy Facebook page + Twitter widget linked; follower counts not checked (UNKNOWN)
• Breakdown: FC13/20 BM13/15 WW11/15 Gap14/15 Dep8/10 Tr8/10 Cv3/5 Sp2/3 DM1/2 | Subs: Gap9 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED — single suite (340 W. Butterfield Rd, Ste 1C), no DSO/group strings in raw HTML; confirm owner(s) on call (MEDIUM confidence) | Decision-maker: UNKNOWN principal — Dr. David M. Karas, DDS (practicing in Oak Brook/Elmhurst since 1987, implant-focused, teaches dentists) and Dr. Alireza Nili, DDS named on /about.html (VERIFIED); yellowpages lists Thomas E. McKenna Jr, DDS at the address
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — implant/surgical scope, Elmhurst/Oak Brook DuPage market, 39-yr lead doctor | Digital spend: No paid vendor seen beyond legacy template credit; Demandforce (reviews)
• Hooks: 1) 3,478 reviews and a 39-year implant educator on a '© 2016 CGDesign' brochure site 2) Two competing identities: oakbrookdentalcenter.com vs contact@obdent.com
• Pitch/offer: Implant-authority relaunch with doctor bios and case gallery; keep Demandforce. $8–12k
• Sources: oakbrookdentalcenter.com raw HTML + /about.html + WebFetch render; local.demandforce.com/b/oakbrookdentalcenter
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Midwest (wave 2)

52. North Shore Prosthodontic Associates - Manhasset / Woodbury, NY - https://www.nspali.com/ - 72/100 - MEDIUM (medium)
• Est/Doctors: Established 1985 per directory listings (INFERRED; another source gives 1987); prosthodontic group with Manhasset, Woodbury and Fifth Avenue NYC offices | Reviews: Birdeye Woodbury 670 reviews / 5.0 + Manhasset 73 / 4.8 (Birdeye directory JSON-LD, 2026-09-30); homepage shows only three first-name testimonials, no ratings
• Site (observed): Dentalfone (footer "(c) 2013 - 2026 by Dentalfone", LayerSlider + Slider Revolution WordPress; hits page-level Cloudflare 'Please wait while your request is being verified...' on team pages); homepage names no physician; service teasers dated "July 11, 2017"; footer address typo "800 a 5th Avenue., Suite 501-A"; title "Dentist - Prosthodontist in Manhasset & Woodbury, NY | NSPA"
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC16/20 BM13/15 WW10/15 Gap10/15 Dep8/10 Tr6/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr7 Tech8 (/10)
• Independence: INFERRED - prosthodontic partnership with named owner-dentists (Korin, Surks, Tuminelli) in directory listings; no group/DSO language or DSO strings on homepage; 3 offices = confirm no DSO/Specialty1 affiliation on call | Decision-maker: Ted Korin, DMD and Dena Surks, DMD (owner-prosthodontists per directory listings); Frank Tuminelli also listed as owner
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 1 (Manhasset/Woodbury/Fifth Avenue; prosthodontics, implants, same-day crowns, Botox/TMJ/sleep apnea) | Digital spend: Dentalfone site (since 2013) + Birdeye review platform
• Hooks: 1) 743 Birdeye reviews and a prosthodontic pedigree but the homepage never names a doctor 2) 2017-dated service blocks and a Dentalfone template on a three-office Nassau/Manhattan prosthodontic group
• Pitch/offer: Group-flagship prosthodontic redesign (doctor pages, case gallery, three-office structure) - $12-15k group-flagship tier
• Sources: nspali.com (curl raw HTML + WebFetch); Birdeye Woodbury NY / Manhasset NY directory JSON-LD; WebSearch directory snippets (Healthgrades, BBB, Doctible)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Dentalfone · region: Northeast (wave 2)

53. Beliveau Dental (E. Charles Beliveau, DDS, PLLC) — North Andover, MA — https://www.beliveaudental.com/ — 71/100 — MEDIUM-HIGH(medium)
• Est/Doctors: Delivering dental excellence since 1989 (VERIFIED, homepage); 30+ years; ~1 doctor visible | Reviews: Birdeye 152 reviews / 5.0 (Birdeye directory JSON-LD, VERIFIED); Yelp 9 reviews / 5.0; Healthgrades 3 reviews; Sharecare 3.7 from 3 ratings; site says 'many people leave us kind words on Google and Facebook' but no count shown (VERIFIED)
• Site (observed): TNT Dental ("Website developed by TNT Dental Content Management System"; footer "©2021 E. Charles Beliveau DDS | designed and maintained by TNT Dental"); 30KB template page; title "Dentist North Andover | E. Charles Beliveau, DDS"; Dawson/Pankey/Spear credentials are buried in a template
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM12/15 WW10/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap7 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED — PLLC in owner's name; bio is owner-authored; no group language | Decision-maker: E. Charles Beliveau, DDS (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (Merrimack Valley; Dawson Academy / Pankey / Spear study-club comprehensive dentistry) | Digital spend: TNT Dental hosting/CMS subscription
• Hooks: 1) Member of the Dawson Academy, Pankey Institute and Spear Study Club — advanced-credential story told by a stock TNT template 2) Delivering dentistry "since 1989" = 37th-year anniversary
• Pitch/offer: Comprehensive-dentistry credential-led redesign — $8–12k; TNT-sub redirect hook.
• Sources: Live fetch beliveaudental.com (home + /meet-dr-beliveau.html) | Wave-2 review enrichment (2026-09-30): Yelp 9, Healthgrades 3, Sharecare 3; site reviews.html; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Northeast (wave 1)

54. Fox Valley Dental Associates (Tami Zuck DDS) — Crystal Lake, IL — foxvalleydentalcl.com — 71/100 — MEDIUM-HIGH (medium-low)
• Est/Doctors: 'Serving Crystal Lake since 1994' (VERIFIED, site header); solo; CEREC, VELscope, prosthodontic pages | Reviews: 4.9 on ~1,180 reviews (Birdeye reviews.birdeye.com/fox-valley-dental-associates-158405325650813, page 75 of listing); serving Crystal Lake since 1994 (Healthgrades directory snippet). [Wave-2 enrichment]
• Site (observed): ProSites — footer "Copyright � 2019 Prosites, Inc."; <title> "Crystal Lake Dentist | Fox Valley Dental Associates"; header tagline 'Tami Zuck, DDS Serving Crystal Lake since 1994....' (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC12/20 BM12/15 WW10/15 Gap12/15 Dep8/10 Tr7/10 Cv5/5 Sp3/3 DM2/2 | Subs: Gap8 Dep8 Tr7 Tech8 (/10)
• Independence: INFERRED — 'Associates' in name but single named DDS; verify no Dental Associates (WI) link | Decision-maker: Dr. Tami Zuck, DDS (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — mid — solo 32-yr practice in Crystal Lake | Digital spend: ProSites
• Hooks: 1) 'Serving Crystal Lake since 1994....' tagline with trailing ellipsis in the header 2) ProSites ©2019 mojibake
• Pitch/offer: Solo redesign. $5–8k
• Sources: foxvalleydentalcl.com raw HTML
• Wave-2 re-score: 60 -> 71. 1,180 Birdeye reviews hidden behind a 'Copyright � 2019 Prosites' template; large Gap upgrade.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 1)

55. Baltimore Dental Arts (Drs. Kevin Murphy, Devon Conklin, Charles & Melody Ward) — Baltimore, MD — https://www.baltimoredentalarts.com/ — 71/100 — MEDIUM-HIGH (MEDIUM: Google count not retrievable; est. year of predecessors UNKNOWN)
• Est/Doctors: Merged from Conklin & Ward Dental Group and Kevin G. Murphy & Associates (site: 'Formerly ...'); founding years UNKNOWN; 4 dentists: Murphy (perio/prosth, Pankey faculty, AAED fellow), Conklin, C. Ward, M. Ward [VERIFIED search + site] | Reviews: Birdeye 45 reviews, 4.8 (crawl 2026-09-30; search snippet 29); Google/Facebook counts UNKNOWN (site sends visitors to Google/Facebook pages)
• Site (observed): TNT Dental. Title verbatim: "Dentist Baltimore, MD | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Baltimore Dental Arts". Footer verbatim: "©2021 Baltimore Dental Arts | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental". Retired UA-187654970-1 tag. Reviews page has no review content (links out to Google/Facebook). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook and Google review links only; counts UNKNOWN.
• Breakdown: FC15/20 BM11/15 WW12/15 Gap8/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap6 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (merger of two named local practices; four owner/associate dentists; single office at 6080 Falls Rd; no group language) - MEDIUM confidence, verify on call | Decision-maker: Dr. Kevin G. Murphy (board-certified periodontist and prosthodontist; AAED fellow 2015) / Dr. Devon Conklin
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Falls Road/Roland Park-Mt. Washington corridor; perio+prosthodontic team, full-mouth reconstruction, implants, implant dentures, bone grafting -> upper tier | Digital spend: TNT Dental subscription; Pay-online link
• Hooks: 1) Prosthodontist/AAED-fellow team wearing a keyword-stuffed TNT title ('Cost of Dental Care') and a ©2021 footer after the practice merger. 2) The merger itself is a rebrand moment: the site still says 'Formerly Conklin & Ward Dental Group'.
• Pitch/offer: Merger-era rebrand: prosthodontic case gallery, four-doctor story, review integration. $12-15k (multi-specialty flagship).
• Sources: baltimoredentalarts.com raw HTML (2026-09-30); Birdeye; Baltimore Magazine directory; WebSearch
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Mid-Atlantic (wave 2)

56. Maras Dentistry (William H. Maras, DDS, PA) — Palm Beach Gardens, FL — https://www.marasdentistry.com/ — 71/100 — MEDIUM-HIGH (confidence: MEDIUM)
• Est/Doctors: Est. UNKNOWN; patient testimonial: "I've known Dr. Maras for about 40 years … his dentist son who works with him now" (site) — INFERRED 35-40 yrs, generational handoff under way; 3 doctors; implants, veneers, Invisalign, Botox listed; 2521 Burns Rd | Reviews: Healthgrades Dr. William Maras 5.0 / 226 ratings (Healthgrades directory search); Google count UNKNOWN
• Site (observed): Homepage banner still reads "The office is closed Wednesday, December 24 and return back to the office on Monday, January 5." (verified live 2026-09-30, i.e. ~9 months stale). Hero copy 'Welcome to Maras Dentistry, where beautiful smiles begin. schedule an appointment' repeated 5x in the slider markup; title "Maras Dentistry - Creating Healthy Smiles" (no city/service). Legacy UA-155179074-6. 59KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC14/20 BM11/15 WW10/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap 7 Dep 8 Tr 8 Tech 9 (/10)
• Independence: INFERRED — family practice (father/son), entity 'William H Maras DDS PA', no group markers; not in EXCLUSIONS.md | Decision-maker: Dr. William Maras, DDS (founder-owner; INFERRED) with son Dr. Kyle Maras, DDS and Dr. Jennifer Shiflet, DDS
• FinCap: Palm Beach Gardens (affluent) + veneers/implants/Botox add-ons + 3 doctors — Mid-High | Digital spend: Unknown vendor (generic WordPress build)
• Hooks: 1) Stale Dec-24 holiday-closure banner still live in late Sept. 2) 226 Healthgrades ratings at 5.0 for a father-son practice on a thin generic site.
• Pitch/offer: Father-son handoff practice refresh — $8–12k
• Sources: marasdentistry.com raw HTML (curl); Healthgrades usearch (Maras); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: Southeast (wave 2)

57. Fishers Family Dentistry — Fishers, IN — fishersfamilydentistry.com — 71/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Founding year UNKNOWN; Demandforce lists patients as customers since 1998 (INFERRED 25+ yrs); 2 dentists (VERIFIED); CEREC and implants listed | Reviews: 3,957 reviews, 5-star aggregate, 99.5% would refer (Demandforce local.demandforce.com/b/fishersfamilydentistry, VERIFIED via fetch). The homepage carries no review display.
• Site (observed): ProSites — raw HTML "Copyright � 2019 Prosites, Inc.  All Rights Reserved." (mojibake), footer "&copy2026 Fishers Family Dentistry | Site Map Site Developed by Prosites.com" (missing entity semicolon); homepage <title> "Make Payment Here | Fishers, IN | Fishers Family Dentistry"; homepage body is a bare shell (map iframe, phone, comcast.net address, menu) with no hero or services copy; practice email fishersfamilydentistry@comcast.net (VERIFIED curl)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC13/20 BM10/15 WW11/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM1/2 | Subs: Gap9 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — 'Fishers Family Dentistry' single address (8410 E 116th St), comcast.net practice email, no DSO strings in raw HTML | Decision-maker: Dr. Scott M. Bassett, DDS (in Fishers since 2010; Spear Study Club) and Dr. Grant Ryan named (VERIFIED, doctor pages); principal UNKNOWN
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — two dentists, CEREC/implants, Fishers IN (affluent Indianapolis NE suburb) | Digital spend: ProSites subscription (redirect target); Demandforce
• Hooks: 1) Homepage title tag reads 'Make Payment Here | Fishers, IN' 2) ~4,000 Demandforce reviews (the biggest corpus in this batch) sit behind a bare ProSites shell
• Pitch/offer: Full relaunch with reviews wall and implant/CEREC landing pages, keep pay link. $8–12k
• Sources: fishersfamilydentistry.com raw HTML + doctor pages; local.demandforce.com/b/fishersfamilydentistry
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 2)

58. Oak Canyon Dentistry (Dr. Steven Haase) - Bee Cave (Austin), TX - https://www.oakcanyondentistry.com/ - 71/100 - MEDIUM-HIGH (medium confidence - founding year UNKNOWN)
• Est/Doctors: UNKNOWN (Oak Canyon is his 'third dental practice'; UMKC DDS 1988) | Dr. Steven Haase solo - VERIFIED; lectures nationally on cosmetic techniques | Reviews: Birdeye 5.0 (506 reviews; JSON-LD, 2026-09-30)
• Site (observed, raw HTML 2026-09-30): ProSites: raw HTML comment 'Prosites Web Engine Technology Version 4.0 Copyright � 2019 Prosites, Inc.' (mojibake) and footer 'Site Developed by ProSites.com'; homepage copy says 'Austin Dentist... our Austin, Texas dental office' though the practice is in Bee Cave; 11 images; boilerplate 'Dr. Steven Haase is dedicated to family dentistry such as Exams, Teeth Whitening, Veneers and more.'
• Social gap: Facebook page present (followers UNKNOWN)
• Breakdown: FC14/20 BM11/15 WW10/15 Gap13/15 Dep7/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED - single named owner-doctor, no group strings in HTML scan | Decision-maker: Dr. Steven Haase, DDS (sole doctor; owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Bee Cave/Westlake affluent corridor; veneers, implant restorations, teaching role = mid-high tier | Digital spend: ProSites subscription (VERIFIED)
• Hooks: (1) '506 five-star reviews in Bee Cave and the site still says Copyright 2019 ProSites.' (2) 'You teach cosmetic dentistry to other dentists - your homepage reads like boilerplate.'
• Pitch/offer: Bee Cave cosmetic/implant homepage featuring Dr. Haase's teaching credentials; $6-9k solo.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /our-practice/meet-our-doctor/; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: South-Central (wave 2)

59. Montrose DDS (Drs. Samuel Carrell & Austin Faulk) - Houston (Montrose), TX - https://montrosedds.com/ - 71/100 - MEDIUM-HIGH (medium confidence)
• Est/Doctors: 1981 (founded by Dr. Bruce Smith; directory + site) | Drs. Carrell (joined 2014, bought practice) and Austin Faulk (joined 2018) - married couple | Reviews: Birdeye 5.0 (323 reviews; JSON-LD, 2026-09-30); Yelp 38 (search snippet)
• Site (observed, raw HTML 2026-09-30): GoDaddy Website Builder (footer 'Powered by GoDaddy Airo'); footer 'Copyright (c) 2018 Montrose DDS - All Rights Reserved.' (VERIFIED raw HTML, frozen 8 years); generic title 'Dentist in Montrose, Houston, TX'; 218 KB homepage with a cookie-consent banner; founder-era content mix.
• Social gap: Facebook montroseDDS, Instagram @montrosedds (followers UNKNOWN)
• Breakdown: FC13/20 BM12/15 WW10/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - owner-doctors named (practice purchase from founder documented), no group strings | Decision-maker: Dr. Samuel Carrell, DDS (purchased the practice from founder Dr. Bruce Smith - VERIFIED on /our-team)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Montrose/Upper Kirby inner-loop; same-day CEREC-type crowns, Invisalign, sedation, sleep/airway = mid-high tier | Digital spend: GoDaddy Website Builder (VERIFIED), cookie-consent tool, Birdeye profile
• Hooks: (1) 'New owners since the Smith handoff, new office, 323 five-star reviews - and the footer is still Copyright 2018.' (2) 'Your site is a GoDaddy builder page; your competitors in Montrose/River Oaks are not.'
• Pitch/offer: Ownership-transition relaunch for a 1981 Montrose practice; $8-10k.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /our-team; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: GoDaddy · region: South-Central (wave 2)

60. Smiles by Martin (Dr. Greg Martin - third generation) - Grapevine, TX - https://www.smilesbymartin.com/ - 71/100 - MEDIUM-HIGH (medium confidence)
• Est/Doctors: YellowPages: 42 years in business | Martin Dental Practice, Dr. Greg Martin joined 2002 - third generation of Martins (VERIFIED on /meet-dr-martin.html) | Reviews: Birdeye 4.9 (277 reviews; JSON-LD, 2026-09-30)
• Site (observed, raw HTML 2026-09-30): TNT Dental template: footer '(c)2021 Martin Cosmetic and Family Dentistry | Privacy Policy | Sitemap | Site designed and maintained by TNT Dental'; '<!-- TNT Dental Content Management System -->'; Google Maps embed stamped 2017 (4v1510162731105); services span All-On-4, CBCT, sedation, sleep apnea yet homepage is a 44 KB template; title 'Dentist Grapevine, TX | Smiles by Martin'.
• Social gap: Facebook SmilesByMartin (followers UNKNOWN)
• Breakdown: FC13/20 BM13/15 WW10/15 Gap11/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - multi-generational family practice, footer entity is the practice itself, no DSO strings | Decision-maker: Dr. Greg Martin, DDS (third-generation owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Grapevine/Southlake corridor; All-On-4, CBCT scanner, full-mouth restoration, 5-year warranty = mid-high tier | Digital spend: TNT Dental (VERIFIED), Facebook, video testimonials
• Hooks: (1) 'Three generations of Martins and the website footer is (c)2021.' (2) 'You offer a 5-year warranty and All-On-4 - the homepage never says it above the fold.'
• Pitch/offer: Legacy-story relaunch (third-generation) with All-On-4 and warranty positioning; $8-12k.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /meet-dr-martin.html; YellowPages Southlake; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 2)

61. Progressive Dentistry (Steven M. Levy, DMD) - Merrick, NY - https://www.merrickdentistry.com/ - 71/100 - MEDIUM (medium)
• Est/Doctors: Owner since 1984; implants since 1986 (VERIFIED, homepage/bio); solo; 2565 Beverly Rd | Reviews: Birdeye 337 reviews / 4.9 (Birdeye Merrick directory JSON-LD, 2026-09-30); Chamber of Commerce listing 179 reviews / 4.9; Healthgrades 13 reviews / 4.4
• Site (observed): PBHS (footer 'Dental Website Design by PBHS (c) 2025', wp-content/themes/Template2120; live site Cloudflare-walled to scripts, read from web.archive.org snapshot 2025-10-15); title "General Dentistry Merrick, NY | Cosmetic Dentistry | Progressive Dentistry" (generic); nav items "Holistic Dentistry", "Over-The-Counter Tooth Whitening", "Fiberoptic Transillumination"
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC13/20 BM13/15 WW9/15 Gap12/15 Dep8/10 Tr7/10 Cv5/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - solo owner named in bio ('has owned his ... practice in Merrick NY since 1984'); no group language or DSO strings in archived raw HTML | Decision-maker: Steven M. Levy, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2 (Merrick, Nassau County; implants, cosmetic, iTero, VELscope; solo) | Digital spend: PBHS subscription (Template 2120)
• Hooks: 1) 337 Birdeye + 179 Chamber reviews carry the practice, not the template site 2) Implants-since-1986 expertise is a bullet in a generic PBHS page - succession/legacy angle at 40 years
• Pitch/offer: Solo redesign leading with implant experience and reviews - $5-8k solo tier
• Sources: merrickdentistry.com (archive.org 2025-10-15, search-indexed pages); Birdeye Merrick NY directory JSON-LD; WebSearch (Chamber of Commerce, Healthgrades snippets)
• QC: liveness HTTP 403 Cloudflare bot-wall — content verified via web.archive.org snapshot / rendered fetch by research agent · social activity NOT YET CHECKED · vendor cluster: PBHS · region: Northeast (wave 2)

62. Thomsen Dental Group — West Omaha, NE — thomsendental.com — 70/100 — MEDIUM-HIGH (medium-high)
• Est/Doctors: 'More than three decades' in Omaha (VERIFIED, site); Brett Thomsen DDS FAGD, AACD member, ICD member, former US Army dental surgeon (UNMC DDS); associate Dr. Wegner (name VERIFIED, credentials UNKNOWN) | Reviews: Thin public corpus: aggregator shows 5.0 on 10 Google reviews (bippermedia.com snippet); Healthgrades 4 for Dr. Allen Thomsen; Yelp/BBB (A+, accredited since 2009) listings exist (WebSearch, INFERRED counts small). Site intermittently timed out in curl on first try, then loaded 200 (95.9KB). [Wave-2 enrichment]
• Site (observed): ProSites platform — raw HTML footer "Copyright � 2019 Prosites, Inc. All Rights Reserved" (mojibake + frozen 2019); <title> "Dentist in West Omaha, Nebraska | Thomsen Dental"; ProSites-style /our-practice/ page structure with generic procedure pages (VERIFIED raw HTML)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC14/20 BM12/15 WW11/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM1/2 | Subs: Gap6 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — 'Thomsen Dental Group' family/cosmetic practice, no DSO strings in HTML/About; entity not seen | Decision-maker: Dr. Brett Thomsen, DDS, FAGD (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — 30+-yr FAGD/AACD family+cosmetic practice in West Omaha (affluent market) | Digital spend: ProSites subscription (redirect target)
• Hooks: 1) ProSites footer still reads 'Copyright � 2019 Prosites, Inc.' on a 30-year FAGD/AACD practice 2) Army-surgeon-to-West-Omaha story and credentials are buried in a template
• Pitch/offer: Credential-forward redesign of a 30-yr AACD/FAGD practice, leave ProSites. $8–12k
• Sources: thomsendental.com raw HTML + /our-practice/dr-brett-thomsen/
• Wave-2 re-score: 72 -> 70. Thin review base lowers Gap/FC vs wave 1. Raw HTML re-verified 2026-09-30: still 'Copyright � 2019 Prosites, Inc.'
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 1)

63. Donna L. Kiesel DDS PA — Coppell, TX — https://www.drdonnakiesel.com/ — 70/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: 35+ yrs (site claim) | Dr. Donna L. Kiesel; veneers, implants, All-on-4, IV sedation (VERIFIED site) | Reviews: Healthgrades 4.9 (284-286 patient ratings); Yelp 10 reviews - search snippets 2026-09-30; Baylor College of Dentistry 1989 grad
• Site (observed): <title> 'Dentist Coppell, TX | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Donna L. Kiesel, DDS, PA' (VERIFIED raw HTML); TNT Dental template ('tntdental' asset paths); no © year in footer. NOTE: visual layer is relatively polished (photo/video) — gap is SEO/title/template, not raw looks.
• Social gap: UNKNOWN (site shows Instagram photos).
• Breakdown: FC15/20 BM14/15 WW9/15 Gap12/15 Dep7/10 Tr6/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr6 Tech8 (/10)
• Independence: INFERRED | Decision-maker: Dr. Kiesel
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Coppell (75019), full-arch + IV sedation menu, Top Docs recognition = mid-high tier | Digital spend: TNT Dental (VERIFIED)
• Hooks: (1) "Your title tag reads 'Dentist Near Me | … | Cost of Dental Care'." (2) "Top Docs 2019/2020/2025 — none of it is in the search snippet."
• Pitch/offer: Title/structure + premium visual rebuild; $8–10k.
• Sources: https://www.drdonnakiesel.com/ (curl + WebFetch).
• Wave-2 update (2026-09-30): score 66 -> 70. Reviews found: Healthgrades ~284 @4.9. URL live (200); title still keyword-spam.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 1)

64. Byerly Family Dentistry — Montgomery (Cincinnati), OH — byerlydental.com — 70/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Dr. Lee Byerly 'over thirty years' in Montgomery (VERIFIED); son/associate Dr. Ryan Byerly 'moved back to Montgomery to practice' (both OSU) — generational handoff; All-on-4, implants, sedation, Invisalign, sleep-apnea appliances listed (VERIFIED) | Reviews: Count still UNKNOWN: Google/Birdeye/HG counts not surfaced by WebSearch. Nextdoor 'Neighborhood Favorite' 2019-2022 (WebSearch snippet); on-site testimonials from Demandforce; 30+ yrs (site). [Wave-2 enrichment]
• Site (observed): Frozen footer "© 2017. All Rights Reserved | Powered by"; dead Google+ link in raw HTML "plus.google.com/106753258023680623363"; WordPress generator tag "WordPress 6.2.13" (end-of-life core); <title> "Byerly Family Dentistry | Montgomery, Ohio Dentist"; tagline banner "Over Thirty Years of Dental Experience"; hours Mon/Tue/Thu 7–3 (VERIFIED raw HTML)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC13/20 BM12/15 WW11/15 Gap10/15 Dep7/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap7 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED — father/son family practice; single street address; no group language; no DSO strings in HTML | Decision-maker: Dr. Lee Byerly, DDS / Dr. Ryan Byerly, DDS (both VERIFIED; principal split UNKNOWN)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — Montgomery OH is a high-income Cincinnati suburb; All-on-4 + sedation scope | Digital spend: Demandforce (reviews/reminders), Pay Online link
• Hooks: 1) Father–son practice: Ryan Byerly joining is a natural moment to modernize the front door 2) Footer still ©2017 and a dead plus.google.com link
• Pitch/offer: Generational-practice relaunch with All-on-4/implant landing pages; keep Demandforce + pay link. $8–12k
• Sources: byerlydental.com raw HTML + /about/
• Wave-2 re-score: 70 -> 70. No new count found; score unchanged. Raw HTML re-verified: '© 2017. All Rights Reserved', WordPress 6.2.13.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: Midwest (wave 1)

65. Wallingford Station Family Dental — Wallingford (Media), PA — https://www.wallingforddental.com/ — 70/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Founded 1948; three generations [VERIFIED on site]; Stephen P. Howarth Sr. DMD ('voted top dentist in greater Philadelphia' 18 times per site), Stephen P. Howarth Jr. DMD, Daniella Rizzo DMD [VERIFIED on site] | Reviews: Thin public corpus: Yelp 10, Healthgrades 2 (Dr. Howarth), Birdeye 0 (search 2026-09-30); Google count UNKNOWN. Founded 1948 by Dr. Willard Howarth; run by Dr. Stephen Howarth Sr. and Jr. (3 generations) - heritage story is the asset, not review volume
• Site (observed): ProSites/PracticeMojo. Title tag verbatim: " Dentist in Wallingford & Media | Wallingford Station Family Dental "; source comment "Prosites Web Engine Technology Version 4.0 Copyright � 2019 Prosites, Inc." (mojibake); jQuery 1.9.1; 19 of 25 images have no alt text; table/font markup. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Only Yelp link found; no Facebook/Instagram in source [VERIFIED]; social footprint UNKNOWN.
• Breakdown: FC14/20 BM15/15 WW11/15 Gap7/15 Dep7/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Gap5 Dep7 Tr8 Tech9 (/10)
• Independence: INFERRED (Howarth Sr./Jr. family practice since 1948; no group language) | Decision-maker: Dr. Stephen P. Howarth Sr. DMD (principal); Dr. Howarth Jr. (successor)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Wallingford/Swarthmore Delaware County affluent pocket, full-arch replacement and implants offered, 3 dentists -> mid-upper tier | Digital spend: ProSites subscription; patient-reviews page; Google Analytics 4
• Hooks: 1) 18-time 'top dentist' claim sits on a ProSites page with a mojibake engine footer. 2) Sr. -> Jr. handoff is the obvious timing event.
• Pitch/offer: Heritage + succession redesign (1948 -> Jr.); $8-12k.
• Sources: wallingforddental.com raw HTML + rendered fetch; Healthgrades/Yelp search snippets (2026-09-30)
• Wave-2 note: score 73 -> 70 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

66. Midtown Dental Sacramento — Sacramento, CA — https://www.midtowndentalsacramento.com/ — 70/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: Site '2013 - 2020'; practice founding UNKNOWN | 3 dentists | Reviews: Yelp 280 reviews (Jenny Apekian DDS - Midtown Dental listing, Jul 2026; site claims 'over 150 five-star' on Yelp and Google 5.0); site schema ratingCount 68 / 5.0. In-house dental lab + CEREC. Source: yelp.com via WebSearch + raw HTML schema
• Site (observed): Divi child theme; footer '© Midtown Dental Sacramento 2013 - 2020 | All Rights Reserved | Web Design & SEO by Capitol Tech Solutions'. Testimonial copy still says 'Is going to the dentist your nightmare? With COVID...'. Title 'Sacramento Dentist - Cosmetic CEREC Crowns Dental Implant & Invisalign - Midtown Dental' (keyword string).
• Social gap: UNKNOWN
• Breakdown: FC13/20 BM9/15 WW11/15 Gap12/15 Dep9/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep9 Tr8 Tech8
• Independence: INFERRED - no group language; owner not stated. | Decision-maker: Dr. Gina Crippen (15 yrs), Dr. Jenny Apekian (10+ yrs), Dr. Sarah Mathai - owner UNKNOWN
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — CEREC, on-site lab, 3 dentists, Midtown Sacramento (tier: mid) | Digital spend: agency SEO (Capitol Tech Solutions)
• Hooks: 'Your homepage still mentions COVID and your footer stops at 2020.'
• Pitch/offer: Midtown premium rebuild; $8k.
• Wave-2 update (2026-09-30): 64 -> 70. Big Yelp corpus (280) under a (c) 2013 - 2020 footer that still references COVID: 64 -> 70. Live.
• Sources: Raw HTML, WebFetch homepage
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: West (wave 1)

67. Johann Prosthetics of Boulder (Andrew R. Johann DDS MS PC) — Boulder, CO — https://www.andrewjohannddsmspc.com/ — 70/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: Boulder prosthodontic practice since 1999 (MS Prosthodontics, U Minnesota; DDS Indiana 1996 - VERIFIED on /meet-dr-johann/); YellowPages lists 28 yrs (INFERRED) | 2 prosthodontists (Johann + associate Dr. Paul Child Jr., LSU prosthodontics, CDT, AAED member - VERIFIED) | Reviews: Google/Yelp counts UNKNOWN (Google/Yelp/Facebook are bot-blocked from this environment; Opencare Boulder listing shows 0 reviews); site claims 'selected by his peers into the 5280 Magazine for best in his specialty field for the last ten years' and a 'top dentist 2017 by 5280 Magazine' badge
• Site (observed): ProSites v4 engine (VERIFIED raw footer 'Copyright � 2019 Prosites, Inc. All Rights Reserved.' with mojibake, 'Site Developed by ProSites.com'). Homepage <title> is 'Boulder Prosthodontist | Andrew R Johann DDS | Prosthodontics and Cosmetic Dentsitry' (typo 'Dentsitry' in the title tag). Body copy is vendor filler: 'This website is a resource we hope you'll find both useful and interesting.' Latest badge is 2017 (5280) while the bio claims ten consecutive years.
• Social gap: Instagram @johannprostheticsofboulder, a Facebook page with a reviews tab and a Yelp listing are all linked; follower counts UNKNOWN.
• Breakdown: FC15/20 BM12/15 WW12/15 Gap8/15 Dep8/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech8
• Independence: INFERRED (strong) - owner-named specialty PC, one associate, no group language | Decision-maker: Dr. Andrew R. Johann (owner); Dr. Paul Child Jr. (associate)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Boulder affluent market, two prosthodontists, in-house CBCT (Vatech Green X 18x15), TScan and Diagnodent, implant/full-arch/veneer menu (tier: upper) | Digital spend: ProSites subscription; Opencare and Yocale badges
• Hooks: 'Your title tag literally reads Cosmetic Dentsitry and the footer is frozen at 2019 on a site that undersells a two-prosthodontist, CBCT-equipped Boulder specialty practice.' / New associate (Dr. Child, AAED) is a natural relaunch moment.
• Pitch/offer: Specialty-practice rebuild that leads with prosthodontic credentials and case gallery, keeping existing forms/financing links; $8-12k standard.
• Sources: Raw HTML curl 200 (title, footer, ProSites strings); WebFetch of /, /our-practice/meet-dr-johann/, /our-practice/meet-dr-child/; Opencare Boulder listing; YellowPages Boulder listing; EXCLUSIONS grep clear
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: West (wave 2)

68. Baccellieri Family Dentistry (Dr. Carl Baccellieri Jr.) — Kennett Square, PA — https://bfdentistry.com/ — 70/100 — MEDIUM-HIGH (MEDIUM-HIGH)
• Est/Doctors: Practicing since 1997 (site: 'providing exceptional dental care since 1997') [VERIFIED on site]; 3 dentists: C. Baccellieri Jr. DMD (Temple), T. Santana DDS (joined 2016), R. Starner DDS (part-time, 2016) [VERIFIED on site] | Reviews: Birdeye 877 reviews, 4.9 (C E Baccellieri DDS listing, crawl 2026-09-30)
• Site (observed): WEO Media (TouchPoint Communications). Footer verbatim: "Copyright (c) 2011-2026 WEO MEDIA (TouchPoint Communications LLC). All rights reserved." and a visible keyword line "Page Phrases: dentist Kennett Square PA, ...". Title verbatim: "Home - dentist Kennett Square PA - Baccellieri Family Dentistry". Internal pages use the WEO '.asp' pattern (e.g. /p/dentist-Kennett-Square-PA-About-p42238.asp). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook/Instagram counts UNKNOWN; 877 Birdeye reviews not on the homepage [VERIFIED].
• Breakdown: FC11/20 BM10/15 WW12/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (founder-named practice; single office at 630 Cope Rd; associates joined 2016; no group language) - MEDIUM-HIGH confidence, verify on call | Decision-maker: Dr. Carl Baccellieri Jr., DMD (founder)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Chester County/Kennett Square affluent-adjacent; CEREC, Invisalign, implants; 3 docs -> mid tier | Digital spend: WEO Media hosting/marketing subscription (2011-2026 credit); CEREC
• Hooks: 1) Visible 'Page Phrases: dentist Kennett Square PA' keyword footer and .asp URLs on a 29-year-old, 877-review practice. 2) Two 2016 associates make a succession-planning conversation natural.
• Pitch/offer: Replace WEO shell with a premium site featuring CEREC/implant story and review wall; keep booking. $8-12k.
• Sources: bfdentistry.com raw HTML + meet-the-doctors page (2026-09-30); reviews.birdeye.com/d/dental/kennett-square-pa
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WEO Media · region: Mid-Atlantic (wave 2)

69. March Dentistry — Upper Arlington (Columbus), OH — marchdentistry.com — 70/100 — MEDIUM-HIGH (medium)
• Est/Doctors: 'over 25 years of private practice'; Columbus Monthly 'Top Dentist'; Columbus Dental Society president 2014; ICD Fellow 2013 (VERIFIED, site); full-mouth reconstruction, implants, TMJ, sleep apnea, CEREC, laser, veneers listed; solo | Reviews: 3,331 reviews, 5-star aggregate, 99.6% would refer (Demandforce local.demandforce.com/b/marchdentistry, VERIFIED via fetch; customers since 2002 shown). Not shown on the homepage.
• Site (observed): Agency-built mid-2010s template — footer "© Copyright 2026 March Dentistry. All Rights Reserved. Website Designed and Maintained by Herb Gillen Agency"; stale credentials in body copy: "selected as the Angie’s List #1 ranked general dentist in Central Ohio", "President of the Columbus Dental Society for 2014", "Fellow of the International College of Dentists in 2013"; carousel + card layout (WebFetch render); Thursday 7–12, Friday by appointment (VERIFIED raw HTML)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC14/20 BM11/15 WW9/15 Gap13/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — solo owner-dentist eponymous practice, single address (1580 Fishinger Rd), no DSO strings in raw HTML | Decision-maker: Dr. Timothy O. March, DDS (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper — solo restorative/full-mouth practice in Upper Arlington (affluent Columbus suburb), 25+ yrs | Digital spend: Agency retainer ('designed and maintained'), Demandforce
• Hooks: 1) Angie's List credential (the brand no longer exists) on the homepage of a Top Dentist with 3,331 reviews 2) Full-mouth reconstruction/TMJ/sleep services buried in a mid-2010s template
• Pitch/offer: Credential-forward restorative site (full-mouth, TMJ, sleep apnea); replace agency template. $6–9k
• Sources: marchdentistry.com raw HTML + WebFetch render; local.demandforce.com/b/marchdentistry
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Midwest (wave 2)

70. Todd Phelan DDS (Drs. S. Todd Phelan & Tyler Gossett) - Rogers, AR - https://www.nwadentist.com/ - 70/100 - MEDIUM-HIGH (medium confidence)
• Est/Doctors: Since 2004 ('Rogers' Trusted Dental Home Since 2004' - VERIFIED; '20+ years'); Dr. Phelan 25+ yrs (Spear Institute, Dawson Academy CE) + Dr. Tyler Gossett - 2 doctors VERIFIED | Reviews: Birdeye 4.9 (621 reviews; JSON-LD lookup, 2026-09-30)
• Site (observed, raw HTML 2026-09-30): TNT Dental: title tag reads 'Dentist Rogers, PA | Dentist Near Me | Todd Phelan, DDS' - the wrong state (PA, not AR) in the title (VERIFIED); footer '(c) S. Todd Phelan, DDS, PA | Sitemap | Privacy Policy | Site designed and maintained by TNT Dental' (no year); 22 KB homepage.
• Social gap: Instagram @nwadentist, Facebook ToddPhelanDDS (followers UNKNOWN)
• Breakdown: FC13/20 BM10/15 WW10/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - 'S. Todd Phelan, DDS, PA' professional-association footer; no DSO strings | Decision-maker: Dr. S. Todd Phelan, DDS, PA (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Rogers/NW Arkansas (Walmart-region affluent growth market); Spear/Dawson-trained comprehensive care = mid-high tier | Digital spend: TNT Dental (VERIFIED)
• Hooks: (1) 'Your title tag says Rogers, PA - Pennsylvania - to Google.' (2) '621 five-star reviews in NW Arkansas and a 22 KB TNT template.'
• Pitch/offer: NW Arkansas comprehensive-dentistry homepage built around Spear/Dawson positioning; $8-10k.
• Sources: curl + raw HTML (2026-09-30); Birdeye todd-phelan-dds JSON-LD; /about-us.html, /meet-the-dentists.html; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: South-Central (wave 2)

71. Thomas J. Emmer, DDS, PA (Prosthodontist) — Morristown, NJ — https://www.tjemmer.com/ — 70/100 — MEDIUM(medium)
• Est/Doctors: Practice began 1962 (Mountain Lakes); Emmer in Morristown since 1992 (VERIFIED, About page); solo | Reviews: Thin and mixed: Birdeye 7 reviews / 3.7 stars (one complaint alleging unnecessary tooth prep); Healthgrades/Sharecare 9 reviews 4.2; Vitals 4 ratings 4.8; US News PX score 4.3 from 15 reviews; NJ Monthly Top Dentist each year (VERIFIED via snippets)
• Site (observed): Wix.com Website Builder (generator meta); footer "© 2018 by Thomas J. Emmer, DDS, PA | Created by Jersey Girls Marketing"; title "Dr. T.J Emmer, DDS, PA | Morristown, NJ Prosthodontist"; 660KB Wix page for a 60-year prosthodontic practice ("practicing in the Morris County area longer than any other prosthodontist")
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM14/15 WW11/15 Gap8/15 Dep8/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap5 Dep7 Tr9 Tech8 (/10)
• Independence: INFERRED — solo PA under Dr. Emmer's name; About page shows owner-dentist; no group language or DSO strings | Decision-maker: Thomas J. Emmer, DDS (owner/prosthodontist)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 1-2 (Morristown/Morris County; prosthodontics, full-mouth restorations, implants) | Digital spend: Wix plan + Jersey Girls Marketing (freelancer/agency footer credit)
• Hooks: 1) "The practice began in 1962" — six decades of heritage presented on a 2018 Wix template 2) Listed as a board-recognized prosthodontist (Specialty #3929) but site does not showcase case work
• Pitch/offer: Prosthodontic case-gallery and referral-focused site rebuild — $8–12k standard tier; possible succession/legacy angle.
• Sources: Live fetch tjemmer.com raw HTML (generator, footer) + About text | Wave-2 review enrichment (2026-09-30): Birdeye, Sharecare, Vitals, US News; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Wix · region: Northeast (wave 1)

72. Moulton Dentistry of Hoover — Hoover (Birmingham), AL — https://www.moultondentistry.com/ — 70/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: 'Over 30 years of experience' (VERIFIED, site); Dr. Gunn also listed ('Meet Dr. Gunn' nav); office 3821 Lorna Rd (Hoover/Riverchase) | Reviews: Healthgrades Dr. Marc Moulton 4.9 / 158 ratings (Healthgrades directory search); Google count UNKNOWN (WebSearch quota exhausted)
• Site (observed): TNT Dental (HTML comment 'site developed by TNT Dental Content Management System'; footer 'Site designed and maintained by TNT Dental'). Homepage <title>: "Dentist Hoover, AL | Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care | Moulton Dentistry of Hoover". 37KB page; template copy 'Locally-Owned & Operated … We Value Your Time'. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC12/20 BM12/15 WW13/15 Gap9/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Subs: Gap 6 Dep 8 Tr 8 Tech 9 (/10)
• Independence: VERIFIED (on-page) — 'Locally-Owned & Operated'; no DSO markers in raw HTML; not in EXCLUSIONS.md | Decision-maker: Dr. Marc W. Moulton, DMD (owner — INFERRED from 'Locally-Owned & Operated')
• FinCap: Hoover/Riverchase (affluent Birmingham suburb) family + implant dentistry, 30-year solo-led practice — Mid | Digital spend: TNT Dental (retainer/hosting likely redirectable)
• Hooks: 1) Title tag: 'Dentist Near Me | Local Dentist | Dentist Office Near Me | Cost of Dental Care'. 2) 158 Healthgrades ratings at 4.9 for a 30-year solo — reputation far ahead of a stock template.
• Pitch/offer: Solo-plus-associate Hoover family/implant practice — $5–8k
• Sources: moultondentistry.com raw HTML (curl); WebFetch none; Healthgrades usearch (Marc Moulton); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 2)

73. Portland Dental Health Care & Implant Center - Portland, ME - https://www.portlandmainedental.com/ - 70/100 - MEDIUM (low-medium)
• Est/Doctors: Serving Portland families since 1978 (search snippet, INFERRED); 3 doctors; IV/oral sedation + implants; 315 Auburn St | Reviews: US News: Dr. Verrier-Davis 5.0 with 19 reviews and 6 patient awards; BBB profile; Yelp listing with mixed comments (a billing complaint); Google count UNKNOWN (the 126-review Birdeye 'Portland Health Center' entry could not be tied to this practice, so not used)
• Site (observed): PBHS (footer "(c) 2021 PBHS, Inc. All Rights Reserved. www.pbhs.com" plus 'Dental Website Design by PBHS (c) 2025', wp-content/themes/Template2120; live site Cloudflare-walled, read from web.archive.org snapshot 2025-10-14); COVID-19 limited-services notice still on homepage; title "Dentist Portland ME | Dental Implant & Sedation Dentistry Experts"; social links to Facebook, Google, Twitter and RSS (2010s widget set)
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC14/20 BM14/15 WW12/15 Gap8/15 Dep8/10 Tr7/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap6 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - named husband-and-wife owner-dentists (Verrier-Davis, Davis); no group/DSO language or DSO strings in archived raw HTML | Decision-maker: Michelle R. Verrier-Davis, DMD, MAGD, DICOI / Peter M. Davis, DMD, MAGD, DICOI (also Donald W. Verrier, DMD listed)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2 (Portland ME; implants, IV sedation - one of few Maine general practices with IV/oral sedation permits; 3 doctors) | Digital spend: PBHS subscription
• Hooks: 1) COVID limited-services notice still on the homepage 5+ years on 2) Rare IV-sedation + implant credentials (MAGD/DICOI x2) under a stock PBHS template
• Pitch/offer: Standard redesign: sedation + implant landing pages - $8-12k standard tier
• Sources: portlandmainedental.com (archive.org 2025-10-14); WebSearch (US News, BBB, Yelp snippets)
• QC: liveness HTTP 403 Cloudflare bot-wall — content verified via web.archive.org snapshot / rendered fetch by research agent · social activity NOT YET CHECKED · vendor cluster: PBHS · region: Northeast (wave 2)

74. Ross & Sourlis Family Dentistry of Rock Hill (domain: Coombs and Ross legacy) — Rock Hill, SC — https://www.crsmile.com/ — 70/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: 'Improving Smiles Since 1993' / 'trusted us for over 30 years' (VERIFIED, site); 'over 50 years of combined experience'; implants, All-on-4, CEREC, veneers, ClearCorrect listed; 'VIP Smile Club' membership ($48/mo adult) signals price-sensitive mix | Reviews: Homepage badge alt-text: 'top rated dentist on Google over 500 5 star reviews' (VERIFIED on-page; Google count not independently confirmed)
• Site (observed): TNT Dental. Homepage <title>: "Dentist Rock Hill, SC | Dentist Near Me | Ross & Sourlis Family Dentistry of Rock Hill". Domain crsmile.com is a legacy 'Coombs and Ross' name while the brand is now Ross & Sourlis; legacy Universal Analytics UA-113342617-1; 44KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC10/20 BM13/15 WW13/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Subs: Gap 7 Dep 8 Tr 8 Tech 9 (/10)
• Independence: INFERRED — two named owner-doctors, no group language; not in EXCLUSIONS.md | Decision-maker: Drs. Ross and Sourlis (owners; INFERRED)
• FinCap: Rock Hill/Fort Mill growth corridor; value-priced family practice with implant/cosmetic menu — Low-Mid | Digital spend: TNT Dental (retainer/hosting likely redirectable)
• Hooks: 1) 500+ Google reviews and 30 years behind a 'Dentist Near Me' title and a legacy-name domain. 2) VIP Smile Club membership offer suggests a redesign can lift implant/cosmetic conversion.
• Pitch/offer: Two-doctor legacy practice — $5–8k
• Sources: crsmile.com raw HTML (curl) + pg text; EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 2)

75. Perry Hall Smiles (Caroline F. Owens, DDS, PA) — Perry Hall (Baltimore), MD — http://www.perryhallsmiles.com/ — 69/100 — MEDIUM-HIGH (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Dr. Roedel Jaeger began in Overlea and then Perry Hall 'almost 50 years ago'; 'four generations of patients' [VERIFIED on site]; Dr. Caroline Foster Owens DDS (owner carrying the office forward), Dr. Marina Burdusi (joined); Dr. Ronald Carter earlier partner [VERIFIED on site] | Reviews: No Google/Birdeye count found (Birdeye has no listing; Yelp listing exists under 'Caroline Foster Owens DDS PA'); Baltimore Magazine Top Dentist recognition; snippet says practice 'established 2015' under Dr. Owens (earlier generations of patients) - maturity and corpus unproven, docked
• Site (observed): ProSites. HTTPS is broken: curl -> "SSL: no alternative certificate subject name matches target host name 'www.perryhallsmiles.com'", so the site is only usable as http ('Not Secure'). Title tag has a ZIP in it: " Perry Hall Dentist | Caroline F. Owens, DDS | 21236 Dental Care ". Source comment "Copyright � 2019 Prosites, Inc." (mojibake); jQuery 1.9.1; UA-60422405-1 retired Analytics; only 4 images. [VERIFIED raw HTML + curl, 2026-09-30]
• Social gap: No Facebook/Instagram/YouTube links found in source [VERIFIED]; social footprint UNKNOWN.
• Breakdown: FC10/20 BM11/15 WW14/15 Gap8/15 Dep8/10 Tr9/10 Cv4/5 Sp3/3 DM2/2 | Gap6 Dep8 Tr9 Tech9 (/10)
• Independence: INFERRED (successor-owner narrative Jaeger -> Carter -> Owens; PA professional-association entity; no group language) - verify on call | Decision-maker: Dr. Caroline F. Owens DDS (owner-dentist)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Perry Hall / NE Baltimore County suburban market; family & cosmetic mix -> lower-mid tier (site quality is the standout gap, not affluence) | Digital spend: ProSites subscription; legacy Google Analytics
• Hooks: 1) The site has no valid HTTPS certificate for its own hostname - browsers warn every visitor. 2) Generational handoff story (Jaeger -> Owens) is unused on a ZIP-in-title ProSites page.
• Pitch/offer: Fix-the-basics premium rebuild (secure, mobile, review-led) for a 50-year practice; $5-8k.
• Sources: perryhallsmiles.com raw HTML + curl SSL test (2026-09-30)
• Wave-2 note: score 73 -> 69 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

76. Always Great Smiles (Drs. Pecora & Langner) — Glen Ellyn, IL — alwaysgreatsmiles.com — 69/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Testimonial: 'since we moved to Glen Ellyn over 25 years ago' (INFERRED practice age ≥25 yrs); Langner joined at graduation 1995 (VERIFIED); Pecora U of Illinois; implants, veneers, prosthodontic, sedation, CEREC pages (VERIFIED) | Reviews: 4.9 on 393-396 reviews (Birdeye reviews.birdeye.com/always-great-smilescom-pc-146486020505051); Yelp 18; Facebook 98% recommend (WebSearch). Reviews also name a Dr. Zaremba - confirm roster. [Wave-2 enrichment]
• Site (observed): ProSites — footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; <title> "Welcome | GLEN ELLYN, IL | Always Great Smiles" (generic 'Welcome' + all-caps city, no service keyword) (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC13/20 BM12/15 WW10/15 Gap12/15 Dep7/10 Tr7/10 Cv4/5 Sp3/3 DM1/2 | Subs: Gap8 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — named owner-dentists, no group language | Decision-maker: Dr. Pecora (first name UNKNOWN) / Dr. Jennifer J. Langner, DDS, ABDSM (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — two-doctor practice in affluent Glen Ellyn (DuPage) | Digital spend: ProSites subscription
• Hooks: 1) Title tag is 'Welcome | GLEN ELLYN, IL | Always Great Smiles' 2) 'Copyright � 2019 Prosites' on a 25-year, two-doctor practice
• Pitch/offer: Two-doctor DuPage cosmetic/sedation redesign. $8–12k
• Sources: alwaysgreatsmiles.com raw HTML + about pages
• Wave-2 re-score: 64 -> 69. Large Birdeye corpus behind a 'Copyright � 2019 Prosites' template (re-verified raw HTML).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 1)

77. Schilling Farms Dental (Drs. Midyett & Prine) — Collierville (Memphis), TN — https://www.schillingfarmsdental.com/ — 69/100 — MEDIUM-HIGH (confidence: MEDIUM) [BELOW 68 CUT LINE — bench only]
• Est/Doctors: Est. UNKNOWN; 3 doctors ('group practice') | 3 doctors: Midyett, Prine, Jason Glick; one office; footer "(c) 2026 DentalWebsites.com (Advanced Web Systems LLC)"; site describes itself as "group practice" - independence MEDIUM | Reviews: Birdeye 1,892 reviews / 4.9 (search snippet, birdeye.com); Yelp 18; BBB A+ (not accredited). Own homepage shows only four 5-star Google review excerpts, no aggregate count (VERIFIED via fetch) = large invisible corpus [WAVE 2]
• Site (observed): raw HTML contains "Copyright 2011-2014 Twitter, Inc." (Bootstrap 2) and "Copyright 2013 - Forever, Weborithm.com"; rendered footer "© 2026 DentalWebsites.com (Advanced Web Systems LLC)" and encoded bullet artifacts "â€¢". Title: "Collierville - Memphis Dentist -Schilling Farms Dental".
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC12/20 BM10/15 WW10/15 Gap13/15 Dep7/10 Tr8/10 Cv5/5 Sp3/3 DM1/2 | Gap 8 Dep 7 Tr 8 Tech 8
• Independence: MEDIUM confidence — verify on call ('group practice' wording, three doctors, no ownership page reviewed) | Decision-maker: Dr. Clay Midyett (owner status UNKNOWN)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Collierville (affluent Memphis suburb) 3-doctor group, implants/veneers/Invisalign — Mid | Digital spend: DentalWebsites.com / Weborithm (observed)
• Hooks: 1) Mojibake "â€¢" bullets in the footer. 2) 2011-era Bootstrap 2 under a 2026 footer.
• Pitch/offer: Group-practice redesign — $8–12k
• Sources: schillingfarmsdental.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: DentalWebsites.com · region: Southeast (wave 1)

78. Dental Arts of Delaware (Drs. Gregg Fink & Christopher Appleman) — Newark, DE — https://dentalartsofdelaware.com/ — 69/100 — MEDIUM-HIGH (MEDIUM: est. year UNKNOWN)
• Est/Doctors: Founding year UNKNOWN; Dr. Fink lectures/expert witness, hygienist tenure since 2008 [VERIFIED on site]; 2 dentists: Fink (Penn Dental; AGD fellow; ICOI fellow; places and restores implants in-house) and Appleman DDS (AGD fellowship in progress) [VERIFIED on site] | Reviews: Birdeye 1,334 reviews, 4.9 (crawl 2026-09-30)
• Site (observed): Avada (Fusion) theme on WordPress core 5.7.19 (EOL) with Slider Revolution 6.4.6 [VERIFIED raw asset versions]. Footer verbatim: "Copyright © New Patients, Inc. All Rights Reserved. [ Designed by NPIClick ]" (vendor's copyright, no practice name). Title verbatim: "Newark Dentistry, Dental Arts of Delaware". Boxed-modal slider hero. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook/Instagram counts UNKNOWN; 1,334-review corpus not surfaced beyond 3 testimonial snippets [VERIFIED].
• Breakdown: FC12/20 BM12/15 WW8/15 Gap13/15 Dep8/10 Tr7/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap8 Dep8 Tr7 Tech8 (/10)
• Independence: VERIFIED (homepage: 'proud members of the Independent Dental Society of Delaware... locally owned and dentist-led') | Decision-maker: Dr. Gregg Fink, DMD, FAGD, FICOI (senior partner; past president Delaware Academy of General Dentistry)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Newark/Christiana corridor; in-house implants (ICOI fellow), Short-Term Ortho, evening and Saturday hours; 1,300+ reviews imply strong patient flow -> mid tier | Digital spend: New Patients, Inc. (NPI) site/marketing subscription; online scheduling
• Hooks: 1) WordPress 5.7.19 core + Slider Revolution 6.4.6 under a footer that credits 'New Patients, Inc.' rather than the practice, above 1,334 Birdeye reviews. 2) Their own 'independent, not DSO' statement is a ready-made brand pillar the current site buries.
• Pitch/offer: Independent-and-proud rebrand: implant story, Fink credentials, review wall. $8-12k.
• Sources: dentalartsofdelaware.com raw HTML + meet-the-doctors page (2026-09-30); reviews.birdeye.com/d/dental/newark-de
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: Mid-Atlantic (wave 2)

79. CMB Family Dentistry (Drs. David Brown & Josh Alter) — Broomall, PA — https://www.cmbdental.com/ — 69/100 — MEDIUM-HIGH (MEDIUM-HIGH)
• Est/Doctors: 'For more than 40 years' (site) [VERIFIED on site]; Main Line Today 'Best of the Main Line Dentists' consecutive years since 2009 (site claim); 2 dentists: Brown (implant-trained, AGD) and Alter (DMD, MS) [VERIFIED on site] | Reviews: Birdeye 460 reviews, 5.0 (crawl 2026-09-30; a second Birdeye page shows 306); aggregator 362
• Site (observed): TeleVox/Milestone CMS 6.0. Footer verbatim: "CMB Family Dentistry - 7 Davis Ave., Broomall, PA 19008 ... 2026 © All Rights Reserved | Privacy Policy | Website Design By: Televox®". Homepage keeps a <center> tag and a layout <table style="width: 100%">; interior-page navigation still carries a "COVID-19 Update" item; menu items 'Cmb News' and 'Staff News'. Title verbatim: "CMB Family Dentistry" (brand-only). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook/Google/YouTube links on site [VERIFIED]; counts UNKNOWN.
• Breakdown: FC12/20 BM13/15 WW10/15 Gap11/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr7 Tech9 (/10)
• Independence: INFERRED (two named owner dentists; single office at 7 Davis Ave; membership plan run in-house; 'Now Accepting Selected Cigna PPO Plans' - no group language) - MEDIUM-HIGH confidence, verify on call | Decision-maker: Dr. David Brown, DDS (joined 2001) and Dr. Josh Alter, DMD, MS (joined 2013)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Delaware County/Main Line edge; full-mouth rehab, veneers, implants, laser, Invisalign; in-house membership plan -> mid tier | Digital spend: TeleVox/Milestone subscription; Pay Now link; in-house membership plan
• Hooks: 1) A 40-year Main Line Today 'Best of' practice whose site still carries a COVID-19 nav item (interior pages) and a <center>/<table> homepage layout. 2) Practice name is founder initials with the principals now Brown (2001) and Alter (2013) - a natural rebrand moment.
• Pitch/offer: Full rebrand around the 'Best of the Main Line' proof and full-mouth-rehab cases. $8-12k.
• Sources: cmbdental.com raw HTML + meet-the-doctor pages (2026-09-30); reviews.birdeye.com/d/dental/broomall-pa; WebSearch
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TeleVox/Milestone · region: Mid-Atlantic (wave 2)

80. Cinco Meadows Dental (Dr. Brian Williams) - Katy (Cinco Ranch), TX - https://www.cincomeadowsdental.com/ - 69/100 - MEDIUM-HIGH (medium confidence - founding year UNKNOWN)
• Est/Doctors: UNKNOWN | Dr. Brian Williams (Texas A&M; Baylor College of Dentistry DDS), 'Meet Our Doctors' page - VERIFIED; YP lists a prior/alternate name 'Joel Nickles, DDS' (ownership history UNKNOWN) | Reviews: Birdeye 4.9 (898 reviews; JSON-LD, 2026-09-30)
• Site (observed, raw HTML 2026-09-30): ProSites: raw HTML 'Prosites Web Engine Technology Version 4.0 Copyright � 2019 Prosites, Inc.' (mojibake); title 'Brian Williams DDS | Cinco Meadows Dental | Cosmetic Dentistry | Katy TX 77494' (ZIP code in title tag); 12 images; 'Modern Dentistry in a Classic Environment' tagline on a legacy template.
• Social gap: Facebook CincoMeadowsDental (followers UNKNOWN)
• Breakdown: FC13/20 BM8/15 WW10/15 Gap14/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap9 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - single named doctor, no DSO strings | Decision-maker: Dr. Brian Williams, DDS (named owner-doctor)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Cinco Ranch/Katy (Fort Bend-Harris affluent suburb), veneers, implants, Invisalign = mid-high tier | Digital spend: ProSites subscription (VERIFIED)
• Hooks: (1) '898 five-star reviews and a ZIP code in your title tag.' (2) 'Cinco Ranch is one of Houston's most affluent suburbs; the site is a 2019-engine ProSites template.'
• Pitch/offer: Cinco Ranch cosmetic homepage that converts the 898-review corpus; $6-9k solo.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /our-practice/meet-our-doctors/; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: South-Central (wave 2)

81. Dr. Rosenbaum & Associates — Modesto, CA — https://www.docsforteeth.com/ — 69/100 — MEDIUM (medium confidence)
• Est/Doctors: Founded 42+ years ago (VERIFIED on site) | 3 dentists | Reviews: Yelp 91 reviews (Jul 2026); Facebook 51 reviews (100% recommend); Modesto Bee Readers' Choice 9 yrs per search snippet ('175+ five-star, 4.9'). The earlier '700 five-star Google reviews' self-claim was NOT found in the current raw HTML. Source: yelp.com, facebook.com via WebSearch
• Site (observed): TNT Dental (VERIFIED source comment 'developed by TNT Dental Content Management System'; 'maintained by tntdental.com'). Title: 'Dentist Modesto, CA | Dentist Near Me | Dr. Rosenbaum & Associates' (keyword-spam pattern). Homepage HTML is only ~29KB. Footer '© Dr. Rosenbaum & Associates' carries no year.
• Social gap: UNKNOWN
• Breakdown: FC12/20 BM14/15 WW10/15 Gap11/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM1/2 | Subs: Gap7 Dep8 Tr7 Tech8
• Independence: INFERRED - founder-named, no group language; 3 dentists (associate model - verify on call). | Decision-maker: Robert Rosenbaum, DDS (founder, Georgetown); associates Gerardo Malogan, DDS and Pradip Katharotiya, DDS
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — 700+ reviews, 3 dentists, in-house implants, CareCredit; insurance-heavy general mix (tier: mid) | Digital spend: TNT Dental subscription
• Hooks: '700 five-star reviews and your title tag says Dentist Near Me.'
• Pitch/offer: Rebuild + review integration, redirect TNT spend; $5-8k.
• Wave-2 update (2026-09-30): 68 -> 69. Reviews verified but smaller than the site's earlier claim; net +1. curl 200; homepage <title> re-confirmed 'Dentist Modesto, CA | Dentist Near Me | Dr. Rosenbaum & Associates'.
• Sources: Raw HTML, WebFetch homepage
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: West (wave 1)

82. Pelandale Dental Care (Dr. Param Gill) — Modesto, CA — https://www.pelandaledental.com/ — 69/100 — MEDIUM (medium confidence)
• Est/Doctors: Practice founding year UNKNOWN; Gill 25+ yrs experience (VERIFIED on site) | 1 named dentist | Reviews: Yelp 71 reviews (Aug 2026); practice claims '250+ 5-star' top-rated in Central Valley; BBB profile exists. Source: yelp.com, bbb.org via WebSearch
• Site (observed): ProSites (VERIFIED: 'Prosites Web Engine Technology Version 4.0' comment). <title> is 'Welcome | Modesto, California | Pelandale Dental' and meta description is 'Welcome to our Welcome page.' Footer reads 'Robot enabled surgery center - 2026'. No review counts or aggregate rating on page.
• Social gap: Facebook and Twitter linked in footer; activity UNKNOWN.
• Breakdown: FC14/20 BM10/15 WW10/15 Gap11/15 Dep9/10 Tr8/10 Cv4/5 Sp2/3 DM1/2 | Subs: Gap7 Dep8 Tr8 Tech8
• Independence: INFERRED - single named dentist-owner, no group language. | Decision-maker: Dr. Param Gill (owner-dentist; 25+ yrs clinical experience)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — YOMI robot, LANAP laser, ortho + implants (tier: mid; capex-heavy for market) | Digital spend: ProSites subscription
• Hooks: 'Your meta description literally reads: Welcome to our Welcome page.'
• Pitch/offer: Technology-forward implant site; $8k.
• Wave-2 update (2026-09-30): 67 -> 69. Also markets YOMI robotic implant surgery (only one in the Modesto area per its own copy) = capex and high-ticket work; now also runs a GoHighLevel funnel site (pelandale-dental.com, (c) 2026) beside the ProSites (c)2019 main site. Live.
• Sources: Raw HTML, WebFetch homepage
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: West (wave 1)

83. Annapolis Dental Associates — Annapolis, MD — https://www.annapolisdentalassociates.net/ — 69/100 — MEDIUM (review enrichment wave 2, 2026-09-30)
• Est/Doctors: Site footer ©2004; patient testimonial 'over 20 years' [VERIFIED on site]; founding year INFERRED ~2004; 5 dentists: Drs. Waddell, Bjorklund, Warfield, Shanahan, Ahmed; ADA, AGD, ICOI and laser-dentistry memberships [VERIFIED on site] | Reviews: 92 verified reviews, 4.8 (aggregator, search snippet); BBB profile; Yelp listing; 5 testimonials on homepage. In business ~31 yrs per aggregator; footer '(c) 2004 -' [VERIFIED]
• Site (observed): Custom/legacy vendor. Footer verbatim: "© 2004 - 2026 American Dental Software All rights reserved • Site Designed, Maintained & Hosted by Siva Solutions Inc."; title tag verbatim: "Dentist Near Me | Dentist Office Near Me | Annapolis, MD"; table/font markup; 11 of 34 images have no alt text; mixed http assets. [VERIFIED raw HTML + rendered fetch, 2026-09-30]
• Social gap: Facebook, Instagram, YouTube, Twitter links present [VERIFIED].
• Breakdown: FC14/20 BM11/15 WW11/15 Gap9/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM1/2 | Gap7 Dep8 Tr8 Tech8 (/10)
• Independence: MEDIUM confidence - verify on call (5-dentist group practice; no ownership statement; no DSO keywords found; ownership entity 'American Dental Software' in footer is a vendor string) | Decision-maker: Dr. Waddell (senior dentist named first; owner UNKNOWN)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Annapolis (Ridgely Ave medical corridor), 5 dentists, lasers, implants (ICOI), sedation -> upper-mid tier | Digital spend: Siva Solutions hosting/maintenance; social channels active links
• Hooks: 1) Title tag is literally "Dentist Near Me | Dentist Office Near Me". 2) Footer credits 'American Dental Software' and Siva Solutions.
• Pitch/offer: Multi-doctor flagship redesign; $10-14k.
• Sources: annapolisdentalassociates.net raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 70 -> 69 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Mid-Atlantic (wave 1)

84. James A. Vito, DMD (Prosthodontics & Periodontics) — Wayne, PA — https://www.jamesvito.com/ — 69/100 — MEDIUM (review enrichment wave 2, 2026-09-30)
• Est/Doctors: 'Over 30 years of experience' [VERIFIED on site]; 1 dentist (Dr. James A. Vito DMD), advanced training in prosthodontics and periodontics; in-office ceramist [VERIFIED on site]; board certification UNKNOWN | Reviews: Healthgrades 86 reviews (Dr. James Vito); Yelp listing; Facebook page; dual-board specialist (perio/prosth/implant), in practice since 1987 (search snippet 2026-09-30)
• Site (observed): ProSites. Footer verbatim: "©2026 James A. Vito D.M.D - All Rights Reserved | Site Developed by ProSites.com"; source comment with mojibake "Copyright � 2019 Prosites, Inc."; jQuery 1.9.1; 11 of 17 images have no alt text; title " Dentist in Wayne & St. David's, PA | Prosthodontics ...". [VERIFIED raw HTML, 2026-09-30]
• Social gap: Facebook and Yelp links only [VERIFIED].
• Breakdown: FC13/20 BM11/15 WW11/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Gap7 Dep8 Tr8 Tech9 (/10)
• Independence: INFERRED (solo owner; PA professional practice) | Decision-maker: Dr. James A. Vito DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Wayne / Main Line, implants + All-on-X + sedation + laser + in-house ceramist -> upper-mid tier for a solo | Digital spend: ProSites subscription
• Hooks: 1) Advanced prosthodontic/perio work presented on a generic ProSites layout. 2) Retirement-horizon solo: pitch as legacy/transition-ready site.
• Pitch/offer: Solo prosthodontic authority redesign; $6-9k.
• Sources: jamesvito.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 68 -> 69 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 1)

85. Serafin Family Dentistry — Carlisle, PA — https://www.serafinfamilydentistry.com/ — 69/100 — MEDIUM (LOW-MEDIUM confidence: est year, reviews, doctors' tenure UNKNOWN)
• Est/Doctors: UNKNOWN [no founding year on site]; Dr. Robert Serafin, Dr. Tamara Shore (Serafin) [VERIFIED on site] | Reviews: Birdeye 389 reviews, 5.0; Chamber of Commerce 5.0 from 249 reviewers; Facebook 98% recommend / 69; Yelp listed (search 2026-09-30). Homepage shows no counts [VERIFIED]
• Site (observed): Progressive Dental template. Dead Google+ link in source (plus.google.com/107238089648275731748/about?hl=en); no copyright year in footer; footer verbatim "Dental Website Development By Progressive Dental"; YouTube icon links to a bare placeholder "http://"; title tag "Drs. Robert Serafin & Tamara Shore | Carlisle Dentist" (no service/keyword content). [VERIFIED raw HTML, 2026-09-30]
• Social gap: Google+ and YouTube (placeholder href) only; no Facebook/Instagram [VERIFIED].
• Breakdown: FC11/20 BM10/15 WW12/15 Gap13/15 Dep8/10 Tr8/10 Cv4/5 Sp1/3 DM2/2 | Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED (husband-and-wife practice; no group language) | Decision-maker: Dr. Robert Serafin DDS
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Carlisle / Cumberland County, implants + full-mouth reconstruction + implant dentures -> mid tier | Digital spend: Progressive Dental site subscription
• Hooks: 1) Google+ link (retired in 2019) and a placeholder YouTube href are still on the homepage. 2) No copyright year at all.
• Pitch/offer: Implant/full-mouth-led redesign; $5-8k.
• Sources: serafinfamilydentistry.com raw HTML + rendered fetch (2026-09-30)
• Wave-2 note: score 62 -> 69 after review-count enrichment; site re-fetched live 2026-09-30 (HTTP 200).
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Progressive Dental Marketing · region: Mid-Atlantic (wave 1)

86. Allison Family & Cosmetic Dentistry (F. Vincent Allison III, DDS, PA) — Durham, NC — https://www.allisonfamilydentistry.com/ — 69/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: Est. UNKNOWN (site carries no history page); office 6208 Fayetteville Rd Ste 102, South Durham; family + cosmetic (veneers, whitening) positioning | Reviews: Healthgrades Dr. F. Vincent Allison 4.8 / 188 ratings (Healthgrades directory search); Google count UNKNOWN (WebSearch quota exhausted)
• Site (observed): ProSites. Raw HTML carries "Copyright � 2019 Prosites, Inc. All Rights Reserved" (mojibake). Homepage <title>: "Durham Dentist, Dr. F. Vincent Allison III" (no service or practice name). Legacy Universal Analytics id UA-1769281-1 and jQuery 1.9.1 in source; 5 of 10 images without alt text. 108KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC11/20 BM10/15 WW14/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Subs: Gap 7 Dep 8 Tr 8 Tech 8 (/10)
• Independence: INFERRED — professional-association entity 'F. Vincent Allison III, DDS, PA'; no group language; not in EXCLUSIONS.md (Triangle exclusions are Lehmann/Triangle Restoration only) | Decision-maker: Dr. F. Vincent Allison III, DDS (owner — 'F. Vincent Allison III, DDS, PA' entity in footer)
• FinCap: South Durham cosmetic/family practice with 188 Healthgrades ratings — Mid | Digital spend: ProSites subscription (observed)
• Hooks: 1) 188 Healthgrades ratings at 4.8 vs. a ProSites shell whose title is just 'Durham Dentist, Dr. F. Vincent Allison III'. 2) ProSites mojibake footer + UA-1769281-1 tag from the 2000s.
• Pitch/offer: Solo/small cosmetic practice — $5–8k
• Sources: allisonfamilydentistry.com raw HTML (curl) + WebFetch not needed; Healthgrades usearch (Allison); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Southeast (wave 2)

87. Iglesias Dental Group (formerly Walter K. Kulick, DMD, PA) — Coral Springs, FL — https://www.dentistrycoralsprings.com/ — 69/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: Practice 'Dr. Walter Kulick founded in 1988'; 'over 30 years' (VERIFIED, site); Iglesias doctors now 'carry on a legacy' (generational handoff); CBCT, guided implant surgery, in-house digital lab (VERIFIED, site) | Reviews: Google count UNKNOWN (WebSearch quota exhausted); Healthgrades: Dr. Kulick 5.0/14, Dr. Ghodsi 4.6/12 at same address (thin)
• Site (observed): TNT Dental (footer 'Site designed and maintained by TNT Dental'). Homepage <title>: "Dentist Coral Springs | Dentist Near Me | Iglesias Dental Group". Domain dentistrycoralsprings.com still carries the Kulick-era Coral Springs keyword slug vs. new Iglesias brand. 39KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC13/20 BM13/15 WW12/15 Gap6/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap 5 Dep 8 Tr 8 Tech 9 (/10)
• Independence: VERIFIED — site states 'As a privately-owned practice'; owner-doctors named; no DSO markers | Decision-maker: Drs. Daniyel and Haissel Iglesias, DDS (owners — VERIFIED 'privately-owned practice')
• FinCap: Coral Springs implant/restorative practice with CBCT and in-house lab — Mid-High | Digital spend: TNT Dental (retainer/hosting likely redirectable)
• Hooks: 1) Ownership transition (Kulick 1988 → Iglesias) with a 'Dentist Near Me' title and slug domain. 2) CBCT + in-house digital lab capex not reflected on a stock template.
• Pitch/offer: Rebrand/handoff redesign — $8–12k
• Sources: dentistrycoralsprings.com raw HTML (curl) + pg text; Healthgrades usearch; EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Southeast (wave 2)

88. DeMartin Dental Associates - Fairfield, CT - https://www.demartindental.com/ - 69/100 - MEDIUM (low-medium)
• Est/Doctors: 'Serving Fairfield County For Over 65 Years' (VERIFIED, homepage); 2 doctors; 69 Sherman St | Reviews: Birdeye 113 reviews / 4.7 (Birdeye Fairfield directory JSON-LD, 2026-09-30); Healthgrades link on site
• Site (observed): Sesame 24-7 (footer "Website Powered by Sesame 24-7 (TM) | Site Map | Back to Top"); 29,312-byte homepage; meta description "...Invisalign(R) to patients in Fairfield, Westport, and Bridgeport, CT"; nav 'Our Blog / Office Tour / Testimonials' template set
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC13/20 BM14/15 WW11/15 Gap9/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM1/2 | Subs: Gap6 Dep8 Tr8 Tech8 (/10)
• Independence: INFERRED - two named doctors, legacy family name, no group language or DSO strings in raw HTML (legacy-name-with-new-owners pattern: confirm no DSO on call) | Decision-maker: Edward V. Finnigan, DDS / Matthew E. Vinoski, DMD (ownership split UNKNOWN - verify on call)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2 (Fairfield CT; general + Invisalign + veneers; 2 doctors) | Digital spend: Sesame 24-7 subscription
• Hooks: 1) '65 years' heritage sold with a stock Sesame template 2) Generational hand-off (legacy DeMartin name, two current doctors) = timing event
• Pitch/offer: Standard redesign around heritage + doctors - $8-12k standard tier
• Sources: demartindental.com (curl raw HTML); Birdeye Fairfield CT directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Northeast (wave 2)

89. Egidio Dental Care (Aaron J. Egidio, DDS) - Madison, CT - https://www.egidiodentalcare.com/ - 69/100 - MEDIUM (medium)
• Est/Doctors: 'more than 20 years' (VERIFIED, homepage); solo; 149 Durham Rd | Reviews: Birdeye 342 reviews / 5.0 (Birdeye Madison CT directory JSON-LD, 2026-09-30); Healthgrades link on site
• Site (observed): Sesame 24-7 (footer "Website Powered by Sesame 24-7(TM) | Site Map | Back to Top"); 18,359-byte homepage; title "Dentist in Madison, CT | Egidio Dental Care"; services list shows only 'Digital X-rays / Teeth Whitening / Preventive Care'
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC12/20 BM10/15 WW11/15 Gap12/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep8 Tr9 Tech9 (/10)
• Independence: INFERRED - solo owner-dentist named; no group language or DSO strings in raw HTML | Decision-maker: Aaron J. Egidio, DDS (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2 (Madison CT shoreline; preventive/restorative/aesthetic; solo) | Digital spend: Sesame 24-7 subscription
• Hooks: 1) 342 reviews at 5.0 not surfaced on an 18KB template 2) Homepage services list is preventive-only for a 20-year shoreline practice
• Pitch/offer: Solo redesign - $5-8k solo tier
• Sources: egidiodentalcare.com (curl raw HTML); Birdeye Madison CT directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Northeast (wave 2)

90. Blossfeld Family Dentistry (Dr. Carol M. Blossfeld) - Edmond / Oklahoma City, OK - https://www.drblossfeld.com/ - 69/100 - MEDIUM (medium confidence - succession unknown (40+ yrs in field))
• Est/Doctors: YellowPages: 29 years in business | Dr. Blossfeld (dental school 1996, 'more than 40 years in the dental field'), solo - VERIFIED on /meet-the-doctor-and-team/ | Reviews: Birdeye 5.0 (440 reviews) + two further Birdeye profiles 5.0 (194) and 5.0 (142), 2026-09-30 (may overlap)
• Site (observed, raw HTML 2026-09-30): ProSites: raw HTML comment 'Prosites Web Engine Technology Version 4.0 Copyright � 2019 Prosites, Inc.' (mojibake); title 'Edmond Dentist, Blossfeld Family Dentistry - Welcome' (trailing 'Welcome'); only 3 images on the homepage; footer 'Site Developed by ProSites.com'; bot-intermittent (site sometimes returns an empty body to curl).
• Social gap: Facebook drblossfeld (followers UNKNOWN)
• Breakdown: FC12/20 BM12/15 WW10/15 Gap12/15 Dep7/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED - single named owner, no DSO strings | Decision-maker: Dr. Carol M. Blossfeld, DDS (solo owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Edmond/north OKC affluent market; veneers, dental makeovers, sedation = mid tier | Digital spend: ProSites subscription (VERIFIED)
• Hooks: (1) 'Three Birdeye profiles, 440+ five-star reviews - and a 3-image ProSites page titled "Welcome".' (2) 'Dr. Blossfeld built this practice from day one; the site has not been rebuilt since the 2019 ProSites engine.'
• Pitch/offer: Edmond cosmetic/family homepage with review wall; $6-8k solo.
• Sources: curl + raw HTML (2026-09-30); Birdeye JSON-LD; /meet-the-doctor-and-team/; YellowPages Edmond; EXCLUSIONS/log grep clean
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: South-Central (wave 2)

91. Perfect Smiles Dental Care — Lenexa, KS — perfectsmilesdentalcare.com — 68/100 — MEDIUM-HIGH (medium-high)
• Est/Doctors: Serving Lenexa since 1991 (VERIFIED, site); 2 doctors: Kelly Bridenstine DDS (Univ. of Iowa 1987; IV/oral sedation Level II permit 2009) + Tracy Boldry DMD, MS, board-certified prosthodontist (VERIFIED, site) | Reviews: 4.4 avg on 61 reviews (aggregator snippet, WebSearch); Yelp 15 reviews; 'dentists helping patients for more than 30 years' (site snippet). [Wave-2 enrichment]
• Site (observed): TNT Dental template — footer 'Site designed and maintained by TNT Dental'; homepage <title> is the keyword-spam pattern "Dentist Lenexa, KS | Dentist Near Me | Perfect Smiles Dental Care"; a board-certified prosthodontist and 'official cosmetic dentist for multiple USA Pageant circuits' positioning sit inside a generic 'Dentist Near Me' template (VERIFIED, raw HTML + render). Note: rendered layout is responsive with online booking, so the gap is positioning/SEO-title more than raw age.
• Social gap: UNKNOWN (not checked)
• Breakdown: FC13/20 BM12/15 WW9/15 Gap9/15 Dep8/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap6 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — no group/DSO language on home/About; directory entity 'Bridenstine Kelly D DDS' (single-owner PC); no Heartland/Aspen/MB2/Marquee strings in HTML | Decision-maker: Dr. Kelly Bridenstine, DDS (owner; VERIFIED on site)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — in-house prosthodontist + IV sedation + pageant-cosmetic positioning in Johnson County KS | Digital spend: TNT Dental hosting/maintenance (existing vendor to redirect)
• Hooks: 1) Title tag reads 'Dentist Lenexa, KS | Dentist Near Me | Perfect Smiles Dental Care' — a 35-year prosthodontist-backed practice branded as 'near me' 2) 'Since 1991' + board-certified prosthodontist + pageant-circuit cosmetic work deserve a flagship homepage
• Pitch/offer: Premium prosthodontic/cosmetic flagship homepage replacing TNT template; keep booking. $8–12k
• Sources: site homepage/about (curl+render), dentistsup.com listing
• Wave-2 re-score: 70 -> 68. Moderate corpus, 4.4 avg is below premium band; Gap lowered.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Midwest (wave 1)

92. Somerset Hills Family Dentist (Joseph M. Micale, DMD, PA) — Basking Ridge, NJ — https://www.somersethillsfamilydentist.com/ — 68/100 — MEDIUM-HIGH(medium)
• Est/Doctors: Serving Somerset Hills since 1993 (VERIFIED, site copy); multi-doctor UNKNOWN | Reviews: Modest corpus: Birdeye 42 reviews / 5.0 (Birdeye directory JSON-LD); Healthgrades 2; Yelp few reviews, 5 stars (VERIFIED). Site has /testimonials/ and /patient-reviews/ pages
• Site (observed): ProSites; footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; /our-practice/meet-the-doctor/ returns a soft "Page Not Found" ("Sorry, we looked all over but couldn't find the page you requested"); title "Basking Ridge NJ Dentist | Dr Joseph Micale | General Dentistry | NJ Cosmetic Dentist" (keyword chain); http:// address does not redirect to https
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC14/20 BM11/15 WW11/15 Gap10/15 Dep8/10 Tr7/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap7 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — PA named for owner Dr. Micale; no group language or DSO strings | Decision-maker: Joseph M. Micale, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 1-2 (Somerset Hills/Bernardsville affluent market; implants 23 mentions, cosmetic) | Digital spend: ProSites subscription
• Hooks: 1) Doctor-bio URL /our-practice/meet-the-doctor/ 404s with "Sorry, we looked all over" on the practice's own site 2) Since 1993 with patients of "over 40 years" quoted in testimonials — none of it is structured as proof
• Pitch/offer: Somerset Hills boutique redesign with fixed doctor bio + review integration — $8–12k standard tier.
• Sources: Live fetch somersethillsfamilydentist.com raw HTML | Wave-2 review enrichment (2026-09-30): Healthgrades, Yelp snippets; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 1)

93. North Macon Dental Associates — Macon, GA — https://www.northmacondentalassociates.com/ — 68/100 — MEDIUM-HIGH (confidence: MEDIUM-HIGH)
• Est/Doctors: Founded 40+ years ago by Dr. Lee Stockslager (VERIFIED, site: "over 40 years"); ownership transitioned to Dr. Baker-Anday (generational handoff) | Reviews: Facebook 92% recommend / 55 reviews; Chamber of Commerce 4.0 stars / 49; Yelp 12; BestProsInTown 125 aggregated (search snippets) - thin/mixed corpus, one reviewer alleges missed cavities, community calls it "among the cheapest rates" (low-ticket signal) [WAVE 2]
• Site (observed): Wix Website Builder (generator meta), 1.26MB page. Footer: "© 2035 by North Macon Dental Associates" (raw HTML). Placeholder phone "123-456-7890" appears in the page next to the real 478-280-9158 (raw HTML). Rendered header nav items all point to the homepage. Title: "North Macon Dental Associates | Family & Cosmetic Dentist in Macon, GA".
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC8/20 BM14/15 WW13/15 Gap8/15 Dep7/10 Tr9/10 Cv4/5 Sp3/3 DM2/2 | Gap 6 Dep 7 Tr 9 Tech 8
• Independence: INFERRED — successor-doctor owner language, no group/DSO markers on page | Decision-maker: Dr. Jordan Baker-Anday (current owner/operator — per site; founder Dr. Lee Stockslager retired)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Single active doctor, CBCT + 3D printing + implants/full-mouth restorations; Macon mid-market — Mid | Digital spend: Wix plan (observed)
• Hooks: 1) © 2035 and a 123-456-7890 placeholder phone are live on the homepage. 2) New owner-dentist inheriting a 40-year name — natural moment to rebuild.
• Pitch/offer: Successor-owner rebrand/redesign — $5–8k
• Sources: northmacondentalassociates.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Wix · region: Southeast (wave 1)

94. Passidomo Cosmetic & Family Dentistry (Dr. Passidomo & Dr. Brij Patel) — Centerville (Dayton), OH — dpsmilecenter.com — 68/100 — MEDIUM-HIGH (medium)
• Est/Doctors: Passidomo DMD 1993 (~33 yrs since degree; practice founding year UNKNOWN); second dentist Dr. Brij Patel (page title 'Dr. Danial Passidomo and Dr. Brij Patel Family Dentistry') — possible succession/associate transition (INFERRED) | Reviews: Yelp 23 reviews; Healthgrades 5 reviews for Dr. Passidomo; ~4.9 avg per aggregate snippet; RateMDs/WebMD/US News listings exist (WebSearch). Corpus small for a 33-yr practice. [Wave-2 enrichment]
• Site (observed): TNT Dental — footer "&copy; 2014 Daniel Passidomo, DMD | Site designed and maintained by TNT Dental"; live COVID banner "Click Here to See our Advanced COVID Safety Protocols -->"; misspelling 'Dr. Danial Passidomo' in the Meet-Our-Dentists page title; menu: Full Mouth Reconstruction, Porcelain Veneers, Smile Makeover, NV Soft Tissue Laser (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC12/20 BM11/15 WW12/15 Gap9/15 Dep7/10 Tr8/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap6 Dep7 Tr8 Tech8 (/10)
• Independence: INFERRED — directory entity 'Daniel J Passidomo DMD Cosmetic & Family Dentistry'; Patel practice line suggests merger/associate — verify ownership on call; no DSO strings | Decision-maker: Dr. Dan Passidomo, DMD (Kentucky DMD 1993; VERIFIED) — Dr. Brij Patel is a second named dentist
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — upper-mid — cosmetic/full-mouth scope in Centerville (affluent Dayton suburb) | Digital spend: TNT Dental (redirect target)
• Hooks: 1) Footer frozen at ©2014 and COVID-protocol banner still on the homepage 2) A 'Passidomo + Patel' handoff is a natural rebrand moment
• Pitch/offer: Two-doctor rebrand/succession site with cosmetic showcase. $8–12k
• Sources: dpsmilecenter.com raw HTML + /meet-our-dentists.html
• Wave-2 re-score: 70 -> 68. Small review base lowers Gap/FC. Raw HTML re-verified: '&copy; 2014 ... Site designed and maintained by TNT Dental'.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: TNT Dental · region: Midwest (wave 1)

95. Michael A. MacInnes, DDS, PLLC — Sammamish, WA — https://www.macinnesdentistry.com/ — 68/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: NYU dental 2001 (VERIFIED); 'Serving Sammamish, Issaquah, & Redmond for Sixteen Years' (VERIFIED on site); YellowPages tenure 21 yrs (INFERRED) | 1 doctor | Reviews: Google/Yelp counts UNKNOWN (bot-blocked); YellowPages 1; Opencare 0; homepage banner 'Trusted by Dental Specialists ... 16 Consecutive Years 2011~2026' (Seattle Met Top Dentists, self-reported)
• Site (observed): Weebly build (VERIFIED: cdn11.editmysite.com assets, weebly.com formSubmit, Bootstrap 3.3.7 CDN). Homepage <title> = 'Michael MacInnes DDS, PLLC - "cosmetic dentist", "family dentist", "open saturdays", saturday, (425) 391-8830' (keyword list + phone in title). Footer 'Michael A. MacInnes, DDS, PLLC | Privacy Policy | 2022 © All Rights Reserved'; newest content is a June 2023 newsletter; legacy /your-visit-old.html still linked.
• Social gap: UNKNOWN (no social links located in raw HTML).
• Breakdown: FC13/20 BM11/15 WW12/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp1/3 DM2/2 | Subs: Gap7 Dep8 Tr9 Tech9
• Independence: VERIFIED - PLLC in footer, solo doctor, no group language | Decision-maker: Dr. Michael A. MacInnes (owner)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Sammamish Plateau affluent market; CEREC, 3-D X-ray/CBCT, Isolite, implants ('especially complicated surgical procedures'), conscious sedation (tier: upper-mid) | Digital spend: Weebly plan, Wufoo dental-history form
• Hooks: 'Sixteen years as a Seattle Met Top Dentist and the site is a 2022 Weebly with a phone number in the title tag.' / Implant and CEREC menu buried behind a services list.
• Pitch/offer: Solo premium rebuild keeping his Wufoo intake; $5-8k solo.
• Sources: Raw HTML curl 200 (title, editmysite/weebly assets, footer); text of /; YellowPages Sammamish listing (WebFetch); Opencare Sammamish listing; EXCLUSIONS grep clear
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Weebly · region: West (wave 2)

96. Kahala Smile Professionals, LLC (Drs. Candace & Robert Wada) — Honolulu (Kahala), HI — https://www.kahalasmileprofessionals.com/ — 68/100 — MEDIUM-HIGH (medium confidence)
• Est/Doctors: Dr. Candace M. Wada 'over 30 years' of practice (VERIFIED on doctors page); YellowPages 29 yrs (INFERRED) | 2 doctors: founder Candace Wada + son Dr. Robert J. M. Wada (associate, 'recently joined') | Reviews: Google/Yelp counts UNKNOWN (bot-blocked); site shows Opencare-verified and 'Patients' Choice Awards (2015)' badges and lists Honolulu Magazine Top Dentist 2015-2022 (Candace) / 2018-2022 (Robert)
• Site (observed): ProSites v4 (VERIFIED raw footer 'Copyright � 2019 Prosites, Inc. All Rights Reserved.'). Homepage <title> 'Welcome | Honolulu, HI | Kahala Smile Professionals, LLC'; meta description begins 'Welcome to our Welcome page. Contact Kahala Smile Professionals, LLC today at (808) 732-9232...'. Source also links a leaked staging URL (directory.staging.asird.org/doctors/candace-wada) and a bare relative 'OurPractice.aspx' link. Newest recognition on the page is 2022.
• Social gap: UNKNOWN.
• Breakdown: FC14/20 BM11/15 WW12/15 Gap8/15 Dep8/10 Tr8/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap7 Dep8 Tr8 Tech8
• Independence: INFERRED (strong) - family-run LLC, no group language | Decision-maker: Dr. Candace M. Wada (founder; office email drcandacewada@gmail.com on the site)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Waialae Ave/Kahala office in Honolulu's most affluent enclave, CEREC, 3i implants, laser, veneers, two doctors, CareCredit (tier: upper-mid) | Digital spend: ProSites subscription; Opencare listing
• Hooks: 'Meta description reads Welcome to our Welcome page' / Generational handoff to Dr. Robert Wada is a natural relaunch moment; eight years of Honolulu Magazine awards not reflected in a 2019-era site.
• Pitch/offer: Family-practice rebuild that showcases both doctors and awards; keep existing CareCredit/forms links; $8-10k standard.
• Sources: Raw HTML curl 200 (title, meta description, footer, staging link); WebFetch of / and /our-practice/meet-the-doctors/; YellowPages Honolulu listing; EXCLUSIONS grep clear (Hawaii entries: Hawaii Cosmetic Dental, Yasuhara/Okuda/Umeda only)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: West (wave 2)

97. Lee Dental Care — Fort Myers, FL — https://www.leedental.net/ — 68/100 — MEDIUM-HIGH (confidence: MEDIUM) [BELOW 68 CUT LINE — bench only]
• Est/Doctors: "Serving Fort Myers since 1983" (VERIFIED, meta description) | Founded 1983 as group practice; Drs. Yassamin Lenzi, Efrain Plaza, Annelise Perez, Keith Morse, Paul Uliasz (search snippet); serves Fort Myers/N. Fort Myers/Cape Coral; positioning "affordable" = lower ticket; fetch found no DSO/parent language | Reviews: Birdeye 6,838 reviews / 4.8 (search snippet, birdeye.com; another snapshot 6,853); Yelp 61; embedded Birdeye widget on own site. Very large corpus [WAVE 2]
• Site (observed): raw footer "Website Powered by Sesame 24-7™ | Site Map | Privacy Policy"; no © year anywhere; Birdeye widget embed. Title: "Fort Myers Family Dentist | Dental Implants & Invisalign | Lee Dental Care".
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC11/20 BM13/15 WW8/15 Gap13/15 Dep7/10 Tr7/10 Cv5/5 Sp3/3 DM1/2 | Gap 8 Dep 7 Tr 7 Tech 8
• Independence: MEDIUM confidence — verify on call (doctor names not shown on homepage) | Decision-maker: UNKNOWN (doctor names not on homepage)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — General/implant/Invisalign — Fort Myers — Mid | Digital spend: Sesame 24-7 + Birdeye (observed)
• Hooks: 1) Sesame 24-7 template with no copyright line. 2) Birdeye reviews present but buried in a widget.
• Pitch/offer: Standard redesign — $5–8k
• Sources: leedental.net (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Southeast (wave 1)

98. Delmar Dental Medicine (Thomas H. Abele, DMD, FAGD) — Delmar, NY — https://delmardental.com/ — 68/100 — MEDIUM(medium)
• Est/Doctors: Located in Delmar since 1969 (VERIFIED, homepage); Abele offering implants 30+ years; other doctors UNKNOWN | Reviews: Moderate corpus: Birdeye 57 reviews / 5.0 (plus a 7-review / 2.7 duplicate listing); Dentascore 23 reviews; Healthgrades 9 reviews; Vitals 3.4/5 (5 ratings); BBB profile; Yelp listing; long-tenure patient comments (30+ yrs) (VERIFIED via snippets)
• Site (observed): Legacy .htm site (22KB): footer "Copyright &copy; Delmar Dental Medicine 2016. All Rights Reserved. Website Design by WebDesign" (unrendered HTML entity in visible text); title is a keyword string "Dentist Delmar NY Dental Practice Glenmont Dental Office Slingerlands NY Dental Care"; pages named /dentalimplants.htm, /oralsurgery.htm; http:// URL does not redirect to https
• Social gap: UNKNOWN (social channels not inspected this run)
• Breakdown: FC12/20 BM13/15 WW13/15 Gap10/15 Dep7/10 Tr6/10 Cv3/5 Sp2/3 DM2/2 | Subs: Gap7 Dep6 Tr9 Tech9 (/10)
• Independence: INFERRED — homepage names sole owner Dr. Abele; no group language or DSO strings | Decision-maker: Thomas H. Abele, DMD, FAGD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Tier 2 (Capital District; on-site lab, conscious sedation, implants/oral surgery) | Digital spend: Custom/agency-built site (2016); no vendor subscription identified
• Hooks: 1) Open in Delmar "since 1969" and on-site ceramic lab, yet the site is a keyword-stuffed 2016 .htm build with an unrendered "&copy;" in the footer 2) Sedation + implants + in-house lab are undersold by the current pages
• Pitch/offer: Heritage-forward redesign ('since 1969') with sedation/implant service pages — $8–12k. Retirement-horizon flag (55+ years in one location); succession unknown.
• Sources: Live fetch delmardental.com raw HTML; About-page text via search snippet (Delmar Dental Medicine since 1969) | Wave-2 review enrichment (2026-09-30): Dentascore 23, Healthgrades 9, Vitals 5; homepage re-curled 200 OK
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Custom-dated / small agency · region: Northeast (wave 1)

99. Family Smile Dentistry (Drs. Foroughi & Jarquin) — Lakewood Ranch (Bradenton), FL — https://familysmiledentistry.com/ — 68/100 — MEDIUM (confidence: MEDIUM-HIGH)
• Est/Doctors: "Since 2001"; "more than 25 years" (VERIFIED, site); 2 doctors | Reviews: Yelp 15 reviews; directory average "5 stars" - Google count NOT found (UNKNOWN); thin visible corpus [WAVE 2]
• Site (observed): 36KB legacy template. <title> = " Implants, dentures, crown and bridge - Family Smile Dentistry  Lakewood Ranch, Bradenton, Sarasota Dentist Cosmetic and general dentistry with crowns in 1 day". No copyright notice at all in footer (just address/phone/fax). Rendered page shows broken/placeholder decorative images and duplicated nav.
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC11/20 BM12/15 WW12/15 Gap8/15 Dep7/10 Tr9/10 Cv4/5 Sp3/3 DM2/2 | Gap 6 Dep 7 Tr 9 Tech 8
• Independence: INFERRED — 'family-owned, privately operated dental practice'; no group markers; email on practice domain | Decision-maker: Drs. Foroughi & Jarquin (owner status INFERRED — 'family-owned, privately operated')
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — CEREC same-day crowns, digital dentures, implants in Lakewood Ranch (affluent, fast-growing) — Mid | Digital spend: Vendor-hosted template (observed)
• Hooks: 1) Homepage title is a 30-word keyword run-on with a leading space. 2) No copyright/footer identity at all.
• Pitch/offer: Family/cosmetic redesign — $5–8k
• Sources: familysmiledentistry.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Unknown / unattributed template · region: Southeast (wave 1)

100. Jonson Dental Care (George P. Jonson DDS) — Kettering (Dayton), OH — jonsondentalcare.com — 68/100 — MEDIUM (medium)
• Est/Doctors: 'Over 30 years of experience' (VERIFIED, site); IDIA implant fellowship listed; sedation, laser, TMJ, sleep-apnea appliances; team unnamed — solo, retirement-horizon flag | Reviews: Birdeye 72 reviews, 4.4; homepage/reviews page widget links to Demandforce profile 'comprehensivegeneralandimplantdentistry' whose snippet shows 990 reviewers, 99.5% would refer (INFERRED same practice, VERIFIED widget link in raw HTML); 30+ yrs (site). [Wave-2 enrichment]
• Site (observed): ProSites — footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; dead Google+ link "plus.google.com/117333242418443823074/about"; legacy-format Facebook link 'facebook.com/pages/George-P-Jonson-DDS/…'; office email on ISP domain gpjoffice@swohio.twcbc.com; <title> "Kettering Dentist | Dayton Dentistry | Jonson Dental Care" (VERIFIED raw HTML)
• Social gap: Facebook page link is the pre-2015 'pages/' format (VERIFIED); activity UNKNOWN
• Breakdown: FC11/20 BM12/15 WW11/15 Gap11/15 Dep7/10 Tr7/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap7 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — solo 'George P. Jonson DDS'; no group language | Decision-maker: Dr. George P. Jonson, DDS (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — mid — implant/sedation solo in Kettering | Digital spend: ProSites subscription
• Hooks: 1) Practice email is a Time Warner Cable address (gpjoffice@swohio.twcbc.com) and Google+ link is still in the HTML 2) 30+ year implant-fellow solo — a legacy-capture site before transition
• Pitch/offer: Solo implant/sedation redesign. $5–8k
• Sources: jonsondentalcare.com raw HTML + render
• Wave-2 re-score: 66 -> 68. Demandforce corpus (~990) sits behind an old widget; Gap raised.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 1)

## Bench (101–108, full profiles)

101. Orinda Dental Care — Orinda, CA — https://orindadentalcare.com/ — 68/100 — MEDIUM (MEDIUM confidence - verify on call)
• Est/Doctors: 'over 30 yrs' (self-stated on site) | 2 doctors | Reviews: Yelp 88 reviews (Aug 2026); Birdeye 4.8 (70); site widget shows 69 Google reviews (VERIFIED in page source). Source: yelp.com, birdeye.com via WebSearch + raw HTML
• Site (observed): WordPress 'dentalia' theme + Slider Revolution; footer 'Copyright ©2021. Designed by VANTECHS'; <title> 'Orinda Dental Care General , Cosmetic and Family Dentist' (stray space before comma). Copy is generic ('state of the art technology').
• Social gap: UNKNOWN
• Breakdown: FC15/20 BM11/15 WW9/15 Gap9/15 Dep8/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap6 Dep8 Tr8 Tech8
• Independence: INFERRED (upgraded from MEDIUM) - search snippet names Dr. Morgan Mehranfard as owner and lead dentist; no group language | Decision-maker: Dr. Morgan Mehranfard, DDS (owner/lead); Dr. Deepti Singh, DDS (associate)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Orinda/Lamorinda affluent market; Invisalign/iTero/implants/TMJ (tier: upper-mid) | Digital spend: agency site (VANTECHS)
• Hooks: 'Your footer is frozen at 2021 in a town where patients research for veneers and implants.'
• Pitch/offer: Lamorinda premium rebuild; $8k.
• Wave-2 update (2026-09-30): 65 -> 68. Search snippets name Dr. Morgan Mehranfard as 'owner and lead dentist' (upgrades DM and independence from MEDIUM to INFERRED-owner-led). Live.
• Sources: Raw HTML, WebFetch /about/
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: West (wave 1)

102. Lundstrom Family Dentistry — Fargo, ND — fargodentist.net — 68/100 — MEDIUM (medium)
• Est/Doctors: 'Practicing dentistry in our community for 33 years' (VERIFIED, About); U of Minnesota DDS 1993; solo; CEREC same-day crowns, 'SMART' amalgam-removal protocol, holistic + cosmetic + implants | Reviews: 4.7 on 196-197 reviews (Birdeye reviews.birdeye.com/lundstrom-family-dentistry-155336071935659); Yelp 17; Healthgrades 5; est. 1993 (Healthgrades directory). [Wave-2 enrichment]
• Site (observed): ProSites — footer "Copyright � 2019 Prosites, Inc. All Rights Reserved"; dead Google+ link "plus.google.com/116994733654569657567"; COVID-era masking/vaccine disclosure still on homepage; <title> "Dentist in Fargo, ND | General, Restorative & Cosmetic Dentistry" (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC12/20 BM12/15 WW10/15 Gap11/15 Dep7/10 Tr7/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap7 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — solo owner-dentist 'Lundstrom Family Dentistry'; no group language | Decision-maker: Dr. Jim Lundstrom, DDS (VERIFIED)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — mid — solo practice in a mid-size, growing market; cosmetic/implant scope | Digital spend: ProSites subscription
• Hooks: 1) 33-year Fargo practice with COVID-era text and 'Copyright � 2019 Prosites' still live 2) Dead plus.google.com link in the source
• Pitch/offer: Solo cosmetic/holistic redesign leaving ProSites. $5–8k
• Sources: fargodentist.net raw HTML + render
• Wave-2 re-score: 65 -> 68. Solid Birdeye corpus, est. 1993.
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Midwest (wave 1)

103. Staller Dental & Associates — Delray Beach, FL — https://www.stallerdental.com/ — 68/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: 'has served the Delray Beach area since 1994' (VERIFIED, site); Drs. Staller, Catherine Harb, Jason Sheikh, Lauren Mitchell named in copy; full-mouth reconstruction, veneers, All-on-4, Straumann implants, nitrous (VERIFIED, site) | Reviews: Healthgrades Dr. Nathaniel Staller 4.8 / 50 ratings (Healthgrades directory search); Google count UNKNOWN
• Site (observed): Sesame 24-7 (footer 'Powered by Sesame 24-7™'). Doctor roster inconsistent: body copy names "Dr. Nat Staller, Dr. Catherine Harb, Dr. Jason Sheikh, and Dr. Lauren Mitchell" while nav says "Meet Dr. Staller Meet Dr. Harb Meet Dr. Sheikh Meet Dr. Norkin". jQuery 1.11.3. 27KB page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC14/20 BM12/15 WW10/15 Gap8/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Subs: Gap 6 Dep 8 Tr 8 Tech 8 (/10)
• Independence: INFERRED — 'Staller Dental & Associates', doctors named individually, Sesame footer only; no group markers; not in EXCLUSIONS.md | Decision-maker: Dr. Nat Staller, DDS (founder-owner; INFERRED)
• FinCap: Delray Beach (affluent) 4-doctor practice with full-arch/implant/veneer menu — Mid-High | Digital spend: Sesame 24-7 (observed footer)
• Hooks: 1) Nav lists 'Dr. Norkin' while body copy names Dr. Mitchell — visibly stale team page. 2) 30-year Delray practice on a 27KB Sesame template.
• Pitch/offer: 4-doctor Delray flagship refresh — $8–12k
• Sources: stallerdental.com raw HTML (curl) + pg text; Healthgrades usearch (Staller); EXCLUSIONS.md grep (no match; Signature Dental Group Delray is a different, excluded practice)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: Sesame 24-7 · region: Southeast (wave 2)

104. Lansdale Dental, P.C. (Dr. Gopimanohar N. Varma) — Lansdale, PA — https://www.lansdaledentalpc.com/ — 68/100 — MEDIUM (MEDIUM: est. year UNKNOWN; solo)
• Est/Doctors: Dr. Varma graduated 1998 (UMDNJ); practice founding year UNKNOWN [VERIFIED bio, partial]; 1 principal dentist (attending at Lehigh Valley Hospital GPR) [VERIFIED on site] | Reviews: Birdeye 571 reviews, 4.9 (Lansdale Dental, P.C. listing, crawl 2026-09-30)
• Site (observed): ProSites template. Title verbatim: "Lansdale Dentist | Lansdale Dental P.C. | Dental Practice in Lansdale, PA 19446". Source carries "Copyright � 2019 Prosites, Inc.", 37 legacy <font> tags, a dead plus.google.com/113011177841499412957/about link, retired UA-62628145-1, and a nav item 'COVID'. [VERIFIED raw HTML, 2026-09-30]
• Social gap: Google+ link (dead product) instead of live social [VERIFIED]; other counts UNKNOWN.
• Breakdown: FC11/20 BM8/15 WW12/15 Gap11/15 Dep8/10 Tr9/10 Cv4/5 Sp3/3 DM2/2 | Subs: Gap7 Dep8 Tr9 Tech9 (/10)
• Independence: INFERRED (single owner-dentist P.C.; single office at 1011 N Broad St; no group language) - MEDIUM-HIGH confidence, verify on call | Decision-maker: Dr. Gopimanohar N. Varma, DMD (owner)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — Montgomery County/North Penn; general + cosmetic; solo owner with hospital-affiliated teaching role -> mid tier | Digital spend: ProSites subscription; retired UA tag
• Hooks: 1) Dead plus.google.com link, 37 <font> tags and a COVID nav item still live on the homepage source. 2) 571 Birdeye reviews (4.9) that the template does not showcase.
• Pitch/offer: Modern single-doctor practice site with review wall and cosmetic gallery. $5-8k.
• Sources: lansdaledentalpc.com raw HTML + Dr. Varma page (2026-09-30); reviews.birdeye.com/d/dental/lansdale-pa
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Mid-Atlantic (wave 2)

105. Dental Images, PC (Drs. Brock & Nieri) — Knoxville, TN — https://www.mydentalimage.com/ — 68/100 — MEDIUM (confidence: MEDIUM)
• Est/Doctors: Est. UNKNOWN; 2 doctors; cosmetic dentistry, veneers, implants, TMJ, sleep-apnea appliances (VERIFIED, WebFetch); 1715 Downtown West Blvd (West Knoxville) | Reviews: Healthgrades Dr. Steven Brock 4.8 / 124 ratings and Dr. Chase Nieri 5.0 / 18 ratings (Healthgrades directory search); Google count UNKNOWN
• Site (observed): ProSites (footer 'Site Developed by ProSites.com'; raw HTML 'Copyright � 2019 Prosites, Inc.'). Homepage <title>: "Dr. Steven Brock-Dr. Chase Nieri-Dental Images- Cosmetic Dentist - Knoxville, TN 37919" (doctor names and ZIP code in the title). jQuery 1.9.1; only 2 images on the 107KB home page. Live 200.
• Social gap: Not assessed (Facebook/Instagram counts not retrievable this run) — UNKNOWN
• Breakdown: FC12/20 BM11/15 WW11/15 Gap10/15 Dep8/10 Tr8/10 Cv3/5 Sp3/3 DM2/2 | Subs: Gap 7 Dep 8 Tr 8 Tech 8 (/10)
• Independence: INFERRED — 'Dental Images, PC' professional entity, two named doctors, ProSites footer only; not in EXCLUSIONS.md | Decision-maker: Dr. Steven Brock, DDS (owner; INFERRED) with Dr. Chase Nieri, DDS
• FinCap: West Knoxville cosmetic practice, 142 combined Healthgrades ratings — Mid | Digital spend: ProSites subscription (observed)
• Hooks: 1) ZIP code and two doctor names crammed into the <title> tag of a 'Cosmetic Dentist' site. 2) Brock's 124 Healthgrades ratings at 4.8 vs. a two-image ProSites homepage.
• Pitch/offer: 2-doctor cosmetic practice — $5–8k
• Sources: mydentalimage.com raw HTML (curl); WebFetch homepage; Healthgrades usearch (Brock, Nieri); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Southeast (wave 2)

106. East Avenue Dentistry PLLC - Rochester, NY - https://www.eastavenuedentistry.com/ - 68/100 - MEDIUM (low-medium)
• Est/Doctors: UNKNOWN (founding year not stated); 6 dentists + visiting specialists (periodontics, endodontics, oral surgery); 1641 East Ave Suite A | Reviews: Birdeye 676 reviews / 4.8 (Birdeye Rochester directory JSON-LD, 2026-09-30); Demandforce widget on site
• Site (observed): ProSites (footer "Copyright (mojibake) 2019 Prosites, Inc. All Rights Reserved."); nav 'COVID-19 Information' page still present; image 'Dino_Dental-Cleaning-600x400.jpg' (cartoon dinosaur); 109,813-byte page; title "Welcome | East Avenue Dentistry PLLC | Rochester, NY"; stacked 'More (1)/(2)/(4)' menu items
• Social gap: UNKNOWN (social channels not inspected this wave)
• Breakdown: FC12/20 BM10/15 WW12/15 Gap12/15 Dep8/10 Tr7/10 Cv5/5 Sp2/3 DM0/2 | Subs: Gap8 Dep8 Tr8 Tech8 (/10)
• Independence: MEDIUM confidence - verify on call: PLLC with six dentists, 'Careers' page and 'Great Place to Work' badge (group-scale for one office); no DSO strings in raw HTML | Decision-maker: UNKNOWN - six dentists listed (Aaron Rosen, Jessica Hillman, Daniel Connors, Krystyna Zhezherya, Karen Milla, Dr. Huang); Birdeye listing names Lindsey Keck, DDS
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market - Tier 2-3 (East Ave Rochester/Brighton; family, pediatric, special-needs, sedation; 6 dentists) | Digital spend: ProSites subscription + Demandforce
• Hooks: 1) 676 reviews and six dentists on a 2019 ProSites template with COVID nav still live 2) 'Welcome' title tag on a brand with real search demand
• Pitch/offer: Group-scale redesign: doctor directory, specialist scheduling, review integration - $12-15k group tier (if ownership single)
• Sources: eastavenuedentistry.com (curl raw HTML + WebFetch); Birdeye Rochester NY directory JSON-LD
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: ProSites · region: Northeast (wave 2)

107. Michele Claeys, DMD — Augusta, GA — https://savetheteeth.com/ — 67/100 — MEDIUM-HIGH (confidence: MEDIUM-HIGH) [BELOW 68 CUT LINE — bench only]
• Est/Doctors: Est. UNKNOWN (testimonials cite 20+ year patients); solo | Practice established 1985 (directory snippet); serves Augusta, Evans, Ft. Gordon, Martinez | Reviews: Birdeye 706 reviews / 4.8 (search snippet); Healthgrades 30; Yelp 18; Yahoo 17. Site testimonials page only [WAVE 2]
• Site (observed): generator "WordPress 6.4.12" + "Powered by WPBakery Page Builder", theme dt-the7 (child). Title: "Dentist Dr. Michele Claeys - Cosmetic and Family Dentistry | Augusta, GA". Rendered: duplicated navigation markup, repeated 'Our office pictures' sections; COVID-era 'Electrostatic Spraying System' claim as main tech mention.
• Social gap: Not assessed — UNKNOWN
• Breakdown: FC10/20 BM13/15 WW9/15 Gap12/15 Dep7/10 Tr8/10 Cv4/5 Sp2/3 DM2/2 | Gap 8 Dep 7 Tr 8 Tech 7
• Independence: INFERRED — solo, doctor-named practice, no group language | Decision-maker: Dr. Michele Claeys, DMD (solo owner)
• FinCap: inferred from publicly observable scale/pricing/facilities/positioning/market — Solo cosmetic/family/sedation — Augusta GA — Mid-Low | Digital spend: Unknown
• Hooks: 1) COVID-era electrostatic-spray disinfectant is the headline 'technology'. 2) Unsupported WP 6.4 core.
• Pitch/offer: Solo redesign — $5–8k
• Sources: savetheteeth.com (curl + rendered fetch); EXCLUSIONS.md grep (no match)
• QC: liveness HTTP 200 · social activity NOT YET CHECKED · vendor cluster: WordPress (generic/agency, dated) · region: Southeast (wave 1)

108. Booker Family Dentistry — Trenton, MI — downriversmiles.com — 67/100 — MEDIUM-HIGH (medium)
• Est/Doctors: 'Established in 1976' and 'serving the Downriver community for over 35 years' (VERIFIED, site via web.archive.org capture); solo; implants, Invisalign, Six Month Smiles, sedation, sinus surgery listed | Reviews: 2,247 reviews, 5-star aggregate, 99.7% would refer (Demandforce local.demandforce.com/b/bookerfamilydentistry, VERIFIED via fetch); 'Patient Reviews' page on site shows only a few.
• Site (observed): Officite stock template — footer "Copyright © 2025 MH Sub I, LLC dba Officite. Admin Log In Site Map" (vendor-owned footer, no practice branding); domain downriversmiles.com vs practice name 'Booker Family Dentistry' (Demandforce slug bookerfamilydentistry); generic article copy (nitrous oxide, sedation dentistry, sinus surgery 'Read More' blocks); title "Booker Family Dentistry - Dentist in Trenton, MI". Direct curl bot-walled; verified via web.archive.org capture (VERIFIED)
• Social gap: UNKNOWN (not checked)
• Breakdown: FC10/20 BM12/15 WW9/15 Gap13/15 Dep8/10 Tr7/10 Cv4/5 Sp2/3 DM2/2 | Subs: Gap8 Dep7 Tr7 Tech8 (/10)
• Independence: INFERRED — solo owner-dentist, named practice, single address (2911 West Rd), no DSO strings | Decision-maker: Dr. Nicholas Booker, DDS (VERIFIED; took over the practice from Dr. Brian Hartwell in 2012)
• FinCap: inferred from publicly observable business scale, pricing, facilities, service positioning and market — mid — solo, implant/sedation scope, Downriver Detroit market (middle-income), 50-yr practice | Digital spend: Officite subscription (redirect target); Demandforce
• Hooks: 1) 2,247 Demandforce reviews and a 1976 heritage behind a stock Officite template 2) 2012 ownership handoff from Dr. Hartwell is a natural rebrand moment
• Pitch/offer: Brand-owning relaunch on the practice's own domain, keep Demandforce. $5–8k
• Sources: downriversmiles.com (web.archive.org capture, 2026); local.demandforce.com/b/bookerfamilydentistry
• QC: liveness HTTP 403 Cloudflare bot-wall — content verified via web.archive.org snapshot / rendered fetch by research agent · social activity NOT YET CHECKED · vendor cluster: Officite · region: Midwest (wave 2)

## Extended bench (109–163) — profiled finalists below the cut; full profiles in `output/work/*_top18_v2.json` / `*_wave2.json`

| # | Practice | Location | URL | Score | Likelihood | Region | Vendor |
|---|---|---|---|---|---|---|---|
| 109 | Macon Smiles Laser & Cosmetic Family Dentistry | Macon, GA | https://www.maconsmiles.com/ | 67 | MEDIUM-HIGH | Southeast | TeleVox/Milestone |
| 110 | Virginia Dentistry by Design (Dr. Sonia Dilolli) | Herndon, VA | https://www.virginiadentistrybydesign.com/ | 67 | MEDIUM-HIGH | Mid-Atlantic | TNT Dental |
| 111 | Steven DeCasperis, DMD (Dazzling Smiles) | Lebanon (Clinton area), NJ | https://www.dazzlingsmilesnj.com/ | 67 | MEDIUM | Northeast | Sesame 24-7 |
| 112 | Hawk Dental Artistry (Ronald E. Hawk DDS, PA) | Boca Raton, FL | https://www.hawkdentalartistry.com/ | 67 | MEDIUM | Southeast | Custom-dated / small agency |
| 113 | University General Dentistry | Tuscaloosa, AL | https://tuscaloosauniversitydentistry.com/ | 67 | MEDIUM | Southeast | DentalMarketing.com family (Gilleard) |
| 114 | Coastal Cosmetic Dental Associates (Dr. Patty Van Wie) | Little River (North Myrtle Beach), SC | https://www.coastalcosmeticdental.com/ | 67 | MEDIUM | Southeast | ProSites |
| 115 | Trolley Dental Care (Douglas Trolley, DDS) | Pittsford, NY | https://trolleydental.com/ | 67 | MEDIUM | Northeast | WordPress (generic/agency, dated) |
| 116 | Gooch Family Dental | Birmingham (Highway 280 / Tattersall Way), AL | https://www.goochdental.com/ | 67 | MEDIUM | Southeast | Einstein Dental |
| 117 | Lifetime Cosmetic Dentistry / Lifetime Dentistry (Keller) | Keller (Fort Worth), TX | https://www.lifetimecosmeticdentistry.com/ | 67 | MEDIUM | South-Central | ProSites |
| 118 | Westlake Hills Dental Arts (Dr. Rebecca Long) | West Lake Hills (Austin), TX | https://www.westlakehillsdentalarts.com/ | 67 | MEDIUM | South-Central | TNT Dental |
| 119 | Park Cities Family Dentistry (Drs. Jeffrey Hubbard & Lyle Petrutsas) | Dallas (Park Cities / N Central Expy), TX | https://www.cosmeticdentistindallas.com/ | 67 | MEDIUM | South-Central | Sesame 24-7 |
| 120 | Howard D. Booth Jr., DDS, MAGD | Macon, GA | https://www.drhowardbooth.com/ | 66 | MEDIUM-HIGH | Southeast | Custom-dated / small agency |
| 121 | Friedman Family & Cosmetic Dentistry | Westfield, IN | https://friedmanfamilydentistry.com | 66 | MEDIUM-HIGH | Midwest | Custom-dated / small agency |
| 122 | Alberto J. Lamberti DMD, PA | Boca Raton, FL | https://www.smilespecialist.com/ | 66 | MEDIUM | Southeast | TNT Dental |
| 123 | Esplanade Dental Care | Downers Grove, IL | https://esplanade-dental.com | 66 | MEDIUM | Midwest | TNT Dental |
| 124 | Southern Dental Implant Center (Drs. Collier & Locante) | Cordova (Memphis), TN | https://www.southerndentalimplant.com/ | 66 | MEDIUM | Southeast | Einstein Dental |
| 125 | Aesthetic Dentistry of Scottsdale (Dr. Michael T. Kelly) | Scottsdale, AZ | https://www.aestheticdentistryofscottsdale.com/ | 66 | MEDIUM | West | ProSites |
| 126 | Main Street Family Dentistry (Coakley / Burns) | Montpelier, VT | https://www.mainstreetfamilydentistryvt.com/ | 66 | MEDIUM | Northeast | ProSites |
| 127 | Anna K. Talmood, DDS | Fullerton, CA | https://www.fullertondentistry.com/ | 66 | MEDIUM | West | ProSites |
| 128 | Diablo Valley Prosthodontics (Donna K. Barpal, DDS) | Walnut Creek, CA | https://www.diablovalleyprosthodontics.com/ | 66 | MEDIUM | West | ProSites |
| 129 | Issaquah Valley Dental Care (Drs. Ramanan & Bhan-Kachroo) | Issaquah, WA | https://www.issaquahdental.com/ | 66 | MEDIUM | West | Sesame 24-7 |
| 130 | DiCostanzo Dental (Drs. Gabriel & Megan DiCostanzo) | Coraopolis, PA | https://www.coraopolisdentist.com/ | 66 | MEDIUM | Mid-Atlantic | ProSites |
| 131 | Curtis A. Crandall, DDS | Plano (East Plano), TX | https://www.drcurtiscrandall.com/ | 66 | MEDIUM | South-Central | ProSites |
| 132 | The Art of Dentistry (Dr. Gregory J. Wych) | Irmo (Columbia), SC | https://www.irmocosmeticdentist.com/ | 65 | MEDIUM | Southeast | Wix |
| 133 | Garcia / Mayoral Dentistry | Coral Gables, FL | https://www.garciamayoraldentistry.com/ | 65 | MEDIUM | Southeast | Custom-dated / small agency |
| 134 | Charleston Center for Cosmetic & Restorative Dentistry (Dr. John F. Rink) | Charleston, SC | https://www.cccrdentistry.com/ | 65 | MEDIUM | Southeast | Custom-dated / small agency |
| 135 | Olberding Dental (Louis F. Olberding DDS PC) | Lincoln, NE | https://olberdingdental.com | 65 | MEDIUM | Midwest | TNT Dental |
| 136 | Katkow Dentistry | Columbia, MD | https://www.katkowdentistry.com/ | 65 | MEDIUM | Mid-Atlantic | ProSites |
| 137 | Lakewood Ranch Family & Cosmetic Dentistry (Drs. Scala, Rubinski & Johnson) | Lakewood Ranch (Sarasota), FL | https://www.lakewoodranchsmiles.com/ | 65 | MEDIUM | Southeast | ProSites |
| 138 | David W. Garrett DDS (Garrett Family Dental) | Waco, TX | https://www.garrettfamilydental.com/ | 64 | MEDIUM-HIGH | South-Central | ProSites |
| 139 | White Clay Dental Associates | Newark, DE | https://www.whiteclaydental.com/ | 64 | MEDIUM-HIGH | Mid-Atlantic | TNT Dental |
| 140 | Legacy Family Dental (Todd McConnell DDS PA) | Plano, TX | https://www.legacyfamilydental.com/ | 64 | MEDIUM | South-Central | TNT Dental |
| 141 | Manhattan Beach Family Dentists (Drs. Au & Hsieh) | Manhattan Beach, CA | https://www.manhattanbeachfamilydentists.com/ | 64 | MEDIUM | West | Wix |
| 142 | Campbell Dental (Jarrod Campbell DDS) | Cedar Park, TX | https://www.jarrodcampbelldds.com/ | 64 | MEDIUM | South-Central | ProSites |
| 143 | Michel Dental (Michael E. Michel DDS PA / Dr. Michael Weber) | Topeka & Silver Lake, KS | https://www.micheldental.com/ | 64 | MEDIUM | South-Central | TNT Dental |
| 144 | Tummarello & Pandak Family Dentistry | Fairfax, VA | https://www.dentist-in-fairfax.com/ | 64 | MEDIUM | Mid-Atlantic | Great Dental Websites |
| 145 | Gary N. Pointer DDS PLLC | Fort Worth (Bryant Irvin), TX | https://www.garypointerdds.com/ | 63 | MEDIUM | South-Central | TNT Dental |
| 146 | Wagner Family Dentistry | Green Bay, WI | https://wagnerfamilydds.com | 63 | MEDIUM | Midwest | Sesame 24-7 |
| 147 | Austin Primary Dental | Austin (West Gate Blvd), TX | https://austinprimarydental.com/ | 63 | MEDIUM | South-Central | Doctor Genius |
| 148 | Terri Alani DDS ('Texas Tooth Lady') | Houston (Galleria/Westheimer), TX | https://www.texastoothlady.com/ | 62 | MEDIUM | South-Central | TNT Dental |
| 149 | Upper Valley Esthetic Dental Designs (Roger A. Phillips, DMD, FICOI) | Hanover, NH | https://www.drrogerphillips.com/ | 62 | MEDIUM | Northeast | ProSites |
| 150 | Drs. Zizic & Salata (Cosmetic & Family Dentistry) | Libertyville, IL | https://drzizic.com | 61 | MEDIUM | Midwest | Weebly |
| 151 | Houston Prosthodontic Specialists (Drs. Saab, Gittleman, El-Dahdah, Haber) | Houston (Memorial), TX | https://www.hpsdoctors.com/ | 60 | MEDIUM | South-Central | Unknown / unattributed template |
| 152 | Bull Valley Dentistry | McHenry, IL | https://bullvalleydentistry.com | 60 | MEDIUM | Midwest | ProSites |
| 153 | Marblehead Dental (Fern E. Selesnick, DMD) | Marblehead, MA | https://www.marbleheaddental.com/ | 60 | MEDIUM | Northeast | Weebly |
| 154 | Sacramento Prosthodontics (Jeffrey G. Light, DDS) | Sacramento, CA | https://www.sacprostho.com/ | 60 | LOW | West | ProSites |
| 155 | Madison Family Dental Associates | Madison / DeForest, WI | https://madisonfamilydental.com | 59 | MEDIUM | Midwest | WEO Media |
| 156 | Laura Randolph, DMD | Mahwah, NJ | https://www.drlaurarandolph.com/ | 58 | MEDIUM | Northeast | ProSites |
| 157 | The Castleberry Center (Darrick L. Castleberry DDS) | Houston (Vintage Park/Louetta), TX | https://www.castleberrycenter.com/ | 58 | LOW-MEDIUM | South-Central | TNT Dental |
| 158 | DeLeon Family Dental | Wheaton / Glen Ellyn, IL | https://deleonfamilydental.com | 57 | MEDIUM | Midwest | ProSites |
| 159 | Alexander Dentistry (Kim A. Alexander DDS) | Greenwood, IN | https://alexanderdentistry.net | 56 | MEDIUM | Midwest | ProSites |
| 160 | John Groves DDS (South Tulsa Family Dentistry) | Tulsa (74137), OK | https://www.southtulsafamilydentistry.com/ | 56 | LOW-MEDIUM | South-Central | ProSites |
| 161 | Titensor Dental (Dr. Brett Titensor) | Flower Mound, TX | https://www.titensordental.com/ | 55 | LOW-MEDIUM | South-Central | Custom-dated / small agency |
| 162 | Gary L. White DDS | Fort Worth (Hulen St), TX | https://www.garywhitedds.com/ | 53 | LOW-MEDIUM | South-Central | TNT Dental |
| 163 | Family Dental Center (Drs. Harris, Johnson, Silvestri, Inboden) | Fayetteville, AR | https://www.fayfdc.com/ | 52 | LOW-MEDIUM | South-Central | Sesame 24-7 |

## Notable DSO / corporate catches (this round)

- Green & Glasser Dental Associates, Commack NY — The Smilist (Northeast)
- New Haven Dental Group (CT), Taylor Street Dental (Springfield MA), EMA Dental (Northampton MA) — 42 North Dental (Northeast)
- Dentists Office of the Hudson Valley, Lake Katrine NY — Dental Care Alliance (Northeast)
- Fairfield County Implants & Periodontics (Sonick) — Specialty1 Partners; also perio referral (Northeast)
- Hodosh Cosmetic & Implant Dentistry, Providence RI — suspected Dental Care Alliance string (Northeast)
- Signature Smiles, Chesapeake VA — Atlantic Dental Care division (Mid-Atlantic)
- Dental Care Burke, VA — MB2 string in HTML (Mid-Atlantic)
- Midlothian Dental Center, VA — 'a division of' language (Mid-Atlantic)
- Cox Family Dentistry — Smile Brands theme (Mid-Atlantic)
- 'Dentists of Bristow', 'Dentists of Centreville', 'Modern Dentistry Richmond' — Pacific Dental Services naming pattern (Mid-Atlantic)
- Saint Petersburg Dental (Clearwater FL) — nadentalgroup.com email (Southeast)
- Exceptional Dental of St. Pete, FIT Dental Center (Chattanooga), The Collierville Dentist, Dentistry Today — MB2 markers (Southeast)
- Biltmore Dental Group, Asheville NC — Heartland strings (Southeast)
- Miami Center for Cosmetic & Implant Dentistry — Dental Care Alliance markers (Southeast)
- DentFirst Smyrna GA — DentFirst (Southeast)
- Fox Dental, Asheville NC — careers page links dag.dental (Southeast)
- Lovett Dental West U, Houston TX — Lovett (South-Central)
- Aspen Dental / Affordable Dentures, Olive Branch MS & Bowling Green KY (South-Central)
- Midwest Dental, Wichita KS — Smile Brands (South-Central)
- Noblesville Family Dentistry, IN — Grin Dentistry group (Midwest)
- Aesthetic Dentistry of Frankfort, IL — smilesbyad multi-office group (Midwest)
- Lincoln Dental Group, NE — suspected Marquee/MB2 strings (Midwest)
- Station Dental — Smile Partners USA (West)
- Fuller Smiles (11 locations), Espire, Hawaii Family Dental, Alcan/Anchorage Dental Group (White Mountain Holdings) (West)
- Visalia Modern Dentistry, Marin Modern Dentistry — Pacific Dental Services 'Modern Dentistry' pattern (West)

## Vendor-cluster summary (demo workflow)

Group the 100 by template vendor: one demo build per cluster can be re-skinned across its members.

| Vendor / platform | Count | Ranks |
|---|---|---|
| ProSites | 32 | #9, #11, #12, #19, #21, #22, #25, #29, #31, #32, #36, #39, #41, #42, #44, #46, #54, #57, #58, #62, #65, #67, #75, #76, #80, #82, #84, #86, #90, #92, #96, #100 |
| TNT Dental | 24 | #5, #8, #13, #14, #15, #20, #24, #30, #33, #34, #45, #47, #48, #53, #55, #60, #63, #70, #72, #74, #81, #87, #91, #94 |
| Custom-dated / small agency | 10 | #2, #6, #7, #28, #40, #49, #51, #69, #83, #98 |
| Sesame 24-7 | 7 | #17, #26, #37, #38, #88, #89, #97 |
| WordPress (generic/agency, dated) | 5 | #18, #56, #64, #66, #78 |
| Wix | 3 | #10, #71, #93 |
| PBHS | 3 | #16, #61, #73 |
| Progressive Dental Marketing | 2 | #3, #85 |
| GoDaddy | 2 | #23, #59 |
| Dental Revenue | 2 | #27, #43 |
| Dentalfone | 2 | #35, #52 |
| Hibu | 1 | #1 |
| Officite | 1 | #4 |
| Practice Cafe | 1 | #50 |
| WEO Media | 1 | #68 |
| DentalWebsites.com | 1 | #77 |
| TeleVox/Milestone | 1 | #79 |
| Weebly | 1 | #95 |
| Unknown / unattributed template | 1 | #99 |

**ProSites** (32): #9 Christensen Dental Associates (Waldwick, NJ); #11 Meetinghouse Dental Care (Hatboro Integrative Dentistry) (Hatboro, PA); #12 Cosmetic & Implant Dentistry of Maryland (Dr. Jennifer Ouazana) (Pikesville, MD); #19 Harbor Dental (Plymouth, MN); #21 Devine Dental LLC (Devine & DeFina) (Greenwich, CT); #22 Pacific Dental Associates (Duhn family; NOT Pacific Dental Services) (San Francisco (Pacific Heights), CA); #25 Robert I. Halle, DMD, PC (Commack, NY); #29 Hagerstown Smiles Dental Care (Hagerstown, MD); #31 Main Line Dental Aesthetics (James A. Godorecci Jr., DMD) (Paoli, PA); #32 Locust Valley Dentistry (Locust Valley, NY); #36 Gates Family Dentistry (Loveland, OH); #39 New Canaan Dental Care (Anthony T. Festa, DDS) (New Canaan, CT); #41 Progressive Dental Studio & Implant Center (Drs. Kevin Metsger & Maropis) (Greensburg, PA); #42 West University Dentistry (Drs. Ross Pickei & James M. Seale) (Houston (West U/Bellaire Blvd), TX); #44 Aesthetic Image Dentistry (Debra Duryea, DMD) (Mendham, NJ); #46 Fox Chapel Advanced Dental Care (Dr. J. Kevin Pawlowicz) (Pittsburgh (Fox Chapel), PA); #54 Fox Valley Dental Associates (Tami Zuck DDS) (Crystal Lake, IL); #57 Fishers Family Dentistry (Fishers, IN); #58 Oak Canyon Dentistry (Dr. Steven Haase) (Bee Cave (Austin), TX); #62 Thomsen Dental Group (West Omaha, NE); #65 Wallingford Station Family Dental (Wallingford (Media), PA); #67 Johann Prosthetics of Boulder (Andrew R. Johann DDS MS PC) (Boulder, CO); #75 Perry Hall Smiles (Caroline F. Owens, DDS, PA) (Perry Hall (Baltimore), MD); #76 Always Great Smiles (Drs. Pecora & Langner) (Glen Ellyn, IL); #80 Cinco Meadows Dental (Dr. Brian Williams) (Katy (Cinco Ranch), TX); #82 Pelandale Dental Care (Dr. Param Gill) (Modesto, CA); #84 James A. Vito, DMD (Prosthodontics & Periodontics) (Wayne, PA); #86 Allison Family & Cosmetic Dentistry (F. Vincent Allison III, DDS, PA) (Durham, NC); #90 Blossfeld Family Dentistry (Dr. Carol M. Blossfeld) (Edmond / Oklahoma City, OK); #92 Somerset Hills Family Dentist (Joseph M. Micale, DMD, PA) (Basking Ridge, NJ); #96 Kahala Smile Professionals, LLC (Drs. Candace & Robert Wada) (Honolulu (Kahala), HI); #100 Jonson Dental Care (George P. Jonson DDS) (Kettering (Dayton), OH)

**TNT Dental** (24): #5 Goodman Dental Care (Annapolis, MD); #8 Klein Family Dentistry (Harrisburg, PA); #13 Wahl Family Dentistry (Wilmington, DE); #14 Bedford Cosmetic & Restorative Dentistry (Hedstrom / Persha) (Bedford, NH); #15 Advanced Dental Solutions of Pittsburgh (Pittsburgh (Upper St. Clair/Bethel Park), PA); #20 Highland Smiles Dental (Dr. Girish Sandadi / Dr. Rachna Patel) (Dallas (Highland Park / McKinney Ave), TX); #24 Total Dental Solutions for Adults (Dr. George A. Hoop) (Fort Myers, FL); #30 Ridgepointe Dental (Austin Amos DDS, JD) (The Colony, TX); #33 Dental Group West (Toledo, OH); #34 Transforming Smiles (Bruce E. Carter, DMD PC) (Lawrenceville, GA); #45 Vason Family Dentistry of Buckhead (Atlanta (Buckhead), GA); #47 Heck Family Dentistry of Lawrence (Dr. Brian Heck + 3 dentists) (Lawrence, KS); #48 Garden Oaks Family & Cosmetic Dentistry (Drs. Patrick Ruehle & Erika Eide) (Denton, TX); #53 Beliveau Dental (E. Charles Beliveau, DDS, PLLC) (North Andover, MA); #55 Baltimore Dental Arts (Drs. Kevin Murphy, Devon Conklin, Charles & Melody Ward) (Baltimore, MD); #60 Smiles by Martin (Dr. Greg Martin - third generation) (Grapevine, TX); #63 Donna L. Kiesel DDS PA (Coppell, TX); #70 Todd Phelan DDS (Drs. S. Todd Phelan & Tyler Gossett) (Rogers, AR); #72 Moulton Dentistry of Hoover (Hoover (Birmingham), AL); #74 Ross & Sourlis Family Dentistry of Rock Hill (domain: Coombs and Ross legacy) (Rock Hill, SC); #81 Dr. Rosenbaum & Associates (Modesto, CA); #87 Iglesias Dental Group (formerly Walter K. Kulick, DMD, PA) (Coral Springs, FL); #91 Perfect Smiles Dental Care (Lenexa, KS); #94 Passidomo Cosmetic & Family Dentistry (Dr. Passidomo & Dr. Brij Patel) (Centerville (Dayton), OH)

**Custom-dated / small agency** (10): #2 Luis E. Martinez DMD, PA (St. Pete Cosmetic Dentistry) (St. Petersburg, FL); #6 Cosmetic & Implant Dentistry of Naples (Naples, FL); #7 Coral Gables Dentistry & Prosthodontics (Coral Gables, FL); #28 OKC Dental Arts (Drs. Michael Fling & Cama Cord) (Oklahoma City (NW 63rd St), OK); #40 Heights Family Dentistry (Carol L. Price DDS PC) (Houston (Heights), TX); #49 Stephen J. Rothman, DMD & Cammarano, DMD (Woodbridge, CT); #51 Oak Brook Dental Center (Elmhurst, IL); #69 March Dentistry (Upper Arlington (Columbus), OH); #83 Annapolis Dental Associates (Annapolis, MD); #98 Delmar Dental Medicine (Thomas H. Abele, DMD, FAGD) (Delmar, NY)

**Sesame 24-7** (7): #17 Kalil & Kress Family & Cosmetic Dentistry (Nashua, NH); #26 Paolucci Family Dentists (with Paolucci Lincoln Dental Associates) (Providence / Lincoln, RI); #37 Devon Dental Associates (Drs. Steven Hart & Robert Rose) (Wayne (Devon/Berwyn), PA); #38 Comprehensive Esthetic Restorative & Implant Dentistry (Murali R. Ravel, DMD) (Bedford, NH); #88 DeMartin Dental Associates (Fairfield, CT); #89 Egidio Dental Care (Aaron J. Egidio, DDS) (Madison, CT); #97 Lee Dental Care (Fort Myers, FL)

**WordPress (generic/agency, dated)** (5): #18 Park Cities Dental Group (Dr. Phillip Allison / Dr. Ted Smith) (Dallas (Highland Park), TX); #56 Maras Dentistry (William H. Maras, DDS, PA) (Palm Beach Gardens, FL); #64 Byerly Family Dentistry (Montgomery (Cincinnati), OH); #66 Midtown Dental Sacramento (Sacramento, CA); #78 Dental Arts of Delaware (Drs. Gregg Fink & Christopher Appleman) (Newark, DE)

**Wix** (3): #10 Southdale Dental Associates (Edina, MN); #71 Thomas J. Emmer, DDS, PA (Prosthodontist) (Morristown, NJ); #93 North Macon Dental Associates (Macon, GA)

**PBHS** (3): #16 Center for Dental Excellence, LLC (Christian) (Simsbury / West Hartford / Litchfield, CT); #61 Progressive Dentistry (Steven M. Levy, DMD) (Merrick, NY); #73 Portland Dental Health Care & Implant Center (Portland, ME)

**Progressive Dental Marketing** (2): #3 Brewer Family Dentistry (Modesto, CA); #85 Serafin Family Dentistry (Carlisle, PA)

**GoDaddy** (2): #23 Marin Dental Implant Center / David W. Epstein, DDS, Inc. (Novato, CA); #59 Montrose DDS (Drs. Samuel Carrell & Austin Faulk) (Houston (Montrose), TX)

**Dental Revenue** (2): #27 Pioneer Valley Dental Arts (Evans / Ziemba / Reilly / Lucido) (Longmeadow, MA); #43 Gotwalt Dentistry (Lititz/Akron, PA)

**Dentalfone** (2): #35 Greater Baltimore Prosthodontics, PA (Towson, MD); #52 North Shore Prosthodontic Associates (Manhasset / Woodbury, NY)

**Hibu** (1): #1 D'Angelo/Olson La Jolla Dentistry (La Jolla, CA)

**Officite** (1): #4 Mt. Lookout Dentistry (Cincinnati, OH)

**Practice Cafe** (1): #50 Canyon Golf Family Dentistry (Dr. Bryan E. Soto) (San Antonio (Stone Oak), TX)

**WEO Media** (1): #68 Baccellieri Family Dentistry (Dr. Carl Baccellieri Jr.) (Kennett Square, PA)

**DentalWebsites.com** (1): #77 Schilling Farms Dental (Drs. Midyett & Prine) (Collierville (Memphis), TN)

**TeleVox/Milestone** (1): #79 CMB Family Dentistry (Drs. David Brown & Josh Alter) (Broomall, PA)

**Weebly** (1): #95 Michael A. MacInnes, DDS, PLLC (Sammamish, WA)

**Unknown / unattributed template** (1): #99 Family Smile Dentistry (Drs. Foroughi & Jarquin) (Lakewood Ranch (Bradenton), FL)


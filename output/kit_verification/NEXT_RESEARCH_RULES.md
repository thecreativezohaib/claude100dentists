# Next research round: rules and mistakes to avoid

Paste this whole file into the research session before it starts the next batch (#201 onward).

## Goal

Find US independent dental practices that are good redesign prospects. A practice qualifies only if it passes **all six** gates below, checked against live data. Build a homepage kit only for practices that pass. Do not build kits first and filter later.

## The six gates (all must pass)

1. **No website of its own.** Facebook, Instagram, Linktree, Google business.site and directory pages (Yelp, Healthgrades, Zocdoc, Delta Dental, Vitals, WebMD, dr-leonardo, PatientConnect365, weence, rymap/rymaps) do not count as a website. A dead domain also counts as no website: one that fails DNS, is parked or for sale, shows "site not published", or returns 4xx/5xx.
   Before marking a practice "no website", you must check all of these:
   - the email's domain, if it isn't a free provider;
   - every URL on the Google listing;
   - at least two web searches (practice name + town, and dentist name + town);
   - 3–5 guessed domains (practicename.com, drlastname.com, lastnamedental.com);
   - free site builders: wixsite.com, square.site, GoDaddy, Weebly, Squarespace, WordPress.com, Google Sites.
   If any live site exists for the practice, it fails.
2. **Open.** Not marked temporarily or permanently closed on Google.
3. **Rating 4.5 or higher** on the practice's own Google listing.
4. **At least 15 Google reviews.**
5. **At least one review in the last 6 months.** Sort reviews by Newest and record the date. "6 months ago" or older fails.
6. **No red flags.** All of these fail the gate:
   - a review alleging a scam, fraud, overbilling, injury or damage;
   - license discipline (search the state dental board and the news);
   - a malpractice suit;
   - a practice that has closed, retired or been sold;
   - any doubt that the name, address, phone and email belong to the same business.

## Mistakes the previous research made. Do not repeat them

Gemini built kits #001–#075. Verification found these errors.

| Mistake | Examples | Rule |
|---|---|---|
| **Made-up Google place IDs.** IDs that follow a pattern rather than coming from a real listing. | 16 kits: #016, 018, 021–025, 036, 038–045 | Copy the place ID or Maps URL from the actual listing you opened. Never construct one. If you can't open the listing, write "NOT VERIFIED". |
| **Wrong phone numbers** | #043 was a used-car dealer, #044 a towing company, #038 and #045 were personal phones, #036 another business. #018 and #019 didn't match the listings. | Take the phone number from the Google listing, then confirm it on at least one other source. Record both sources. |
| **Wrong or dead emails** | #036 belonged to another practice. #037 was on Delta Dental's domain. #011's domain has no mail records (MX). #052's domain expires in October 2026. | Check MX records for every email domain. Make sure the email belongs to this practice, not a vendor, insurer or other dentist. Record where you found it. |
| **"No website" claims that were wrong** | #031 (live Hibu site), #035 (live Wix site), #054 (live site), #073 (live site; only the Google link was broken) | Run every check in gate 1. A broken link on Google doesn't mean there's no site. |
| **Kits built for practices that had already failed** | 8 kits the tracker itself marked "HAS WEBSITE" | Never build a kit for a practice that fails any gate. |
| **Practices below the bar** | 26 rated below 4.5. 9 had no review in 6 months. 1 was temporarily closed (#062). 1 had no reviews (#028). | Apply gates 2–5 before writing anything. |
| **Inflated numbers** | #070 claimed 36 reviews; Google shows 13 | Copy rating and review count exactly from the live listing, with the date checked. |
| **Missed red flags** | License suspensions (#035 in 2020, #045 in 2024). A Department of Health case over prescriptions (#002). A malpractice suit (#035). Scam and damage reviews (#054, #055). | Search "[dentist name] dental board" and "[dentist name] lawsuit", and read the lowest-rated reviews. |
| **Wrong business or moved practice** | Address or phone belonging to someone else (#020, #026, #053, #055). A previous owner's listing (#004, #007, #033). Dentists who had moved states (#052). | Make sure the Google listing name and address match the kit. Note any predecessor or new owner. |
| **Unverified claims presented as facts** | "Castle Connolly Top Dentist since 2012" (#014). That list didn't exist then. | Only state awards, years and credentials you've seen on a source page. Otherwise label them UNVERIFIED. |
| **Specialists and groups not flagged** | Oral surgeon (#038). Possible DSO (corporate group) contact (#074). Former multi-office group (#023). Pediatric practices. | Flag specialists and group or DSO ownership clearly. |

## Problems in the Claude batch (#076–#200)

That batch didn't apply the gates before building kits:
- **55 of 125** list a rating below 4.5.
- **48** list fewer than 15 reviews.
- **8** have place IDs with a suspicious repeated pattern: #091, 110, 114, 116, 150, 155, 187, 195.
- **#081** is an oral surgery practice.

Apply the gates first next time.

## Don't repeat practices

Skip every practice in `already_researched_001_200.csv` (by name, address, phone or email). Also skip everything in `EXCLUSIONS.md`.

## Each record must include (with sources)

- **Google listing:** the Maps URL you opened, the listing name, address, phone, status, rating, review count, and the date of the newest review.
- **Website check log:** each URL or domain checked, with its HTTP or DNS result, and the searches you ran.
- **Email:** the address, the page where you found it, and the result of the MX check.
- **Red-flag check:** the board/news searches you ran and what you found, plus a quote from any serious complaint.
- **Evidence label on every claim:** VERIFIED (with source), INFERRED, or UNVERIFIED.

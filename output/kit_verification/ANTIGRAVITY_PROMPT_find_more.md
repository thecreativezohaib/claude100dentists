# Prompt for Antigravity: find 120 more dental practices

Copy everything below the line into Antigravity. Attach `already_researched_001_200.csv` with it.

---

## Task

Find **120 new US dental practices** that pass **all six rules** below. The six rules are hard requirements, so check every rule live before you add a row. A practice that fails any rule must not appear in the file. The practices will be verified again independently afterwards, so accuracy matters more than speed. One wrong row is worse than one missing row.

## The six rules (all must pass)

1. **No website of its own.**
   - **Doesn't count as a website:** Facebook, Instagram, Linktree, a Google "business.site" page, or a directory or listing page. That includes Yelp, Healthgrades, Zocdoc, WebMD, Vitals, Delta Dental, Sharecare, Opencare, PatientConnect365, dr-leonardo, weence, rymap/rymaps and newpatientsinc.
   - **Also doesn't count:** a dead domain, meaning one that doesn't load, is parked or for sale, says "site not published", or shows an error page.
   - **Does count, and fails the rule:** any live site for the practice, including free ones like Wix (wixsite.com), Square, GoDaddy, Weebly, Squarespace, WordPress.com and Google Sites.
   - **Before saying "no website", you must:**
     - open the website link on the Google listing, if there is one;
     - visit the email's domain, if the email isn't a free provider (gmail, yahoo, aol, outlook, hotmail, comcast, att, verizon and similar);
     - search "[practice name] [town] [state]" and "Dr. [last name] dentist [town]";
     - try likely domains such as [practicename].com, dr[lastname].com and [lastname]dental.com.
2. **Open.** Google doesn't show "Temporarily closed" or "Permanently closed".
3. **Google rating 4.5 or higher.**
4. **At least 15 Google reviews.** Aim for 25 or more, because the count is re-checked.
5. **At least one Google review in the last 5 months.** Sort reviews by **Newest**. Reject anything that shows "6 months ago" or older.
6. **No red flags.**
   - Sort reviews by **Lowest** and read the 1–2 star ones. Reject the practice if any mention a scam, fraud, overbilling, unnecessary treatment, injury, nerve damage, botched work or a lawsuit.
   - Search "[dentist full name] dental board" and "[dentist full name] lawsuit". Reject any license discipline or suspension, or malpractice news.
   - Reject practices that are closed, retired, sold or moving.
   - Reject anything owned by a DSO or chain (Aspen, Heartland, Pacific Dental, Smile Brands, Western Dental, MB2, etc.) or with 3 or more locations.
   - Reject it if the name, address and phone don't clearly belong to the same business.

## What kind of practice to look for

- US, independent, owner-run **general or family dentistry**. Avoid specialists (oral surgeons, periodontists, endodontists, orthodontists, prosthodontists). If you do include one, mark it.
- Small and mid-size towns work best. Search Google Maps for "dentist" in towns across states such as KY, TN, OH, PA, WV, AL, MS, AR, MO, IN, MI, VA, NC, SC, GA, TX, OK, KS, IA, NE, WI, MN, IL, NY and NJ. Open each listing that has **no website button**.
- The practice must have an **email address you can find publicly**: on its Facebook page, the Delta Dental directory, a state filing, or a directory. Record the page you found it on. Skip practices with no findable email.

## Don't repeat these

- Skip every practice in the attached `already_researched_001_200.csv`. Match by practice name, dentist name, address, phone and email.
- Skip duplicates within your own list.

## Mistakes from the last rounds. Do not repeat them

1. **Never make up or construct a Google Maps link or place ID.** Copy the real URL from the browser after you open the listing. Earlier rounds produced fake place IDs that followed a pattern.
2. **Phone:** copy it exactly from the Google listing. Earlier rounds gave numbers that belonged to a car dealer, a towing company and personal cells. If the listing shows a toll-free call-routing number (833, 844, 855, 866, 877 or 888), write it, but also find the practice's local number on another source and give both.
3. **Email:** it must belong to this practice. Earlier rounds gave emails belonging to other practices and to an insurance company, plus domains that can't receive mail.
4. **Rating and review count:** copy them exactly from the listing; don't estimate. Earlier rounds overstated review counts (36 claimed versus 13 real).
5. **Website field:** only put a real website URL. Never put a Google search link, a directory or scraper link (rymap, weence, etc.) or a Facebook link there. Those go in their own columns.
6. **Newest review date:** copy Google's text exactly, e.g. "3 weeks ago". Don't guess.
7. **Two Google listings for one practice:** use the one whose name, address and phone match best, and mention the other in notes.
8. **Wrong dentist:** confirm who the dentist is from the listing or a directory. Earlier rounds named the wrong dentist and wrong owners.
9. **Claims:** don't add awards, years in business or credentials unless you saw them on a page, and give the URL.
10. **No silent gaps:** if you couldn't check something, write "NOT CHECKED" in that cell. Never leave it blank or guess.

## Output

One CSV file named `new_candidates_201_320.csv`, numbered 201–320, with exactly these columns:

```
num,practice_name,dentist_name,specialty (general/family or name the specialty),address,town,state,google_maps_url (copied from browser),google_listing_name,phone_on_listing,local_phone_if_different,status,rating,review_count,newest_review_date,website_on_listing (real site or none),website_search_done (what you searched and checked),email,email_source_url,facebook_url,instagram_url,lowest_reviews_checked (none or quote),board_and_lawsuit_search (none or what you found),notes
```

Before finishing, re-read every row and delete any that fails a rule. Then report how many rows you kept and how many practices you rejected for each rule.

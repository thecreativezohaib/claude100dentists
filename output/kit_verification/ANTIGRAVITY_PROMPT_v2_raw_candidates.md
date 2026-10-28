# Prompt for Antigravity (v2): collect raw Google Maps candidates only

Copy everything below the line into Antigravity. Attach `already_researched_001_320.csv`.

---

## Your job this time: collect, don't verify

Last round you reported 120 practices as "verified". Independent checking showed:
- **79** had a live website. You marked several of those "dead".
- **25** broke the recent-review rule according to your own data.
- **About 20** specialists were labelled "General Dentistry".
- **110** Google Maps links were built rather than copied.
- The emails could not be traced to any page.

So this time, **do not verify anything and do not write any summary statistics**. Copy exactly what Google Maps shows. The website checks, email checks and red-flag checks will be done separately.

## What to collect

**250 Google Maps listings** of US dental practices, numbered 321–570, that meet all of these on the listing itself:

1. **No website button** on the Google listing. If it has a website link, skip it.
2. **Open:** no "Temporarily closed" or "Permanently closed" label.
3. **Rating 4.5 or higher.**
4. **Between 15 and 250 Google reviews.** Practices with more than 250 reviews nearly always have websites.
5. **Newest review is 5 months old or less.** Click Reviews, then sort by Newest. Skip the listing if it shows "6 months ago" or older.
6. **General or family dentist only.** Skip any name containing: pediatric, kids, children, orthodontic(s), braces, endodontic(s), root canal, periodontic(s), perio, oral surgery, maxillofacial, implant center, denture center, sleep, or "Group" with several locations.
7. **Not a chain or corporate group.** Skip Aspen, Heartland, Pacific Dental, Smile Brands, Western Dental, MB2, Dental365, Marquee, Specialty1, Bright Now, Coast Dental, Affordable Dentures, Family Dental Health, Mint Dental, Celebrate Dental, and any listing with "Location", "Locations" or a city suffix like "- Omaha".
8. **Not already researched.** Check the attached file by practice name, dentist name, address and phone.

Search Google Maps for "dentist" in small and mid-size towns, about 15–20 per state, across KY, TN, OH, PA, WV, AL, MS, AR, MO, IN, MI, VA, NC, SC, GA, TX, OK, KS, IA, NE, WI, MN, IL, NY, NJ, LA, FL and ID.

## Strict copying rules

- **google_maps_url:** copy it from the browser address bar after clicking the listing. It must contain `/maps/place/`. Never build a `/maps/search/` link.
- **Phone:** copy exactly. If it starts with 800/833/844/855/866/877/888, still copy it.
- **Rating, review count and newest review text:** copy exactly ("3 weeks ago", "a month ago").
- **Lowest reviews:** sort by Lowest and copy the first 1–2 star review word for word, up to 300 characters. Write "none" only if there are no 1–2 star reviews.
- **Email:** only if you can see it on a page, with that page's exact URL. A homepage like deltadental.com doesn't count. If you can't see one, leave it blank. **Never guess or construct an email.**
- **Facebook:** if a Facebook page link is shown on the listing or found for the practice, copy it.
- **Unknown values:** if you can't see a value, write NOT SEEN. Never fill a cell with a guess.

## Output

One CSV, `raw_candidates_321_570.csv`, with these columns:

```
num,google_listing_name,dentist_name_if_shown,address,town,state,google_maps_url,phone_on_listing,status,rating,review_count,newest_review_text,lowest_review_quote,email,email_page_url,facebook_url,category_shown_on_listing
```

At the end, reply with only the file path and the row count. No other claims.

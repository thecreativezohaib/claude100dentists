# Prompt for Antigravity (v3): find real emails and social links

Copy everything below the line into Antigravity. Attach `email_search_needed.csv`.

---

## Task

The attached sheet lists 53 US dental practices.
- **40 have no email yet.**
- **13 have an email that can't be found anywhere online.** Confirm it or replace it.

For each practice, find an email address that you can **actually see on a page**, plus the practice's Facebook and Instagram pages. Fill the FILL_ columns.

## Where to look, in this order

1. **The Google Maps listing:** check "From the business", the Updates/posts section and Q&A for an email.
2. **The practice's Facebook page:** About section, then Contact info, then Intro. Also check the page's recent posts.
3. **Instagram bio.**
4. **Yelp, BBB (bbb.org), Yellow Pages / Superpages, MapQuest and Chamber of Commerce member directories:** look for a business profile with an email or "Email business" address shown.
5. **The state business registry filing**, where it shows a contact email.
6. **Job posts by the practice** on Indeed, ZipRecruiter or dental school job boards. These often show an office email.
7. **Old website domains.** These practices still receive email at their old domains, but the exact address isn't known:
   - #475 floresdentalcare.com
   - #382 drblaineleeds.com
   - #477 markaddingtondds.com
   - #359 hondodowntowndental.com

   Look for an address at that domain on any page above.

## Strict rules

- **Only record an email you can see on a page.** Put that page's exact URL in FILL_email_page_url. A homepage like deltadental.com is not a source.
- **Never build or guess an address,** such as info@ or office@ on a domain, or practicename@gmail.com. If you can't see one, leave FILL_email blank.
- **Check the email belongs to this practice.** Same practice name, dentist or address on the page. If it belongs to a different practice, don't use it.
- **Facebook and Instagram:** only copy a page that clearly belongs to this practice (same name and town). Copy the URL from the browser.
- **FILL_owner_dentist_name:** fill it only if a page shows it.
- **No claims or statistics in your reply.** Just give the file path and how many rows got an email.

## Output

Save the same sheet as `email_search_filled.csv` with the FILL_ columns completed.

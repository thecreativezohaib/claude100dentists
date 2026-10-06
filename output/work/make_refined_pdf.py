#!/usr/bin/env python3
"""Refined High-Conversion 100: contact table + pitch angle per practice, in conversion-score order."""
import csv, os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from make_contact_pdf import OUT, ST, ACCENT, BAND, RULE, MUTED, esc, link



def build(rows, title, pdf_name, csv_name):
    with open(os.path.join(OUT, csv_name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["#", "business", "city", "state", "website", "email", "facebook", "instagram",
                    "latest_social_post", "google_rating", "google_reviews", "pitch_angle"])
        for i, r in enumerate(rows, 1):
            c = r["conv"]
            w.writerow([i, r["name"], r.get("city"), r.get("state"), r["url"], r["emails"][0],
                        r["fb"][0] if r["fb"] else "", r["ig"][0] if r["ig"] else "", r.get("latest_post") or "",
                        c["rating"] or "", c["reviews"] or "", r["pitch"]])
    doc = SimpleDocTemplate(os.path.join(OUT, pdf_name), pagesize=landscape(letter), leftMargin=0.45 * inch,
                            rightMargin=0.45 * inch, topMargin=0.45 * inch, bottomMargin=0.5 * inch,
                            title=title, author="Dental prospect research", subject="High-conversion redesign outreach list")
    story = []
    head = ["#", "Business", "Website", "Email", "Facebook", "Instagram", "Why they should buy"]
    data = [[Paragraph(h, ST["h"]) for h in head]]
    for i, r in enumerate(rows, 1):
        c = r["conv"]
        loc = ", ".join(x for x in [r.get("city"), r.get("state")] if x)
        g = f"{c['rating']}★ · {c['reviews']} reviews" if c["rating"] else ""
        data.append([
            Paragraph(str(i), ST["c"]),
            Paragraph(f"<b>{esc(r['name'])}</b><br/><font color='#5f6b7a'>{esc(loc)}{(' · ' + g) if g else ''}</font>", ST["c"]),
            Paragraph(link(r["url"]), ST["c"]),
            Paragraph("<br/>".join(f"<link href='mailto:{esc(e)}' color='#0f5e7a'>{esc(e)}</link>" for e in r["emails"][:2]), ST["c"]),
            Paragraph(link(r["fb"][0]) if r["fb"] else "-", ST["c"]),
            Paragraph(link(r["ig"][0]) if r["ig"] else "-", ST["c"]),
            Paragraph(esc(r["pitch"]) + f"<br/><font color='#5f6b7a'>last post {esc(r.get('latest_post'))}</font>", ST["c"]),
        ])
    t = Table(data, colWidths=[0.34, 1.95, 1.4, 1.6, 1.4, 1.1, 2.31], repeatRows=1)
    t._argW = [w * inch for w in t._argW]
    style = [("BACKGROUND", (0, 0), (-1, 0), ACCENT), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 0), (-1, -1), 0.25, RULE), ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    for i in range(2, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), BAND))
    t.setStyle(TableStyle(style))
    story.append(t)

    def foot(cv, d):
        cv.saveState(); cv.setFont("DV", 7); cv.setFillColor(MUTED)
        cv.drawString(0.45 * inch, 0.3 * inch, title)
        cv.drawRightString(landscape(letter)[0] - 0.45 * inch, 0.3 * inch, f"Page {d.page}")
        cv.restoreState()
    doc.build(story, onFirstPage=foot, onLaterPages=foot)
    print("wrote", pdf_name, "and", csv_name)

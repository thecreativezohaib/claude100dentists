#!/usr/bin/env python3
"""Refined High-Conversion 100: contact table + conversion score, tier and pitch angle per practice."""
import csv, os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from make_contact_pdf import OUT, ST, ACCENT, BAND, RULE, MUTED, esc, link

TIER_COL = {"A": "#1b7f3b", "B": "#0f5e7a", "C": "#8a6d1d"}


def build(rows, method, title, sub, pdf_name, csv_name):
    with open(os.path.join(OUT, csv_name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["#", "tier", "conversion_score", "business", "city", "state", "website", "email", "facebook", "instagram",
                    "latest_social_post", "google_rating", "google_reviews", "design_grade_1to5", "pitch_angle"])
        for i, r in enumerate(rows, 1):
            c = r["conv"]
            w.writerow([i, r["tier"], c["total"], r["name"], r.get("city"), r.get("state"), r["url"], r["emails"][0],
                        r["fb"][0] if r["fb"] else "", r["ig"][0] if r["ig"] else "", r.get("latest_post") or "",
                        c["rating"] or "", c["reviews"] or "", c["visual"] or "", r["pitch"]])
    doc = SimpleDocTemplate(os.path.join(OUT, pdf_name), pagesize=landscape(letter), leftMargin=0.45 * inch,
                            rightMargin=0.45 * inch, topMargin=0.45 * inch, bottomMargin=0.5 * inch,
                            title=title, author="Dental prospect research", subject="High-conversion redesign outreach list")
    story = [Paragraph(esc(title), ST["t"]), Spacer(1, 3), Paragraph(esc(sub), ST["s"]), Spacer(1, 8)]
    for para in method:
        story += [Paragraph(para, ST["s"]), Spacer(1, 4)]
    story.append(PageBreak())
    head = ["#", "Tier", "Business", "Website", "Email", "Facebook", "Instagram", "Why they should buy"]
    data = [[Paragraph(h, ST["h"]) for h in head]]
    for i, r in enumerate(rows, 1):
        c = r["conv"]
        loc = ", ".join(x for x in [r.get("city"), r.get("state")] if x)
        g = f"{c['rating']}★ · {c['reviews']} reviews" if c["rating"] else ""
        data.append([
            Paragraph(str(i), ST["c"]),
            Paragraph(f"<font color='{TIER_COL[r['tier']]}'><b>{r['tier']}</b></font><br/><font color='#5f6b7a'>{c['total']}</font>", ST["c"]),
            Paragraph(f"<b>{esc(r['name'])}</b><br/><font color='#5f6b7a'>{esc(loc)}{(' · ' + g) if g else ''}</font>", ST["c"]),
            Paragraph(link(r["url"]), ST["c"]),
            Paragraph("<br/>".join(f"<link href='mailto:{esc(e)}' color='#0f5e7a'>{esc(e)}</link>" for e in r["emails"][:2]), ST["c"]),
            Paragraph(link(r["fb"][0]) if r["fb"] else "-", ST["c"]),
            Paragraph(link(r["ig"][0]) if r["ig"] else "-", ST["c"]),
            Paragraph(esc(r["pitch"]) + f"<br/><font color='#5f6b7a'>last post {esc(r.get('latest_post'))}</font>", ST["c"]),
        ])
    t = Table(data, colWidths=[0.34, 0.36, 1.71, 1.35, 1.5, 1.35, 1.05, 2.44], repeatRows=1)
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

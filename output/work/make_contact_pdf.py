#!/usr/bin/env python3
"""Contact-sheet PDF + CSV: business name, website, email, Facebook, Instagram (+ last post date when known)."""
import csv, os, re
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "output")
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
ACCENT = colors.HexColor("#0f5e7a"); BAND = colors.HexColor("#eef3f6"); RULE = colors.HexColor("#d5dbe1")
INK = colors.HexColor("#1f2933"); MUTED = colors.HexColor("#5f6b7a")
ST = {
    "t": ParagraphStyle("t", fontName="DVB", fontSize=17, leading=22, textColor=INK),
    "s": ParagraphStyle("s", fontName="DV", fontSize=9, leading=12.5, textColor=MUTED),
    "c": ParagraphStyle("c", fontName="DV", fontSize=7.6, leading=9.6, textColor=INK, wordWrap="CJK"),
    "cb": ParagraphStyle("cb", fontName="DVB", fontSize=7.8, leading=9.8, textColor=INK),
    "h": ParagraphStyle("h", fontName="DVB", fontSize=7.8, leading=9.8, textColor=colors.white),
}


def esc(t):
    return str(t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def link(u, label=None):
    if not u:
        return "—"
    label = label or re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return f"<link href='{esc(u)}' color='#0f5e7a'>{esc(label)}</link>"


def build(rows, cutoff=None, today=None, title="Dental Active 100", note=None,
          pdf_name="Dental_Active_100.pdf", csv_name="ACTIVE_100.csv"):
    with open(os.path.join(OUT, csv_name), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["#", "business", "city", "state", "website", "email", "facebook", "instagram", "latest_social_post"])
        for i, r in enumerate(rows, 1):
            w.writerow([i, r["name"], r.get("city"), r.get("state"), r["url"], r["emails"][0] if r["emails"] else "",
                        r["fb"][0] if r["fb"] else "", r["ig"][0] if r["ig"] else "", r.get("latest_post") or ""])
    doc = SimpleDocTemplate(os.path.join(OUT, pdf_name), pagesize=landscape(letter), leftMargin=0.5 * inch,
                            rightMargin=0.5 * inch, topMargin=0.5 * inch, bottomMargin=0.5 * inch,
                            title=title, author="Dental prospect research", subject="Business name, website, email, social links")
    sub = note or (f"{len(rows)} independent dental practices · each has an email address on its own website and a Facebook/Instagram link"
                   + (f" · latest social post on or after {cutoff}" if cutoff else "") + (f" · checked {today}" if today else ""))
    story = [Paragraph(esc(title), ST["t"]), Spacer(1, 3), Paragraph(esc(sub), ST["s"]), Spacer(1, 10)]
    head = ["#", "Business", "Website", "Email", "Facebook", "Instagram", "Last post"]
    data = [[Paragraph(h, ST["h"]) for h in head]]
    for i, r in enumerate(rows, 1):
        loc = ", ".join(x for x in [r.get("city"), r.get("state")] if x)
        data.append([
            Paragraph(str(i), ST["c"]),
            Paragraph(f"<b>{esc(r['name'])}</b>" + (f"<br/><font color='#5f6b7a'>{esc(loc)}</font>" if loc else ""), ST["c"]),
            Paragraph(link(r["url"]), ST["c"]),
            Paragraph("<br/>".join(f"<link href='mailto:{esc(e)}' color='#0f5e7a'>{esc(e)}</link>" for e in r["emails"][:2]) or "—", ST["c"]),
            Paragraph(link(r["fb"][0]) if r["fb"] else "—", ST["c"]),
            Paragraph(link(r["ig"][0]) if r["ig"] else "—", ST["c"]),
            Paragraph(esc(r.get("latest_post") or "—"), ST["c"]),
        ])
    t = Table(data, colWidths=[0.3, 2.15, 1.75, 1.85, 1.75, 1.35, 0.85], repeatRows=1)
    t._argW = [w * inch for w in t._argW]
    style = [("BACKGROUND", (0, 0), (-1, 0), ACCENT), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 0), (-1, -1), 0.25, RULE), ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    for i in range(2, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), BAND))
    t.setStyle(TableStyle(style))
    story.append(t)

    def foot(c, d):
        c.saveState(); c.setFont("DV", 7); c.setFillColor(MUTED)
        c.drawString(0.5 * inch, 0.3 * inch, title)
        c.drawRightString(landscape(letter)[0] - 0.5 * inch, 0.3 * inch, f"Page {d.page}")
        c.restoreState()
    doc.build(story, onFirstPage=foot, onLaterPages=foot)
    print("wrote", os.path.join(OUT, pdf_name), "and", csv_name)

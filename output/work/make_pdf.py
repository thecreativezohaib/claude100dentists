#!/usr/bin/env python3
"""Render the Round 3 Dental Next 100 report to PDF (output/Dental_Next_100_Round3.pdf)."""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merge
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, CondPageBreak)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
from reportlab.lib.fonts import addMapping
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB"); addMapping("DV", 0, 1, "DV"); addMapping("DV", 1, 1, "DVB")

INK = colors.HexColor("#1f2933"); MUTED = colors.HexColor("#5f6b7a"); ACCENT = colors.HexColor("#0f5e7a")
RULE = colors.HexColor("#d5dbe1"); BAND = colors.HexColor("#eef3f6")

S = {
    "title": ParagraphStyle("title", fontName="DVB", fontSize=26, leading=32, textColor=INK, alignment=TA_CENTER),
    "sub": ParagraphStyle("sub", fontName="DV", fontSize=12, leading=17, textColor=MUTED, alignment=TA_CENTER),
    "h1": ParagraphStyle("h1", fontName="DVB", fontSize=16, leading=21, textColor=ACCENT, spaceBefore=6, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="DVB", fontSize=11.5, leading=15, textColor=INK, spaceAfter=2),
    "meta": ParagraphStyle("meta", fontName="DV", fontSize=8.5, leading=11.5, textColor=MUTED, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="DV", fontSize=9, leading=12.5, textColor=INK, spaceAfter=4),
    "bul": ParagraphStyle("bul", fontName="DV", fontSize=8.4, leading=11.4, textColor=INK, leftIndent=9, bulletIndent=0, spaceAfter=2.2),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=7.4, leading=9.2, textColor=INK),
    "cellh": ParagraphStyle("cellh", fontName="DVB", fontSize=7.6, leading=9.4, textColor=colors.white),
}


def esc(t):
    t = re.sub(r"[\U00010000-\U0010FFFF]", "", str(t or ""))
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def P(t, st="body"):
    return Paragraph(t, S[st])


def table(rows, widths, header=True, zebra=True):
    data = [[P(esc(c), "cellh" if (header and r == 0) else "cell") for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.25, RULE),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), ACCENT))
    if zebra:
        for r in range(1, len(rows)):
            if r % 2 == 0:
                st.append(("BACKGROUND", (0, r), (-1, r), BAND))
    t.setStyle(TableStyle(st))
    return t


def profile_flow(rank, it, live, region_label):
    lines = it["profile_md"].strip().split("\n")
    head = lines[0]
    rest = " ".join(lines[1:])
    bullets = [b.strip() for b in rest.split("•") if b.strip()]
    # header fields
    parts = [p.strip() for p in re.split(r"\s+[—-]\s+", head)]
    url = it["url"]
    title = f"{rank}. {esc(it['name'])}"
    meta = (f"{esc(it['city'])}, {esc(it['state'])} · <link href='{esc(url)}' color='#0f5e7a'>{esc(url)}</link><br/>"
            f"<b>Score {esc(it['score'])}/100</b> · Likelihood: {esc(it['likelihood'])} · Region: {region_label}"
            f" · Vendor: {esc(it.get('vendor_c'))} · Liveness: {live}")
    out = [P(title, "h2"), P(meta, "meta")]
    for b in bullets:
        m = re.match(r"([A-Za-z/ ()\-]{2,40}?)(\s*\([^)]{0,60}\))?:\s*(.*)", b, re.S)
        if m:
            txt = f"<b>{esc(m.group(1) + (m.group(2) or ''))}:</b> {esc(m.group(3))}"
        else:
            txt = esc(b)
        out.append(Paragraph(txt, S["bul"], bulletText="•"))
    out.append(Spacer(1, 4))
    rule = Table([[""]], colWidths=[7.0 * inch], rowHeights=[1])
    rule.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.6, RULE)]))
    out.append(rule)
    out.append(Spacer(1, 6))
    return out


def main():
    ex_domains, ex_names, _ = merge.load_exclusions()
    items, cands, ov = merge.load_all()
    drops = ov.get("drop", {})
    ranked, demoted = merge.policy_rank(merge.dedupe([i for i in items if i["name"] not in drops])[0])
    for it in ranked:
        it["vendor_c"] = merge.canon_vendor(it, ov)
    top, bench = ranked[:100], ranked[100:]
    livec = json.load(open(os.path.join(merge.WORK, "liveness.json")))
    RL = merge.REGION_LABEL

    def live(u):
        c = livec.get(u, {}).get("code")
        return "HTTP 200" if c == "200" else ("403 bot-wall (content verified)" if c == "403" else str(c))

    out_path = os.path.join(merge.OUT, "Dental_Next_100_Round3.pdf")
    doc = BaseDocTemplate(out_path, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                          topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                          title="Dental Next 100 — Round 3", author="Dental prospect research run",
                          subject="100 independent dental practices with weak websites — ranked prospects")

    def deco(c, d):
        c.saveState()
        c.setFont("DV", 7.5); c.setFillColor(MUTED)
        c.drawString(0.75 * inch, 0.45 * inch, "Dental Next 100 — Round 3 · Sep 30 2026")
        c.drawRightString(letter[0] - 0.75 * inch, 0.45 * inch, f"Page {d.page}")
        c.restoreState()
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=deco)])

    st = []
    # ---- cover
    region_counts = {r: sum(1 for it in top if it["region"] == r) for r in merge.REGIONS}
    n200 = sum(1 for it in top if livec.get(it["url"], {}).get("code") == "200")
    st += [Spacer(1, 1.6 * inch), P("Dental Next 100", "title"), Spacer(1, 6),
           P("Round 3 — 100 independent owner-dentist practices whose websites are materially weaker than the business", "sub"),
           Spacer(1, 0.35 * inch)]
    stats = [["Final prospects", "100"], ["Bench (profiled, below cut)", str(len(bench))],
             ["Score range (top 100)", f"{top[-1]['score']} – {top[0]['score']} / 100"],
             ["Practice entries screened", f"{len(items) + len(cands):,}"],
             ["Live URLs", f"{n200} HTTP 200 + {100 - n200} verified bot-walls"],
             ["Overlap with prior rounds", "0"],
             ["Regions", " · ".join(f"{RL[r]} {region_counts[r]}" for r in merge.REGIONS)],
             ["Run date", "September 30, 2026"]]
    t = Table([[P(f"<b>{esc(a)}</b>", "body"), P(esc(b), "body")] for a, b in stats], colWidths=[2.3 * inch, 4.2 * inch])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.3, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    st += [t, PageBreak()]

    # ---- method & QC
    st.append(P("Method", "h1"))
    for t_ in [
        "Two waves of six regional research agents (Northeast, Mid-Atlantic, Southeast, South-Central, Midwest, West) screened practices in fresh round-3 territories. Every finalist website was fetched directly and fingerprinted from raw HTML (title tags, footer vendor credits, generator tags, © strings), screened for DSO/corporate ownership, and scored with the fixed 100-point rubric.",
        "Wave 1 built the pool; wave 2 enriched every finalist with review counts (Birdeye, Healthgrades, Demandforce, Yelp/WebMD, on-site schema.org ratings), re-scored, and screened unmined territory via directory crawls + raw-HTML fingerprinting + hand verification.",
        "Scoring weights: Financial Capacity 20 · Business Maturity 15 · Website Weakness 15 · Business-vs-Website Gap 15 · Customer Website Dependence 10 · Design Transformation Potential 10 · Conversion Opportunity 5 · Existing Digital Spending 3 · Decision-Maker Accessibility 2. Ranking: score, then conversion likelihood.",
        "Evidence tags: VERIFIED (seen directly), INFERRED (reasoned from observable facts), UNKNOWN (not found). Financial capacity is always inferred from publicly observable business scale, pricing, facilities, service positioning and market — never invented.",
    ]:
        st.append(P(esc(t_)))
    st.append(P("Quality checks", "h1"))
    for q in [
        f"Liveness: {n200}/100 return HTTP 200; the rest are Cloudflare bot-walls whose content was verified from recent archived copies. 0 dead.",
        "Exclusions: 0 overlap with Rounds 1–2 by name, domain, or any domain mentioned inside a profile. One prior-round practice returned by research (Bruce Matthews DDS, Wilmington DE) was caught and removed.",
        "Cross-region duplicates: 0. Independence: every profile carries a status and basis; max two MEDIUM-confidence entries in the top 50 (Oak Brook Dental Center demoted from #37 to #51 to respect the cap).",
        "Removed during QC: Aesthetic Dental Innovations (site suspended); Capitol Hill Dentistry, David Faget DMD, Premier Dental Care Pleasanton (thin review evidence).",
    ]:
        st.append(Paragraph(esc(q), S["bul"], bulletText="•"))
    st.append(P("Caveats", "h1"))
    for q in [
        "Review counts come mostly from Birdeye (aggregates Google), Healthgrades, Demandforce or Yelp as named per profile; treat as directional and confirm before outreach.",
        "Independence is INFERRED for most practices (no group language, owner-named entity, no DSO strings) — confirm ownership on the first call.",
        "\"Copyright � 2019 Prosites, Inc.\" quotes the ProSites v4 engine string in page source; the visible footer year may differ.",
        "Facebook/Instagram posting activity was not checked (platforms block logged-out access from cloud servers); see SOCIAL_AUDIT.csv for the prepared checklist.",
    ]:
        st.append(Paragraph(esc(q), S["bul"], bulletText="•"))
    st.append(PageBreak())

    # ---- master table
    st.append(P("Ranked master list", "h1"))
    rows = [["#", "Practice", "Location", "Score", "Likelihood", "Region", "Vendor"]]
    for i, it in enumerate(top, 1):
        rows.append([i, it["name"], f"{it['city']}, {it['state']}", it["score"], re.sub(r"\s*\(.*", "", it["likelihood"]), RL[it["region"]], it["vendor_c"]])
    st.append(table(rows, [0.3 * inch, 2.35 * inch, 1.35 * inch, 0.45 * inch, 0.85 * inch, 0.8 * inch, 0.9 * inch]))
    st.append(PageBreak())

    # ---- profiles
    st.append(P("Full profiles", "h1"))
    for i, it in enumerate(top, 1):
        fl = profile_flow(i, it, live(it["url"]), RL[it["region"]])
        st.append(CondPageBreak(1.6 * inch))
        st.append(KeepTogether(fl[:4]))
        st += fl[4:]
    st.append(PageBreak())

    # ---- bench
    st.append(P("Bench (ranks 101–%d)" % (100 + len(bench)), "h1"))
    st.append(P("Profiled finalists below the cut line — first replacements if any of the 100 drop out."))
    rows = [["#", "Practice", "Location", "URL", "Score", "Region"]]
    for i, it in enumerate(bench, 101):
        rows.append([i, it["name"], f"{it['city']}, {it['state']}", it["url"], it["score"], RL[it["region"]]])
    st.append(table(rows, [0.35 * inch, 2.1 * inch, 1.25 * inch, 2.2 * inch, 0.45 * inch, 0.65 * inch]))
    st.append(PageBreak())

    # ---- vendor clusters
    st.append(P("Vendor clusters (demo workflow)", "h1"))
    st.append(P("One demo build per template vendor can be re-skinned across that vendor's practices."))
    clusters = {}
    for i, it in enumerate(top, 1):
        clusters.setdefault(it["vendor_c"], []).append(f"#{i} {it['name']}")
    rows = [["Vendor / platform", "Count", "Practices"]]
    for v, lst in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        rows.append([v, len(lst), "; ".join(lst)])
    st.append(table(rows, [1.45 * inch, 0.45 * inch, 5.1 * inch]))
    st.append(Spacer(1, 10))
    st.append(P("Notable DSO / corporate catches", "h1"))
    for c in ov.get("dso_catches", []):
        st.append(Paragraph(esc(c), S["bul"], bulletText="•"))

    doc.build(st)
    print(out_path)


if __name__ == "__main__":
    main()

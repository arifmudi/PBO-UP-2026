
from pathlib import Path
from xml.sax.saxutils import escape
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Preformatted,
    Table,
    TableStyle,
)

folder = Path(__file__).resolve().parent
file_md = folder / "LKM-P02.md"
file_pdf = folder / "LKM-P02.pdf"

if not file_md.exists():
    raise FileNotFoundError(
        f"File LKM tidak ditemukan: {file_md}"
    )

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="JudulLKM",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=16,
    leading=21,
    alignment=TA_CENTER,
    spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="HeadingLKM",
    parent=styles["Heading2"],
    fontSize=12,
    leading=16,
    spaceBefore=12,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="IsiLKM",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="KodeLKM",
    fontName="Courier",
    fontSize=8,
    leading=11,
    leftIndent=8,
    rightIndent=8,
    spaceBefore=4,
    spaceAfter=8,
))

doc = SimpleDocTemplate(
    str(file_pdf),
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm,
)

story = []
lines = file_md.read_text(encoding="utf-8").splitlines()
in_code = False
code_lines = []
first_heading = True
i = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped.startswith("```"):
        if not in_code:
            in_code = True
            code_lines = []
        else:
            story.append(Preformatted(
                "\n".join(code_lines), styles["KodeLKM"]
            ))
            in_code = False
        i += 1
        continue

    if in_code:
        code_lines.append(line)
        i += 1
        continue

    if not stripped or stripped == "---":
        story.append(Spacer(1, 4))
        i += 1
        continue

    # Mengubah tabel Markdown menjadi tabel PDF
    if stripped.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [
                cell.strip()
                for cell in lines[i].strip().strip("|").split("|")
            ]
            if not all(
                re.fullmatch(r":?-{3,}:?", cell) for cell in cells
            ):
                rows.append(cells)
            i += 1

        if rows:
            column_count = max(len(row) for row in rows)
            data = []
            for row in rows:
                row += [""] * (column_count - len(row))
                data.append([
                    Paragraph(escape(cell), styles["IsiLKM"])
                    for cell in row
                ])

            table = Table(data, repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.append(table)
            story.append(Spacer(1, 8))
        continue

    if stripped.startswith("#"):
        level = len(stripped) - len(stripped.lstrip("#"))
        heading = stripped[level:].strip()
        if level == 1 and first_heading:
            story.append(Paragraph(escape(heading), styles["JudulLKM"]))
            first_heading = False
        else:
            story.append(Paragraph(
                escape(heading), styles["HeadingLKM"]
            ))
        i += 1
        continue

    if stripped.startswith("- ") or stripped.startswith("* "):
        text = "• " + stripped[2:]
        story.append(Paragraph(escape(text), styles["IsiLKM"]))
        i += 1
        continue

    if re.match(r"^\d+\.\s", stripped):
        story.append(Paragraph(escape(stripped), styles["IsiLKM"]))
        i += 1
        continue

    # Format tebal sederhana
    text = escape(stripped)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    story.append(Paragraph(text, styles["IsiLKM"]))
    i += 1

if in_code and code_lines:
    story.append(Preformatted(
        "\n".join(code_lines), styles["KodeLKM"]
    ))

doc.build(story)

print(f"PDF berhasil dibuat: {file_pdf}")

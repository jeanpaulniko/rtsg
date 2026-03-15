#!/usr/bin/env python3
"""Build a KDP-ready PDF for the RTSG Companion Papers collection."""

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import black
from reportlab.pdfgen import canvas


# KDP trim size: 6x9 inches
PAGE_WIDTH = 6 * inch
PAGE_HEIGHT = 9 * inch
MARGIN = 0.75 * inch

# Paper files (main companion papers)
PAPERS = [
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__consciousness.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__federation_consciousness.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__economics.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__psychiatry.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__sociology.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__machine_learning.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__political_science.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__anthropology.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__psychology.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__cogos.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__education.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__neuroscience.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__nature_taxonomy.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__linguistics.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__philosophy.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__companions__philosophy_plato.md',
]

# Appendices (mathematical sections)
APPENDICES = [
    ('/sessions/clever-kind-hypatia/section3_theorem_b_regularity.md', 'Appendix A: Adelic Regularity'),
    ('/sessions/clever-kind-hypatia/section4_discussion_weil_obstructions.md', 'Appendix B: Spectral Obstructions'),
]


def extract_title(content):
    """Extract the first H1 heading."""
    match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def clean_text(text):
    """Clean markdown text for reportlab (minimal formatting)."""
    # Remove YAML frontmatter
    text = re.sub(r'^---.*?---\n', '', text, flags=re.DOTALL)

    # Remove complex markdown elements that cause parsing issues
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`([^`]+)`', r'\1', text)  # inline code

    # Remove LaTeX-style formulas
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$([^\$]+)\$', r'[\1]', text)  # Keep $ content in brackets

    # Remove tables
    text = re.sub(r'\|.*?\|.*?\|.*', '', text)

    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Remove HTML tags (like <b>, </b>, <i>, etc.)
    text = re.sub(r'<[^>]+>', '', text)

    # Remove special admonitions
    text = re.sub(r'^!!!.*?$', '', text, flags=re.MULTILINE)

    # Remove definition/reference styles (like \tA{})
    text = re.sub(r'\\t[A-Z]{}\s*', '', text)

    # Remove link references
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Fix orphaned XML/HTML tags that may cause reportlab parsing errors
    text = re.sub(r'<[^>]*$', '', text, flags=re.MULTILINE)  # Unclosed tags at line end
    text = re.sub(r'^[^<]*>', '', text, flags=re.MULTILINE)  # Closing tags without opening at line start

    return text.strip()


def parse_markdown_to_blocks(content, styles):
    """Parse markdown into reportlab blocks."""
    blocks = []
    content = clean_text(content)
    lines = content.split('\n')
    i = 0

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=11,
        leading=13,
        alignment=TA_JUSTIFY,
        fontName='Times-Roman',
        spaceAfter=8,
    )

    h2_style = ParagraphStyle(
        'H2',
        fontSize=14,
        leading=16,
        fontName='Helvetica-Bold',
        spaceAfter=10,
        spaceBefore=10,
    )

    h3_style = ParagraphStyle(
        'H3',
        fontSize=12,
        leading=14,
        fontName='Helvetica-Bold',
        spaceAfter=8,
        spaceBefore=8,
    )

    while i < len(lines):
        line = lines[i].rstrip()

        # H2
        if line.startswith('## '):
            text = line[3:].strip()
            if text:
                blocks.append(Paragraph(text, h2_style))
            i += 1
            continue

        # H3
        if line.startswith('### '):
            text = line[4:].strip()
            if text:
                blocks.append(Paragraph(text, h3_style))
            i += 1
            continue

        # Skip H1
        if line.startswith('# '):
            i += 1
            continue

        # List items
        if line.startswith('- '):
            text = line[2:].strip()
            blocks.append(Paragraph('• ' + text, body_style))
            i += 1
            continue

        # Regular paragraphs
        if line.strip() and not line.startswith('#'):
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '-')):
                para_lines.append(lines[i])
                i += 1

            text = ' '.join(p.rstrip() for p in para_lines).strip()
            if len(text) > 50 and len(text) < 5000:  # Reasonable paragraph size
                blocks.append(Paragraph(text, body_style))
            continue

        # Empty lines
        if not line.strip():
            blocks.append(Spacer(1, 0.08*inch))
            i += 1
            continue

        i += 1

    return blocks


class PageNumCanvas(canvas.Canvas):
    """Canvas with centered page numbers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_num = 0

    def showPage(self):
        self.page_num += 1
        self.setFont("Times-Roman", 10)
        w = self._pagesize[0]
        self.drawCentredString(w/2, 0.4*inch, str(self.page_num))
        super().showPage()


def build_pdf():
    """Build the KDP PDF."""
    pdf_path = '/sessions/clever-kind-hypatia/mnt/outputs/rtsg_companions_kdp.pdf'

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="RTSG Companion Papers",
        author="Jean-Paul Niko",
    )

    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'Title',
        fontSize=26,
        leading=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        textColor=black,
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        fontName='Times-Roman',
    )

    author_style = ParagraphStyle(
        'Author',
        fontSize=12,
        leading=14,
        alignment=TA_CENTER,
        fontName='Times-Roman',
    )

    # TITLE PAGE
    story.append(Spacer(1, 1.2*inch))
    story.append(Paragraph("Relational Three-Space Geometry", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Companion Papers", subtitle_style))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("Applications Across Disciplines", subtitle_style))
    story.append(Spacer(1, 1.2*inch))
    story.append(Paragraph("by Jean-Paul Niko", author_style))
    story.append(Spacer(1, 0.4*inch))
    version_style = ParagraphStyle(
        'Version',
        fontSize=11,
        leading=13,
        alignment=TA_CENTER,
        fontName='Times-Roman',
    )
    story.append(Paragraph("v6.0 — Definitive Edition", version_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("March 2026", author_style))
    story.append(PageBreak())

    # COPYRIGHT PAGE
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("<b>Relational Three-Space Geometry: Companion Papers</b>", ParagraphStyle(
        'CopyTitle', fontSize=12, fontName='Helvetica-Bold', alignment=TA_LEFT)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Copyright 2026 Jean-Paul Niko. All rights reserved.", ParagraphStyle(
        'Copy', fontSize=10, fontName='Times-Roman', alignment=TA_LEFT)))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "This collection comprises 16 companion papers applying the Relational Three-Space Geometry (RTSG) "
        "framework across disciplines: consciousness, economics, psychology, machine learning, "
        "political science, anthropology, education, neuroscience, linguistics, philosophy, and more. "
        "The volume also includes two mathematical appendices covering adelic regularity theory and spectral obstructions.",
        ParagraphStyle('CopyText', fontSize=10, fontName='Times-Roman', alignment=TA_LEFT)))
    story.append(PageBreak())

    # TABLE OF CONTENTS
    story.append(Paragraph("Table of Contents", ParagraphStyle(
        'TOCTitle', fontSize=16, fontName='Helvetica-Bold', spaceAfter=12)))

    toc_style = ParagraphStyle(
        'TOC', fontSize=10, fontName='Times-Roman', spaceAfter=5)

    page_num = 1
    for i, filepath in enumerate(PAPERS, 1):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            title = extract_title(content)
            page_num += 5
            story.append(Paragraph(f"{i}. {title}", toc_style))
        except:
            pass

    # Appendices in TOC
    for j, (filepath, label) in enumerate(APPENDICES, 1):
        idx = len(PAPERS) + j
        story.append(Paragraph(f"{idx}. {label}", toc_style))

    story.append(PageBreak())

    # PAPERS
    for i, filepath in enumerate(PAPERS, 1):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content)

            # Paper title
            story.append(Spacer(1, 1.5*inch))
            story.append(Paragraph(title, ParagraphStyle(
                'PaperTitle', fontSize=18, fontName='Helvetica-Bold',
                alignment=TA_CENTER, spaceAfter=12)))
            story.append(Paragraph(f"Paper {i} of {len(PAPERS)}", ParagraphStyle(
                'PaperNum', fontSize=9, fontName='Times-Roman', alignment=TA_CENTER)))
            story.append(PageBreak())

            # Paper content
            blocks = parse_markdown_to_blocks(content, styles)
            story.extend(blocks)

            if i < len(PAPERS):
                story.append(PageBreak())

        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            continue

    # APPENDICES
    for i, (filepath, label) in enumerate(APPENDICES, 1):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Appendix title
            story.append(Spacer(1, 1.5*inch))
            story.append(Paragraph(label, ParagraphStyle(
                'AppendixTitle', fontSize=18, fontName='Helvetica-Bold',
                alignment=TA_CENTER, spaceAfter=12)))
            story.append(Paragraph(f"Appendix {i} of {len(APPENDICES)}", ParagraphStyle(
                'AppendixNum', fontSize=9, fontName='Times-Roman', alignment=TA_CENTER)))
            story.append(PageBreak())

            # Appendix content
            blocks = parse_markdown_to_blocks(content, styles)
            story.extend(blocks)

            if i < len(APPENDICES):
                story.append(PageBreak())

        except Exception as e:
            print(f"Error processing appendix {filepath}: {e}")
            continue

    # Build PDF
    doc.build(story, canvasmaker=PageNumCanvas)
    print(f"\nSUCCESS: PDF created at {pdf_path}")
    print(f"Title: Relational Three-Space Geometry: Companion Papers")
    print(f"Version: v6.0 — Definitive Edition")
    print(f"Author: Jean-Paul Niko")
    print(f"Size: 6x9 inches (KDP trim)")
    print(f"Papers: {len(PAPERS)}")
    print(f"Appendices: {len(APPENDICES)}")
    print(f"Margins: 0.75 inches all sides")
    print(f"Fonts: Times-Roman (body), Helvetica-Bold (heads)")


if __name__ == '__main__':
    build_pdf()

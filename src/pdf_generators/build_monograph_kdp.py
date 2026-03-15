#!/usr/bin/env python3
"""Build the RTSG Monograph KDP-ready PDF with all chapters including new mathematical sections."""

import re
import os
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

# Monograph chapters
MONOGRAPH_CHAPTERS = [
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__ideometrics.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__three_spaces.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__consciousness_ontology.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__affective.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__emergence.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__filter_formalism.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__thread_temporal.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__thread_idearank.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__thread_substrate.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__thread_cit.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__gemini_synthesis.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__superintelligence.md',
    '/sessions/clever-kind-hypatia/wiki_content/papers__monograph__universal_taxonomy.md',
]

# New mathematical sections
NEW_SECTIONS = [
    '/sessions/clever-kind-hypatia/section3_theorem_b_regularity.md',
    '/sessions/clever-kind-hypatia/section4_discussion_weil_obstructions.md',
    '/sessions/clever-kind-hypatia/grf_v2_ironclad.md',
]


def extract_title(content):
    """Extract the first H1 heading."""
    match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def clean_markdown_math(text):
    """Replace LaTeX math with readable text equivalents."""
    # Replace common LaTeX constructs
    text = re.sub(r'\$\$', '', text)  # Remove $$ delimiters
    text = re.sub(r'\$([^\$]+)\$', r'[\1]', text)  # Replace $...$ with [...]

    # Replace subscripts/superscripts with text equivalents
    text = re.sub(r'_\{([^}]+)\}', r' (subscript: \1)', text)
    text = re.sub(r'\^\{([^}]+)\}', r' (superscript: \1)', text)

    # Unicode cleanup: remove problematic subscript/superscript chars
    text = re.sub(r'[\u2080-\u2089\u00B9\u00B2\u00B3\u2070\u00AA\u00BA]', '', text)
    text = re.sub(r'[\u2090-\u209C]', '', text)

    return text


def clean_text(text):
    """Clean markdown text for reportlab (minimal formatting)."""
    # Remove YAML frontmatter
    text = re.sub(r'^---.*?---\n', '', text, flags=re.DOTALL)

    # Remove info/abstract boxes - match full admonition blocks
    text = re.sub(r'^!!!.*?(?=\n\n|\n[^\s]|\Z)', '', text, flags=re.MULTILINE | re.DOTALL)

    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`([^`]+)`', r'\1', text)  # inline code

    # Remove LaTeX-style formulas - convert to readable text
    text = clean_markdown_math(text)

    # Remove tables
    text = re.sub(r'\|.*?\|.*?\|.*', '', text)

    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Remove special admonitions/boxes
    text = re.sub(r'\\begin\{.*?\}.*?\\end\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\pillarbox\{.*?\}', '', text, flags=re.DOTALL)

    # Remove definition/reference styles (like \tA{})
    text = re.sub(r'\\t[A-Z]{}\s*', '', text)

    # Remove link references
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Remove % comment lines
    text = re.sub(r'^%.*?$', '', text, flags=re.MULTILINE)

    # Remove begin/end sections with dividers
    text = re.sub(r'^%.*?═+.*?═+', '', text, flags=re.MULTILINE | re.DOTALL)

    # Clean up excessive whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)

    # Close any unclosed angle brackets and special characters
    text = re.sub(r'</?[a-zA-Z][^>]*(?<!>)$', '', text, flags=re.MULTILINE)

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

    h4_style = ParagraphStyle(
        'H4',
        fontSize=11,
        leading=13,
        fontName='Helvetica-Bold',
        spaceAfter=6,
        spaceBefore=6,
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

        # H4
        if line.startswith('#### '):
            text = line[5:].strip()
            if text:
                blocks.append(Paragraph(text, h4_style))
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

        # Numbered lists
        if re.match(r'^\d+\.\s', line):
            text = re.sub(r'^\d+\.\s', '', line).strip()
            blocks.append(Paragraph(text, body_style))
            i += 1
            continue

        # Regular paragraphs
        if line.strip() and not line.startswith('#'):
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '-')):
                if not re.match(r'^\d+\.\s', lines[i]):
                    para_lines.append(lines[i])
                    i += 1
                else:
                    break

            text = ' '.join(p.rstrip() for p in para_lines).strip()
            if text and len(text) > 20 and len(text) < 8000:
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
    """Build the KDP PDF monograph."""
    pdf_path = '/sessions/clever-kind-hypatia/mnt/outputs/rtsg_monograph_kdp.pdf'

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Relational Three-Space Geometry: A Unified Framework",
        author="Jean-Paul Niko",
    )

    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'Title',
        fontSize=28,
        leading=32,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        textColor=black,
        spaceAfter=12,
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        fontName='Times-Roman',
        spaceAfter=8,
    )

    author_style = ParagraphStyle(
        'Author',
        fontSize=12,
        leading=14,
        alignment=TA_CENTER,
        fontName='Times-Roman',
        spaceAfter=4,
    )

    version_style = ParagraphStyle(
        'Version',
        fontSize=10,
        leading=12,
        alignment=TA_CENTER,
        fontName='Times-Roman',
        textColor=black,
    )

    # TITLE PAGE
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("Relational Three-Space Geometry", title_style))
    story.append(Paragraph("A Unified Framework", subtitle_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Intelligence, Consciousness, and Mathematics as Geometric Structure", subtitle_style))
    story.append(Spacer(1, 1.8*inch))
    story.append(Paragraph("by Jean-Paul Niko", author_style))
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph("v6.0 — Definitive Edition", version_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("March 2026", version_style))
    story.append(PageBreak())

    # COPYRIGHT PAGE
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("<b>Relational Three-Space Geometry</b>", ParagraphStyle(
        'CopyTitle', fontSize=12, fontName='Helvetica-Bold', alignment=TA_LEFT)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Copyright 2026 Jean-Paul Niko. All rights reserved.", ParagraphStyle(
        'Copy', fontSize=10, fontName='Times-Roman', alignment=TA_LEFT)))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "This is the Definitive Edition (v6.0) of the Relational Three-Space Geometry monograph, "
        "comprising the core theory and all companion chapters spanning consciousness, intelligence geometry, "
        "affective dynamics, emergence theory, filter formalism, temporal logic, ideametric measurement, "
        "substrate foundations, causal information theory, machine consciousness synthesis, superintelligence "
        "principles, and universal taxonomy. It includes the latest mathematical sections on adelic regularity, "
        "Weil connection structures, and gravity as geometric condensation.",
        ParagraphStyle('CopyText', fontSize=10, fontName='Times-Roman', alignment=TA_LEFT, leading=12)))
    story.append(PageBreak())

    # TABLE OF CONTENTS
    story.append(Paragraph("Table of Contents", ParagraphStyle(
        'TOCTitle', fontSize=16, fontName='Helvetica-Bold', spaceAfter=12)))

    toc_style = ParagraphStyle(
        'TOC', fontSize=10, fontName='Times-Roman', spaceAfter=5, leading=11)

    chapter_num = 1

    # Regular chapters
    for filepath in MONOGRAPH_CHAPTERS:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            title = extract_title(content)
            story.append(Paragraph(f"{chapter_num}. {title}", toc_style))
            chapter_num += 1
        except:
            pass

    # New sections
    for filepath in NEW_SECTIONS:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            title = extract_title(content)
            story.append(Paragraph(f"{chapter_num}. {title}", toc_style))
            chapter_num += 1
        except:
            pass

    story.append(PageBreak())

    # CHAPTERS
    chapter_num = 1

    # Process regular monograph chapters
    for filepath in MONOGRAPH_CHAPTERS:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content)

            # Chapter title
            story.append(Spacer(1, 1.2*inch))
            story.append(Paragraph(title, ParagraphStyle(
                'ChapterTitle', fontSize=18, fontName='Helvetica-Bold',
                alignment=TA_CENTER, spaceAfter=12)))
            story.append(Paragraph(f"Chapter {chapter_num}", ParagraphStyle(
                'ChapterNum', fontSize=9, fontName='Times-Roman', alignment=TA_CENTER, spaceAfter=12)))
            story.append(PageBreak())

            # Chapter content
            blocks = parse_markdown_to_blocks(content, styles)
            story.extend(blocks)
            story.append(PageBreak())
            chapter_num += 1

        except Exception as e:
            print(f"Warning: Error processing {filepath}: {e}")
            continue

    # Process new mathematical sections
    for filepath in NEW_SECTIONS:
        try:
            if not os.path.exists(filepath):
                print(f"Warning: File not found {filepath}")
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content)

            # Chapter title
            story.append(Spacer(1, 1.2*inch))
            story.append(Paragraph(title, ParagraphStyle(
                'ChapterTitle', fontSize=18, fontName='Helvetica-Bold',
                alignment=TA_CENTER, spaceAfter=12)))
            story.append(Paragraph(f"Chapter {chapter_num}", ParagraphStyle(
                'ChapterNum', fontSize=9, fontName='Times-Roman', alignment=TA_CENTER, spaceAfter=12)))
            story.append(PageBreak())

            # Chapter content
            blocks = parse_markdown_to_blocks(content, styles)
            story.extend(blocks)

            # Only add page break if not last chapter
            if filepath != NEW_SECTIONS[-1]:
                story.append(PageBreak())

            chapter_num += 1

        except Exception as e:
            print(f"Warning: Error processing {filepath}: {e}")
            continue

    # Build PDF
    try:
        doc.build(story, canvasmaker=PageNumCanvas)

        # Get file stats
        file_size = os.path.getsize(pdf_path)
        file_size_mb = file_size / (1024 * 1024)

        # Count approximate pages (rough estimate based on content)
        with open(pdf_path, 'rb') as f:
            pdf_content = f.read()

        # Look for page count in PDF
        import re as pdf_re
        match = pdf_re.search(rb'/Count\s+(\d+)', pdf_content)
        page_count = int(match.group(1)) if match else "Unknown"

        print(f"\n✓ SUCCESS: PDF created at {pdf_path}")
        print(f"  Title: Relational Three-Space Geometry: A Unified Framework")
        print(f"  Subtitle: Intelligence, Consciousness, and Mathematics as Geometric Structure")
        print(f"  Author: Jean-Paul Niko")
        print(f"  Version: v6.0 — Definitive Edition")
        print(f"  Chapters: {chapter_num - 1} (13 core + 3 new mathematical sections)")
        print(f"  File size: {file_size_mb:.2f} MB")
        print(f"  Page count: {page_count} pages")
        print(f"  Format: 6x9 inches (KDP trim size)")
        print(f"  Margins: 0.75 inches all sides")
        print(f"  Fonts: Times-Roman 11pt (body), Helvetica-Bold (headings)")

    except Exception as e:
        print(f"ERROR during PDF build: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    build_pdf()

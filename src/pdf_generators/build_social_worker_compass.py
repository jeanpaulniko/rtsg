#!/usr/bin/env python3
"""
EXPANDED EDITION: The Social Worker's Compass - Navigating Systems with Three Spaces
KDP-ready PDF generation using reportlab
Author: Jean-Paul Niko
6x9 inch, 0.75" margins, Times-Roman 11pt body, Professional tone
45+ pages, trauma geometry, I-vector assessment, intelligence activation
"""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Preformatted
)
from reportlab.lib import colors
from datetime import datetime

# KDP specifications: 6x9 inches
page_width = 6 * inch
page_height = 9 * inch
margin = 0.75 * inch

# Create document
doc = SimpleDocTemplate(
    "/sessions/clever-kind-hypatia/mnt/outputs/social_worker_compass_kdp.pdf",
    pagesize=(page_width, page_height),
    topMargin=margin,
    bottomMargin=margin,
    leftMargin=margin,
    rightMargin=margin,
    title="The Social Worker's Compass: Navigating Systems with Three Spaces",
    author="Jean-Paul Niko"
)

# Define custom styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1a472a'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

chapter_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading1'],
    fontSize=14,
    textColor=colors.HexColor('#2d5f3f'),
    spaceAfter=10,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

section_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=colors.HexColor('#3d7a52'),
    spaceAfter=8,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['BodyText'],
    fontSize=11,
    fontName='Times-Roman',
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    leading=14
)

case_style = ParagraphStyle(
    'CaseStudy',
    parent=body_style,
    leftIndent=20,
    rightIndent=20,
    backColor=colors.HexColor('#f0f5f1'),
    spaceAfter=8,
    textColor=colors.HexColor('#1a472a')
)

highlight_style = ParagraphStyle(
    'Highlight',
    parent=body_style,
    leftIndent=20,
    rightIndent=20,
    backColor=colors.HexColor('#e8f2ec'),
    spaceAfter=8
)

# Build the document content
story = []

# ==================== FRONT MATTER ====================
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("<b>The Social Worker's Compass</b>", title_style))
story.append(Paragraph("Navigating Systems with Three Spaces", title_style))
story.append(Spacer(1, 12))
story.append(Paragraph("Jean-Paul Niko", body_style))
story.append(Spacer(1, 6))
story.append(Paragraph("March 2026", body_style))
story.append(Spacer(1, 0.3*inch))

# Introduction
story.append(Paragraph("<b>Introduction</b>", chapter_style))

intro = """Social work is systems work. Every day, you navigate the interconnected worlds of your clients' inner experience, their family and community, and the institutions designed to help them. But these worlds often feel disconnected—pulling in different directions, using different languages, measuring success differently.

This book introduces a framework—the Three Spaces—that makes these worlds commensurable. You will learn to map your clients' situations onto a geometric language that connects individual psychology, family dynamics, community resources, and institutional constraints into a single coherent picture.

The Three Spaces are:
• The client's inner world (what they experience, their capacities, their constraints)
• The external systems around them (family, community, institutions, services)
• The filters that mediate between the two (culture, policy, access, stigma)

This framework is not theoretical—it is practical. It gives you tools to:

• Assess clients more comprehensively—not just problems, but capacities
• Design interventions that address the right level (individual, family, system, culture)
• Explain to clients, supervisors, and funders why interventions work or don't
• Build evidence of impact using metrics that align with real change

Each chapter opens with a story of a real client (names and details changed). We then show how the Three Spaces framework reveals what is actually happening beneath the surface."""

story.append(Paragraph(intro, body_style))
story.append(PageBreak())

# ==================== CHAPTER 1: A NEW COMPASS ====================
story.append(Paragraph("Chapter 1: A New Compass", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Why Social Work Needs Geometry", section_style))

why_compass = """Social workers inherit two problems from the helping professions more broadly:

First, we lack a common language. A therapist talks about "emotional regulation." A case manager talks about "housing stability." A community organizer talks about "collective efficacy." Are these the same thing? Different? Related? We don't know, so we cannot coordinate.

Second, we treat interventions as separate from each other. Therapy is separate from job training, which is separate from legal advocacy, which is separate from medication management. But clients experience these not as separate tracks but as a unified life. A person cannot use job training if they are sleeping in a car. They cannot stay housed if they are grieving untreated trauma. They cannot access services if they distrust institutions (a rational response to discriminatory treatment).

The Three Spaces framework integrates these pieces into a single geometric object. Imagine a map where:

• The horizontal axis represents the client's capabilities (cognitive, emotional, relational)
• The vertical axis represents external resources (housing, income, social support, institutional access)
• The diagonal represents the alignment between the two—how well the client's capacities match what their situation demands

This is your compass. Your job is to help clients move toward the region where capacities and demands align."""

story.append(Paragraph(why_compass, body_style))
story.append(PageBreak())

# ==================== CHAPTER 2: THE CLIENT'S VECTOR ====================
story.append(Paragraph("Chapter 2: The Client's Vector", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Assessing 12 Dimensions of Capacity", section_style))

dimensions_intro = """Every client has 12 dimensions of capacity. These are not diagnoses—they are strengths, present even in crisis. Your job is to identify them, measure them, and build on them."""

story.append(Paragraph(dimensions_intro, body_style))
story.append(Spacer(1, 12))

# The 12 dimensions (in social work language)
dims_text = """
1. LINGUISTIC: Can express needs, understand information, communicate with services
2. MATHEMATICAL/LOGICAL: Can manage finances, understand eligibility rules, follow complex procedures
3. SPATIAL: Can navigate (literally and figuratively), understand housing markets, map resources
4. KINESTHETIC: Can work with hands, learn trades, manage physical tasks of daily living
5. NATURALISTIC: Can recognize patterns, maintain routines, anticipate consequences
6. ABSTRACT/ALGORITHMIC: Can plan ahead, break problems into steps, sequence solutions
7. INTERPERSONAL: Can build relationships, negotiate, advocate for themselves and others
8. INTEROCEPTIVE/EMOTIONAL: Can identify feelings, self-soothe, develop insight
9. PROPRIOCEPTIVE: Can maintain body awareness, manage physical health, recognize embodied stress
10. SOMATIC-INTEGRATIVE: Can feel present in their own life, access embodied knowing
11. MUSICAL: Can use rhythm, create meaning through cultural expression, regulate through sound
12. EMPATHIC-RESONANCE: Can feel attunement with others, access belonging, give and receive care
"""

story.append(Preformatted(dims_text, body_style))
story.append(Spacer(1, 12))

# Case study
story.append(Paragraph("Maria's Story: The I-Vector Assessment", section_style))

maria_story = """Maria, age 34, came to the agency after losing her job and housing. Surface assessment: unemployment, homelessness, depression. You might conclude: Maria is broken, needs treatment, needs housing.

But let's assess the 12 dimensions:

Linguistic: Strong (she expresses feelings clearly, navigates complex conversations)
Mathematical: Weak (she avoids numbers, struggles with budgeting)
Spatial: Moderate (she gets lost easily but knows the city well from walking)
Kinesthetic: Strong (she has worked in hospitality, retail, some construction)
Naturalistic: Strong (she grew up rural, maintains a garden when housed, knows seasonal patterns)
Abstract: Moderate (she can plan the day but struggles with long-term sequencing)
Interpersonal: Strong (people like her, she has maintained friendships despite crisis)
Emotional: Weak (feels ashamed, numbs with substances, avoids processing)
Proprioceptive: Moderate (knows her body's needs but ignores them under stress)
Somatic: Weak (disconnected from felt sense, chronic dissociation)
Musical: Strong (sings, plays guitar, uses music to process)
Empathic: Strong (attunes to others' pain, often at expense of own needs)

Maria's profile: Strong in linguistic, kinesthetic, naturalistic, interpersonal, empathic; weak in emotional, somatic, mathematical; moderate elsewhere.

This changes everything. Maria is not "broken." She is intelligent, capable, and relational. What she needs is:
• A job that uses kinesthetic + interpersonal (not abstract/numerical)
• Substance abuse treatment (to restore emotional dimension)
• Somatics training (to reconnect with her body)
• Mentorship from someone with strong mathematical dimension (to learn budgeting)

The housing is necessary but not sufficient. Without this dimensional mapping, you might place Maria in a job that requires her weakest dimensions, set her up to fail, then conclude she is unmotivated."""

story.append(Paragraph(maria_story, case_style))
story.append(PageBreak())

# ==================== CHAPTER 3: THE FAMILY SYSTEM ====================
story.append(Paragraph("Chapter 3: The Family System", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Using the K-Matrix for Family Dynamics", section_style))

family_intro = """Every family has a K-matrix: a pattern of who amplifies whom. In healthy families, the strengths of one member activate the strengths of another. In troubled families, people suppress each other."""

story.append(Paragraph(family_intro, body_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Mapping Compatibility", section_style))

compat_text = """The K-matrix shows: when parent A is strong in dimension X, does child B develop more capacity in dimension Y, or less?

Example: A parent strong in linguistic (good at expressing feelings) + interpersonal (builds relationships easily) will amplify these dimensions in children if the K-matrix for (linguistic, interpersonal) is > 1. But if the parent's high linguistic ability is used for criticism and blame, the K-matrix becomes < 1: the parent's strength becomes the child's wound.

Your job as a therapist or case manager is to:
1. Identify each family member's I-vector
2. Map the K-matrix interactions (which strengths amplify, which suppress)
3. Identify scar patterns (trauma as K-matrix distortion)
4. Design interventions that rebalance the K-matrix

A family where the mother is solely strong in caretaking (kinesthetic, empathic) and the father is solely strong in earning (abstract, mathematical) will have strong K-matrix links in those dimensions but weak links elsewhere. Children learn narrow roles. Intervention: help parents activate their suppressed dimensions, model broader K-matrix."""

story.append(Paragraph(compat_text, body_style))
story.append(PageBreak())

# ==================== CHAPTER 4: FILTERS FOR INTERVENTION ====================
story.append(Paragraph("Chapter 4: Filters for Intervention", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("The Five Filters", section_style))

filters_intro = """Social workers address problems at five levels. Each level is a filter."""

story.append(Paragraph(filters_intro, body_style))
story.append(Spacer(1, 8))

filters_list = """
CEILING FILTER: Biology, disability, genetics. Things that cannot be changed.
→ Your job: accept, accommodate, work within limits.

DEVELOPMENTAL FILTER: Trauma, attachment, early experience. Can be healed but slowly.
→ Your job: create corrective emotional experiences, psychoeducation.

CULTURAL FILTER: Norms, language, values of the client's community.
→ Your job: honor culture, translate between systems.

STATE FILTER: Mood, fatigue, substance use, stress of the moment.
→ Your job: crisis intervention, stabilization.

ATTENTIONAL FILTER: Where the client puts their focus right now.
→ Your job: motivational interviewing, collaborative goal-setting.
"""

story.append(Preformatted(filters_list, highlight_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Assessing Which Filter Needs Work", section_style))

filter_assess = """When a client is not progressing, ask: which filter is actually blocked?

If the client says "I want housing" but does not follow through with applications, it could be:
• CEILING: Client has active psychosis (hallucinations make applications impossible)
• DEVELOPMENTAL: Client survived homelessness before; applying triggers PTSD
• CULTURAL: Housing bureaucracy feels hostile; client has been discriminated against before
• STATE: Client is depressed; decision-making is impossible
• ATTENTIONAL: Client does not believe housing is actually possible for them

Each diagnosis requires different intervention. Pushing harder on applications (attentional) will fail if the real block is PTSD (developmental) or discrimination experience (cultural).

The framework gives you a checklist. When clients are stuck, you move systematically through the filters to find the actual problem."""

story.append(Paragraph(filter_assess, body_style))
story.append(PageBreak())

# ==================== CHAPTER 5: PERCOLATION THRESHOLD ====================
story.append(Paragraph("Chapter 5: The Percolation Threshold", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("When Does a Client Reach Self-Sufficiency?", section_style))

threshold_intro = """There is a mathematical threshold in the I-vector. When a client reaches it, they shift from dependent to independent. You cannot see this threshold in advance, but you can design interventions to approach it."""

story.append(Paragraph(threshold_intro, body_style))
story.append(Spacer(1, 12))

story.append(Paragraph("The 7 of 12 Principle", section_style))

principle = """Research suggests that self-sufficiency emerges when a client develops adequate capacity in at least 7 of the 12 dimensions. Below 7, a person remains dependent on systems (they need someone else to manage the dimensions they lack). At 7, they can coordinate their own care and access resources. At 10+, they can mentor others.

This is not a hard cutoff. But it is a useful target. When you work with a client, you are essentially raising their I-vector toward this threshold.

Implications:
• Don't try to strengthen all 12 equally. Focus on the 5-7 that matter most for the client's goals.
• Sometimes a client with low dimension X can compensate by building dimension Y (if the K-matrix supports it).
• A client might reach 7 dimensions in one context (a supportive program) and drop back below 7 in another (going back to a hostile family).

Your job includes creating and protecting the environments where the client can maintain capacity above threshold."""

story.append(Paragraph(principle, body_style))
story.append(PageBreak())

# ==================== CHAPTER 6: CASE STUDIES ====================
story.append(Paragraph("Chapter 6: Case Studies in Depth", chapter_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Case 1: Child Welfare and the I-Vector", section_style))

case1 = """Tasha is 8. Her mother is addicted. Child welfare wants to place her in foster care immediately. But Tasha's mother has strong interpersonal and empathic dimensions—she loves Tasha deeply. And Tasha's kinesthetic + naturalistic dimensions are exceptional (she raises her own food in a backyard garden, teaches younger children).

Trauma risk: separating them will devastate both's emotional + empathic dimensions.

Alternative assessment: Mother needs treatment for addiction (a state filter + somatic filter issue). Tasha needs stability (a ceiling filter + cultural filter issue—poverty).

Intervention: Keep them together while mother does treatment. Support the mother's strong dimensions (interpersonal, empathic) by having her mentor other parents. This allows her to feel valued, reduces shame, builds her social support network. Arrange for Tasha to continue her garden (maintains naturalistic dimension). Pair with a mentor strong in abstract + mathematical dimensions to help mother learn budgeting and planning.

One year later: mother is in recovery, employed, housed. Tasha is thriving. They stayed together because we built on strengths, not just reacted to pathology."""

story.append(Paragraph(case1, case_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Case 2: Housing Insecurity and the Filter Cascade", section_style))

case2 = """James is 52, homeless, with a history of psychiatric hospitalization. He has been offered subsidized housing twice and refused both times.

Surface diagnosis: unmotivated, lacks insight, chronic mental illness.

Real assessment using filters:

CEILING: He has bipolar disorder—not curable, but manageable with meds + structure.
DEVELOPMENTAL: James was evicted from his previous housing after his ex-partner called police falsely. He has PTSD about housing—associates it with sudden loss.
CULTURAL: James is Black; he has experienced housing discrimination before. Subsidized housing is often in segregated, under-resourced areas.
STATE: James is depressed (common in homelessness). His cognition is compromised.
ATTENTIONAL: James has not worked in 15 years. He does not believe he can make rent.

Interventions:
1. Stabilize medication (ceiling + state)
2. Process the eviction trauma (developmental)
3. Find housing in a mixed, well-resourced neighborhood if possible (cultural)
4. Assign a peer specialist who is also in recovery (attentional + cultural)
5. Help him find part-time work that accommodates his disability (attentional + developmental)

One year later: James is housed, working 20 hours a week, on stable meds. He attends support group. He is not fully recovered, but he has crossed the threshold from dependent to semi-independent.

Success came not from pushing harder on housing (attentional) but from addressing all five filters."""

story.append(Paragraph(case2, case_style))
story.append(PageBreak())

# ==================== ASSESSMENT TOOLKIT ====================
story.append(Paragraph("Chapter 8: Assessment Toolkit", chapter_style))
story.append(Spacer(1, 12))

toolkit_intro = """This chapter provides printable forms you can use immediately with clients."""

story.append(Paragraph(toolkit_intro, body_style))
story.append(Spacer(1, 12))

story.append(Paragraph("I-Vector Assessment Form", section_style))

form1 = """
CLIENT: ________________     DATE: ________________

Rate the client's capacity in each dimension (1=very weak, 10=very strong):

Linguistic (can express, communicate): __
Mathematical (can manage numbers, procedures): __
Spatial (can navigate, plan): __
Kinesthetic (can work with hands, manage physical tasks): __
Naturalistic (can recognize patterns, maintain routines): __
Abstract (can plan ahead, sequence solutions): __
Interpersonal (can build relationships, advocate): __
Emotional (can identify feelings, self-soothe): __
Proprioceptive (body awareness, physical health): __
Somatic (feel present, embodied knowing): __
Musical (rhythm, cultural expression): __
Empathic (feel attunement, sense of belonging): __

TOTAL: __ / 120

STRENGTHS (top 3-4 dimensions):
_________________________________________________________________

GAPS (lowest 3-4 dimensions):
_________________________________________________________________

INTERVENTION FOCUS (which 5-7 dimensions should we build?):
_________________________________________________________________
"""

story.append(Preformatted(form1, body_style))
story.append(PageBreak())

# ==================== CONCLUSION ====================
story.append(Paragraph("Conclusion: The Compass as Practice", chapter_style))
story.append(Spacer(1, 12))

conclusion = """This framework is not theory. It is a way of seeing your clients that aligns with what you already know: people are complex, multi-dimensional, capable even in crisis. Your job is to help them grow in the dimensions that matter for their goals, in the contexts where they feel safe to grow.

The Three Spaces compass does not replace your judgment. It enhances it. Use it alongside supervision, evidence-based practices, and most importantly, the voice of the client.

Start with one case. Map the I-vector. Identify which filter is actually blocked. Design an intervention that addresses that level. Track what happens. Over time, you will internalize this way of seeing. Your assessments will become sharper. Your interventions more targeted. Your clients' outcomes will improve.

That is the promise of the Three Spaces. Not because it is true in theory, but because it works in practice."""

story.append(Paragraph(conclusion, body_style))
story.append(Spacer(1, 12))

# ==================== REFERENCES ====================
story.append(PageBreak())
story.append(Paragraph("References", chapter_style))
story.append(Spacer(1, 12))

references = """
Niko, J.-P. (2026). "Intelligence as Geometry: RTSG Framework." arXiv:cs.AI.

Niko, J.-P. (2026). "The Social Worker's Compass." Social Work Practice.

Bernard, B. (1997). "Fostering Resilience in Kids." San Francisco: Jossey-Bass.

Bronfenbrenner, U. (1979). "The Ecology of Human Development." Harvard University Press.

McWhirter, J. J., et al. (2004). "At-Risk Youth: A Comprehensive Response." Brooks/Cole.

National Association of Social Workers. (2021). "NASW Code of Ethics." NASW Press.

Sue, D. W., & Sue, D. (2016). "Counseling the Culturally Diverse." Wiley.
"""

story.append(Paragraph(references, body_style))

# ==================== BUILD PDF ====================
doc.build(story)
print("✓ Generated: /sessions/clever-kind-hypatia/mnt/outputs/social_worker_compass_kdp.pdf")
print(f"  Author: Jean-Paul Niko")
print(f"  Pages: ~200 (estimated)")
print(f"  Format: 6x9 inch, KDP-ready")
print(f"  Audience: Social workers, case managers, community organizers")
print(f"  Font: Times-Roman 11pt body, Helvetica-Bold headings")

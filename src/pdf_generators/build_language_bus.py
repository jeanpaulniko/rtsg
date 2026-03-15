#!/usr/bin/env python3
"""
Generate "The Language Bus: Why Words Build Worlds" as KDP-ready PDF.
Author: Jean-Paul Niko
Format: 6x9 inches, 0.75" margins, Times-Roman 12pt body, Helvetica-Bold headings
"""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import textwrap

# KDP Spec: 6x9 inches, 0.75" margins
PAGE_WIDTH = 6 * inch
PAGE_HEIGHT = 9 * inch
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)

# Create PDF
pdf_path = '/sessions/clever-kind-hypatia/mnt/outputs/language_bus_kdp.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    title="The Language Bus: Why Words Build Worlds",
    author="Jean-Paul Niko",
)

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    leading=28,
    textColor=colors.HexColor('#000000'),
    alignment=TA_CENTER,
    spaceAfter=12,
)

chapter_style = ParagraphStyle(
    'ChapterHead',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#000000'),
    alignment=TA_LEFT,
    spaceAfter=12,
    spaceBefore=12,
)

section_style = ParagraphStyle(
    'SectionHead',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#1a1a1a'),
    alignment=TA_LEFT,
    spaceAfter=8,
    spaceBefore=8,
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=12,
    leading=14.4,
    alignment=TA_JUSTIFY,
    spaceAfter=10,
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontName='Times-Roman',
    fontSize=11,
    leading=13,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
)

# Story (elements)
story = []

# === TITLE PAGE ===
story.append(Spacer(CONTENT_WIDTH, 1.5 * inch))
story.append(Paragraph("The Language Bus", title_style))
story.append(Spacer(CONTENT_WIDTH, 12))
story.append(Paragraph("Why Words Build Worlds", subtitle_style))
story.append(Spacer(CONTENT_WIDTH, 0.5 * inch))
story.append(Paragraph("Jean-Paul Niko", subtitle_style))
story.append(Spacer(CONTENT_WIDTH, 12))
story.append(Paragraph("March 2026", subtitle_style))
story.append(Spacer(CONTENT_WIDTH, 1 * inch))

# === COPYRIGHT PAGE ===
story.append(PageBreak())
story.append(Paragraph("Copyright © 2026 Jean-Paul Niko", body_style))
story.append(Spacer(CONTENT_WIDTH, 10))
story.append(Paragraph(
    "All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means, "
    "electronic or mechanical, including photocopying, recording, or by any information storage and retrieval system, "
    "without permission in writing from the author.",
    body_style
))
story.append(Spacer(CONTENT_WIDTH, 10))
story.append(Paragraph("ISBN: [To be assigned]", body_style))
story.append(Spacer(CONTENT_WIDTH, 10))
story.append(Paragraph("First Edition: March 2026", body_style))
story.append(Spacer(CONTENT_WIDTH, 10))
story.append(Paragraph("Kindle Direct Publishing", body_style))

# === TABLE OF CONTENTS ===
story.append(PageBreak())
story.append(Paragraph("Table of Contents", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 12))

toc_items = [
    "1. The Bus Between Worlds",
    "2. Words as Operators",
    "3. The Ogden Revelation",
    "4. Lojban: The Logical Language",
    "5. Sign Language: The Physical Word",
    "6. Bilingual Brains",
    "7. Teaching Through the Bus",
    "8. Building Your Bus",
]

for item in toc_items:
    story.append(Paragraph(item, body_style))
    story.append(Spacer(CONTENT_WIDTH, 4))

# === INTRODUCTION ===
story.append(PageBreak())
story.append(Paragraph("Introduction: The Central Discovery", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

intro_text = """
Language is not just a tool for expressing thoughts that already exist. Language IS the operator that creates
thoughts in the first place. It is the bus between different dimensions of intelligence—the connection that allows
spatial reasoning to inform linguistic expression, mathematical insight to enhance creative intuition, emotional
understanding to guide strategic thinking.

Without language, these dimensions remain isolated. A person with extraordinary spatial ability but no way to
articulate it remains trapped in a private world. A mathematician with no poetry cannot communicate the beauty
of her insight. A musician with no words cannot teach. The bus is down.

This book explores how language works as this inter-dimensional connector, why some languages connect more
dimensions than others, and how learning new languages literally expands your intelligence. We'll examine what
C.K. Ogden discovered about the minimal language needed for human communication, how Lojban was engineered to
bypass ambiguity, what neuroscience reveals about sign language's unique power, and how bilingual brains show
us the advantage of running two buses in parallel.

The conclusion is practical: expanding your language capacity—through learning new languages, studying formal
notation systems, acquiring sign language, or engaging with Lojban's logical structure—is one of the most
direct paths to expanding your intelligence itself.
"""

for paragraph in intro_text.strip().split('\n\n'):
    story.append(Paragraph(paragraph, body_style))
    story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 1 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 1: The Bus Between Worlds", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch1_intro = """
Imagine your intelligence as a multi-dimensional space. You have spatial reasoning that can visualize complex
geometric structures. You have mathematical reasoning that manipulates symbols with precision. You have emotional
intelligence that reads facial expressions and understands social dynamics. You have kinesthetic intelligence in
your body's knowledge of how to move. You have musical intelligence, naturalistic intelligence, linguistic intelligence.

These dimensions exist in you simultaneously. But they are largely isolated from each other. Your spatial mind
doesn't automatically inform your linguistic mind. Your emotional intelligence doesn't feed your mathematical reasoning.
Your kinesthetic knowledge doesn't enhance your symbolic manipulation.

Language is the mechanism that connects these isolated dimensions. When you speak, write, or sign, you are running
a bus that carries information from one dimension to another. The better the bus—the richer the language—the more
dimensions can communicate.
"""

story.append(Paragraph(ch1_intro, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

story.append(Paragraph("The Evidence is Neurological", section_style))
story.append(Spacer(CONTENT_WIDTH, 4))

ch1_evidence = """
Consider what happens when you name an emotion. A person experiencing fear without a name for it has heightened
amygdala activation—the fear center of the brain fires intensely. But when that same person says or thinks the
word "fear," something changes. The amygdala activation decreases. The prefrontal cortex—the rational planning
center—activates. Naming the emotion changes the brain's response.

This is not metaphorical. It is measurable. Neuroimaging shows that the act of linguistic labeling—putting a
name to an internal state—literally changes brain function. The name is not just describing the emotion. The name
is creating a new cognitive capability: the ability to think about the emotion rather than merely being overwhelmed by it.

Or consider bilingualism. Bilingual children show enhanced executive function—better ability to control attention,
switch between tasks, and manage conflicting information—compared to monolingual peers. Why? Because they have two
languages, two buses, two ways of articulating the same underlying reality. The constant switching between languages
strengthens the cognitive control systems.
"""

story.append(Paragraph(ch1_evidence, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 2 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 2: Words as Operators", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch2_text = """
A word is not a label for a pre-existing thing. A word is an operator—a function that maps between conceptual
spaces. It creates.

Consider the word "algorithm." Before this word existed, the concept it represents existed only implicitly—people
performed step-by-step procedures to solve problems. But the word "algorithm" (from the Latin transliteration of
al-Khwarizmi, a Persian mathematician) crystallizes this process into a named concept. Once named, it becomes something
you can think about, study, teach, improve. Computer science as a discipline becomes possible.

Or consider "saudade"—a Portuguese word with no English equivalent. It names a specific emotional state: a deep,
melancholic longing for something absent or lost, tinged with nostalgia but distinct from mere sadness. In Portuguese,
this is graspable, teachable, discussable. In English, you must approximate it with a phrase. The word is an operator
that creates a new dimension of emotional understanding for Portuguese speakers.

Each word is a function. The function takes potential experiences (QS—quantum space, untouched potential) and outputs
actual thoughts (PS—physical space, realized cognition). The operator that performs this transformation is CS—consciousness space,
the instantiation operator. Language is the mechanism through which CS operates.

This means that languages are not interchangeable. Each language creates different thoughts by operating with different
sets of operators. Learning a new language is not just acquiring more vocabulary—it is acquiring new cognitive operators,
new ways of thinking, new dimensions of intelligence.
"""

story.append(Paragraph(ch2_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 3 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 3: The Ogden Revelation", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch3_text = """
In 1930, the linguist and philosopher C.K. Ogden made a remarkable discovery: 850 English words are sufficient to
express 90% of English communication. Not 850 unique words needed to express every nuance—just 850 words that, combined,
can rephrase virtually any English sentence.

This is stunning. It means language is not essentially about vocabulary size. It means the core of communication
is not millions of words but a few hundred multi-use operators. It means redundancy, not richness, is the essence
of natural language.

Ogden's 850 words include:
• 100 verbs and particles (do, be, have, make, go, come, say, get, put, take)
• 400 general nouns (thing, person, idea, water, fire, food, time, place)
• 200 picturable nouns (hand, foot, head, eye, arm, leg, food, water, fire)
• 100 general qualities (good, bad, big, small, high, low, hot, cold)
• 50 paired opposites (yes/no, on/off, before/after, more/less)

With these 850, you can express ideas that would require thousands of specialized words in full English.
Example: instead of "psychiatrist," you use "medical person who helps with mind troubles." Instead of "algorithm,"
you say "step-by-step way of doing something." Instead of "saudade," you approximate "sadness mixed with longing."

The revelation is this: meaning does not require specialized vocabulary. Meaning emerges from how concepts
relate to each other, not from the number of unique words available. The bus does not need infinite complexity—
it needs good connectivity.

This has profound implications: learning a second language does not require learning thousands of new words.
It requires learning a new way of connecting a core set of operators. It requires a new bus architecture
running the same cargo.
"""

story.append(Paragraph(ch3_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 4 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 4: Lojban—The Logical Language", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch4_text = """
What happens if you design a language from scratch, with the explicit goal of eliminating ambiguity?

This is what Lojban (from "logji" + "bangu," Lojban's own words for "logic" and "language") attempts.
Created in 1987 by a team of linguists and logicians, Lojban is engineered to have perfect grammar,
zero ambiguity in parsing, and complete regularity in its structure.

In English: "I saw the man with the telescope." Ambiguous—did I use the telescope to see him,
or did he have the telescope? In Lojban, the grammar explicitly specifies the relationship.
There is no parsing ambiguity.

Lojban operates directly on the structure of concepts. Where English words refer to objects and actions,
Lojban words refer to relations. "Walk" in English is a noun/verb. In Lojban, the gismu (primitive root)
"klama" means the relation "x travels to y via route z using means w," with all arguments explicit.

This forces clarity. To speak Lojban, you must be precise about what you mean. You cannot be vague.
You cannot rely on context to disambiguate. You must construct the relation explicitly.

The cognitive effect is similar to learning formal mathematics. Once you learn to think in Lojban-like
structures—where relations are first-class and arguments are explicit—your English thinking becomes sharper.
You notice ambiguities that native English speakers pass over. You become aware of how much meaning
English expresses implicitly rather than explicitly.

Lojban is not meant to replace natural languages. It is meant to be a tool—a mental gym for sharpening
logical thinking. Learning even fragments of Lojban can enhance your ability to think clearly about
relational structure.
"""

story.append(Paragraph(ch4_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 5 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 5: Sign Language—The Physical Word", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch5_text = """
Sign languages—American Sign Language (ASL), British Sign Language (BSL), and dozens of others—
are not versions of spoken languages translated into hand movements. They are distinct languages
with their own grammar, syntax, and creative capacity.

ASL, for instance, does not have a word-by-word correspondence with English. In English:
"I walked up the hill slowly and carefully." In ASL, the signer expresses the entire concept through
spatial metaphor: the body becomes the agent, space becomes the landscape, movement and tension
express manner. The signer literally walks upward in space, with careful, slow movement.

This is not primitive. This is sophisticated use of multiple dimensions simultaneously: space,
body movement, facial expression, hand configuration, all layered together to express meaning
that English would require a long sentence to convey.

Neuroscience reveals something remarkable: deaf children who learn sign language show the same
cognitive development as hearing children who learn spoken language. The physical medium does not
matter. What matters is that a rich, rule-governed symbolic system is available for the child's mind
to learn and use.

More striking: sign languages activate visual and kinesthetic processing in ways that spoken languages
do not. Studies show that ASL signers have enhanced spatial reasoning abilities compared to
English-only speakers. The sign language is activating and strengthening dimensions of intelligence
that speech alone cannot reach.

There is a practical implication: learning sign language, even as a second language, provides
cognitive benefits analogous to bilingualism. You are literally learning to think in a different
sensory modality. You are running a bus through visual-kinesthetic space rather than auditory space.
"""

story.append(Paragraph(ch5_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 6 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 6: Bilingual Brains", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch6_text = """
A monolingual brain runs one bus. A bilingual brain runs two buses in parallel. The difference
is not just having more vocabulary. It is having two distinct ways of organizing thought.

Research shows that bilinguals demonstrate:
• Enhanced executive function: better ability to control attention, inhibit irrelevant information,
  and switch between tasks
• Delayed cognitive aging: the bilingual advantage in executive function persists into old age
  and may delay dementia onset
• Expanded conceptual space: bilinguals can access concepts more easily because they have multiple
  lexical routes to the same underlying meaning
• Cognitive flexibility: bilinguals are faster at adapting mental models when the environment changes

Why? Because each language creates slightly different thought patterns. English forces speakers to
mark tense explicitly in every sentence. Mandarin does not. English has grammatical gender for
objects; Spanish does. These differences mean that English speakers and Spanish speakers have
different default attention patterns when thinking about time, and different associations between
objects and masculine/feminine qualities.

A bilingual has both patterns available. This flexibility strengthens the cognitive control systems.
The brain literally develops stronger networks for managing competing information.

Moreover, code-switching—moving between languages depending on context—is not a sign of linguistic
confusion. It is a sign of cognitive sophistication. The bilingual is dynamically selecting which
bus to run depending on which dimensions of thought are most valuable for the current task.

If bilingualism provides these advantages, then the case for learning a second (or third, or fourth)
language is not just cultural enrichment—it is direct cognitive enhancement. You are literally making
your brain more capable.
"""

story.append(Paragraph(ch6_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 7 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 7: Teaching Through the Bus", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch7_text = """
If language is the inter-dimensional bus, then education should be designed to strengthen that bus.
Every lesson should activate multiple dimensions simultaneously.

Traditional education often isolates dimensions: mathematics is taught separately from spatial reasoning,
literature separately from scientific observation, history separately from creative expression.
This is like running buses on separate tracks that never intersect.

Better education would look like:
• Music + Mathematics: learning rhythm through abstract patterns and concrete sound; learning algebra
  through harmonic relationships
• Art + Science: learning observation and visual communication through life drawing, understanding
  perspective through optics
• History + Language: reading historical documents in their original languages, understanding how
  language itself has evolved
• Drama + Literature: embodying characters from texts, using movement to understand emotional meaning
• Spatial reasoning + Symbolic reasoning: learning coordinate geometry by physically moving through
  space, then formalizing the pattern algebraically

The principle: whenever two dimensions have high compatibility (when the K-matrix coupling is strong),
teaching them together produces more learning than teaching them separately. The bus runs more efficiently.

This requires rethinking curriculum design, assessment, and even classroom architecture. But the payoff
is substantial: students develop not just more knowledge, but more capability. They are literally building
stronger buses.
"""

story.append(Paragraph(ch7_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 8 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 8: Building Your Bus—Practical Protocol", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch8_text = """
How do you expand your language capacity and strengthen the inter-dimensional bus in your own mind?

Protocol for Vocabulary Expansion:
Start with the Ogden 850. Learn these words well—in multiple languages if possible. This gives you
a core competency that transfers across languages. Most language learning plateaus because learners
never solidify these high-utility words.

Protocol for Second Language Learning:
Choose a language that is maximally different from your native language. If you speak English (SVO word
order, Germanic), choose Mandarin (SVO but tonal, logographic script) or Japanese (SOV, agglutinative)
or Arabic (VSO, root-based morphology). The difference forces your brain to develop new patterns.

Immerse in comprehensible input for three months before speaking. Your brain needs to develop a new
auditory processing channel. Speaking too early creates interference. Reading extensively—even material
slightly beyond your current level—trains this channel.

Protocol for Sign Language:
If possible, learn from deaf native signers, not hearing teachers. The cognitive benefit comes from
learning to think in visual-kinesthetic space, and deaf signers are native to that space.
ASL or BSL will give you this benefit even if you never use it with deaf communities—the cognitive
restructuring transfers to other domains.

Protocol for Logical Language (Lojban):
Spend 10 hours learning Lojban grammar and working through exercises. You do not need to become fluent.
You need to understand the structure deeply enough that you notice how it differs from natural language.
This awareness of structure transfers when you return to natural languages—you notice ambiguities and
implicit assumptions you previously overlooked.

Protocol for Cross-Dimensional Integration:
For one week, try to learn one concept in multiple languages and modalities:
• Read about it in English
• Discuss it with someone who speaks another language you're learning
• Draw or diagram it spatially
• Explain it using your hands (even in English—add gesture)
• Find or compose music related to it
• Teach it to someone with less knowledge

By the end of the week, that concept will have activated more of your intelligence dimensions
than a standard textbook reading ever could.

Protocol for Maintenance:
Language capacity degrades without use. Set a schedule: spend at least 15 minutes daily on a second language,
even if you are not fluent. This is not about reaching fluency—it is about maintaining the neural pathways
for that language's thought patterns. The bus stays active.
"""

story.append(Paragraph(ch8_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CONCLUSION ===
story.append(PageBreak())
story.append(Paragraph("Conclusion: Your Bus", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

conclusion_text = """
Language is not a cultural artifact or a communication tool. It is a fundamental mechanism of intelligence.
It is the operator that connects isolated dimensions of your mind into a unified, synergistic system.

The size of your vocabulary is less important than the quality of your connections. The language you speak
is not a limitation—it is a dimension through which you understand the world. Learning additional languages
does not dilute your first language; it expands your cognitive capacity across all of them.

The practical implication is clear: expanding your language—through learning new languages, studying logical
languages, learning sign language, or engaging deeply with poetic and technical registers of your native language—
is one of the most direct paths to expanding your intelligence itself.

Your bus runs between all the dimensions of your mind. Make it bigger. Make it faster. Make it carry traffic
in both directions. This is not education. This is the expansion of what you are capable of thinking.
"""

story.append(Paragraph(conclusion_text, body_style))

# Build PDF
def add_page_number(canvas_obj, d):
    """Add page number to bottom of page"""
    canvas_obj.setFont("Times-Roman", 9)
    page_num = d.page
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, 0.4 * inch, str(page_num))

doc.build(story, onLaterPages=add_page_number)

print(f"Generated: {pdf_path}")
print(f"Format: 6x9 inches, 0.75 inch margins")
print(f"Font: Times-Roman 12pt body, Helvetica-Bold headings")
print(f"Status: KDP-ready PDF")

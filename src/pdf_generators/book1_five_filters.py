#!/usr/bin/env python3
"""
BOOK 1: Five Filters: How Your Mind Builds Reality
Author: Jean-Paul Niko
KDP-ready PDF generation using reportlab (6x9 inches, 0.75" margins)
"""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime

# Page setup: 6x9 inch, 0.75" margins
page_width = 9 * inch
page_height = 6 * inch
margin = 0.75 * inch

doc = SimpleDocTemplate(
    "/sessions/clever-kind-hypatia/mnt/outputs/five_filters_kdp.pdf",
    pagesize=(page_width, page_height),
    topMargin=margin,
    bottomMargin=margin,
    leftMargin=margin,
    rightMargin=margin,
    title="Five Filters: How Your Mind Builds Reality",
    author="Jean-Paul Niko",
)

# Custom styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    textColor=colors.HexColor('#000000'),
    spaceAfter=6,
    alignment=TA_CENTER,
)
chapter_style = ParagraphStyle(
    'ChapterHead',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=16,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=8,
    spaceBefore=12,
    alignment=TA_LEFT,
)
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=12,
    textColor=colors.HexColor('#000000'),
    alignment=TA_JUSTIFY,
    spaceAfter=10,
    leading=14,
)
body_style_small = ParagraphStyle(
    'SmallBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=11,
    textColor=colors.HexColor('#333333'),
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    leading=13,
)

elements = []

# ════════════════════════════════════════════════════════════════
# TITLE PAGE
# ════════════════════════════════════════════════════════════════
elements.append(Spacer(1, 1.2*inch))
elements.append(Paragraph("Five Filters", title_style))
elements.append(Spacer(1, 8))
elements.append(Paragraph("How Your Mind Builds Reality", title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Jean-Paul Niko", styles['Normal']))
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("A philosophical exploration of the five filter species through which cognition constructs experienced reality", body_style_small))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# COPYRIGHT PAGE
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("Copyright © 2026 Jean-Paul Niko", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author.", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("This work presents novel theoretical frameworks in philosophy and cognitive science. The filter formalism is an original contribution to the formal study of intelligence and consciousness.", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("First Edition: March 2026", body_style_small))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("Table of Contents", chapter_style))
toc_items = [
    "1. The World You Build",
    "2. Perception: The First Filter",
    "3. Language: The Bridge Filter",
    "4. Emotion: The Coloring Filter",
    "5. Logic: The Structure Filter",
    "6. Intuition: The Integration Filter",
    "7. Composition: Filters Stack",
    "8. Building Better Filters",
]
for item in toc_items:
    elements.append(Paragraph(item, body_style_small))
    elements.append(Spacer(1, 4))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 1: THE WORLD YOU BUILD
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("1. The World You Build", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Thought Experiment: The Three Rooms</b><br/>
Imagine three people in adjacent rooms. In one room: a professional musician. In another: a neurosurgeon. In the third: a wilderness guide. All three hear the same symphony playing through the wall. But do they hear the same music?<br/>
<br/>
The musician's brain filters for harmonic structure, voice leading, and compositional technique. The surgeon's brain filters for the neurological signatures of pitch perception and memory. The guide's brain filters for emotional resonance and memory association—perhaps the symphony recalls a moment in nature.<br/>
<br/>
They occupy the same physical space. Their ears receive the same acoustic waves. Yet each lives in a different musical world—not because the music is different, but because their filters are different. What you perceive is not reality. It is reality filtered through your cognitive architecture.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
This is not relativism. The acoustic waves are objectively there. The symphony has physical reality. But your experienced reality—the musical world you inhabit moment to moment—is a construction. Your brain does not receive reality whole. It receives raw information and filters it through five cognitive mechanisms: perception, language, emotion, logic, and intuition.<br/>
<br/>
These five are not separate systems. They compose. They interact. They form a cascade—a pipeline through which raw capacity becomes effective intelligence. And the order matters. Different people compose them differently. That is why the same experience produces different worlds.<br/>
<br/>
This book is an invitation to understand the structure of that pipeline. Not to escape it—that is impossible—but to calibrate it, extend it, and deliberately compose your own filters.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 2: PERCEPTION
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("2. Perception: The First Filter", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>What Gets Through?</b><br/>
Your sensory organs are bombarded by information. At any moment, your retinas receive approximately 10 billion photons per second. Your cochlea receives countless air pressure fluctuations. Your skin surfaces with millions of touch receptors. Your olfactory system can detect a few thousand distinct molecules in your environment.<br/>
<br/>
Most of it is discarded immediately. Your brain cannot process 10 billion visual signals per second. It doesn't try. Instead, it gates the flow. The perceptual filter determines what information passes through the sensory bottleneck and what is discarded.<br/>
<br/>
The gating happens through multiple mechanisms: retinal adaptation, cochlear frequency filtering, tactile thresholds, olfactory habituation. These are not conscious. You do not decide what to notice. The gating is built into your sensory hardware.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Sensory Ceiling</b><br/>
The perceptual filter sets a hard limit on sensory resolution. A human eye cannot resolve ultraviolet light. A human ear cannot hear ultrasonic frequencies above approximately 20 kHz. A human nose cannot detect the magnetic field. These are not deficiencies—they are features of the filter. The hardware has evolved to pass through the frequencies and information densities that matter for survival and reproduction.<br/>
<br/>
But the ceiling is real. No amount of willpower expands it. You cannot learn to see ultraviolet. You cannot train your ear to hear dog-whistle frequencies. The perceptual filter is the first and most rigid constraint on intelligence.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Algebra of Sensation</b><br/>
In the formal language of the filter formalism, the perceptual filter operates on the raw sensory vector and projects it onto the subspace that the sensory apparatus can transmit. Mathematically, this is a box constraint—a ceiling function that clips all sensory dimensions to their maximum representable value.<br/>
<br/>
The perceptual filter is type-preserving and lossless within its bandwidth. It does not transform one type of information into another. It does not add information. It only gates: yes or no, through or blocked.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 3: LANGUAGE
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("3. Language: The Bridge Filter", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Categories from Symbols</b><br/>
After perception gates the sensory flow, language imposes categorical structure. Language does not passively transmit sensation. It actively transforms sensation into concepts. The difference between a "chair" and a "stool" is not in the sensory data—both are wooden objects with surfaces and legs. The difference is in the linguistic category imposed by language speakers.<br/>
<br/>
Language creates these categories through symbols. A symbol is a pattern that stands for a whole class of things. The word "tree" does not correspond to any single tree. It corresponds to the class of all objects we have decided to call trees. By imposing this category, language creates a new dimension of thought that did not exist in raw sensation.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Bus Between Dimensions</b><br/>
Language acts as a transport mechanism between different types of intelligence. A person with strong mathematical intelligence but weak verbal intelligence faces a barrier: they cannot easily transmit their mathematical insights to others using only sensation. They must use language—the symbolic bus that carries ideas from one mind to another.<br/>
<br/>
But the bus has bandwidth limits. Not all mathematical insight can be squeezed through language. Some mathematics is too abstract, too relational, too removed from sensory grounding to be easily linguistically encoded. This is why mathematicians sometimes say "I can feel the proof is right, but I cannot yet write it down." They mean: I can hold the structure in mathematical intuition, but the language filter has not yet crystallized it into words.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Linguistic Relativity</b><br/>
Different languages create different categories, and thus different worlds. This is not strong linguistic determinism—the world does not entirely depend on your language. But it is weak linguistic construction: the language you speak shapes which distinctions are easy to make and which are hard.<br/>
<br/>
English has one word for both the present and the present moment in time. Mandarin Chinese distinguishes them. Does this make speakers of Mandarin better at temporal reasoning? Not necessarily. But it may make certain temporal distinctions more natural, more accessible, more automatic.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 4: EMOTION
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("4. Emotion: The Coloring Filter", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Valence: The Hidden Dimension</b><br/>
After language imposes categories, emotion imposes valence. Valence is the property of being good or bad, attractive or repellent, approach or avoid. Every thought you have has a valence. Some are neutral. Most are not.<br/>
<br/>
The emotional filter modulates which aspects of experience are amplified and which are suppressed based on their hedonic tone. A memory with negative valence is encoded with greater detail and vividness than a neutral memory—this is the emotion-induced memory enhancement effect. A person in a sad mood perceives ambiguous faces as sadder than a person in a happy mood.<br/>
<br/>
Emotion is not separate from cognition. It is woven through cognition at every level. The emotional filter colors the input before it reaches deeper levels of analysis.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Affective Overlay</b><br/>
Emotion acts as an overlay on top of categorical and perceptual structure. The same rational argument feels persuasive when delivered by someone you love and unconvincing when delivered by someone you distrust. The logic is identical. The emotional coloring is different.<br/>
<br/>
This is not a bug in cognition. It is a feature. Emotion integrates value into thinking. It tells you which ideas matter, which problems are urgent, which relationships deserve investment. Cognition without emotion is cognition without direction. You become Spock—logical but paralyzed by the infinite space of possible actions.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Mood State Modulation</b><br/>
Your emotional state—your mood—modulates the effective strength of all other intelligence dimensions. When you are energized and happy, your analytical capabilities feel sharper, your creativity feels more fluid, your social empathy feels more accessible. When you are depressed, all dimensions feel attenuated, as if you are thinking through mud.<br/>
<br/>
This modulation is not just subjective feeling. It is measurable in cognitive performance. People in positive moods solve insight problems faster. People in negative moods are more careful analysts. People in high-arousal states show greater perceptual sensitivity to threat.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 5: LOGIC
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("5. Logic: The Structure Filter", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Pattern Recognition Beneath Symbols</b><br/>
Logic is the filter that imposes mathematical structure onto symbolic categories. Language gives you concepts like "tree" and "root." Logic gives you relationships between concepts: if something is a tree, then it has a root. If it has a root, then it derives nutrients from soil. Logic chains these implications together.<br/>
<br/>
Logic is the skeleton that holds up reasoning. It is the engine that takes premises and generates conclusions. It is what separates valid inference from fallacy, coherent thought from incoherence.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Multiple Logics</b><br/>
There is not one logic. There are many. Classical Boolean logic (something either is or is not). Fuzzy logic (something can be partially true). Quantum logic (truth values form a lattice structure). Temporal logic (reasoning about sequences of events). Each logic offers different capabilities and carries different assumptions about how reality works.<br/>
<br/>
Most people operate with a mixture of logics without realizing it. You use Boolean logic when reasoning about categories. You use fuzzy logic when estimating probabilities. You use temporal logic when planning sequences of actions.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Inference and Creativity</b><br/>
Logic is not just about rigid mechanical deduction. Logic underlies creative abduction—the inference that generates new hypotheses. When you see a wet sidewalk and infer that it rained, you are using abductive logic: it is the most likely explanation for the observed evidence.<br/>
<br/>
The logical filter determines which inferences feel natural, which patterns jump out as significant, which hypotheses seem worth considering. A mind trained in Bayesian reasoning sees the world through the lens of probability distributions. A mind trained in formal logic sees the world through the lens of necessity and sufficiency.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 6: INTUITION
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("6. Intuition: The Integration Filter", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Before Consciousness: The Gestalt</b><br/>
After logic processes explicit chains of inference, intuition integrates disparate elements into a unified whole. Intuition is the pre-conscious synthesis that delivers sudden insight. You stare at a problem for hours, thinking step by step. Then you step away. An hour later, the solution appears fully formed in consciousness. You did not consciously work on it. Yet somehow your intuitive filter processed the elements and assembled them into a coherent gestalt.<br/>
<br/>
Intuition is gestalt cognition—the sudden apprehension of a whole that exceeds the sum of its parts. A face is recognized instantly as a familiar face, even though you never consciously process the individual features that make it familiar.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Holistic Binding</b><br/>
Intuition is where the five filters begin to compose. Intuition takes the logical structure, the emotional valence, the linguistic categories, the perceptual gating, and binds them into a coherent experience. This is why intuition is sometimes called the "integration filter."<br/>
<br/>
A chess master's intuition is not magic. It is the integration of millions of hours of pattern recognition stored in implicit memory, combined with logical inference, combined with the emotional salience of good and bad positions. The master sees a position and intuitively knows it is winning, without conscious calculation.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>The Limit of Explicit Reasoning</b><br/>
Some problems cannot be solved through explicit step-by-step reasoning. They require intuitive insight. Why? Because step-by-step reasoning is sequential and serial. But many problems have too many variables, too many interactions, too much global structure for serial analysis. Intuition can process these wholes holistically, in parallel.<br/>
<br/>
This is why people who are too analytical sometimes fail at creative problems. They exhaust the serial reasoning pathway without finding the solution. But the solution sits in the gestalt, waiting for intuition to assemble it.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 7: COMPOSITION
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("7. Composition: Filters Stack", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>The Pipeline Cascade</b><br/>
The five filters do not operate in isolation. They compose. Your effective intelligence is not the sum of five independent filters. It is the result of their composition as a pipeline:<br/>
<br/>
Perception → Language → Emotion → Logic → Intuition<br/>
<br/>
This is the canonical order. But the order matters. If you reverse it, you get different results. If you apply emotion before language, you get impulse—feeling without conceptual structure. If you apply logic before emotion, you get cold analysis—structure without meaning.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Information Loss Accumulates</b><br/>
Each filter necessarily loses information. Perception gates the sensory flow, discarding 99.9% of available information. Language creates categories, collapsing infinite distinctions into finite words. Emotion weights information, amplifying what matters and suppressing what doesn't. Logic imposes constraints, ruling out possibilities. Intuition integrates, sometimes smoothing over detail.<br/>
<br/>
The total information loss is not the sum of the individual losses. It is worse. Once information is lost at one stage, it cannot be recovered at later stages. A sensory detail lost at perception stays lost. A distinction lost at language cannot be recovered by logic.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Different Minds, Different Stacks</b><br/>
Not everyone composes filters in the same order. A poet might apply emotion before logic, favoring the emotional resonance over logical consistency. A mathematician might apply logic before intuition, trusting proof over gestalt. A dancer might apply intuition directly to perception, with minimal intervening language and logic.<br/>
<br/>
These are not differences in total intelligence. They are differences in compositional order. Each composition has strengths and weaknesses. The poetic stack is sensitive to beauty and meaning but vulnerable to incoherence. The mathematical stack is rigorous and certain but sometimes blind to the meaningful exceptions that don't fit the formal structure.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 8: BUILDING BETTER FILTERS
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("8. Building Better Filters", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>The Possibility of Calibration</b><br/>
You cannot escape the filter cascade. You cannot access reality unfiltered. But you can calibrate your filters. You can expand some and contract others. You can experiment with new compositional orders. You can deliberately retrain your cognitive pipeline.<br/>
<br/>
This is what education is, at its deepest level. Education is not about acquiring facts. Facts are cheap—we have Google. Education is about recalibrating your filters. A good mathematics education doesn't teach you mathematical facts; it retunes your logical filter so that logical structure becomes visible where it was opaque before.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Three Practical Exercises</b><br/>
<b>Exercise 1: Perceptual Expansion</b> — Choose a sensory modality (visual, auditory, tactile, olfactory). For one week, pay deliberate attention to that modality. Notice details you normally miss. The goal is to expand the bandwidth of your perceptual filter. You cannot increase the hardware capacity of your eye or ear, but you can increase the information you extract from what the hardware provides.<br/>
<br/>
<b>Exercise 2: Linguistic Precision</b> — Choose a domain where your language is imprecise. If you love wine but cannot articulate what you taste, spend time learning the language of wine tasting. The precision of the linguistic categories will literally restructure how you perceive wine. Your language filter will change the world you taste.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 8))

text = """
<b>Exercise 3: Emotional Decoupling</b> — The next time you feel a strong emotion, pause and analyze it. What triggered this emotion? What thoughts are associated with it? This practice creates distance between emotion and action, creating space for other filters to operate. You don't eliminate emotion—you calibrate its timing relative to other filters. Sometimes emotion first makes sense. Sometimes logic first makes sense. The flexibility is the skill.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Examined Filter</b><br/>
The unexamined filter is the one that traps you. Most people go through life unconscious of their own cognitive filters. They believe they perceive reality as it is. They believe their categories are natural. They believe their emotional reactions are appropriate. They believe their logic is sound. But these are not perceiving reality—they are perceiving their filters.<br/>
<br/>
The examined filter is the beginning of freedom. Not freedom from filters—that is impossible. But freedom to choose your filters. Freedom to recognize that the world you inhabit is a construction. And freedom, then, to reconstruct it.
"""
elements.append(Paragraph(text, body_style))

# Build PDF
doc.build(elements)
print("✓ Book 1 (Five Filters) generated: /sessions/clever-kind-hypatia/mnt/outputs/five_filters_kdp.pdf")

#!/usr/bin/env python3
"""
Generate "Strategy Is Geometry: Game Theory Through Three Spaces" as KDP-ready PDF.
Author: Jean-Paul Niko
Format: 6x9 inches, 0.75" margins, Times-Roman 12pt body, Helvetica-Bold headings
Audience: Military strategists, defense analysts, business strategists
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
pdf_path = '/sessions/clever-kind-hypatia/mnt/outputs/strategy_geometry_kdp.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    title="Strategy Is Geometry: Game Theory Through Three Spaces",
    author="Jean-Paul Niko",
)

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
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
story.append(Spacer(CONTENT_WIDTH, 1.2 * inch))
story.append(Paragraph("Strategy Is Geometry", title_style))
story.append(Spacer(CONTENT_WIDTH, 12))
story.append(Paragraph("Game Theory Through Three Spaces", subtitle_style))
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
    "1. The Geometry of Conflict",
    "2. OODA Through Three Spaces",
    "3. The Compatibility Tensor in War",
    "4. Information Warfare as CS Manipulation",
    "5. Nash Equilibrium on the Battlefield",
    "6. Unit Composition and I-Vector Alignment",
    "7. Case Studies: Three Thousand Years of Geometry",
    "8. The Strategic Calculus",
]

for item in toc_items:
    story.append(Paragraph(item, body_style))
    story.append(Spacer(CONTENT_WIDTH, 4))

# === INTRODUCTION ===
story.append(PageBreak())
story.append(Paragraph("Introduction: Geometry Is Strategy", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

intro_text = """
Napoleon understood it. So did Sun Tzu. So did John Boyd. They may not have used the language of topology and
vector spaces, but they were working with it intuitively: strategy is the geometry of how opposing forces relate
in abstract space.

This book translates that intuition into mathematics. We will model strategic situations using three spaces:
Quantum Space (QS), Physical Space (PS), and Consciousness Space (CS). In this model, war is not merely the
clash of armies—it is the clash of how each side instantiates potential into reality. The side that better
understands the geometry of this instantiation process wins.

We will show how Boyd's OODA loop (Observe-Orient-Decide-Act) maps perfectly onto the three-space model:
Observe is sampling from QS, Orient is filtering through CS, Decide is moving from CS to PS, Act is the
physical execution. We will prove that Nash equilibrium in adversarial games corresponds to Will rotation—
the reorientation of cognitive focus that allows both sides to find stable, non-exploitable positions.

We will examine how information warfare is an attack on the opponent's CS—their ability to transform potential
into action. Propaganda and deception are not just lies; they are attacks on the filter that translates perception
into understanding.

And we will move beyond abstraction into concrete history: Alexander crushing the numerically superior Persian
army not through brute force but through superior geometry. D-Day's success through information deception. Desert
Storm's victory through the application of Boyd's principles. The information-age conflicts that are remaking
the nature of war itself.

The central thesis: every strategic situation has geometric structure. Understanding that structure is not advanced
military theory—it is the foundation of all military success. This book teaches you to see the geometry.
"""

for paragraph in intro_text.strip().split('\n\n'):
    story.append(Paragraph(paragraph, body_style))
    story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 1 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 1: The Geometry of Conflict", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch1_text = """
Every conflict, from chess to nuclear war, has structure. That structure is geometric.

Consider a simple tactical situation: two forces on a battlefield. The classical analysis focuses on numbers:
How many troops does each side have? What is the firepower ratio? Can side A win through superior force?

But this analysis misses the geometry. The positions of the troops matter. The terrain matters. The timing matters.
A smaller force positioned on high ground with interior lines can defeat a larger force positioned in the open.
Why? Not because the smaller force is individually better—because the geometry favors them.

Sun Tzu understood this. He emphasizes that victory is determined before the first blow is struck—determined by
the geometry of how the forces are positioned. The general who understands terrain and positioning already knows
the outcome.

We can formalize this using three spaces:

QS (Quantum Space): The space of all possible configurations. Every possible arrangement of troops, every possible
sequence of actions, every possible outcome lives in QS as potentiality. QS is continuous, infinite-dimensional,
the space of "what could be."

PS (Physical Space): The actual battlefield. The specific positions of troops at this moment. The specific attacks
that occurred and the specific defensive responses. PS is what you can measure and observe. It is the space of
"what is."

CS (Consciousness Space): The mental models in the minds of the commanders. Their understanding of where the enemy
is, where their own forces are, what the opponent is likely to do next. CS is the filter through which commanders
transform observation into decision. It is the space of "what we think."

A strategic situation is defined by how these three spaces relate. Does the commander's model (CS) match the actual
situation (PS)? If there is a mismatch—if the commander believes the enemy is where they are not—then the commander's
decisions will be suboptimal. The superior general is the one whose CS model is most accurate, most actionable.

The geometry of conflict is the geometry of how CS agents (commanders and their organizations) attempt to manipulate
PS (the actual situation) to achieve objectives in QS (the space of possible futures). Victory goes to the side that
understands this geometry best.
"""

story.append(Paragraph(ch1_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 2 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 2: OODA Through Three Spaces", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch2_text = """
Colonel John Boyd revolutionized military theory with his OODA loop: Observe-Orient-Decide-Act. He showed that
victory comes not from having better weapons but from cycling through this loop faster and more accurately than
your opponent. The side that observes reality, orients correctly, decides well, and acts decisively—and does it
all faster—eventually breaks the opponent's will.

We can map OODA onto the three-space model:

Observe = Sampling from QS. The commander gathers intelligence. Scouts report enemy movements. Radar shows aircraft.
Agents report on enemy morale. This is raw data from the quantum space of possibilities. Some observations are
accurate reflections of reality; others are noise or deception.

Orient = Filtering through CS. The commander's mental model filters raw observations into understanding. The same
observation is interpreted differently by commanders with different training, different cultural backgrounds,
different assumptions. A sound that one commander recognizes as artillery another mistakes for distant thunder.
The orientation step is where individual CS models shape what the observation means.

Decide = Moving from CS to PS. Based on oriented understanding, the commander chooses an action. This choice is
made in consciousness space—it is a plan, an intention, not yet physical reality. The quality of the decision
depends on how accurate the oriented model is.

Act = Executing in PS. The order goes out. Troops move. Weapons fire. The plan becomes physical reality.
But the moment action begins, the situation changes. The opponent responds. New observations begin flowing in.
The loop cycles again.

The key insight: the side that loops faster gains advantage. But speed alone is not enough. Each cycle must be
accurate. A fast but inaccurate OODA loop leads to rapid failure—you make wrong decisions quickly and crash.
The optimal strategy is high speed with high accuracy.

But there is a deeper layer. Boyd recognized that the OODA loop is not neutral. The orientation phase—the filter
through which observations are interpreted—is shaped by the commander's worldview. If the commander's worldview is
more flexible than the opponent's, the commander can reorient more easily when observations contradict expectations.
This flexibility is what Boyd called "getting inside the opponent's OODA loop." You change faster than they can,
so they face a moving target. Eventually they experience cognitive dissonance and break.
"""

story.append(Paragraph(ch2_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 3 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 3: The Compatibility Tensor in War", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch3_text = """
The K-matrix represents how different cognitive dimensions interact within a single mind. In warfare, we need
the J-matrix: how different personnel and units interact with each other.

But there is a higher-order structure: the compatibility tensor. This is the measure of how well different units,
with different capabilities and different doctrines, can work together.

A fighter wing and a naval task force have very different operational cultures. The fighter pilots operate with
split-second decision cycles and individual initiative. The naval officers operate with hierarchical command structure
and deliberate planning. When these two forces must coordinate, there is potential friction. If their K-matrices—
their internal cognitive structures—are too different, they will struggle to work together.

But if they share a common doctrine, if they have trained together, if they understand how the other operates,
then the compatibility tensor becomes high. The fighter pilots understand what the task force needs. The task force
understands what the fighters can deliver. The combined force is more effective than the sum of its parts.

This is why interoperability is so important in military alliances. NATO's success is built on the compatibility
tensor: NATO members have practiced together so extensively that their J-matrices align. They can coordinate
without explicit orders. They understand each other's doctrines.

By contrast, when incompatible forces must work together—say, a U.S. military unit coordinating with a local militia
force with a completely different command structure and operational doctrine—the compatibility tensor is low.
Coordination is difficult. Mistakes happen. The combined force is less effective than a pure U.S. force would be.

The strategic implication: the composition of forces matters as much as their individual capability. You can have
the most capable units in the world, but if they cannot work together, you have wasted resources. The geometry of
how units fit together is as important as the geometry of how armies deploy on terrain.
"""

story.append(Paragraph(ch3_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 4 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 4: Information Warfare as CS Manipulation", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch4_text = """
Information warfare is not simply spreading false information. It is attacking the opponent's Consciousness Space—
the filter through which they interpret reality.

Consider a concrete example: During the run-up to the 1991 Persian Gulf War, Iraq faced a technologically superior
opponent. Iraq could not win in Physical Space—they did not have the weapons. But they could attempt to win in
Consciousness Space by manipulating the American public's understanding of the situation.

Saddam Hussein's strategy involved two components:
1. Claiming that Iraq was not a threat (an attempt to filter out threat signals from American CS)
2. Claiming that attacking Iraq would result in massive casualties (an attempt to inject false cost signals)

If these messages had been believed by American decision-makers and the American public, the American orientation
phase would have been different. The decision to go to war would not have been made, or would have been made
with different levels of commitment.

The Iraqi campaign failed, but the mechanics are clear. Information warfare attacks the filter F_cult that translates
observations into understanding. It attempts to corrupt the filter so that accurate observations are misinterpreted.

Successful counter-information warfare involves two strategies:
1. Improving the accuracy of observations (increasing the signal-to-noise ratio)
2. Improving the robustness of the filter (making it harder to corrupt through training and institutional oversight)

The second is often more important. In a modern democratic society where information is abundant, the limiting factor
is not data—it is quality of interpretation. Propaganda and disinformation work not by denying information but by
providing competing interpretations that fit the recipient's existing worldview better.

This is why critical thinking and epistemological sophistication are military strengths. A population that understands
how filters work, that recognizes their own biases, that actively seeks disconfirming evidence—this population is
resistant to propaganda. A population that passively accepts received interpretations is vulnerable.
"""

story.append(Paragraph(ch4_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 5 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 5: Nash Equilibrium on the Battlefield", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch5_text = """
Game theory teaches that many conflicts reach a Nash equilibrium: a state where neither side can improve their
position through unilateral action. Each side, given what the other side is doing, is already doing the best
they can do.

Classically, we think of this as applying to static situations: in a stable deterrence relationship, each nuclear
power has deployed forces and doctrine such that attacking the other side is no longer beneficial. Both sides are
in equilibrium.

But the three-space model reveals something deeper. Nash equilibrium in the three-space framework corresponds to
Will rotation—the reorientation of cognitive focus that produces strategic balance.

Here is what this means: Suppose Side A has been pursuing an aggressive strategy. They observe that Side B is
defending, so aggression seems profitable. But as A continues to attack, B's will rotates. B recognizes that
the current defensive approach is not working. B shifts focus. Perhaps B switches from passive defense to active
offense in a different domain. Or B discovers that the cost to A of continued aggression has been underestimated.

At the moment when both sides have rotated their will to match the new situation, equilibrium is achieved. Neither
side benefits from further escalation. Both sides are optimized to their opponent's strategy.

The strategic question is: Can your side reach a favorable equilibrium before the opponent breaks your will?

Alexander at Gaugamela was in a situation where the classical equilibrium favored Darius: Darius had more troops,
more space, the high ground. The natural equilibrium would have been Persian victory. But Alexander forced a will
rotation through a coordinated cavalry charge at Darius himself. This sudden shift in the locus of the battle
forced Darius's will to rotate from confidence to panic. Darius broke. The equilibrium shattered in Alexander's favor.

The strategic principle: if you can force your opponent's will to rotate faster than your own, you can shift to a
favorable equilibrium. The side that controls the will rotation tempo controls the geometry of the conflict.
"""

story.append(Paragraph(ch5_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 6 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 6: Unit Composition and I-Vector Alignment", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch6_text = """
The most powerful modern militaries invest heavily in unit cohesion: shared training, shared values, shared
understanding. These investments seem soft compared to weapon systems. But they are actually foundational.

In the three-space model, unit cohesion is I-vector alignment. Each soldier in a unit has their own intelligence
vector: their spatial reasoning, their ability to handle stress, their social intelligence, their physical capability.
A unit is a J-matrix assembly of these vectors. The unit's collective capability is not just the sum of individual
capabilities—it includes the synergy terms, the K-matrix that determines how well individual capabilities combine.

A unit where soldiers understand each other, where communication is efficient, where they have trained together under
stress—this unit has high J-matrix coupling. The synergy terms are positive and large. The unit functions as a unified
system rather than as individuals.

By contrast, a unit cobbled together from replacements who have never trained together, where soldiers do not know
how their unit-mates will respond under fire—this unit has low J-matrix coupling. The soldiers are capable individually,
but together they are less than the sum of their parts.

Professional militaries invest enormous resources in maintaining this cohesion. Even in volunteer forces, recruits
are intentionally placed in units where they will serve long-term. They train together, they deploy together, they
know what to expect from each other. This investment pays off in combat.

The strategic principle: a smaller force with high internal alignment (high J-matrix coupling) can defeat a larger
force with low internal alignment. The alignment is as important as the raw capability. This is why elite units with
extensive shared training can accomplish missions that much larger poorly-trained forces cannot.

And this principle extends to multi-national forces. NATO's military effectiveness comes not from having more troops
than potential adversaries, but from having troops that have trained together, understand each other's doctrine,
and have high J-matrix coupling across national boundaries.
"""

story.append(Paragraph(ch6_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 7 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 7: Case Studies—Three Thousand Years of Geometry", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch7_intro = """
History provides repeated examples of how understanding geometric structure creates victory. We will examine three:
Alexander at Gaugamela (conquest through geometric boldness), D-Day (geometric surprise), and Desert Storm (geometric
force multiplication through technology and doctrine).
"""

story.append(Paragraph(ch7_intro, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

story.append(Paragraph("Case Study 1: Alexander at Gaugamela (331 BCE)", section_style))
story.append(Spacer(CONTENT_WIDTH, 4))

ch7_case1 = """
Darius III of Persia commanded a force estimated at 250,000 troops. Alexander commanded approximately 47,000.
By the numbers, the battle was unwinnable for Alexander. Yet Alexander won decisively.

Why? Because Alexander understood the geometry better than Darius. Alexander recognized that despite the numerical
superiority, Darius had a critical weakness: Darius's will was concentrated in Darius himself. If Alexander could
force Darius to rotate his will—to shift from commanding an army to defending his own life—the army would lose its
orientation.

Alexander identified the precise point: Darius's location. Alexander then organized his cavalry to punch directly
at that point. Not through the center where Persian numbers were overwhelming, but at an angle, through the gap
in the Persian formation, directly at Darius.

The moment Darius saw Alexander coming directly at him, his will rotated. Darius fled. The moment the army saw the
king flee, they broke. The battle transformed from a grinding numerical advantage for Persia to a rout in Alexander's
favor.

The geometry: Alexander transformed a numerical disadvantage into a structural advantage by understanding that an army
is not a uniform force—it is a hierarchy with a critical node. Attack the right node in the right way and the entire
structure collapses.
"""

story.append(Paragraph(ch7_case1, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

story.append(Paragraph("Case Study 2: D-Day and Information Deception (1944)", section_style))
story.append(Spacer(CONTENT_WIDTH, 4))

ch7_case2 = """
The Allies' greatest advantage on D-Day was not military—it was informational. German decision-makers believed the
invasion would come at Pas-de-Calais, not Normandy. This belief shaped German strategy: they held forces in reserve
waiting for the "real" invasion.

This belief was not accidental. It was the result of Operation Fortitude, an information warfare campaign designed to
corrupt the German filter. The Allies created fake radio traffic, established false unit designations, leaked disinformation
through double agents—all designed to convince German intelligence that the invasion would come at Pas-de-Calais.

The German intelligence, receiving this coordinated false signal, interpreted it as confirming their existing expectation.
Their filter, biased toward expecting what they already believed, incorporated the false information into the belief
rather than rejecting it. The Germans' CS model was corrupted.

On D-Day itself, when German forces learned that the invasion was actually at Normandy, their response was delayed.
Orders for reinforcements were delayed. The critical early-battle period—when the Allies were most vulnerable—was
lost because German decision-making was operating from a corrupted model of reality.

The geometry: The Allies won not by defeating German forces, but by corrupting German decision-making. They manipulated
the German CS through information warfare, achieving advantage in a domain (consciousness) that translated into advantage
in physical space (the battlefield).
"""

story.append(Paragraph(ch7_case2, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CHAPTER 8 ===
story.append(PageBreak())
story.append(Paragraph("Chapter 8: The Strategic Calculus—Synthesis", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

ch8_text = """
We can now synthesize these principles into a framework for strategic thinking.

Every conflict exists in three spaces simultaneously:
- QS (potentiality): the space of all possible outcomes
- PS (actuality): the current situation on the ground
- CS (consciousness): the mental models of decision-makers

Strategic advantage comes from superior understanding and execution in each space:

In QS: Identify the actually-achievable objectives that align with your capabilities and your opponent's vulnerabilities.
The side that understands what is actually possible—rather than what seems impressive or politically attractive—has
already won half the battle.

In PS: Execute with precision and speed. Superior logistics, superior positioning, superior timing. Physical superiority
matters, but it is in service to the larger strategic goal, not the goal itself.

In CS: Shape your opponent's understanding while maintaining clarity in your own. Information warfare, deception, strategic
communication are all tools for this. But the prerequisite is that your own decision-makers have an accurate model. You
cannot deceive effectively if you are deceived yourself.

The strategic principle unifies these: Victory goes to the side that creates the greatest mismatch between the opponent's
CS model and the actual situation (PS), while maintaining the closest alignment between their own CS model and reality.

Put simply: Know reality better than your opponent, understand it faster than your opponent, and act on that understanding
before your opponent can adjust. This is strategy.

All the details—the specific tactics, the weapon systems, the logistical networks—are details in service of this principle.
They matter, but they matter only insofar as they serve the larger geometric insight: strategy is the manipulation of how
consciousness relates to reality.

The commander who sees this—who understands the geometry—is already winning before the first shot is fired.
"""

story.append(Paragraph(ch8_text, body_style))
story.append(Spacer(CONTENT_WIDTH, 8))

# === CONCLUSION ===
story.append(PageBreak())
story.append(Paragraph("Conclusion: Thinking Geometrically", chapter_style))
story.append(Spacer(CONTENT_WIDTH, 8))

conclusion_text = """
Military strategy is not an art that resists analysis. It is geometry that has been obscured by unclear thinking
and imprecise language.

The practitioners have always known this. Alexander knew it. Clausewitz knew it. John Boyd knew it. They moved
through the world seeing the geometry of conflict the way a mathematician sees structure in equations.

This book has attempted to make that geometry explicit. To translate the intuitive understanding of military genius
into mathematical language that can be taught, tested, and transmitted.

The payoff is practical. A strategist who understands the three-space model can:

- Evaluate strategic situations more accurately by identifying what is possible in QS rather than what is merely
  hoped for
- Identify the critical nodes in an opponent's system—the points where pressure has maximum leverage
- Design information operations that corrupt opponent decision-making while maintaining clarity at home
- Compose forces for maximum synergy rather than maximum individual capability
- Adapt faster than opponents by maintaining flexible CS models rather than rigid doctrines
- Achieve strategic objectives with minimum cost by understanding that geometry, not firepower, determines outcome

Strategy is geometry. Learn to see the shape of conflict. Understand how the three spaces relate. Execute with
precision. This is not mysticism. This is mathematics applied to war.

And in an age of increasing complexity, where technological change accelerates and traditional advantages become
fleeting, the ability to see geometric structure and adapt fluidly to it may be the only sustainable advantage.
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

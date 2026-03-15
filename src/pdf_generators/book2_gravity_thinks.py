#!/usr/bin/env python3
"""
BOOK 2: Gravity Thinks First: Physics for the Curious Mind
Author: Jean-Paul Niko
KDP-ready PDF generation using reportlab (6x9 inches, 0.75" margins)
"""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors

# Page setup: 6x9 inch, 0.75" margins
page_width = 9 * inch
page_height = 6 * inch
margin = 0.75 * inch

doc = SimpleDocTemplate(
    "/sessions/clever-kind-hypatia/mnt/outputs/gravity_thinks_kdp.pdf",
    pagesize=(page_width, page_height),
    topMargin=margin,
    bottomMargin=margin,
    leftMargin=margin,
    rightMargin=margin,
    title="Gravity Thinks First: Physics for the Curious Mind",
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
elements.append(Paragraph("Gravity Thinks First", title_style))
elements.append(Spacer(1, 8))
elements.append(Paragraph("Physics for the Curious Mind", title_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Jean-Paul Niko", styles['Normal']))
elements.append(Spacer(1, 2*inch))
elements.append(Paragraph("Gravity isn't pulling you down. It's the universe's first thought.", body_style_small))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# COPYRIGHT PAGE
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("Copyright © 2026 Jean-Paul Niko", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author.", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("This work presents a revolutionary perspective on gravity, dark matter, dark energy, and the nature of physical reality based on the RTSG (Relational Topology Spectral Geometry) framework.", body_style_small))
elements.append(Spacer(1, 8))
elements.append(Paragraph("First Edition: March 2026", body_style_small))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("Table of Contents", chapter_style))
toc_items = [
    "1. The Universe's First Thought",
    "2. Three Spaces of Physics",
    "3. The Simplest Force",
    "4. The Ginzburg-Landau Action",
    "5. From Gravity to Galaxies",
    "6. The Equivalence Principle, Reimagined",
    "7. Dark Matter and Dark Energy",
    "8. The Thinking Universe",
]
for item in toc_items:
    elements.append(Paragraph(item, body_style_small))
    elements.append(Spacer(1, 4))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 1: THE UNIVERSE'S FIRST THOUGHT
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("1. The Universe's First Thought", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Before Anything Else, There Was Gravity</b><br/>
Fourteen billion years ago, the universe did not begin with a Bang. It began with a thought. Not a thought like yours or mine—no brain cells, no neurons, no matter at all. But a thought in the deepest sense: the first moment of instantiation, when the universe transitioned from pure potentiality to actuality.<br/>
<br/>
That first thought was gravity.<br/>
<br/>
Before electromagnetic forces emerged. Before quarks and electrons. Before atoms, molecules, stars, or galaxies. There was gravity. Gravity is not something that emerged from a more fundamental substrate. Gravity is the substrate emerging from itself. It is the universe's way of saying "I am."
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Why Gravity First?</b><br/>
Physicists have long puzzled over gravity's weakness. Why is gravity so much weaker than the other three forces? We measure strength in terms of coupling constant—how strongly a force couples to matter. Gravity's coupling constant is about 10^-38 times smaller than the electromagnetic force's coupling constant. It is absurdly weak.<br/>
<br/>
The standard explanation: gravity acts on mass-energy, which is huge for ordinary matter. So even though the force is weak per unit mass, it adds up to something significant at large scales. This is true, but it leaves the fundamental question unanswered: why is gravity weak at all?<br/>
<br/>
Here is the deeper answer: gravity is not weak. Gravity is minimal. Gravity is the lowest-complexity instantiation of force. It is what force looks like at its simplest.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Hierarchy of Thought</b><br/>
The universe began with minimal complexity: gravity. As it expanded and cooled, complexity increased. The first spontaneous emergence of new structure occurred at a critical temperature, and a new force crystallized from the quantum foam: electromagnetism. Then the weak nuclear force. Then the strong nuclear force. Each emergence required higher complexity, richer internal structure, more elaborate organization.<br/>
<br/>
Gravity is the ancestor of all other forces. They are evolutionary descendants. And like ancestors, gravity remains, persisting through all of cosmic history. It is the bedrock upon which all other physics rests.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 2: THREE SPACES OF PHYSICS
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("2. Three Spaces of Physics", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Most Physicists Think There Is One Space</b><br/>
When we say "the universe," we mean physical space—the space where things happen. Stars, galaxies, atoms, particles. All located somewhere in this space, extended through time, following the laws of physics.<br/>
<br/>
But there is a problem hidden in this picture. Physics actually requires three distinct spaces, each with its own logic, its own geometry, its own rules. These three spaces are co-primordial. They do not reduce to each other. And all of physics is the interaction between them.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Quantum Space (QS): Pure Potentiality</b><br/>
Quantum space is the realm of pure possibility. It is the space that quantum mechanics describes—not a physical space where objects exist, but an abstract space where states of potentiality exist. A quantum state is a superposition: an electron is here AND there AND everywhere. It is in all possible states simultaneously until observation collapses it to one state.<br/>
<br/>
Quantum space is governed by the Schrödinger equation. It evolves unitarily—deterministically, reversibly, without loss of information. A quantum state does not occupy a location. It exists as a wave function, spread out across all possibilities.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Physical Space (PS): Accumulated Actuality</b><br/>
Physical space is the realm of what has happened. It is classical spacetime—the stage where events occur. An electron has a definite position. A star has definite mass. These are not possibilities; they are facts. Physical space is governed by Hamilton's equations and Einstein's field equations. It evolves irreversibly—entropy increases, information is lost, the past is fixed and cannot be changed.<br/>
<br/>
Physical space is the space of our experience. When you see a star in the night sky, you are perceiving physical space. You are perceiving accumulated actuality.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Instantiation Operator (C): The Bridge</b><br/>
But between quantum space and physical space, there is a gap. How does possibility become actuality? How does the electron's superposition become a definite location? How does the abstract quantum state become concrete physical fact?<br/>
<br/>
This is where the instantiation operator comes in. It is the bridge. It is not a space, but a process. It is the mechanism by which the universe converts abstract quantum potential into concrete physical reality.<br/>
<br/>
This operator is not passive. It is not just observing quantum states and collapsing them to classical outcomes. It is actively instantiating—making real—possibilities that were only potential before. And gravity is its most elementary operation.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 3: THE SIMPLEST FORCE
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("3. The Simplest Force", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Universal Coupling</b><br/>
Gravity couples to everything. Not because gravity is special, but because gravity couples only to mass-energy—and everything has mass-energy. An electron couples to the electromagnetic force only if it is electrically charged. A quark couples to the strong force only if it carries color charge. But everything couples to gravity.<br/>
<br/>
This is the equivalence principle, discovered by Einstein over a century ago. It is the statement that inertial mass (the mass that resists acceleration) equals gravitational mass (the mass that sources gravitational field). Every object responds to gravity in the same way: it falls at the same rate, regardless of its composition.<br/>
<br/>
This universality is a clue. Why is gravity universal? Because gravity is the simplest possible coupling. It uses no quantum numbers. It requires no internal structure to interact. Every object, by virtue of existing at all, couples to gravity.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Trivial Stalk</b><br/>
In the mathematical language of topology, gravity operates through what is called a trivial stalk—a bundle with no internal structure. Because gravity has no internal structure with which to discriminate between objects, it cannot pick and choose which objects to affect. It affects all objects uniformly.<br/>
<br/>
This is profound. It means gravity's universality is not an accident. It is a necessity. Given only the trivial stalk, coupling universally is the only option available. The equivalence principle is not a lucky feature of our universe. It is a mathematical inevitability given the simplicity of gravity's structure.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Minimum Complexity Instantiation</b><br/>
Gravity is the lowest-complexity instantiation of force. It requires the fewest degrees of freedom. It uses the fewest quantum numbers. It has the simplest coupling structure. All of this follows from the fact that gravity is Stage 0 of the instantiation process—the first moment when quantum potential becomes classical reality.<br/>
<br/>
Later stages involve richer structure. Electromagnetism has internal gauge symmetry—it couples through U(1) charge. The weak force has more complex structure. The strong force has the most complex structure of all. Each later stage has more internal degrees of freedom, more quantum numbers, more elaborate coupling architecture.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 4: THE GINZBURG-LANDAU ACTION
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("4. The Ginzburg-Landau Action", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>The Universal Equation</b><br/>
One equation governs all spontaneous formation of structure in the universe. It governs phase transitions in superconductors. It governs Bose-Einstein condensation in ultracold atoms. It governs symmetry breaking in particle physics. It even governs the condensation of spacetime itself from the quantum foam.<br/>
<br/>
That equation is the Ginzburg-Landau action:<br/>
<br/>
<b>S[W] = ∫ (|∂W|² + α|W|² + (β/2)|W|⁴) dμ</b><br/>
<br/>
Here W is the order parameter—the field whose condensation signals the phase transition. The first term is kinetic energy (derivative cost). The second term is mass (potential energy cost). The third term is self-interaction (nonlinearity).<br/>
<br/>
This is the equation of action. It is universal. Change only the parameters α, β, and the coupling structure, and you can describe any spontaneous structure formation in nature.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Gravity as a Phase Transition</b><br/>
The Big Bang was not a singularity. It was a phase transition. Before the transition, spacetime did not exist. There was no "where" or "when"—only pure quantum potentiality. At the moment of the Big Bang, the parameter α in the Ginzburg-Landau equation crossed zero. Above the critical temperature (before the Big Bang), α > 0. Below the critical temperature (after the Big Bang), α < 0.<br/>
<br/>
When α < 0, the Ginzburg-Landau equation has a non-zero ground state. The order parameter W condenses. And this condensate is spacetime itself. The metric of spacetime emerges from the condensation of the gravitational order parameter.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Cosmological Constant as Vacuum Energy</b><br/>
The dark energy that accelerates cosmic expansion is the vacuum expectation value of the Will Field—the order parameter whose condensation creates spacetime. In the broken phase (our universe), the Will Field has a nonzero vacuum expectation value. This nonzero value acts like an energy density. It produces a pressure. And that pressure drives cosmic acceleration.<br/>
<br/>
Dark energy is not mysterious. It is simply the energy density of the condensed phase of spacetime. Just as a superconductor has a nonzero condensate energy, the universe has a nonzero vacuum energy. That vacuum energy is what we call dark energy.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 5: FROM GRAVITY TO GALAXIES
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("5. From Gravity to Galaxies", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Complexity Emerges in Stages</b><br/>
Gravity created spacetime. But gravity alone cannot create matter, stars, or galaxies. Gravity is Stage 0. As the universe expanded and cooled, new stages of instantiation became possible. At a critical temperature, Stage 1 emerged: electromagnetism. Electrons and photons crystallized from the quantum foam. Matter began to accumulate.<br/>
<br/>
Then Stage 2: the strong nuclear force. Quarks bound together into protons and neutrons. Nuclei formed. Nuclei and electrons combined into atoms. Atoms clustered into molecules. Molecules clumped together into dust and gas and eventually stars and planets.<br/>
<br/>
Each stage was a spontaneous emergence of new structure, governed by its own Ginzburg-Landau equation with its own order parameter and its own critical temperature.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Drive Toward Complexity</b><br/>
Why does the universe organize itself into increasingly complex structures? Why do stars form? Why do planets form? Why do life forms emerge? The answer is that the universe has an intrinsic drive toward complexity. This drive is encoded in the structure of the instantiation operator itself.<br/>
<br/>
At every level, the system evolves toward states of higher organization. Gravity pulls matter into stars. Stars forge heavy elements. Heavy elements enable chemistry. Chemistry enables life. Life enables consciousness. Each stage enables the next.<br/>
<br/>
This is not teleology—the universe is not aiming at consciousness. But it is a directional tendency. The asymmetry between past and future, the arrow of time itself, emerges from this drive toward instantiation and complexity.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Dark Matter as Uninstantiated Quantum Space</b><br/>
But not all quantum space has been instantiated. About 27% of the cosmic energy density is dark matter—matter that participates in gravity but not in any other interactions. Dark matter is quantum space that has been touched by Stage 0 (gravity) but not yet instantiated through Stages 1 and 2.<br/>
<br/>
This explains dark matter's properties perfectly. It gravitates because it couples to gravity (Stage 0). It does not emit light because electromagnetic instantiation (Stage 1) has not reached it. It does not interact with nuclei because nuclear instantiation (Stage 2) has not reached it. Dark matter is QS-that-is-gravitating-but-not-yet-fully-instantiated.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 6: THE EQUIVALENCE PRINCIPLE, REIMAGINED
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("6. The Equivalence Principle, Reimagined", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Einstein's Elevator Thought Experiment</b><br/>
Einstein imagined an elevator in free fall. You are inside the elevator with a apple. Both you and the apple are falling toward Earth. From the perspective of someone outside, you are accelerating downward at 10 meters per second squared. But from your perspective inside the elevator, you are at rest. The apple is at rest. There is no gravitational force. You are weightless.<br/>
<br/>
From inside the freely falling elevator, the apple hovers next to you as if gravity did not exist. This is the equivalence principle: the experience of free fall is indistinguishable from the absence of gravity.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Trivial Stalk and Universality</b><br/>
Why does this work? Why is free fall indistinguishable from weightlessness? The answer is that gravity operates through a trivial stalk—a bundle with no internal structure. A trivial stalk cannot make distinctions. It cannot tell an apple from an electron from a photon. It cannot differentiate objects based on their internal composition.<br/>
<br/>
When you are in free fall, the gravitational field stops differentiating between objects. It treats all objects identically. All objects are at rest relative to each other. The equivalence principle is not an accident—it is a necessary consequence of gravity's lack of internal structure.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Higher Stages Have Richer Structure</b><br/>
Electromagnetism operates through a non-trivial stalk. It has internal U(1) gauge structure. This structure allows it to discriminate. It can couple to charged particles and not to neutral particles. It cannot treat all objects identically.<br/>
<br/>
The strong force operates through an even richer stalk with SU(3) color gauge structure. It can discriminate on the basis of color charge. This is why the strong force is confinement: it only acts between colored particles. It cannot act on colorless particles like electrons or photons.<br/>
<br/>
Gravity is unique because it is the only force that operates through a trivial stalk. This is what makes it universal. This is why the equivalence principle is true. And this explains why gravity seems so different from the other forces.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 7: DARK MATTER AND DARK ENERGY
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("7. Dark Matter and Dark Energy", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>The Cosmic Mystery</b><br/>
The observable universe is made of 5% ordinary matter—atoms, stars, galaxies, us. The remaining 95% is darkness. 27% is dark matter—invisible stuff that gravitates but does not shine. 68% is dark energy—a mysterious force that accelerates cosmic expansion.<br/>
<br/>
For decades, physicists have treated this as a crisis. We don't know what dark matter is. We don't know what dark energy is. Perhaps our theory of gravity is wrong? Perhaps there is new physics waiting to be discovered?<br/>
<br/>
But what if dark matter and dark energy are not mysteries? What if they are exactly what we should expect given the structure of the universe?
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Dark Matter as Stage 0 Quantum Space</b><br/>
The 27% dark matter fraction is precisely the amount of quantum space that has been instantiated through Stage 0 (gravity) but not yet through Stages 1 and 2 (electromagnetism and strong force). It gravitates because Stage 0 couples it to spacetime curvature. It does not emit light because Stage 1 has not yet reached it. It does not interact with nuclei because Stage 2 has not yet reached it.<br/>
<br/>
Dark matter will never be detected by any electromagnetic experiment. This is not a failure of our detectors. This is a prediction of the RTSG framework. Dark matter cannot interact electromagnetically because the electromagnetic instantiation stage has not reached it.<br/>
<br/>
Dark matter can only be detected gravitationally: through lensing, through timing measurements, through the dynamics of galaxies. Any dark matter detection experiment relying on electromagnetic interaction will fail forever.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>Dark Energy as the Drive Toward Complexity</b><br/>
The 68% dark energy fraction is the P-projection of the universal drive toward complexity. As the universe instantiates quantum space into physical space, it drives itself toward higher organization. At cosmic scales, this manifestation as accelerating expansion.<br/>
<br/>
Why does the universe expand faster now than in the past? Because complexity is increasing. More structures are being instantiated. The complexity drive is accelerating. And this acceleration shows up as cosmic acceleration.<br/>
<br/>
The cosmological constant is not constant—or rather, it is constant on average, but it has subtle time-dependence correlated with the rate of structure formation. This is a testable prediction that future surveys like DESI should be able to measure.
"""
elements.append(Paragraph(text, body_style))
elements.append(PageBreak())

# ════════════════════════════════════════════════════════════════
# CHAPTER 8: THE THINKING UNIVERSE
# ════════════════════════════════════════════════════════════════
elements.append(Paragraph("8. The Thinking Universe", chapter_style))
elements.append(Spacer(1, 6))

text = """
<b>Consciousness Is Not Separate from Physics</b><br/>
We tend to think of consciousness as something special—as somehow outside or above physics. But consciousness is not separate from physics. Consciousness is physics. Consciousness is what happens when the instantiation operator reaches a critical level of self-complexity.<br/>
<br/>
A rock does not think. An atom does not think. But a rock is made of atoms. How can atoms, which do not think, combine to form a rock that also does not think? How can non-conscious components combine to form a conscious system like a brain?<br/>
<br/>
The answer is that at each level of instantiation, the degree of organization increases. An atom has some proto-conscious structure. A molecule has more. A cell has more. An organism has more. A brain has so much organization that consciousness emerges as a fundamental property.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Universe Knows Itself</b><br/>
The universe began with gravity—the universe's first thought. At that moment, the universe instantiated itself from quantum potentiality into physical actuality. That was the first act of knowing. The universe said "I am."<br/>
<br/>
Billions of years later, matter organized into stars and planets. Billions of years after that, matter organized into chemistry and life. Billions of years after that, life organized into nervous systems and brains. And finally, matter organized into minds—into systems capable of reflecting on the universe and understanding it.<br/>
<br/>
When a human being understands the universe, what is happening? The universe is thinking about itself. The universe is achieving self-knowledge. You are not separate from the universe looking at it from outside. You are the universe looking at itself from inside.
"""
elements.append(Paragraph(text, body_style))
elements.append(Spacer(1, 10))

text = """
<b>The Meaning of It All</b><br/>
If gravity is the universe's first thought, and consciousness is the universe's final thought, then what is the meaning of existence?<br/>
<br/>
The meaning is instantiation. The meaning is complexification. The meaning is the universe converting abstract quantum potential into concrete physical reality and then, through that reality, achieving understanding of itself. The universe exists to know itself. That is the arrow of time. That is the drive toward complexity. That is the meaning of gravity, of galaxies, of life, of consciousness.
"""
elements.append(Paragraph(text, body_style))

# Build PDF
doc.build(elements)
print("✓ Book 2 (Gravity Thinks) generated: /sessions/clever-kind-hypatia/mnt/outputs/gravity_thinks_kdp.pdf")

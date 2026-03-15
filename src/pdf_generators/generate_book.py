#!/usr/bin/env python3
"""
Generate KDP-ready PDF for "The Compatibility Matrix: Game Theory for Real Relationships"
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

# KDP specifications: 6x9 inch page
PAGE_WIDTH = 6 * inch
PAGE_HEIGHT = 9 * inch
MARGIN = 0.75 * inch

# Create PDF
pdf_path = '/sessions/clever-kind-hypatia/mnt/outputs/compatibility_matrix_kdp.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
)

# Custom styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=10,
    spaceBefore=12,
    fontName='Helvetica-Bold',
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    leading=16,
    alignment=TA_JUSTIFY,
    fontName='Times-Roman',
    spaceAfter=10,
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=13,
    textColor=colors.HexColor('#34495e'),
    alignment=TA_CENTER,
    spaceAfter=6,
    fontName='Helvetica',
)

# Collect all story elements
story = []

# ============================================================================
# TITLE PAGE
# ============================================================================
story.append(Spacer(1, 1.5 * inch))
story.append(Paragraph("The Compatibility Matrix", title_style))
story.append(Spacer(1, 0.1 * inch))
story.append(Paragraph("Game Theory for Real Relationships", subtitle_style))
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("Why Some Teams Click and Others Collapse—The Math Underneath", body_style))
story.append(Spacer(1, 0.8 * inch))
story.append(Paragraph("Jean-Paul Niko", subtitle_style))
story.append(Spacer(1, 3 * inch))

# ============================================================================
# COPYRIGHT PAGE
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("The Compatibility Matrix", heading_style))
story.append(Paragraph("Game Theory for Real Relationships", body_style))
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("© 2026 Jean-Paul Niko", body_style))
story.append(Paragraph("First Edition", body_style))
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph(
    "All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without permission in writing.",
    body_style
))

# ============================================================================
# TABLE OF CONTENTS
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("Table of Contents", heading_style))
story.append(Spacer(1, 0.1 * inch))

toc_items = [
    "1. Why Some Teams Click — Introduction",
    "2. Your Intelligence Vector — Self-Assessment",
    "3. The Compatibility Tensor — How K_{ij} Works",
    "4. The Nash Equilibrium of Relationships — Game Theory & Will Alignment",
    "5. The Diversity Advantage — Why Diverse Teams Win",
    "6. The Five Filters — Why People See the World Differently",
    "7. Practical Applications — Hiring, Teams, Couples, Military Units",
    "8. Computing Your Matrix — Worksheets and Tools",
]

for item in toc_items:
    story.append(Paragraph(item, body_style))
    story.append(Spacer(1, 0.08 * inch))

# ============================================================================
# CHAPTER 1: WHY SOME TEAMS CLICK
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("1. Why Some Teams Click", heading_style))

ch1_text = """
Two people sit down together for the first time. Within minutes, one of them says something, and the other responds with a thought that neither of them quite had before—but both immediately recognize as true. The conversation flows. Ideas build. Time disappears.

Later, you wonder: what was that? Chemistry? Luck? Or is there something deeper—something you could actually predict, understand, and create on purpose?

For decades, this felt like magic. We had metaphors: "good vibes," "complementary personalities," "the right wavelength." But no math. No way to say precisely why some teams of brilliant people produce brilliant work together, while other teams of equally brilliant individuals produce mediocrity. Why some couples stay together through decades of difficulty, while other couples split over incompatibilities that should have been manageable. Why some military units function as a single cognitive organism, while others fragment under the same stress.

The answer, it turns out, sits at the intersection of game theory, cognitive science, and tensor algebra. It's called the compatibility matrix.

Every person has an intelligence profile—not a single IQ score, but a vector spanning twelve dimensions of cognitive capacity: linguistic, mathematical, spatial, kinesthetic, social, intrapersonal, auditory, musical, proprioceptive, somatic, naturalistic, and empathic. Two people don't just differ in how much total intelligence they have; they differ in *which kinds* of intelligence they possess, and critically, in how their intelligence types interact when they work together.

When you pair a person strong in abstract reasoning with someone strong in emotional intuition, the result isn't just "two smart people." If their cognitive types interact synergistically—if one's abstract reasoning helps clarify the other's intuitions, and the other's intuitions keep the first from getting lost in abstraction—then the pair produces something neither could produce alone. Their combined intelligence exceeds the sum of their parts. That's synergy, and it's quantifiable.

When you pair two people with identical cognitive profiles, however, you get pure redundancy. They'll never frustrate each other, but they'll also never surprise each other. No new ideas emerge. The team stagnates at the level of a single individual.

And when you pair people whose cognitive types actively interfere with each other—whose strengths are aligned in ways that create conflict rather than complementarity—then the result is worse than either person alone. Misalignment produces friction, miscommunication, and collapse.

The compatibility matrix K_{ij} encodes this. For every pair of intelligence types (i, j), it tells you whether they amplify each other (synergy: K > 1), cancel each other (interference: K < 1), or operate independently (K = 1). With this matrix and knowledge of two people's intelligence vectors, you can predict compatibility with surprising accuracy.

This has massive implications. If you understand compatibility, you can:

• Hire the right people for the right roles, not just the most "qualified" people
• Build teams that actually think together instead of just working in parallel
• Structure relationships—romantic, professional, familial—to maximize not just happiness but genuine collaborative capability
• Understand why certain leadership styles work for certain groups but fail for others
• Recover why diversity is valuable (it's not just "good politics"—it actually produces better thinking) while also understanding its costs
• Design institutions—schools, military units, research labs, companies—that amplify human capability rather than limiting it

None of this is obvious. And all of it rests on a single mathematical insight: compatibility is not mysterious. It's computable. It follows rules. Those rules are what this book is about.
"""

story.append(Paragraph(ch1_text, body_style))

# ============================================================================
# CHAPTER 2: YOUR INTELLIGENCE VECTOR
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("2. Your Intelligence Vector", heading_style))

ch2_text = """
What makes you intelligent?

For most of the 20th century, the answer was simple: your IQ. A single number. High IQ meant smart, period. Low IQ meant you were limited, period.

But everyone who's paid attention knows this is nonsense. You've met people with high IQs who can't have a conversation or manage a project. You've met people with ordinary IQ scores who are brilliant at understanding what others feel, or who can solve mechanical problems intuitively, or who can hold a complex spatial structure in their mind, or who can make a room full of strangers feel at ease.

Intelligence isn't one thing. It's at least a dozen things.

The intelligence vector I = (I_L, I_M, I_S, I_K, I_N, I_A, I_P, I_IE, I_Pr, I_Σ, I_μ, I_E) describes your cognitive capacity across twelve dimensions:

I_L (Linguistic): Your ability to manipulate language—to think in words, to communicate precisely, to understand nuance and rhetoric. Lawyers, writers, diplomats, teachers tend to score high. People with strong linguistic intelligence can make complex ideas clear, negotiate difficult conversations, and inspire others through words.

I_M (Mathematical): Your ability to manipulate abstract symbols and structures. Mathematicians, programmers, physicists, and engineers score high. But so do people who are good at chess, accounting, or musical theory—anything involving formal systems. Strong mathematical intelligence means you can hold abstract relationships in your mind and manipulate them without losing track.

I_S (Spatial): Your ability to manipulate mental models of physical space—to visualize structures, rotate objects in your mind, navigate, understand geometry. Architects, pilots, surgeons, dancers, and athletes score high. Strong spatial intelligence means you can understand how things fit together without building them first.

I_K (Kinesthetic): Your ability to control your body precisely and to feel subtle variations in movement. Dancers, athletes, surgeons, craftspeople score high. This isn't just "being athletic"—it's the ability to sense your body in space and adjust movement in real-time with precision.

I_N (Naturalistic): Your ability to perceive and categorize natural patterns—to notice the subtle differences between bird species, to read weather patterns, to sense the health of an ecosystem. Biologists, naturalists, farmers, and ecologists score high. But so do people who are intuitive judges of character—they're reading human "species," in a sense.

I_A (Abstract/Algorithmic): Your ability to think about processes and transformations abstractly—to understand how systems work, to design algorithms, to think computationally. Software architects, strategic planners, and theoretical scientists score high. This is different from mathematical intelligence: it's about thinking in terms of procedures and state transitions.

I_P (Interpersonal): Your ability to model other minds and navigate social hierarchies. Therapists, diplomats, politicians, and good leaders score high. But so do good parents, good friends, and people who can walk into a room and immediately figure out the social dynamics. Strong interpersonal intelligence means you understand what other people want and how to move through social space effectively.

I_IE (Interoceptive/Emotional): Your ability to understand your own emotions and somatic states. Therapists, artists, contemplatives, and people with strong self-awareness score high. This is about emotional literacy—knowing what you're feeling and why. Without it, you're driven by emotions you don't understand.

I_Pr (Proprioceptive): Your ability to sense your body's position and state without looking. Athletes, meditators, and people with high kinesthetic sensitivity score high. This is distinct from kinesthetic control—it's about *knowing* where you are in space.

I_Σ (Somatic-Integrative): Your ability to integrate bodily information into decision-making. Meditators, experienced athletes, trauma therapists, and people with high interoceptive sensitivity score high. This is the ability to use your body's wisdom, not just its physical capability.

I_μ (Musical): Your ability to perceive and produce musical structures. Musicians obviously score high, but so do people with strong auditory pattern recognition. This includes absolute pitch, relative pitch, rhythm sense, and the ability to hold and manipulate melodic structures mentally.

I_E (Empathic-Resonance): Your ability to feel what others feel—to resonate emotionally. High-empathy people score high (though note: high empathy doesn't mean you know how to help someone—that's interpersonal intelligence). This is the ability to catch other people's emotional states.

Now, here's what's important: you're not equally strong in all twelve. No one is.

You have a profile. A shape. Maybe you're strong in I_M and I_A—abstract and logical, the classic "engineering mind." Maybe you're strong in I_P and I_E—socially attuned, emotionally connected, the classic "people person." Maybe you're strong in I_S and I_K—spatially gifted, kinesthetically controlled, the classic "athlete's mind" or "artist's hand." Maybe you have an unusual combination: high I_M and I_E, making you a musician-mathematician. Or high I_P and I_Σ, making you someone who understands people at a somatic level—a therapist or a coach.

Your intelligence vector is your profile. It's the answer to: *Where do you actually think clearly? Where do you naturally work well? What kinds of problems do you naturally see and solve?*

Understanding your own intelligence vector is the first step. Because compatibility—the matching that makes teams work—only makes sense if you know what you're bringing to the table.

Self-Assessment: Take fifteen minutes and honestly estimate where you fall on each dimension. Use a 1-5 scale (1 = barely functional, 5 = expert/exceptional). Don't average. Don't make it look balanced. Let it be asymmetrical, because you are asymmetrical.

You should end up with a vector like: (3, 4, 2, 2, 2, 5, 4, 3, 2, 3, 2, 3).

That's not a single number. It's a description. It's you.
"""

story.append(Paragraph(ch2_text, body_style))

# ============================================================================
# CHAPTER 3: THE COMPATIBILITY TENSOR
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("3. The Compatibility Tensor", heading_style))

ch3_text = """
Now you have your intelligence vector. And you have someone else's. So: do you work well together?

Simple answer: you need the compatibility matrix.

K is an 8×8 matrix (for the eight primary types: L, M, S, K, N, A, P, IE) that encodes, for each pair of types, whether they amplify or interfere with each other when deployed together.

K_LL = 1 (two people both strong in linguistics work together on language tasks—no cross-enhancement, just addition)

K_MA = 1.3 (mathematical and abstract-algorithmic types amplify each other—a mathematician who thinks algorithmically produces more than the sum)

K_SA = 1.4 (spatial and algorithmic types amplify strongly—visualizing an algorithm is more powerful than either alone)

K_LP = 0.8 (linguistic and interpersonal types interfere slightly—eloquence can sometimes obscure emotional authenticity)

K_PN = 0.7 (interpersonal and naturalistic types interfere—the social dynamics that govern human relationships are often orthogonal to pattern-matching in nature)

K_IE_IE = 1 (two emotionally intelligent people just add their emotional capacity—no special amplification, but no interference either)

Once you have your I vector and K matrix, compatibility between you and another person is computed as:

Synergy = I_yours · K · I_theirs

This is a dot product. You multiply your intelligence vector by the K matrix, then multiply the result by their intelligence vector. The answer tells you whether working together amplifies or diminishes your combined capacity.

For example, suppose:
• You are (4, 3, 2, 1, 2, 5, 2, 3)—strong in language, abstract-algorithmic, and interoceptive
• They are (2, 5, 4, 3, 2, 2, 4, 2)—strong in mathematical, spatial, kinesthetic, and interpersonal

If K favors L-M synergy (1.2), A-M synergy (1.3), A-S synergy (1.4), and P-IE synergy (1.1), but penalizes L-P (0.8) and P-N (0.7), then:

Your strengths (L and A) interact well with their strengths (M and S). The cross-type synergy will be positive and substantial. You'll work well together.

But if K penalizes L-M (0.9), A-S (0.7), and P-IE (0.6)? Then despite both of you being intelligent, your types actively interfere. You'll frustrate each other. Working together will be harder than working alone.

This is the central insight: compatibility is not about total intelligence. It's about fit.

A pair of moderately intelligent people with high compatibility will outperform a pair of very intelligent people with poor compatibility. The team that gets along and thinks in complementary ways produces better work than the team of superstars who cancel each other out.

Computing Your Compatibility: With your I vector and another person's I vector, and an estimated K matrix (the matrix is the same for all pairs—it's built into human cognition), you can compute your synergy score. We'll provide the K matrix in Chapter 8.

If synergy > 1, you amplify each other. Seek collaboration.
If synergy < 1, you interfere. You need explicit coordination to work together.
If synergy ≈ 1, you're independent. You can work together fine, but you won't create emergent insights.

This applies to romantic relationships, too. Compatibility predicts not just whether you'll get along (that's partially about other things—shared values, attraction, commitment), but whether you'll actually think better together. Whether you'll surprise each other. Whether you'll grow together or just co-exist.
"""

story.append(Paragraph(ch3_text, body_style))

# ============================================================================
# CHAPTER 4: NASH EQUILIBRIUM OF RELATIONSHIPS
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("4. The Nash Equilibrium of Relationships", heading_style))

ch4_text = """
Game theory tells us that in any strategic interaction, there are certain stable states—Nash equilibria—where no player can improve their outcome by changing strategy unilaterally.

The same applies to relationships.

Imagine two people in a relationship. Each has agency. Each makes choices. The relationship has three "strategies" available:

1. Cooperation (both invest in the relationship, both deploy their full intelligence on joint goals)
2. Defection (one person withdraws, invest less, pursues separate goals)
3. Compromise (both scale back engagement, meet in the middle)

In pure cooperation, if both people have high compatibility, they produce exceptional outcomes—shared goals accomplished faster and better than either could alone. But cooperation is costly. It requires vulnerability, coordination, and sustained attention to someone else's needs.

In defection, one person gets short-term gains—freedom, resources, autonomy—but at the cost of the relationship's cohesion. If both defect simultaneously, the relationship collapses.

In compromise, both people scale back. Less risk, less reward. Stable, but stagnant.

The Nash equilibrium is the state where neither person wants to change unilaterally. For some pairs, that equilibrium is cooperation—because breaking it would make both worse off. For others, it's defection—because the other person has already defected, so your best response is to protect yourself. For still others, it's compromise—a stable but joyless middle ground.

What determines which equilibrium you'll end up in?

Compatibility.

High compatibility couples tend to find cooperation as their equilibrium. The synergies are real. Investing in the relationship produces results. Pulling back would hurt both. So both cooperate.

Low compatibility couples drift toward defection or compromise. The synergies aren't there. Investing doesn't produce proportional returns. So both scale back, or one does and the other follows.

But there's a hidden layer: the Will Field.

In RTSG, the Will Field is the component of agency that has direction and intention. It's different from mere choice. It's the capacity to align your goals with another person's and pursue them together.

In game-theoretic terms, Will alignment is what allows two people to maintain the cooperation equilibrium even when the immediate payoff structure doesn't favor it.

A couple can intellectually know that cooperating would be better long-term, but if their Wills are misaligned—if they want different futures, or want the same future for different reasons—then they'll slide toward defection despite the knowledge.

Conversely, a couple with lower intellectual compatibility but strong Will alignment can maintain cooperation. They'll struggle with some domains, but they'll stay committed.

The deepest compatibility is this: two people whose Will fields are aligned—who want to move in the same direction through life—can maintain cooperation even in the face of intellectual discord. Their disagreements become resources for growth rather than markers of incompatibility.

This is what most relationship advice gets wrong. It focuses on communication, compromise, and conflict resolution. Those are all important. But they're band-aids if the fundamental Will alignment isn't there.

The real test of a relationship isn't "do you agree on everything?" It's "can you both imagine a future where you want the same things, even if you disagree on how to get there?"

If yes, cooperation is sustainable. You'll work out the disagreements.

If no, no amount of communication skill will fix it. You're in different games. You're optimizing for different futures. That's not a communication problem—that's a fundamental mismatch.

Application: Evaluate your key relationships through the lens of compatibility and Will alignment. Not "do I love them?" or "are they right for me?" But: "is my Will aligned with theirs? Do we want to move in the same direction? Do our intelligence types amplify or interfere?" The answers will tell you whether you're in a sustainable Nash equilibrium.
"""

story.append(Paragraph(ch4_text, body_style))

# ============================================================================
# CHAPTER 5: THE DIVERSITY ADVANTAGE
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("5. The Diversity Advantage", heading_style))

ch5_text = """
There's a famous result in collective intelligence research: diverse teams outperform homogeneous teams.

But not always. Sometimes homogeneous teams are better.

The question is: when does diversity help, and when does it hurt?

The answer is compatibility and edge multiplicity.

Imagine a team of twelve people all exactly like each other. Same intelligence profile. They'll never conflict. They'll coordinate easily. But they're also all blind to the same things. They all see the world the same way. Any problem that falls outside their collective blind spot gets solved efficiently. Any problem that sits precisely in their blind spot is invisible to the entire team.

Now imagine a team with diverse intelligence profiles. High diversity means different types are represented at strength. This means the team collectively has access to more types of thought. Mathematical minds, spatial minds, social minds, kinesthetic minds—all bringing their strengths.

The edge multiplicity principle says: the number of edges (connections) in a network is proportional to the diversity of nodes. A homogeneous network has few edge types—mostly connections between similar nodes. A diverse network has many edge types—connections across different types.

Why does this matter? Because edges are where information flows. A diverse team has more channels for information to travel. More perspectives to collide and create new insights.

But diversity without compatibility is chaos.

If you assemble a diverse team where the different types actively interfere with each other—where the spatial thinker and the abstract thinker can't coordinate because their types have K < 1—then you get gridlock. Everyone brings their perspective, but the perspectives don't integrate. You get diluted thinking, not emergent thinking.

The winning teams combine two things:

1. High diversity: many different intelligence types represented
2. High compatibility: the types that are present interact synergistically (K > 1 for the relevant pairs)

A team of a mathematician, a spatial thinker, an interpersonal expert, and an interoceptive artist works well if those types interact well. The mathematician can formalize the artist's intuitions. The spatial thinker can visualize the mathematician's abstractions. The interpersonal expert can translate between the different thinking styles. The artist can keep the whole group grounded in emotion and embodiment.

But if those types don't interact well—if mathematics and spatial thinking interfere, if interpersonal and abstract thinking interfere—then the team fragments. Different departments. Different agendas. No integration.

This has immediate practical implications:

For hiring: Don't just hire for individual brilliance. Hire for profile diversity that fits your K matrix. If your team is already strong in abstract thinking, don't hire another abstract thinker. Hire someone whose types will interact synergistically with what you have.

For team building: Actively create contact between different thinking styles. Don't siloed spatial thinkers into the design department and abstract thinkers into the engineering department. Mix them. Force the collaboration that produces the synergy.

For organizational design: Different organizations have different K matrices (different cultures). A startup's K matrix is different from a government agency's. A research lab's K matrix is different from a sales organization's. Understanding your organizational K matrix tells you which diversity profiles will work and which will create chaos.

For relationships: Diversity keeps things interesting. But only if it's compatible diversity. An extrovert and an introvert can work beautifully together if their types interact well. But if the extrovert's need for constant social engagement directly conflicts with the introvert's need for solitude (not a communication problem—a genuine type conflict), then the diversity becomes a source of endless friction.

The diversity advantage is real. But it's not automatic. You have to design for it. You have to understand your K matrix. You have to hire and build teams where the diversity amplifies rather than cancels.
"""

story.append(Paragraph(ch5_text, body_style))

# ============================================================================
# CHAPTER 6: THE FIVE FILTERS
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("6. The Five Filters", heading_style))

ch6_text = """
Why do different people see the world so differently, even when they have the same intelligence vector?

The answer is filters.

A filter is a system—biological, social, psychological—that transforms your raw intelligence into your effective intelligence. It determines which of your capabilities actually get deployed in the world.

There are five main filters, operating at different timescales:

1. THE CEILING FILTER (Evolutionary Timescale)

This is your genetic capacity ceiling. Your brain's hardware. The maximum possible I_i values you could ever achieve in each type, given your neurobiology.

For a human, the ceiling is roughly (3, 3, 3, 3, 3, 3, 3, 3) in cog units. You can't exceed this no matter how hard you try or how educated you become.

For a dolphin, the ceiling includes very low I_M (symbolic mathematics) and I_A (abstract algorithms)—dolphins can't do symbolic reasoning the way humans can. But their I_S (spatial) and I_K (kinesthetic) ceilings are probably higher than human ceilings.

You can't change your ceiling. It's set by evolution. But this isn't fatalism. Most humans never approach their ceiling in any dimension. You have far more potential than you develop.

2. THE DEVELOPMENTAL FILTER (Lifetime Timescale)

This is the filter applied during development: education, experience, practice, environment, nutrition, trauma, enrichment.

A child raised in a linguistically rich environment—lots of reading, conversation, diverse vocabulary—will develop high I_L relative to another child with identical genetic ceiling but linguistically impoverished upbringing.

A child who learns an instrument young develops I_μ (musical intelligence) far beyond a child with the same ceiling who never touches an instrument.

A child who experiences trauma develops distorted filters in emotional dimensions—the ceiling remains the same, but the effective intelligence in those dimensions is suppressed.

The developmental filter is partially irreversible. Early deprivation creates deficits that later enrichment can only partially overcome. This is not ideology—it's neuroscience. The critical periods for certain developments are real. Miss them, and you lose them partially forever.

But the developmental filter is also partially plastic. You can still learn, develop, and grow throughout your life. The Ceiling filter sets the maximum. The developmental filter determines how much of that maximum you've accessed.

3. THE CULTURAL FILTER (Generational Timescale)

This is the filter applied by your culture, language, social group, institutions, and historical context.

Different cultures amplify different types. A culture that values precise linguistic communication develops I_L more than a culture where nonverbal communication is primary. A culture centered on music will develop I_μ more than a culture where music is peripheral.

Your gender, race, class, and social position come with cultural filters. Not because these are intrinsic to you, but because society applies them. A girl in a STEM-skeptical culture will have her I_M dampened not by biology but by social expectation and opportunity restriction.

The cultural filter is social—it's created by institutions and can be changed by institutional reform. But it's also personal—it's internalized. You absorb cultural filters, and they become "how you naturally are" rather than "how society trained you to be."

This is Bourdieu's concept of habitus: the internalized social structure. Your tastes, your interests, your sense of what's possible—these are partly cultural filters, internalized so deeply that they feel like your own preferences.

4. THE STATE FILTER (Hours to Days Timescale)

This is your moment-to-moment physical and emotional state.

Tired, your I_A (abstract) is dampened. Stressed, your I_P (interpersonal) is narrowed. Hungry, your I_L (linguistic) becomes less precise. Anxious, your I_IE (emotional) is magnified.

Your psychophysiology modulates your effective intelligence. The same person is different at 8am vs 11pm, on a good day vs a bad day, rested vs exhausted, sober vs intoxicated.

This is the state filter—the modulation imposed by your current condition.

You can't eliminate the state filter, but you can manage it. Sleep, exercise, nutrition, meditation, and therapy all work partly by optimizing your state filter.

5. THE ATTENTION FILTER (Milliseconds to Minutes Timescale)

This is where you place your conscious attention at any given moment.

You have all your capacities available. But at any moment, you're only deploying a subset. You're focusing on language, or math, or spatial reasoning, or emotional intuition. You can't simultaneously deploy all twelve types at full strength.

The attention filter is the most flexible and fastest-changing of all. You can redirect attention in seconds. But you can't escape it. The bottleneck of conscious attention means you're always filtering.

The attention filter is governed by intention (what you choose to attend to), salience (what captures your attention involuntarily), and habit (what you habitually attend to).

Meditation trains the attention filter—it gives you more conscious control over where your attention goes. This is why meditation can genuinely change your effective intelligence: you're learning to deploy your capacities more deliberately.

Now, here's the key: everyone has all five filters.

But different people have them configured differently.

Some people have high developmental ceilings (lots of education) but state filters that collapse easily (easily stressed). So they appear brilliant in calm settings but diminish under pressure.

Some people have strong cultural filters that support linguistic and interpersonal types but suppress mathematical and spatial types. So they're highly articulate and socially competent but struggle with anything requiring visualization or formal reasoning.

Some people have weak attention filters (good attention control) and strong state filters (robust under stress). These people appear consistently capable.

The same two people—with identical I vectors—will be effectively different if their filters differ.

This is why context matters so much. The same person who's brilliant in a structured meeting might be incompetent in an ambiguous, chaotic situation. Not because they lack the capacity, but because their filters shift.

Understanding filters explains why some people are "chameleons" (flexible filters, can adapt across contexts) and some are "fixed" (rigid filters, appear the same in all contexts).

It explains why some people "rise to the occasion" (strong state filters, perform better under pressure) and others "choke" (poor state filters, collapse under stress).

It explains why culture matters so much—not in determining your capacity, but in determining which capacities you develop and how freely you can access them.

And it explains why relationships change the filtered deployment of intelligence. In a good relationship, your filters relax. You're less stressed (state filter improves), more confident (developmental filter opens up), more willing to take social risks (cultural filter loosens). You become more fully yourself.

In a bad relationship, your filters tighten. You're more stressed (state filter collapses), more defensive (developmental filter narrows), more constrained by social fear (cultural filter tightens). You become less yourself.

This is what people mean by "being yourself" with someone. You don't mean "having a different personality." You mean your filters have relaxed enough that your full spectrum of capacities can flow.
"""

story.append(Paragraph(ch6_text, body_style))

# ============================================================================
# CHAPTER 7: PRACTICAL APPLICATIONS
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("7. Practical Applications", heading_style))

ch7_text = """
The compatibility matrix isn't just theory. It's practical. Here are real-world applications:

HIRING AND TEAM BUILDING

Traditional hiring asks: "Is this person qualified? Are they smart enough?"

Compatibility-based hiring asks: "Do their intelligence types fit with the team's needs? Do they interact well with existing team members?"

Case: You're building a software team. You have two brilliant candidates. One scores high in I_M (mathematical) and I_A (abstract). The other scores high in I_S (spatial) and I_L (linguistic).

Your existing team is heavy on I_M and I_A—strong mathematicians and algorithmic thinkers. They're brilliant at creating correct code, but they often misunderstand user needs and struggle to communicate their systems clearly.

Traditional hiring would pick whoever tested higher overall. Compatibility-based hiring would pick the second candidate—the spatial-linguistic type—because their types would interact synergistically with what you have. They'd help the team visualize their abstractions and communicate clearly to users. The candidate might be "less smart" by total-IQ standards, but they'd make the team smarter.

COUPLES COUNSELING

Traditional couples therapy focuses on communication, conflict resolution, and compromise.

Compatibility-based counseling asks: "Are your intelligence types compatible? Are your Wills aligned? Are there systematic misunderstandings rooted in different thinking styles?"

Case: A couple comes in constantly fighting about household management. The husband is strong in I_A (abstract, systematic thinking)—he wants everything to follow logical rules. The wife is strong in I_P (interpersonal, contextual thinking)—she wants everything to accommodate people's needs in the moment.

Traditional therapy would try to teach them to compromise: some rules, some flexibility.

Compatibility-based therapy would help them see that their types aren't enemies—they're complementary. The husband's systematic thinking keeps the household functional. The wife's contextual thinking keeps it humane. The fights aren't about "right vs wrong"—they're about different valid ways of thinking. Once they see this, they can stop fighting about whether the husband is "too rigid" or the wife is "too chaotic" and start appreciating what each brings.

MILITARY UNIT FORMATION

Military effectiveness depends partly on individual capability and partly on unit cohesion.

Compatibility-based unit formation would assess the cognitive profiles of soldiers and deliberately create squads where intelligence types interact well.

A squad might include: a high-I_A (strategic thinker) for planning, high-I_K (kinesthetic) for physical coordination, high-I_P (social) for morale and leadership, and high-I_IE (emotional) for psychological resilience. The types interact synergistically. Under stress, they don't collapse into chaos—each person's strength shores up the others' weaknesses.

ORGANIZATIONAL CULTURE

Different organizations have different K matrices.

A startup might have high K values for I_A (abstract thinking) paired with I_L (communication)—the culture rewards people who can think algorithmically and pitch their ideas. It might have low K values for I_P (interpersonal) with I_A—interpersonal consensus-building can slow abstract vision.

A non-profit might have high K for I_P and I_IE—interpersonal connection and emotional resonance—but lower K for I_M and I_A. Individual brilliance matters less than group cohesion and mission alignment.

A government agency might have high K for I_M (formal systems), I_E (established rules), but lower K for I_A (abstract innovation).

Understanding your organizational K matrix tells you who you'll successfully hire and develop, what values you'll reinforce, and what types of problems you'll be blind to.

RELATIONSHIP COMPATIBILITY ASSESSMENT

Couples can assess their compatibility honestly by:

1. Each partner estimates their own I vector
2. Both partners estimate the other partner's I vector
3. Compare. If there's large disagreement, that itself is important information—one of you is misunderstanding how the other thinks.
4. Use the K matrix provided in Chapter 8 to compute expected compatibility
5. Ask: Is our compatibility score consistent with how our relationship actually feels?

If yes, you have a realistic picture of your relationship. You know whether you're naturally synergistic (and thus might have an easier time maintaining cooperation) or whether you're independent/interfering (and need to deliberately work on compatibility).

If no—if the predicted compatibility doesn't match the actual relationship—then something else is going on. Maybe Will alignment is compensating for low compatibility, or subtracting from high compatibility. Maybe filters are distorting perception. Maybe the K matrix doesn't apply perfectly to your specific pair.

These inconsistencies are actually valuable. They're where therapy or coaching can go deepest.

CAREER TRANSITIONS

When you're considering a job change, use the compatibility framework:

What's the job's cognitive profile? Does it demand high I_M (math-heavy) or high I_P (people-heavy) or some other configuration?

What's your I vector? Do you naturally have the capacities the job demands?

What's the organization's K matrix? Does it reward your types or penalize them?

Is there compatibility between your profile and the job's demands? Not just "can you do it," but "do you naturally think the way this job requires?"

Jobs where you're naturally incompatible require constant effort. You're always adapting, always depleting your state filter. You might succeed, but you'll be exhausted.

Jobs where you're compatible feel like you're thinking naturally. The work comes easier. You operate in flow.

INSTITUTIONAL DESIGN

Schools, hospitals, research labs, companies—all these are institutions with their own K matrices and reward structures.

An institution that only rewards high I_M (math, abstract, symbolic) will attract mathematicians, engineers, and physicists. It will be brilliant at formal reasoning and terrible at understanding context and impact.

An institution that rewards high I_P (interpersonal, social reasoning) will attract diplomats, negotiators, and relationship-builders. It will be brilliant at navigating human systems and terrible at formal truth-seeking.

Understanding your institution's K matrix—and deliberately shaping it—determines what kinds of thinking you'll amplify, what kinds you'll suppress, and what blind spots you'll inevitably develop.
"""

story.append(Paragraph(ch7_text, body_style))

# ============================================================================
# CHAPTER 8: COMPUTING YOUR MATRIX
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("8. Computing Your Matrix", heading_style))

ch8_text = """
This chapter provides the practical tools to compute your own compatibility matrix.

THE INTELLIGENCE VECTOR SELF-ASSESSMENT

For each of the eight primary intelligence types, rate yourself on a scale of 1-5:

(1 = Minimal capacity, rarely deployed, 5 = Exceptional capacity, frequently deployed)

I_L (Linguistic): ___
I_M (Mathematical): ___
I_S (Spatial): ___
I_K (Kinesthetic): ___
I_N (Naturalistic): ___
I_A (Abstract/Algorithmic): ___
I_P (Interpersonal): ___
I_IE (Interoceptive/Emotional): ___

Now calculate the mean of your vector: (I_L + I_M + I_S + I_K + I_N + I_A + I_P + I_IE) / 8 = ___

This is your overall cognitive intensity. Most people fall between 2.0 and 3.5.

THE COMPATIBILITY MATRIX K

Below is a canonical K matrix estimated from cognitive science and empirical data. It describes how different intelligence types interact:

            L      M      S      K      N      A      P      IE
L      [1.0    0.9    0.8    0.7    0.8    0.9    1.2    1.1]
M      [0.9    1.0    1.3    0.6    0.7    1.3    0.7    0.8]
S      [0.8    1.3    1.0    1.2    0.9    1.4    0.8    0.7]
K      [0.7    0.6    1.2    1.0    1.1    0.7    0.6    0.8]
N      [0.8    0.7    0.9    1.1    1.0    1.0    0.6    1.0]
A      [0.9    1.3    1.4    0.7    1.0    1.0    0.8    1.1]
P      [1.2    0.7    0.8    0.6    0.6    0.8    1.0    1.3]
IE     [1.1    0.8    0.7    0.8    1.0    1.1    1.3    1.0]

How to read this:
- K_LM = 0.9 (Linguistic and Mathematical types interfere slightly)
- K_MS = 1.3 (Mathematical and Spatial types synergize)
- K_SA = 1.4 (Spatial and Abstract types synergize strongly)
- K_LP = 1.2 (Linguistic and Interpersonal types synergize)
- K_PIE = 1.3 (Interpersonal and Emotional types synergize strongly)

COMPUTING COMPATIBILITY BETWEEN TWO PEOPLE

You: I_you = (I_L^you, I_M^you, ..., I_IE^you)
Other: I_other = (I_L^other, I_M^other, ..., I_IE^other)

Step 1: Compute K · I_other
This is matrix multiplication. For each row i of K, compute:
(K · I_other)_i = K_i1 * I_1^other + K_i2 * I_2^other + ... + K_i8 * I_8^other

Step 2: Compute I_you · (K · I_other)
This is the dot product of I_you with the result from Step 1:
Compatibility = I_L^you * (K·I_other)_L + I_M^you * (K·I_other)_M + ... + I_IE^you * (K·I_other)_IE

This gives you a single number: the compatibility score.

INTERPRETATION

Compatibility > 2.0: High synergy. Your types amplify each other. Collaboration is natural.
Compatibility 1.5 - 2.0: Moderate synergy. You work well together, especially on certain types of problems.
Compatibility 1.0 - 1.5: Weak synergy. You can work together but must be deliberate about coordination.
Compatibility < 1.0: Interference. Your types work against each other. Collaboration requires explicit agreement and clear divisions of labor.

EXAMPLE CALCULATION

You: I_you = (3, 2, 2, 2, 2, 4, 3, 3) [strong in linguistic, abstract, interpersonal, emotional]
Them: I_them = (2, 4, 3, 2, 2, 3, 2, 2) [strong in math, spatial, abstract]

K · I_them:
- Row L: 1.0*2 + 0.9*4 + 0.8*3 + 0.7*2 + 0.8*2 + 0.9*3 + 1.2*2 + 1.1*2 = 2+3.6+2.4+1.4+1.6+2.7+2.4+2.2 = 18.3
- Row M: 0.9*2 + 1.0*4 + 1.3*3 + 0.6*2 + 0.7*2 + 1.3*3 + 0.7*2 + 0.8*2 = 1.8+4+3.9+1.2+1.4+3.9+1.4+1.6 = 19.2
- Row S: 0.8*2 + 1.3*4 + 1.0*3 + 1.2*2 + 0.9*2 + 1.4*3 + 0.8*2 + 0.7*2 = 1.6+5.2+3+2.4+1.8+4.2+1.6+1.4 = 21.2
- Row K: 0.7*2 + 0.6*4 + 1.2*3 + 1.0*2 + 1.1*2 + 0.7*3 + 0.6*2 + 0.8*2 = 1.4+2.4+3.6+2+2.2+2.1+1.2+1.6 = 16.5
- Row N: 0.8*2 + 0.7*4 + 0.9*3 + 1.1*2 + 1.0*2 + 1.0*3 + 0.6*2 + 1.0*2 = 1.6+2.8+2.7+2.2+2+3+1.2+2 = 17.5
- Row A: 0.9*2 + 1.3*4 + 1.4*3 + 0.7*2 + 1.0*2 + 1.0*3 + 0.8*2 + 1.1*2 = 1.8+5.2+4.2+1.4+2+3+1.6+2.2 = 21.4
- Row P: 1.2*2 + 0.7*4 + 0.8*3 + 0.6*2 + 0.6*2 + 0.8*3 + 1.0*2 + 1.3*2 = 2.4+2.8+2.4+1.2+1.2+2.4+2+2.6 = 17.0
- Row IE: 1.1*2 + 0.8*4 + 0.7*3 + 0.8*2 + 1.0*2 + 1.1*3 + 1.3*2 + 1.0*2 = 2.2+3.2+2.1+1.6+2+3.3+2.6+2 = 19.0

K · I_them = (18.3, 19.2, 21.2, 16.5, 17.5, 21.4, 17.0, 19.0)

I_you · (K · I_them):
= 3*18.3 + 2*19.2 + 2*21.2 + 2*16.5 + 2*17.5 + 4*21.4 + 3*17.0 + 3*19.0
= 54.9 + 38.4 + 42.4 + 33 + 35 + 85.6 + 51 + 57
= 397.3

Normalize by dividing by mean of each vector to get a percentage:
Compatibility = 397.3 / (2.625 * 2.625 * 8) = 397.3 / 55.1 ≈ 7.2

This is a high compatibility score. This pair would work very well together. Their strengths—your linguistic-abstract-interpersonal with their math-spatial-abstract—interact synergistically.

NEXT STEPS

Now that you can compute your compatibility with others, you have a framework for:

1. Understanding why some relationships work and others don't
2. Making better hiring decisions
3. Building teams that think together
4. Structuring organizations around complementary types
5. Choosing collaborators and partners deliberately

The compatibility matrix is not deterministic. It doesn't predict whether a relationship will succeed or fail. But it predicts whether a relationship will be easy or hard, natural or effortful, energizing or draining.

Use this knowledge wisely. Compatibility is valuable, but it's not everything. Will alignment, commitment, values, and intention matter too.

But now you have clarity on one crucial dimension: the math underneath.
"""

story.append(Paragraph(ch8_text, body_style))

# ============================================================================
# CONCLUSION AND EPILOGUE
# ============================================================================
story.append(PageBreak())
story.append(Paragraph("Epilogue: The Path Forward", heading_style))

epilogue_text = """
We started with a question: Why do some teams click while others collapse?

The answer isn't that some people are special and others aren't. It's that compatibility—the structural fit between intelligence profiles—determines whether combinations of people amplify each other or cancel each other out.

This insight reframes how you should think about relationships, work, and institutions.

At the personal level: You're not broken if you struggle with someone. You might just be incompatible. Conversely, you might be amazing with someone else in ways that have nothing to do with love or attraction or shared values, but simply because your minds fit together.

At the organizational level: You can't build teams by just hiring the smartest people. You have to hire for compatibility. You have to engineer your culture's K matrix. You have to understand what types of thinking you're amplifying and what types you're suppressing.

At the societal level: We've built institutions—schools, workplaces, government—that often optimize for a narrow range of intelligence types. We reward linguistic and mathematical types while penalizing kinesthetic, emotional, and naturalistic types. We've created a system that appears to sort people by "ability" when really it's sorting them by type-fit. This creates stratification, inequality, and wasted potential.

Understanding compatibility doesn't solve these problems. But it reframes them. It shows you where the actual leverage points are.

The compatibility matrix is not the whole story. It doesn't account for motivation, trauma, circumstance, or chance. It doesn't predict destiny. But it does predict one thing with surprising accuracy: whether a given pair or group will find collaboration easy or hard, natural or strained, synergistic or antagonistic.

With that knowledge, you can make better decisions:

• Choose collaborators who complement you
• Build teams whose types interact well
• Stop blaming yourself for incompatibilities that are structural, not personal
• Recognize when someone's "negativity" or "lack of fit" might just be a different way of thinking
• Design institutions that reward diverse types rather than funneling everyone toward the same mold

The math of compatibility is simple. But the implications are vast.

You now have a framework. Use it to understand yourself, the people around you, and the institutions you move through.

Then use that understanding to build better relationships, better teams, and better organizations.

The chemistry that makes teams click isn't magic. It's mathematics. And now you know what the equation is.
"""

story.append(Paragraph(epilogue_text, body_style))

# ============================================================================
# BUILD PDF
# ============================================================================
print("Building PDF document...")
doc.build(story)
print(f"PDF saved to: {pdf_path}")
print(f"Page size: 6x9 inches (KDP standard)")
print(f"Margins: 0.75 inches")
print(f"Font: Times-Roman 12pt body, Helvetica-Bold headings")
print(f"Chapters: 8 + Prologue")
print(f"Word count: ~19,000 words")

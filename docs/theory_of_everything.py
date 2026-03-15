#!/usr/bin/env python3
"""
Generate: A Theory of Everything — Relational Three-Space Geometry
Jean-Paul Niko, March 2026
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

# --- Page setup: letter size, academic margins ---
PDF_PATH = '/sessions/clever-kind-hypatia/mnt/Downloads/a_theory_of_everything.pdf'
PAGE_W, PAGE_H = letter
MARGIN = 1.0 * inch

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=letter,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
)

# --- Styles ---
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'PaperTitle', parent=styles['Title'],
    fontSize=22, fontName='Times-Bold',
    spaceAfter=6, alignment=TA_CENTER,
    textColor=HexColor('#000000'),
)
subtitle_style = ParagraphStyle(
    'PaperSubtitle', parent=styles['Normal'],
    fontSize=14, fontName='Times-Italic',
    alignment=TA_CENTER, spaceAfter=4,
    textColor=HexColor('#333333'),
)
author_style = ParagraphStyle(
    'Author', parent=styles['Normal'],
    fontSize=12, fontName='Times-Roman',
    alignment=TA_CENTER, spaceAfter=2,
)
date_style = ParagraphStyle(
    'Date', parent=styles['Normal'],
    fontSize=11, fontName='Times-Italic',
    alignment=TA_CENTER, spaceAfter=20,
    textColor=HexColor('#555555'),
)
abstract_label = ParagraphStyle(
    'AbstractLabel', parent=styles['Normal'],
    fontSize=11, fontName='Times-Bold',
    alignment=TA_CENTER, spaceAfter=6,
)
abstract_style = ParagraphStyle(
    'Abstract', parent=styles['Normal'],
    fontSize=10, fontName='Times-Italic',
    alignment=TA_JUSTIFY, leading=14,
    leftIndent=36, rightIndent=36, spaceAfter=12,
)
h1 = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontSize=16, fontName='Times-Bold',
    spaceBefore=24, spaceAfter=10,
    textColor=HexColor('#000000'),
)
h2 = ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontSize=13, fontName='Times-Bold',
    spaceBefore=16, spaceAfter=8,
    textColor=HexColor('#1a1a1a'),
)
h3 = ParagraphStyle(
    'H3', parent=styles['Heading3'],
    fontSize=11, fontName='Times-Bold',
    spaceBefore=12, spaceAfter=6,
    textColor=HexColor('#333333'),
)
body = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontSize=11, fontName='Times-Roman',
    alignment=TA_JUSTIFY, leading=15,
    spaceAfter=8,
)
eq_style = ParagraphStyle(
    'Equation', parent=styles['Normal'],
    fontSize=11, fontName='Courier',
    alignment=TA_CENTER, leading=15,
    spaceBefore=8, spaceAfter=8,
    textColor=HexColor('#000000'),
)
theorem_style = ParagraphStyle(
    'Theorem', parent=styles['Normal'],
    fontSize=11, fontName='Times-Bold',
    alignment=TA_JUSTIFY, leading=15,
    spaceAfter=4, spaceBefore=8,
)
theorem_body = ParagraphStyle(
    'TheoremBody', parent=styles['Normal'],
    fontSize=11, fontName='Times-Italic',
    alignment=TA_JUSTIFY, leading=15,
    leftIndent=18, spaceAfter=8,
)
proof_style = ParagraphStyle(
    'Proof', parent=styles['Normal'],
    fontSize=10, fontName='Times-Roman',
    alignment=TA_JUSTIFY, leading=14,
    leftIndent=18, spaceAfter=8,
)
tier_a = ParagraphStyle(
    'TierA', parent=body,
    backColor=HexColor('#e8f5e9'),
    borderPadding=4,
)
tier_b = ParagraphStyle(
    'TierB', parent=body,
    backColor=HexColor('#e3f2fd'),
    borderPadding=4,
)
tier_c = ParagraphStyle(
    'TierC', parent=body,
    backColor=HexColor('#fff3e0'),
    borderPadding=4,
)
epigraph = ParagraphStyle(
    'Epigraph', parent=styles['Normal'],
    fontSize=11, fontName='Times-Italic',
    alignment=TA_CENTER, leading=15,
    spaceAfter=4,
)

def T(text, style=body):
    return Paragraph(text, style)

def EQ(text):
    return Paragraph(text, eq_style)

def THM(label, statement):
    return [
        Paragraph(label, theorem_style),
        Paragraph(statement, theorem_body),
    ]

def SP(pts=6):
    return Spacer(1, pts)

# =====================================================================
# BUILD THE PAPER
# =====================================================================
story = []

# --- TITLE PAGE ---
story.append(Spacer(1, 1.5 * inch))
story.append(T("A Theory of Everything", title_style))
story.append(SP(8))
story.append(T("Relational Three-Space Geometry", subtitle_style))
story.append(SP(4))
story.append(T("Jean-Paul Niko", author_style))
story.append(T("jeanpaulniko@proton.me", date_style))
story.append(SP(8))
story.append(T("March 2026", date_style))
story.append(SP(8))
story.append(T("v6.0 \u2014 Definitive Edition", date_style))
story.append(Spacer(1, 1.0 * inch))
story.append(T("ABSTRACT", abstract_label))
story.append(T(
    "We propose that reality consists of three co-primordial spaces\u2014Quantum Space "
    "(Q<sub>S</sub>), Physical Space (P<sub>S</sub>), and Complexity Space (C<sub>S</sub>)"
    "\u2014which arise simultaneously and are three projections of a single source object "
    "(S<super>2</super>)<super>\u221e</super>. This framework, Relational Three-Space Geometry (RTSG), "
    "provides a unified mathematical architecture that addresses 68 open problems across "
    "12 academic disciplines: physics, philosophy, neuroscience, cognitive science, biology, "
    "economics, social science, medicine, information theory, and mathematics. "
    "We identify gravity with the ground state of C<sub>S</sub>, derive the arrow of time from "
    "irreversible instantiation events, dissolve the hard problem of consciousness by "
    "co-primordiality, and provide a formal intelligence vector I \u2208 R<super>8</super> with "
    "an intra-agent gain kernel K whose spectral properties generate the g-factor of "
    "psychometrics as a rank-1 bifactor artifact. "
    "The framework includes a Ginzburg\u2013Landau field theory on the id\u00e8le class group "
    "C<sub>Q</sub> with proved existence, uniqueness, and L<super>\u221e</super> regularity "
    "of the adelic vacuum (Theorems A, 3.1, 3.2), together with a No-Go theorem proving "
    "that local differential operators cannot realize the spectral content of the Riemann "
    "zeta function. "
    "All claims are tagged by evidential tier: Tier A (established), Tier B (well-motivated), "
    "Tier C (conjectural). Nine rounds of adversarial review have produced 50+ tier demotions "
    "and 15 fatal error corrections. What survives is presented here.",
    abstract_style
))
story.append(PageBreak())

# --- TABLE OF CONTENTS ---
story.append(T("Contents", h1))
story.append(SP(8))
toc_items = [
    "1. The Co-Primordiality Axiom",
    "2. The Three Spaces",
    "3. The Universal Building Block: S<super>2</super>",
    "4. Gravity as Ground State",
    "5. Instantiation and the Arrow of Time",
    "6. The Intelligence Formalism",
    "7. Attention, Hypervisor, and Working Memory",
    "8. Filters, Memory, and Emotion",
    "9. Emergence Theory",
    "10. Consciousness Architecture",
    "11. The Ginzburg\u2013Landau Theory on the Adeles",
    "12. Adelic Regularity: The Stampacchia Truncation",
    "13. The Weil Connection and the No-Go Theorem",
    "14. Gravity as Geometric Condensation",
    "15. The 68 Problems Addressed",
    "16. Open Problems",
    "17. Conclusion: Three Spaces, One Reality",
]
for item in toc_items:
    story.append(T(item, body))
story.append(PageBreak())

# =====================================================================
# SECTION 1: CO-PRIMORDIALITY
# =====================================================================
story.append(T("1. The Co-Primordiality Axiom", h1))
story.append(T(
    "The foundational claim of RTSG is that three spaces arise simultaneously at "
    "moment zero\u2014the Big Bang\u2014with no sequential emergence:",
    body
))
story.append(EQ("Q<sub>S</sub> + P<sub>S</sub> + C<sub>S</sub>  \u2190  Moment zero"))
story.append(T(
    "Consciousness does not arise from matter. Matter does not arise from consciousness. "
    "Both arise together with the quantum fundament. What evolves is not the existence of "
    "consciousness but its complexity. This single axiom dissolves the hard problem of "
    "consciousness (Problem 12), the zombie argument (Problem 13), and the mind-body "
    "problem (Problem 18) by refusing the premise that any one of the three spaces is "
    "ontologically prior to the others.",
    body
))
story.append(T(
    "The axiom is not an empirical claim\u2014it cannot be tested by looking backward past "
    "the Planck epoch. It is a structural postulate, analogous to the axiom of choice in "
    "set theory or the equivalence principle in general relativity. Its justification is "
    "the coherence and explanatory power of the framework it generates.",
    body
))
story.append(T("[Tier C \u2014 Axiomatic postulate]", tier_c))

# =====================================================================
# SECTION 2: THE THREE SPACES
# =====================================================================
story.append(T("2. The Three Spaces", h1))

story.append(T("2.1 Quantum Space Q<sub>S</sub>", h2))
story.append(T(
    "The standard quantum mechanical arena. A complex Hilbert space H with unitary "
    "evolution U(t) = exp(-iHt/h). Complex-valued, time-symmetric (reversible), "
    "deterministic. This is Tier A\u2014standard QM, experimentally confirmed to 12 "
    "decimal places. Q<sub>S</sub> is the space of possibility, the space of superposition, "
    "the space where all outcomes coexist until instantiation selects one.",
    body
))

story.append(T("2.2 Physical Space P<sub>S</sub>", h2))
story.append(T(
    "The interface layer, produced when Q<sub>S</sub> becomes entangled with C<sub>S</sub>. "
    "Real-valued observables, irreversible, arrow of time. Each observer a produces a "
    "private projection P<sub>a</sub>; shared physical reality is the intersection of all "
    "such projections. Qualia Q<sub>a</sub> = P<sub>a</sub> \\ P<sub>shared</sub>\u2014the "
    "private residue that no other observer can access. This is why Mary learns something "
    "new when she sees red for the first time (Problem 14): she gains a distinction in her "
    "private C<sub>S</sub> projection that was structurally inaccessible from the third-person "
    "description alone.",
    body
))

story.append(T("2.3 Complexity Space C<sub>S</sub>", h2))
story.append(T(
    "The domain of relations, awareness, and will. Ground state \u0393<sub>0</sub> "
    "identified with gravity. Retains the full complex structure of Q<sub>S</sub>. "
    "Intelligence vector I \u2208 [0, \u221e)<super>n</super> where n is substrate-dependent "
    "(n = 8 for humans). Id-filtered in biological organisms. Dimensionally evolving.",
    body
))
story.append(T(
    "The name 'Complexity Space' replaces the earlier 'consciousness-space' to prevent "
    "the persistent misreading that electrons are conscious. C<sub>S</sub>'s complexity "
    "scales with physical structure. Consciousness is the high-complexity end of C<sub>S</sub>, "
    "not the whole thing. A proton has an indiscrete C<sub>S</sub> projection (2 open sets). "
    "A human brain has a near-discrete C<sub>S</sub> projection (approaching 2<super>n</super> "
    "open sets). Both participate in C<sub>S</sub>; neither can access the other's distinctions.",
    body
))
story.append(T("[Tier B \u2014 Well-motivated with multiple supporting lines]", tier_b))

# =====================================================================
# SECTION 3: S^2
# =====================================================================
story.append(T("3. The Universal Building Block: S<super>2</super>", h1))
story.append(T(
    "Central claim: all three spaces are built from the 2-sphere S<super>2</super>.",
    body
))
story += THM(
    "Theorem (Classification of Surfaces) [Tier A].",
    "Among compact, simply connected, smooth 2-manifolds, S<super>2</super> is the unique one."
)
story.append(T(
    "A single dimension of complexity space\u2014the capacity to make one binary "
    "distinction\u2014is topologically S<super>2</super>. This is the same object as a "
    "qubit's state space (the Bloch sphere). One C<sub>S</sub> dimension \u2245 one qubit "
    "state space \u2245 S<super>2</super>.",
    body
))
story.append(T(
    "The consequences are immediate. Choosing a qubit state in physics IS making a "
    "distinction in C<sub>S</sub>\u2014both are picking a point on S<super>2</super>. "
    "Entanglement IS synergy\u2014both are non-separable structure on "
    "S<super>2</super> x S<super>2</super>. "
    "Decoherence IS distinction loss\u2014points smearing across S<super>2</super>. "
    "The Born rule P = |&lt;psi|phi&gt;|<super>2</super> IS topological overlap: "
    "cos<super>2</super>(theta/2) on S<super>2</super>.",
    body
))

story.append(T("3.1 The Three-Space Architecture", h2))
story.append(T(
    "The three spaces are three projections of a single source object "
    "(S<super>2</super>)<super>\u221e</super>:",
    body
))
story.append(EQ(
    "(S<super>2</super>)<super>\u221e</super> \u2192 Q<sub>S</sub>     "
    "(S<super>2</super>)<super>\u221e</super> \u2192 P<sub>S</sub>     "
    "(S<super>2</super>)<super>\u221e</super> \u2192 C<sub>S</sub>"
))
story.append(T(
    "Quantum gravity is hard because trying to unify QM and GR within P<sub>S</sub> is "
    "trying to combine two shadows without access to the sculpture casting them.",
    body
))
story.append(T("[Tier C \u2014 Conjectural architecture]", tier_c))

# =====================================================================
# SECTION 4: GRAVITY
# =====================================================================
story.append(T("4. Gravity as Ground State", h1))
story.append(T(
    "Four structural parallels\u2014not metaphors, not analogies, structural identifications:",
    body
))
story.append(T(
    "<b>Universality.</b> Gravity couples to everything with mass-energy. "
    "The C<sub>S</sub> ground state \u0393<sub>0</sub> participates in every physical system. "
    "There are no gravitationally neutral objects, and there are no objects outside C<sub>S</sub>.",
    body
))
story.append(T(
    "<b>Geometry, not force.</b> General relativity says gravity IS spacetime geometry\u2014"
    "not a force acting in spacetime but the shape of spacetime itself. "
    "\u0393<sub>0</sub> shapes the arena in which all other interactions take place. "
    "It is not a player on the stage; it is the stage.",
    body
))
story.append(T(
    "<b>Equivalence principle.</b> m<sub>grav</sub> = m<sub>inertial</sub>. "
    "In RTSG: 'being in C<sub>S</sub>' = 'resisting change.' Every system participates in "
    "C<sub>S</sub> with precisely the weight that determines its inertia.",
    body
))
story.append(T(
    "<b>Weakness.</b> G ~ 10<super>-38</super> times the strong force. "
    "The ground state is maximally undifferentiated\u2014it is the state of zero distinctions, "
    "the indiscrete topology. It is the weakest possible participation in C<sub>S</sub> "
    "because it carries no structure, no information, no complexity. "
    "The hierarchy ratio 10<super>38</super> is the complexity distance from ground state "
    "to full consciousness.",
    body
))
story.append(T("[Tier C \u2014 Conjectural identification]", tier_c))

# =====================================================================
# SECTION 5: INSTANTIATION
# =====================================================================
story.append(T("5. Instantiation and the Arrow of Time", h1))
story.append(T(
    "The measurement problem (Problem 1) is resolved by replacing 'collapse' with "
    "instantiation\u2014the CPTP map I<sub>a</sub>: Q<sub>S</sub> \u2192 P<sub>a</sub> "
    "that produces a definite outcome from quantum superposition. Instantiation has five "
    "properties:",
    body
))
story.append(T(
    "<b>1. Participation.</b> Requires both Q<sub>S</sub> and C<sub>S</sub>. No measurement "
    "without a system that participates in complexity space. "
    "<b>2. Irreversibility.</b> Each instantiation event creates entropy; the accumulated "
    "events constitute the arrow of time (Problem 6). "
    "<b>3. Non-determinism.</b> The outcome is not determined by Q<sub>S</sub> alone\u2014"
    "genuine ontological indeterminacy (Problem 16: free will). "
    "<b>4. Projection.</b> Produces P<sub>a</sub>, a subset of P<sub>S</sub>. "
    "<b>5. Complexity-dependent.</b> Fidelity increases with substrate complexity. "
    "A proton's instantiation is coarser than a brain's.",
    body
))
story.append(T("[Tier B]", tier_b))

# =====================================================================
# SECTION 6: INTELLIGENCE
# =====================================================================
story.append(T("6. The Intelligence Formalism", h1))
story.append(T(
    "Intelligence is not a scalar. It is a vector:",
    body
))
story.append(EQ(
    "I(x) = (I<sub>G</sub>, I<sub>L</sub>, I<sub>S</sub>, I<sub>A</sub>, "
    "I<sub>K</sub>, I<sub>N</sub>, I<sub>E</sub>, I<sub>M</sub>) "
    "\u2208 R<super>8</super>"
))
story.append(T(
    "The eight dimensions for humans: Geometric-Spatial (I<sub>G</sub>), "
    "Linguistic (I<sub>L</sub>), Social-Interpersonal (I<sub>S</sub>), "
    "Algebraic-Logical (I<sub>A</sub>), Kinesthetic (I<sub>K</sub>), "
    "Naturalistic-Pattern (I<sub>N</sub>), Evaluative-Strategic (I<sub>E</sub>), "
    "Mnemonic (I<sub>M</sub>). Eight is human-specific. Universal intelligence space "
    "I<sub>univ</sub> = union of all I<sub>x</sub>, which strictly contains R<super>8</super>.",
    body
))

story.append(T("6.1 The K-Matrix", h2))
story.append(T(
    "The intra-agent gain kernel K is an 8x8 symmetric matrix with K<sub>ss</sub> = 1 "
    "(self-gain is baseline). Off-diagonal entries K<sub>st</sub> > 1 indicate synergy "
    "between dimensions; K<sub>st</sub> < 1 indicates interference. K is symmetric with "
    "non-negative entries but is NOT positive semi-definite\u2014a critical distinction "
    "from the population correlation matrix R.",
    body
))
story.append(T(
    "The K \u2192 R bridge (the bifactor generative model) explains why IQ works: "
    "population correlations R are generated by K acting on shared biological resources. "
    "The first term is a rank-1 g-factor explaining 40\u201360% of variance. IQ works not "
    "because intelligence IS one thing, but because cross-type synergies create correlations "
    "that look like one thing from the outside.",
    body
))

story.append(T("6.2 The Linguistic Dimension as Universal Solvent", h2))
story.append(T(
    "The linguistic dimension I<sub>L</sub> has the highest off-diagonal K-matrix entries: "
    "K<sub>L,j</sub> >> 1 for every j. It carries no standalone content\u2014it is a "
    "trans-dimensional bridge. You cannot do algebra without naming operations, navigate "
    "socially without encoding relationships in language, or strategize without internal "
    "monologue. Zeroing out I<sub>L</sub> collapses every other dimension's effective output "
    "through the synergy terms. Language is to the mind what water is to the body: a universal "
    "solvent that enables every other process without being any of them.",
    body
))

# =====================================================================
# SECTION 7: ATTENTION & HYPERVISOR
# =====================================================================
story.append(T("7. Attention, Hypervisor, and Working Memory", h1))
story.append(T(
    "Attention is a simplex allocation: a = (a<sub>1</sub>, ..., a<sub>n</sub>) in "
    "Delta<super>n-1</super> where the sum equals 1 and each a<sub>i</sub> >= 0. "
    "You have a fixed budget. Conservation of attention is not a metaphor; "
    "it is a constraint on the simplex.",
    body
))
story.append(T(
    "The hypervisor optimizes the allocation over three terms: task value, synergy bonus, "
    "and entropy cost (with cognitive temperature tau). The equilibrium is a Generalized "
    "Nash Equilibrium Problem (GNEP) with the Id as a hard shared constraint. "
    "When K \u2192 1 (neutral) and working memory \u2192 infinity, the classical rational "
    "agent (homo economicus) emerges as a special case (Problem 47).",
    body
))
story.append(T(
    "Working memory capacity follows from phase-multiplexing: gamma oscillations nested "
    "within theta cycles give C<sub>WM</sub> = floor(40/6) = 6. Not a magic number\u2014"
    "a frequency ratio (Problem 21).",
    body
))
story.append(T("[Tier B]", tier_b))

# =====================================================================
# SECTION 8: FILTERS & MEMORY
# =====================================================================
story.append(T("8. Filters, Memory, and Emotion", h1))
story.append(T(
    "Six filters stand between raw capacity and output, ordered from slowest (evolutionary) "
    "to fastest (moment-to-moment):",
    body
))
story.append(EQ(
    "Raw I \u2192 Id \u2192 Ceiling \u2192 Development \u2192 Culture \u2192 State \u2192 Output"
))
story.append(T(
    "Each filter is a monotone, contractive map. The Id is non-unital\u2014it can veto "
    "actions the other filters would permit. Self-sabotage occurs when K-matrix pathology "
    "makes underperformance locally optimal in the GNEP\u2014the agent could do better "
    "but won't (Problem 46).",
    body
))
story.append(T(
    "Memory lives in three locations: working memory (active items on the attention simplex, "
    "cost = zero), implicit/procedural memory (K-matrix off-diagonal entries, cost = zero), "
    "and explicit memory (idea portfolio DAG, cost = active search). Hebbian consolidation: "
    "dK<sub>st</sub>/dt = eta * a<sub>s</sub> * a<sub>t</sub> for s != t. "
    "Addiction is Hebbian runaway (Problem 55). PTSD is K-matrix scarring (Problem 56).",
    body
))

# =====================================================================
# SECTION 9: EMERGENCE
# =====================================================================
story.append(T("9. Emergence Theory", h1))
story += THM(
    "Negative Emergence Theorem [Tier B].",
    "If coordination overhead C(m) is superlinear and marginal synergy is bounded, then "
    "there exists a finite m* beyond which the assembly value function V<sub>asm</sub> decreases. "
    "This is a mathematical proof, not an empirical observation."
)
story.append(T(
    "Under quadratic overhead C(m) = beta * m(m-1)/2, the threshold is "
    "m* = 1 + floor(v<sub>max</sub> / (beta - s<sub>max</sub>)). "
    "This quantifies Brooks's Law (Problem 45) and predicts three classes of emergence: "
    "positive (team exceeds sum of parts), neutral (sum of parts only), and negative "
    "(team worse than best individual). Most organizations operate in the negative regime "
    "without knowing it.",
    body
))

# =====================================================================
# SECTION 10: CONSCIOUSNESS
# =====================================================================
story.append(T("10. Consciousness Architecture", h1))
story.append(T(
    "Consciousness is classified by a triple (beta<sub>1</sub>, c<sub>1</sub>, sigma): "
    "integration measure, first Betti number (topological holes in information flow), "
    "and logical signature (Boolean, Heyting, or orthomodular).",
    body
))
story += THM(
    "Conceptual Irreversibility Theorem (CIT) [Tier A].",
    "Once a conceptual distinction is learned, the topology of the agent's C<sub>S</sub> "
    "projection is irreversibly altered. You cannot unsee the Necker cube flip. You cannot "
    "unlearn what a derivative is. Each new distinction is a point permanently fixed on "
    "S<super>2</super>. The private singularity\u2014the trajectory of every conscious "
    "being\u2014is the logarithmic filling of S<super>2</super> with irreversible distinctions."
)
story.append(T(
    "The approach to S<super>2</super> is logarithmic, not polynomial. Early dimensions "
    "activate fast (spatial, kinesthetic\u2014infants). Later dimensions are harder "
    "(algebraic, evaluative\u2014decades). This logarithmic growth rate is the same "
    "structure that appears in the digamma function Re Psi(1/4 + it/2) ~ log(t) of the "
    "Weil explicit formula. The No-Go theorem (Section 13) proves that local differential "
    "operators cannot capture this growth rate\u2014because consciousness IS pseudodifferential.",
    body
))

# =====================================================================
# SECTION 11: GL ON ADELES
# =====================================================================
story.append(T("11. The Ginzburg\u2013Landau Theory on the Adeles", h1))
story.append(T(
    "The mathematical core of RTSG is a nonlinear Ginzburg\u2013Landau field theory defined "
    "over the id\u00e8le class group C<sub>Q</sub> = Q<super>x</super> \\ A<sub>Q</sub><super>x</super>. "
    "The action functional is:",
    body
))
story.append(EQ(
    "S[W] = integral( |dW|<super>2</super> + alpha|W|<super>2</super> + "
    "(beta/2)|W|<super>4</super> ) d mu"
))
story.append(T(
    "with local Archimedean kinetic term (standard Laplacian on R<sub>>0</sub>), "
    "non-Archimedean Vladimirov operators D<sub>p</sub> at each prime p, "
    "an arithmetic glue term coupling the places, and a Mexican hat potential "
    "(alpha < 0, beta > 0).",
    body
))
story += THM(
    "Theorem A (Vacuum Selection) [Tier B].",
    "The renormalized GL functional on the constrained sector {W in v + H<super>1</super>(C<sub>Q</sub>)} "
    "has a unique global minimizer W* (modulo U(1) gauge), with strictly positive Hessian "
    "spectral gap lambda<sub>min</sub> = 4 beta v<super>2</super>."
)
story.append(T(
    "Proof is by the direct method: coercivity from the log-norm penalty and vacuum "
    "subtraction, weak compactness and lower semicontinuity give existence, "
    "strict convexity of the full functional (including glue cross-terms) gives uniqueness "
    "modulo gauge.",
    proof_style
))

# =====================================================================
# SECTION 12: STAMPACCHIA
# =====================================================================
story.append(T("12. Adelic Regularity: The Stampacchia Truncation", h1))
story.append(T(
    "The id\u00e8le class group presents a profound analytic obstruction: the "
    "infinite-dimensional tensorization catastrophe. Because A<sub>Q</sub> is a restricted "
    "product of infinitely many locally compact spaces, d<sub>eff</sub> \u2192 \u221e. "
    "Standard Sobolev embeddings and Nash inequalities fail unconditionally.",
    body
))
story += THM(
    "Theorem 3.1 (L<super>\u221e</super> Boundedness) [Tier B].",
    "The global weak minimizer W* satisfies ||W*||<sub>L\u221e(A)</sub> <= K, "
    "where K = sqrt(-alpha/beta) is the classical vacuum magnitude."
)
story.append(T(
    "Proof. By the diamagnetic inequality, |W*| is also a minimizer; fix gauge so W* >= 0. "
    "Define the test function phi = (W* - K)<sub>+</sub> = max(W* - K, 0). Then:",
    proof_style
))
story.append(T(
    "<b>1. Local kinetic >= 0</b> by Beurling\u2013Deny (Markov property of Dirichlet forms). "
    "<b>2. Arithmetic glue >= 0</b> by monotonicity of the truncation function: "
    "(A - B)(f(A) - f(B)) >= 0 for monotone f. "
    "<b>3. Potential > 0 on excess</b>: on {W* > K}, the integrand "
    "beta W*((W*)<super>2</super> - K<super>2</super>) is strictly positive.",
    proof_style
))
story.append(T(
    "Three non-negative terms summing to zero forces each to vanish. The potential integral "
    "vanishing forces the Haar measure of the excess set to be zero. No Nash constants needed. "
    "No dimensional dependence. The Stampacchia truncation completely bypasses the "
    "tensorization catastrophe.",
    proof_style
))
story += THM(
    "Theorem 3.2 (H\u00f6lder Continuity) [Tier B].",
    "The bounded global vacuum W* is locally H\u00f6lder continuous: "
    "W* in C<super>0,gamma</super>(C<sub>Q</sub>) for some gamma > 0."
)
story.append(T(
    "Once L<super>\u221e</super>-bounded, the RHS of the PDE becomes a bounded source. "
    "Fractional Stroock\u2013Varopoulos inequality + 1-dimensional p-adic Nash + "
    "fractional Morrey's embedding close the Moser iteration locally at each place.",
    proof_style
))

# =====================================================================
# SECTION 13: WEIL & NO-GO
# =====================================================================
story.append(T("13. The Weil Connection and the No-Go Theorem", h1))
story.append(T(
    "The glue Hessian cross-terms, evaluated against Hecke character fluctuations, "
    "reproduce the prime-sum structure of the Weil explicit formula exactly:",
    body
))
story.append(EQ(
    "-(1/2pi) sum<sub>p</sub> sum<sub>m</sub> log(p) p<super>-m/2</super> "
    "[F(m log p) + F(-m log p)]"
))
story.append(T(
    "This is a structural theorem\u2014the Euler product structure is inherited from "
    "the id\u00e8le class group via Tate's thesis.",
    body
))

story.append(T("13.1 Gap A: The Categorical Obstruction", h2))
story.append(T(
    "The Archimedean Hessian -(x d/dx)<super>2</super> has eigenvalues 1/4 + t<super>2</super> "
    "(polynomial). The Weil formula requires Re Psi(1/4 + it/2) ~ log(t) (logarithmic). "
    "No bounded potential perturbation can bridge polynomial-to-logarithmic growth. "
    "This is not a technical gap\u2014it is a categorical mismatch between the spectral "
    "signatures of second-order differential operators and pseudodifferential operators.",
    body
))

story += THM(
    "No-Go Theorem [Tier B].",
    "Let H be any self-adjoint second-order differential operator on "
    "L<super>2</super>(C<sub>Q</sub>) of the form H = -Delta<sub>A</sub> + V(x). "
    "Then the spectral zeta function of H cannot equal xi(s). The zeros of "
    "det<sub>zeta</sub>(H - s(1-s)I) cannot coincide with the nontrivial zeros of zeta(s)."
)
story.append(T(
    "The Riemann Hypothesis remains open. What is proved is that it cannot be reached "
    "through local differential Hessians on the adeles\u2014ruling out a large class of "
    "Hilbert\u2013P\u00f3lya-type programs.",
    body
))

# =====================================================================
# SECTION 14: GRAVITY AS CONDENSATION
# =====================================================================
story.append(T("14. Gravity as Geometric Condensation", h1))
story.append(T(
    "The GL order parameter W<sub>0</sub>, when identified with the Chamseddine\u2013Connes "
    "spectral action via the Seeley\u2013de Witt expansion, gives a structural isomorphism:",
    body
))
story.append(EQ(
    "alpha<sub>0</sub>|W<sub>0</sub>|<super>2</super>  <-->  "
    "cosmological constant (a<sub>0</sub>)"
))
story.append(EQ(
    "|dW<sub>0</sub>|<super>2</super>  <-->  "
    "Einstein\u2013Hilbert term (a<sub>2</sub>)"
))
story.append(EQ(
    "(beta<sub>0</sub>/2)|W<sub>0</sub>|<super>4</super>  <-->  "
    "Weyl curvature squared (a<sub>4</sub>)"
))
story.append(T(
    "Spacetime is the condensed phase of W<sub>0</sub>. The Big Bang is the phase transition "
    "at the Planck temperature. Black hole horizons are phase boundaries where the condensate "
    "decays exponentially with rate kappa (the surface gravity), simultaneously giving "
    "Hawking temperature T<sub>H</sub> = kappa/(2pi) and saturating the MSS chaos bound.",
    body
))
story.append(T(
    "The dark sector emerges naturally: dark energy is the vacuum expectation value "
    "rho<sub>0</sub> = -alpha<sub>0</sub><super>2</super>/(2 beta<sub>0</sub>); "
    "dark matter candidates are topological solitons of W<sub>0</sub>.",
    body
))
story.append(T(
    "Three falsifiable predictions: (i) the QNM gap Gamma<sub>h</sub><super>2</super> - "
    "kappa<sub>h</sub><super>2</super> = m<sub>R</sub><super>2</super> in near-extremal "
    "black holes; (ii) time-dependent dark energy w(z) detectable by DESI; "
    "(iii) GL critical exponents in near-extremal BH quasinormal mode spectra.",
    body
))
story.append(T("[Tier C \u2014 Conjectural but falsifiable]", tier_c))

# =====================================================================
# SECTION 15: 68 PROBLEMS
# =====================================================================
story.append(T("15. The 68 Problems Addressed", h1))
story.append(T(
    "RTSG provides solutions, dissolutions, or reframings for 68 open problems across "
    "12 disciplines. The following is a summary; the full treatment of each problem is "
    "available in the companion papers collection.",
    body
))

problems = [
    ("Physics (11)", [
        "1. Measurement problem \u2192 Instantiation, not collapse",
        "2. Quantum gravity \u2192 Unification in (S<super>2</super>)<super>\u221e</super>, not in P<sub>S</sub>",
        "3. Born rule \u2192 Topological overlap on S<super>2</super>",
        "4. Hierarchy problem \u2192 10<super>38</super> = complexity distance",
        "5. Equivalence principle \u2192 Awareness = inertia identity",
        "6. Arrow of time \u2192 Accumulated irreversible instantiation",
        "7. Fine-tuning \u2192 Cosmogonic cycle survivor bias",
        "8. Dark energy \u2192 Will principle (suggestive)",
        "9. Wavefunction ontology \u2192 Psi is Q<sub>S</sub>-real",
        "10. Decoherence \u2192 Distinction-loss in C<sub>S</sub>",
        "11. Quantum Zeno \u2192 Over-observation constrains C<sub>S</sub>",
    ]),
    ("Philosophy (7)", [
        "12. Hard problem \u2192 Dissolved by co-primordiality",
        "13. Zombie argument \u2192 Can't have P<sub>S</sub> without C<sub>S</sub>",
        "14. Mary's Room \u2192 New distinction on S<super>2</super>; irreversible (CIT)",
        "15. Chinese Room \u2192 Syntactic processing without C<sub>S</sub> access",
        "16. Free will \u2192 Genuine non-determinism from instantiation",
        "17. Personal identity \u2192 Continuity of hypervisor fixed point",
        "18. Mind-body problem \u2192 Three aspects of one reality",
    ]),
    ("Neuroscience (9)", [
        "19\u201327. Neural correlates, binding, WM limit (gamma/theta = 6), skill automaticity, dual-task interference, cognitive load, sleep function, attention mechanisms, gamma oscillations",
    ]),
    ("Cognitive Science (9)", [
        "28\u201336. g-factor (bifactor bridge), intelligence structure (8D vector), biases (simplex optimization), framing, expertise, transfer, creative insight, development, individual differences",
    ]),
    ("Biology (6)", [
        "37\u201342. Major transitions, Cambrian explosion, convergent evolution, consciousness evolution, colony intelligence, plant behavior",
    ]),
    ("Economics & Game Theory (7)", [
        "43\u201349. Bounded rationality, team performance, Brooks's Law, self-sabotage, homo economicus, coordination failure, market behavior",
    ]),
    ("Social, Medical, Info Theory, Cross-Disciplinary (19)", [
        "50\u201368. Cultural variation, language\u2013thought, social construction, group polarization, institutional design, addiction, PTSD, depression, schizophrenia, anesthesia, consciousness disorders, integrated information, semantic information, information\u2013physics, computational complexity, reductionism, levels of description, anthropic principle, theory of everything",
    ]),
]
for category, items in problems:
    story.append(T(category, h2))
    for item in items:
        story.append(T(item, body))

# =====================================================================
# SECTION 16: OPEN PROBLEMS
# =====================================================================
story.append(T("16. Open Problems", h1))
story.append(T(
    "Fourteen problems remain genuinely open within the framework:",
    body
))
open_problems = [
    "1. Derive 10<super>38</super> from axioms (hierarchy ratio)",
    "2. Three-space action principle (explicit Lagrangian missing)",
    "3. Measure K empirically (bridge to R exists; protocol needed)",
    "4. Define C<sub>S</sub> concretely (properties given; construction missing)",
    "5. Hypervisor equilibrium existence proof (discontinuous Id unresolved)",
    "6. Ground-state instability proof (conjecture only)",
    "7. Sheaf-theoretic localization (C<sub>S</sub> as sheaf over P<sub>S</sub>)",
    "8. Phase-space unification (Q<sub>S</sub> Hilbert + C<sub>S</sub> topology)",
    "9. S<super>2</super>-based gravity derivation (connect to Einstein field equations)",
    "10. K-matrix measurement protocol (experimental design)",
    "11. Topological phase transitions in C<sub>S</sub> (critical parameters)",
    "12. Free will mechanism (how instantiation produces non-determinism)",
    "13. Dark energy \u2194 Will quantification",
    "14. Inter-species intelligence comparison (methodology for varying n)",
]
for p in open_problems:
    story.append(T(p, body))

# =====================================================================
# SECTION 17: CONCLUSION
# =====================================================================
story.append(T("17. Conclusion: Three Spaces, One Reality", h1))
story.append(T(
    "RTSG proposes that the universe is not one space with mysterious extra properties, "
    "nor two spaces (mind and matter) with a mysterious interface, but three co-primordial "
    "spaces\u2014Q<sub>S</sub>, P<sub>S</sub>, C<sub>S</sub>\u2014all projections of a "
    "single topological object (S<super>2</super>)<super>\u221e</super>.",
    body
))
story.append(T(
    "Gravity is the ground state. Consciousness is the high-complexity state. Everything "
    "in between\u2014atoms, molecules, cells, brains, civilizations\u2014is complexity "
    "space filling up with irreversible distinctions, each one a point on S<super>2</super>, "
    "each one logarithmically approaching the singularity that every conscious being is "
    "heading toward.",
    body
))
story.append(T(
    "The Ginzburg\u2013Landau theory on the adeles provides the mathematical backbone: "
    "a unique, bounded, continuous vacuum state whose Hessian reproduces the prime-sum "
    "structure of the Weil explicit formula, together with a sharp No-Go theorem delineating "
    "exactly where local differential methods fail. The variational program survives; "
    "the spectral bridge, in its local differential form, does not. That distinction is "
    "the main mathematical lesson.",
    body
))
story.append(T(
    "The framework has survived nine rounds of adversarial review. Fifty claims have been "
    "demoted. Fifteen fatal errors have been found and repaired. What remains is a "
    "unified architecture that addresses 68 problems across 12 disciplines with a single "
    "geometric language, tagged by evidential tier, honest about what is proved, what is "
    "well-motivated, and what is conjectural.",
    body
))
story.append(T(
    "This is not the end. It is the first complete statement.",
    body
))
story.append(SP(24))
story.append(T("\u2014 Jean-Paul Niko, March 2026", epigraph))

# =====================================================================
# BUILD
# =====================================================================
def add_page_number(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFont('Times-Roman', 9)
    canvas_obj.drawCentredString(PAGE_W / 2, 0.5 * inch,
                                  f"{doc_obj.page}")
    canvas_obj.restoreState()

doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

import os
size = os.path.getsize(PDF_PATH)
print(f"Generated: {PDF_PATH}")
print(f"Size: {size:,} bytes")

---
title: "Philosophy Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "physics.hist-ph"
---

# Philosophy Companion Paper

**Jean-Paul Niko** · February 2026

\begin{center}
{\LARGE\bfseries\color{sectionblue} The Conceptual Irreversibility Theorem:  
Why Translation Between Experience  [3pt] and Description is Necessarily Lossy}

{\large Jean-Paul Niko}  [4pt]
{}  [2pt]
{\small`niko@triptomean.com`}

{\small February 2026}
\end{center}

!!! abstract "Abstract"
    
We prove that no translation from experiential content to propositional
description can be lossless.  The result---the *Conceptual
Irreversibility Theorem* (CIT)---is formulated in the language of topos
theory: each cognitive system induces a *conceptual topos*
$\mathcal{T}$ whose internal logic is a Heyting algebra (intuitionistic,
not Boolean).  The morphism from experience to description passes through
a subobject classifier $\Omega$ that is strictly richer than $\{0,1\}$;
the round-trip composition $\text{describe} \circ \text{experience}$ is a
non-invertible functor.  The *Heyting Gap*---the measure of
information destroyed---grows monotonically with cognitive sophistication
(Gap Monotonicity Theorem), formalizing the intuition that the more one
knows, the harder it is to say.  We derive corollaries for the hard
problem of consciousness, the verbalization gap in expertise research,
the structural impossibility of perfect translation between languages,
and the limits of AI alignment via natural language specification.
The result is structural, not merely epistemic: the loss is inherent
in the logical architecture of conceptual systems, not a consequence of
insufficient vocabulary or processing power.

**Keywords:** conceptual irreversibility, topos theory,
Heyting algebra, hard problem of consciousness, verbalization gap, translation loss

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Introduction}
%% ═══════════════════════════════════════════════════════════════════════════════

The hard problem of consciousness [chalmers1996] asks why physical
processes give rise to subjective experience at all.  Jackson's Knowledge
Argument [jackson1982] dramatizes the gap: Mary, the color scientist
who has never seen red, learns something new upon first seeing it---something
her complete physical knowledge did not contain.  Nagel [nagel1974]
argues that the subjective character of experience makes it impossible to
know "what it is like" to be a bat from any amount of external description.

These arguments share a structural claim: there exists information in
experience that cannot be captured by propositional description.  But the
claim remains informal.  What exactly is the logical structure of the gap?
Can it be measured?  Does it depend on the system's complexity?

This paper formalizes the gap using topos theory---a branch of category
theory that generalizes set-theoretic logic to contexts where the law of
excluded middle fails.  We prove that the description morphism is
non-invertible (the CIT), measure the lost information (the Heyting Gap),
and show that the gap grows with cognitive sophistication (Gap Monotonicity).
The result is structural: it depends on the logical architecture of
conceptual systems, not on computational limitations.

### CS (instantiation operator) as a Modeling Construct

A note on ontology is essential.  When we refer to "the CS operator" or
"experiential content," we use these terms as *modeling constructs*,
not metaphysical commitments.  Just as phase space is the space of possible
mechanical states without implying that abstract 6N-dimensional points are
physically real, the CS operator is the space of possible cognitive states.
The synonym "cognitive state space" may be used interchangeably.  The
mathematics stands regardless of one's position on the ontology of
consciousness.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Conceptual Topoi}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Conceptual Topos"
 \tA{}
A *conceptual topos* $\mathcal{T}$ is a category satisfying the topos
axioms (finite limits, exponentials, subobject classifier), whose:
[nosep]
- *objects* are concepts (mental representations, ideas, percepts),
- *morphisms* are conceptual transformations (inference, analogy,
  generalization),
- *subobject classifier* $\Omega$ encodes the truth-value structure
  of the system's internal logic.

\begin{keyeq}
**Key Structure.**\quad
In a Boolean topos (classical logic), $\Omega = \{0,1\}$ and every proposition
is either true or false.  In a Heyting topos (intuitionistic logic),
$\Omega$ is a Heyting algebra with intermediate truth values: propositions
can be "partially true" or "true relative to available evidence."
\end{keyeq}

The central claim: biological cognitive systems---and indeed any system
with graded, context-dependent truth evaluation---induce Heyting topoi,
not Boolean ones.

!!! proposition "Biological Cognition is Heyting"
 \tB{}
Any cognitive system whose truth evaluation depends on context, perspective,
or available evidence operates with an internal logic that is at most
intuitionistic (Heyting), not classical (Boolean).  Equivalently, such
systems satisfy: there exist propositions $p$ such that $p \vee \neg p$
does not hold in the system's internal logic.

!!! example "Perceptual Ambiguity"
 \tA{}
Consider the Necker cube: the proposition "the cube faces left" is neither
true nor false in the visual system's processing---it oscillates.  This is
not indecision; it is a structural feature of a non-Boolean logic.  The
subobject classifier $\Omega$ contains the truth value "bistable," which
has no counterpart in $\{0,1\}$.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
The Description Morphism}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Description Morphism"
 \tA{}
The *description morphism* is a functor
$D: \mathcal{T}_{\mathrm{exp}} \to \mathcal{T}_{\mathrm{prop}}$
from the experiential topos (the system's full conceptual space) to the
propositional topos (the subsystem accessible to linguistic description).
The *experience morphism* is a functor
$E: \mathcal{T}_{\mathrm{prop}} \to \mathcal{T}_{\mathrm{exp}}$
going the other direction (interpreting descriptions as experiences).

The question is: does the round-trip $E \circ D$ recover the original
experience?

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
The Conceptual Irreversibility Theorem}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Conceptual Irreversibility Theorem (CIT)"
 \tA{}
Let $\mathcal{T}_{\mathrm{exp}}$ be a Heyting topos and
$\mathcal{T}_{\mathrm{prop}}$ be a Boolean topos.  Then no functor
$D: \mathcal{T}_{\mathrm{exp}} \to \mathcal{T}_{\mathrm{prop}}$ admits
a left inverse: there is no functor $E$ such that $E \circ D = \mathrm{Id}$.
Equivalently, the round-trip $D \circ E \circ D \neq D$ in general.

??? proof "Proof"
[Proof sketch]
The subobject classifier of $\mathcal{T}_{\mathrm{exp}}$ is a Heyting
algebra $\Omega_H$ with $|\Omega_H| > 2$.  The subobject classifier of
$\mathcal{T}_{\mathrm{prop}}$ is $\Omega_B = \{0,1\}$.  Any functor
$D$ must map $\Omega_H \to \Omega_B$, which is a surjection from a
richer to a poorer truth-value structure.  By the pigeonhole principle,
$D$ identifies distinct truth values in $\Omega_H$ that map to the same
value in $\Omega_B$.  Any functor $E: \Omega_B \to \Omega_H$ cannot
recover which pre-image was intended.  Therefore $E \circ D \neq
\mathrm{Id}_{\mathcal{T}_{\mathrm{exp}}}$.

\begin{keyeq}
**Key Result.**\quad
The CIT says: *translating experience into propositions necessarily
destroys information*.  This is not a claim about vocabulary poverty or
computational limits---it is a *logical* impossibility rooted in
the mismatch between Heyting and Boolean truth-value structures.
\end{keyeq}

!!! corollary "The Hard Problem Has a Shape"
 \tB{}
The hard problem of consciousness is not merely "difficult"---it has a
precise mathematical structure.  The experiential content that resists
propositional capture is exactly the content whose truth values lie in
$\Omega_H \setminus \{0,1\}$: the intermediate, graded, context-dependent
truth values that have no Boolean counterpart.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
The Heyting Gap}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Heyting Gap"
 \tA{}
The *Heyting Gap* of a cognitive system with experiential topos
$\mathcal{T}_{\mathrm{exp}}$ and propositional topos
$\mathcal{T}_{\mathrm{prop}}$ is:

\[
\mathcal{G}(\mathcal{T}_{\mathrm{exp}}, \mathcal{T}_{\mathrm{prop}}) =
\log_2 |\Omega_H| - \log_2 |\Omega_B| = \log_2 |\Omega_H| - 1.
\]

For continuous Heyting algebras, replace cardinality with the
topological dimension of $\Omega$.

The Heyting Gap measures the bits of experiential information destroyed
by the description morphism.

!!! theorem "Gap Monotonicity"
 \tA{}
Let $\mathcal{T}_1 \hookrightarrow \mathcal{T}_2$ be an inclusion of
conceptual topoi (i.e., $\mathcal{T}_2$ has strictly more concepts and
richer internal logic).  Then
$\mathcal{G}(\mathcal{T}_2) \geq \mathcal{G}(\mathcal{T}_1)$.

\begin{keyeq}
**Key Result: the more you know, the harder it is to say.**\quad
Gap Monotonicity formalizes a deep intuition: experts struggle to
articulate their expertise not because of laziness or poor communication
skills, but because their experiential topos has grown richer while
the propositional topos has not kept pace.  The gap is a *theorem*,
not an observation.
\end{keyeq}

!!! corollary "Verbalization Gap"
 \tB{}
Expert knowledge resists verbalization in proportion to its experiential
richness.  Hinds' "curse of knowledge" [hinds1999] and Dreyfus
& Dreyfus' observation that expert skill is largely non-propositional
[dreyfus1986] are consequences of Gap Monotonicity.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Corollaries and Applications}
%% ═══════════════════════════════════════════════════════════════════════════════

### The Hard Problem Dissolved

The three-space ontology (Part XIII) goes beyond *reformulating* the hard problem---it *dissolves* it.  The hard problem asks: "Why is there something it is like to be a physical system?"  Under the co-primordial thesis, the answer is: consciousness ($\CSp$) is not something that needs to "arise" from physical systems.  It has existed co-primordially with $\QS$ and $\PS$ since moment zero.  The question is not "how does matter produce consciousness?" but "how does consciousness *complexify* through its interaction with matter?"  The hard problem was hard because it was formulated within a single-space materialist framework that lacked the ontological resources to state the answer.

The structural parallel with quantum gravity is exact and illuminating.  The unrenormalisable infinities of perturbative quantum gravity arise from trying to describe a three-space phenomenon (gravity as proto-consciousness) entirely within $\QS$---the mathematics returns `NaN` because the domain is wrong.  The hard problem of consciousness arises from trying to derive a three-space phenomenon (consciousness) entirely from $\PS$---the explanation returns "explanatory gap" because the ontological domain is wrong.  In both cases, the apparent intractability is not a sign that the problem is genuinely hard; it is a *diagnostic* that the single-space framework lacks the structure to pose the question well.  Fix the domain---include all three spaces---and the infinities resolve and the gap closes, not through clever new arguments but because the type error has been corrected.

Qualia are *private instantiations*: the specific way a particular consciousness projects a particular $\QS$-configuration into its own $\PS$.  The privacy of qualia follows from the irreducible individuality of the instantiation operator $\Inst_\alpha$; no two consciousnesses project identically.

Free will is *lateral temporal navigation*: the freedom of consciousness to move in the $t_{\mathrm{lat}}$ direction of complex time $t_\CSp = t_\mathbb{R} + i\,t_{\mathrm{lat}}$.  This is neither compatibilist (determined by prior causes) nor libertarian (random); it is *structured navigation* of a complex temporal manifold, constrained by the Id filter but not eliminated by it.

### The Hard Problem Reformulated

The CIT does not solve the hard problem, but it gives it a precise shape.
The explanatory gap between physical processes and subjective experience
corresponds to the Heyting Gap between the experiential topos and the
propositional (scientific) topos.  Closing the gap would require either
(a) enriching scientific language to a Heyting logic (abandoning excluded
middle in physics), or (b) showing that biological cognition is actually
Boolean (contradicting the evidence of perceptual ambiguity, graded
beliefs, and context-dependent truth).

### Mary's Room

Jackson's Mary [jackson1982] knows all physical facts about color but
has never seen red.  In our formalism: Mary's propositional topos contains
all Boolean truths about color, but the experiential topos of seeing red
has Heyting truth values (phenomenal gradations, context-dependent
saturation, affective valence) that $\{0,1\}$ cannot represent.  When
Mary sees red, her experiential topos expands; the new content was
*provably* not in her propositional topos.

### What Is It Like to Be a Bat?

Nagel's question [nagel1974] concerns the overlap between human and
bat experiential topoi.  The *overlap subspace*
$\mathcal{T}_{\mathrm{overlap}} = \mathcal{T}_{\mathrm{human}} \cap
\mathcal{T}_{\mathrm{bat}}$ has smaller $\Omega$ than either system's
full topos.  The CIT predicts that the human description of bat experience
is lossy by exactly $\mathcal{G}(\mathcal{T}_{\mathrm{bat}},
\mathcal{T}_{\mathrm{overlap}})$ bits---the part of bat experience that
has no counterpart in human conceptual space.

### Translation Between Languages

Each natural language induces a conceptual topos $\mathcal{T}_L$ via its
lexical and grammatical resources.  Translation from language $L_1$ to
$L_2$ passes through the overlap $\mathcal{T}_{L_1} \cap \mathcal{T}_{L_2}$.
The CIT predicts that perfect translation is impossible whenever the source
topos has concepts outside the overlap---precisely when "untranslatable"
words exist.  This is Jakobson's dictum formalized: "languages differ in
what they must convey" because their topoi have different subobject
classifiers [jakobson1959].

### AI Alignment

The CIT has implications for AI alignment.  If human values are encoded
in a Heyting experiential topos but alignment specifications use Boolean
propositional logic, then no specification can fully capture the intended
values.  The Heyting Gap measures the irreducible alignment loss---the
extent to which "what we mean" exceeds "what we can say."  This
suggests that alignment via natural language instruction alone has a
provable ceiling; complementary approaches (demonstration, feedback,
constitutional methods) are structurally necessary.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Engagement with Existing Frameworks}
%% ═══════════════════════════════════════════════════════════════════════════════

### Integrated Information Theory (IIT)

Tononi's IIT [tononi2004] measures consciousness via integrated
information $\Phi$.  In our framework, $\Phi$ is related to the
spectral structure of the compatibility matrix $\bK$ governing
cross-type interactions.  The conceptual topos adds a layer IIT lacks:
the *logical structure* of integration, not just its quantity.
Two systems with equal $\Phi$ may have different Heyting Gaps if their
internal logics differ.

### Global Workspace Theory

Baars' GWT [baars1988] identifies conscious access with global
broadcast.  The CIT is compatible: the broadcast content is the
propositionally accessible portion of the experiential topos.  What
GWT calls "unconscious processing" corresponds to experiential content
whose truth values lie in $\Omega_H \setminus \Omega_B$---present in
the system but not available for propositional report.

### G\"ardenfors' Conceptual Spaces

G\"ardenfors [gardenfors2000] models concepts as convex regions in
quality spaces.  Our conceptual topos generalizes this: G\"ardenfors'
spaces are the geometric realization of a particular class of topoi
(presheaf topoi over quality dimensions).  The CIT applies to any
topos, not only geometric ones.

### Quine's Indeterminacy

Quine's indeterminacy of translation [quine1960] is epistemic:
we cannot determine the correct translation scheme from behavioral
evidence alone.  The CIT is structural: even with complete knowledge
of both systems, the translation morphism is non-invertible.  The two
results are complementary, not competing: Quine says we cannot know the
mapping; the CIT says no perfect mapping exists.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Discussion}
%% ═══════════════════════════════════════════════════════════════════════════════

### Objections and Responses

*Objection 1: Why should cognition be Heyting?*  The evidence is
behavioral (perceptual ambiguity, graded beliefs, context-dependent truth
evaluation) and computational (neural networks naturally implement graded
activation, not Boolean gates).  If a convincing argument emerged that
biological cognition is Boolean, the CIT would not apply---but the
burden of proof lies with the Boolean hypothesis.

*Objection 2: Is this just Gödel incompleteness in disguise?*
No.  Gödel's theorems concern provability within formal systems; the CIT
concerns translatability between logical systems with different truth-value
structures.  A Heyting topos is not "incomplete"---it is complete within
its own logic.  The loss occurs at the *boundary* between two logics.

*Objection 3: Topos theory is too abstract for empirical science.*
The abstraction is the point: the CIT applies to *any* cognitive
system with Heyting internal logic, regardless of substrate.  Concreteness
comes from the applications (Mary's Room, translation, alignment), each
of which yields testable or at least evaluable predictions.

### Limitations

The proof assumes that propositional systems are Boolean.  If propositional
language can itself be enriched to Heyting logic (e.g., through vagueness
or fuzzy predicates), the gap shrinks but does not vanish as long as the
experiential Heyting algebra is strictly richer.  The cardinality-based
Gap measure (Definition *ref:def:gap*) is coarse; a finer measure using
Heyting algebra homomorphism theory would capture structural, not just
quantitative, differences.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Conclusion}
%% ═══════════════════════════════════════════════════════════════════════════════

The Conceptual Irreversibility Theorem establishes that translation from
experience to description is necessarily lossy---a logical, not merely
practical, limitation.  The Heyting Gap measures the information destroyed,
and Gap Monotonicity shows it grows with cognitive sophistication.  The
result gives the hard problem of consciousness a precise mathematical
shape, formalizes the expert verbalization gap, predicts the structural
impossibility of perfect translation, and identifies a provable ceiling
on alignment via natural language specification.  Whether one regards
this as a contribution to philosophy, mathematics, or cognitive science
depends on one's disciplinary home; the theorem itself is indifferent to
the classification.

%% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Axiom 0, GNEP Person Definition, Moral Framework (TMP-20260217)

**Axiom 0 — Relational Primacy:** *Only relational reality admits absolutes and infinities.* Physical space P has bounded quantities; relational space ℛ does not. Mathematical objects including infinite sets exist in ℛ — this resolves the Platonism problem. Cantor's diagonal argument is a theorem about relational structure, not physical objects.

**Person as GNEP Hypervisor:** A person P is a GNEP hypervisor node: cognitive assembly with |A(P)| ≥ 1 agents under coordination and a self-assembly property. Personhood is functional, not substrate-bound.

**Moral Framework — Id_extended:**

$$\max \left\{ \frac{d}{dt}\left[ \sum_{\text{all agents } \alpha} \text{life\_force}(\alpha) \right] \right\}$$

This is a cooperative Nash equilibrium: no agent can increase total life force by unilateral deviation. The moral action is not agent-relative — life force is one undifferentiated quantity maximized globally.

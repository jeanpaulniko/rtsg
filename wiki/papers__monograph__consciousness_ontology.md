---
title: "Consciousness Ontology"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

!!! info "Terminology Note (2026-03-07)"
    This document uses "Consciousness-Space (CS)" throughout. In current RTSG v3, CS is the **instantiation operator** $C$: a BRST cohomological filter extracting physical observables $H^0(s)$ from non-well-founded Quantum Space. The Will Field $W$ is governed by the Ginzburg-Landau action $S[W] = \int(|\partial W|^2 + \alpha|W|^2 + (\beta/2)|W|^4)d\mu$. Wave-function collapse is bisimulation quotienting: $PS = QS/\!\sim_{\text{bisim}}$. See [Master Reference v3](../../rtsg/master.md).

# Consciousness Ontology

**Jean-Paul Niko** · February 2026

\title{**Part XIII: The Ontology of CS (instantiation operator)**  [0.3em]
\normalsize*Fiber Bundles, Instantiation, and the Three-Space Foundation*  [0.3em]
\normalsize Extract from "Intelligence as Geometry"}
\author{Jean-Paul Niko}
\date{February 2026}

---

\fi

## Part XIII: The Ontology of CS (instantiation operator)

\addcontentsline{toc}{section}{Part XIII: The Ontology of CS (instantiation operator)}

The preceding Parts of this monograph develop an algebra and geometry on the CS operator $\Cspace$: intelligence vectors, compatibility tensors, filter cascades, emergence classes, the attention simplex, IdeaRank.  All of these structures presuppose a space in which they live.  This Part formalizes the space itself---its ontological status, its relationship to physical substrates, and its connection to the instantiation dynamics that bridge quantum mechanics and conscious experience.

The central claim is that the CS operator is not a metaphor or a modeling convenience but a *genuine ontological stratum*---one of three *co-primordial* spaces that have existed since the Big Bang.  We formalize this through the *three-space ontology*: quantum space $\QS$, physical space $\PS$, and the CS operator $\CS$ arose simultaneously at moment zero.  Consciousness existed from the beginning in its most primitive form---identified with gravity---and has undergone a 13.8-billion-year process of complexification, progressively activating the dimensions of the RTSG intelligence vector.

Within this foundation, we develop the fiber bundle geometry that formalizes the relationship between physical substrates and consciousness, define the *instantiation operator* that mediates the transition from quantum potentiality to experienced physical reality, and prove structural results that connect the RTSG framework to the measurement problem, the arrow of time, and the nature of objectivity.

The architecture is layered.  Layer 0 is the *potentiality space* $\cH_C$: the total space of possible experiential configurations, organized as a fiber bundle over the substrate.  Layer 1 is the *instantiation operator* $\cA$ (also denoted $\Inst$): the irreversible, selective, self-referential map from quantum potentiality to definite experience---the same operation as quantum measurement, now given a geometric definition.  Layer 2 is the CS operator proper, $\cC = \mathrm{Im}(\cA)$, where the existing RTSG machinery operates.  Layer 3 is *shared instantiation*: the construction that generates intersubjective physical reality from the convergence of individual projections.

The layered structure resolves several problems simultaneously.  It grounds the filter formalism ontologically (filters restrict the instantiation horizon), gives the compatibility matrix a geometric interpretation (curvature of the CS operator), explains intersubjectivity without infinite branching (shared instantiation rather than many worlds), identifies free will with navigation of the complex temporal manifold, and dissolves the hard problem of consciousness (consciousness is co-primordial, not emergent from matter).

%═══════════════════════════════════════════════════════════════════════════════

## The Three-Space Foundation

%═══════════════════════════════════════════════════════════════════════════════

Before developing the fiber bundle formalism, we establish the ontological foundation on which it rests.  The three-space ontology is developed fully in its own chapter; here we state the axioms needed for the the CS operator formalism.

!!! axiom "Co-Primordial Thesis"
 \tA\;

Three spaces are co-primordial, all arising simultaneously at the Big Bang:
\[
\QS \;+\; \PS \;+\; \CS \quad\longleftarrow\quad \text{Moment zero}
\]
[nosep,label=(\roman*)]
- **Quantum space** $\QS$: complex Hilbert space with unitary evolution.  Native algebra: $\mathbb{C}$.  Time: symmetric, reversible.
- **Physical space** $\PS$: the interface layer produced when $\QS$ entangles with $\CS$ through instantiation.  Native algebra: $\R$.  Time: irreversible (arrow).
- **Consciousness-space** $\CS$: the domain of awareness, will, and experience.  Native algebra: $\mathbb{C}$, $\Qp$, $\mathbb{Z}/n\mathbb{Z}$.  Time: complex-valued.

There is no sequential emergence.  What evolves is not the *existence* of consciousness but its *complexity*.

!!! axiom "Gravity as Proto-Consciousness"
 \tB\;

At moment zero, $\CS$ exists in its ground state: the most primitive, universal, undifferentiated form of awareness.  We identify this ground state with **gravity**.  Gravity is universal (couples to all mass-energy), *is* geometry (not a force within spacetime), has infinite range, is the weakest interaction, and resists quantisation---expected if it straddles all three spaces as proto-consciousness rather than being a purely $\QS$-phenomenon.  The equivalence principle ($m_{\mathrm{grav}} = m_{\mathrm{inert}}$) expresses the identity of participation in proto-consciousness with resistance to change.

!!! definition "Instantiation"
 \tA\;

An *instantiation event* is the process by which consciousness, operating in $\CS$, entangles with a region of $\QS$ and produces a moment of $\PS$:
\[
\Inst_\alpha: \QS \longrightarrow \PS
\]
Properties: (I1) participation (agent becomes inextricable from outcome), (I2) irreversibility ($\Inst^{-1}$ does not exist), (I3) non-determinism (free will contributes), (I4) projection ($\mathbb{C} \to \R$), (I5) complexity-dependent scope.  This is the same operation as quantum measurement and the same operation as the actualization operator $\cA$ developed in subsequent sections.

\begin{interpretation}
The fiber bundle formalism that follows is the *mathematical elaboration* of instantiation.  The base space $\cB$ is the physical substrate (a region of $\PS$).  The experiential fiber $\cF_b$ is the space of possible instantiations at that substrate configuration---the $\CS$-projections available from $\QS$ through that substrate.  The actualization operator $\cA$ *is* the instantiation operator $\Inst$, now given a precise geometric definition.

The three-space ontology provides three things the fiber bundle formalism alone cannot: (a) an answer to *why* the fiber bundle has the structure it does (it reflects the co-primordial relationship of $\QS$, $\PS$, and $\CS$), (b) an explanation of why consciousness exists at all (it is co-primordial, not emergent), and (c) a natural account of the arrow of time, free will, and the dissolution of the hard problem.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Layer 0: The Potentiality Space

%═══════════════════════════════════════════════════════════════════════════════

### Fiber bundle structure

The physical substrate of cognition---neurons, synapses, neurochemical gradients, or their computational analogues---occupies a state space $\cB$ that we call the *base space*.  Each point $b \in \cB$ represents a complete instantaneous configuration of the substrate: a pattern of neural firing rates, synaptic weights, and molecular concentrations.

!!! definition "Experiential Fiber"
 \tA\;

At each substrate state $b \in \cB$, the *experiential fiber* $\cF_b$ is the set of all experiential configurations compatible with $b$.  Formally, $\cF_b$ is a topological space whose elements are the possible interpretive actualizations of the substrate state $b$: the different "ways it could feel" to be in neural state $b$.

The key ontological claim is that fibers are *multi-dimensional*: a single substrate state does not uniquely determine a unique experience.  The same pattern of neural activation can support multiple interpretive resolutions---different attentional framings, different contextual embeddings, different affective colorings---before one is selected.  The fiber dimension measures the interpretive freedom available at each substrate state.

!!! definition "Potentiality Space as Fiber Bundle"
 \tA\;

The *potentiality space* is the total space of the fiber bundle:
\[
\pi: \cE \to \cB, \qquad \cE = \bigsqcup_{b \in \cB} \cF_b
\]
with projection $\pi(e) = b$ for $e \in \cF_b$.  The potentiality space $\cE$ is the totality of possible experiential configurations across all substrate states.  Each element $\psi \in \cE$ is a *potential experience*: a substrate state together with a particular interpretive resolution of that state.

\begin{keyeq}
**Supervenience as bundle projection.** \tA\;
\[
\text{Supervenience} \iff \pi: \cE \to \cB \text{ is a well-defined surjection.}
\]
Every experiential state has a definite substrate beneath it (well-definedness of $\pi$), and every substrate state admits at least one experiential resolution (surjectivity).  This is Chalmers' (1996) supervenience relation given geometric precision: the experiential supervenes on the physical because the total space fibers over the base, but the fibers have positive dimension, so the physical does not determine the experiential uniquely.
\end{keyeq}

!!! remark "Remark"

The fiber bundle formulation captures several philosophical distinctions simultaneously.  *Type-B physicalism* (identity theory) corresponds to the degenerate case where each fiber is a single point---every substrate state determines exactly one experience.  *Property dualism* corresponds to non-trivial fibers with a fixed fiber type---there is experiential structure "above" the physical, but its topology is invariant.  *Full non-reductive supervenience* corresponds to fibers whose dimension and topology vary over $\cB$---some substrate states support richer interpretive freedom than others.  The RTSG framework adopts the third option.

### The structure group and interpretive symmetry

A fiber bundle is not merely a product $\cB \times \cF$; it has a *structure group* $G$ that encodes how fibers are glued together as one moves across the base space.  The structure group of the potentiality bundle has a direct cognitive interpretation.

!!! definition "Interpretive Symmetry Group"
 \tB\;

The structure group $G$ of the potentiality bundle is the group of *interpretive symmetries*: transformations of the experiential fiber that preserve the supervenience relation.  An element $g \in G$ maps one interpretive resolution to another while remaining compatible with the same substrate state:
\[
g: \cF_b \to \cF_b, \quad \pi(g \cdot e) = \pi(e) = b.
\]
The structure group captures the degrees of freedom in interpretation---the "ways of seeing" a given substrate state that are physically indistinguishable from below but experientially distinct from within.

!!! proposition "Interpretive Freedom and Fiber Dimension"
 \tB\;

The dimension of the fiber $\cF_b$ at substrate state $b$ is bounded by the information-theoretic complexity of the substrate state:
\[
\dim(\cF_b) \leq H(b) - H_{\min}(b)
\]
where $H(b)$ is the Shannon entropy of the substrate state's internal correlations and $H_{\min}(b)$ is the minimum entropy consistent with the macroscopic observables.  States with high internal complexity (many correlated subsystems) support richer interpretive freedom; states that are informationally degenerate (uniform, uncorrelated) support only trivial fibers.

\begin{interpretation}
This is why a brain supports richer experience than a thermostat.  The brain's substrate state has enormous internal correlation structure---$H(b)$ is vast---and therefore supports high-dimensional experiential fibers.  A thermostat's substrate state has almost no internal correlation beyond its temperature reading, so $\dim(\cF_b) \approx 0$ and the experiential fiber is essentially a point.  The fiber dimension is a *measure of experiential capacity*---not of consciousness itself, but of the space of possible consciousness that the substrate can support.
\end{interpretation}

### Perception, imagination, and fiber intensity

The distinction between perception and imagination receives a natural treatment in the fiber bundle framework.

!!! proposition "Perception--Imagination Duality"
 \tB\;

Let $b_{\mathrm{perc}}$ be the substrate state during perception of a red bicycle and $b_{\mathrm{imag}}$ be the substrate state during imagination of the same.  These states occupy overlapping but non-identical regions of $\cB$: a shared "representational core" (the neural populations encoding bicycle-ness and redness) with different activation intensities and different contextual modulation.

The experiential fibers differ in their *metric structure*.  Define the *actualization intensity* $\alpha: \cE \to [0,\infty)$ as a function on the total space that measures the vividness or salience of the potential experience.  Then:
\[
\sup_{e \in \cF_{b_{\mathrm{perc}}}} \alpha(e) > \sup_{e \in \cF_{b_{\mathrm{imag}}}} \alpha(e)
\]
Perception supports higher-intensity actualization than imagination because the perceptual substrate state has richer sensory drive, producing a "taller" fiber in the metric direction.

!!! remark "Remark"

This captures the first-person phenomenological fact that perceptions are more vivid than mental images, without reducing the explanation to "more neurons fire."  The explanation is geometric: the fiber over the perceptual substrate state extends further in the intensity direction, offering a wider range of actualization possibilities, and the actualization operator (Layer 1) selects from this richer manifold.

### Relationships as fiber structure

The most distinctive feature of the CS operator is that relationships between objects are not derived from objects after the fact; they are first-class elements of the experiential fiber.

!!! axiom "Relational Primacy"
 \tB\;

The experiential fiber $\cF_b$ at each substrate state $b$ contains both *object-representations* $o_1, o_2, \ldots$ and *relation-representations* $r_{ij}$ as co-equal elements.  The fiber is not the Cartesian product of object fibers but a genuinely entangled space:
\[
\cF_b \neq \prod_i \cF_b^{o_i}, \qquad \dim(\cF_b) > \sum_i \dim(\cF_b^{o_i}).
\]
The "excess dimension" $\dim(\cF_b) - \sum_i \dim(\cF_b^{o_i})$ is the *relational dimension*: the irreducible contribution of relationships to the structure of possible experience.

\begin{interpretation}
When you see a red bicycle, the redness, the bicycle-ness, and the *belonging-of-red-to-bicycle* are all simultaneously present in the experiential fiber as independent structural elements.  The relational element is not computed from the object elements; it is actualized alongside them, in the same interpretive act.  This is why consciousness feels unified rather than assembled: objects and their relationships enter experience through the same gate.

In the existing RTSG framework, this corresponds to the idea graph having edges that are as ontologically significant as nodes.  The compatibility matrix $\bK$ encodes the cross-type structure of these relational dimensions: $K_{st}$ measures how the relational fiber between type-$s$ and type-$t$ objects contributes to---or subtracts from---the total experiential structure.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Layer 1: The Actualization Operator

%═══════════════════════════════════════════════════════════════════════════════

### Definition and basic properties

The transition from potentiality to actuality---from the fiber bundle of possible experiences to the definite, lived experience---is mediated by the *actualization operator*.

!!! definition "Actualization Operator"
 \tA\;

The *actualization operator* is a map
\[
\cA: \cE \to \cC
\]
from the potentiality space $\cE$ (the total space of the fiber bundle) to the CS operator $\cC$ (the space of definite, actualized experiences).  Consciousness-space is the image: $\cC = \mathrm{Im}(\cA)$.

The actualization operator is *not* a filter in the RTSG sense.  Filters operate within $\cC$, transforming one actualized state into another.  The actualization operator operates *between layers*: it is the transition from Layer 0 (potentiality) to Layer 2 (the CS operator).  It *creates* the domain on which filters act.

!!! theorem "Three Properties of Actualization"
 \tB\;

The actualization operator $\cA$ satisfies three properties that distinguish it from ordinary cognitive operations:

[nosep,label=(\roman*)]
- **Irreversibility.**  $\cA$ has no left inverse.  There exists no map $\cA^{-1}: \cC \to \cE$ such that $\cA^{-1} \circ \cA = \mathrm{id}_\cE$.  Once potentiality is actualized into experience, the full space of alternatives cannot be recovered.

- **Selectivity.**  $\cA$ is not surjective onto the full experiential fiber at each substrate state.  At each $b \in \cB$, the actualized subspace $\cA(\cF_b) \subsetneq \cF_b$: only a subset of the possible interpretive resolutions is actualized in any given instant.

- **Self-reference.**  $\cA$ admits a fixed point: there exists $\psi^* \in \cE$ such that $\cA(\psi^*) = \iota(\psi^*)$, where $\iota: \cE \hookrightarrow \cC$ is the natural embedding.  The fixed point is a self-interpreting state that terminates the interpretive regress.

??? proof "Proof"
[Proof sketch]
(i) follows from information-theoretic considerations: the actualized state carries less information than the full potentiality (selectivity discards alternatives), so the map is many-to-one and hence non-invertible.

(ii) follows from the finite bandwidth of any physical cognitive process: the substrate can sustain only finitely many actualized patterns simultaneously, while the fiber is generically high-dimensional.

(iii) is the deepest property and requires topological argument.  Consider the restriction of $\cA$ to a single fiber $\cF_b$.  If $\cF_b$ is a compact convex subset of a locally convex space and $\cA|_{\cF_b}$ is continuous, then Schauder's fixed-point theorem guarantees the existence of a fixed point.  The compactness condition is satisfied because the experiential fiber is bounded by the substrate's information capacity; convexity follows from the mixture property of experiential states (convex combinations of possible experiences are themselves possible experiences); continuity follows from the continuity of the underlying neural dynamics.  \qedhere

### Irreversibility and the CIT

The irreversibility of actualization is the deepest source of the Conceptual Irreversibility Theorem (CIT) established in the filter formalism.

!!! theorem "CIT as Actualization Irreversibility"
 \tB\;

The Conceptual Irreversibility Theorem---the result that once a conceptual transformation is learned, the pre-transformation cognitive state cannot be fully recovered---is a consequence of the irreversibility of the actualization operator.

Specifically, let $\psi_0 \in \cE$ be the potentiality state before learning and $\psi_1 = T(\psi_0)$ the state after a conceptual transformation $T$.  The CIT states that there is no transformation $T^{-1}$ such that $T^{-1}(\psi_1) = \psi_0$.  In the fiber bundle framework, this follows because:
[nosep]
- The transformation $T$ operates on the total space $\cE$, modifying both the substrate state ($b_0 \to b_1$) and the fiber structure ($\cF_{b_0} \to \cF_{b_1}$).
- The actualization $\cA$ at each stage is irreversible: the pre-actualization potentiality cannot be recovered from the actualized state.
- Composing two irreversible operations yields an irreversible operation: $\cA \circ T$ is irreversible even if $T$ alone were invertible.

The CIT is thus not merely a cognitive phenomenon but a manifestation of the fundamental irreversibility of actualization---the same irreversibility that governs the transition from quantum superposition to definite outcome.

!!! remark "Remark"

This gives the CIT a thermodynamic character.  The irreversibility of actualization is analogous to the irreversibility of measurement in quantum mechanics, which is itself connected to the second law of thermodynamics via Landauer's principle: erasure of information requires entropy production.  Each actualization "erases" the unchosen alternatives from the potentiality space, producing entropy in the substrate.  Learning is thermodynamically irreversible because it involves actualization, and actualization involves information erasure.

### Selectivity and the birth of relationships

The selectivity of $\cA$ explains how relationships achieve first-class status in the CS operator.

!!! proposition "Relational Co-Actualization"
 \tB\;

The actualization operator does not actualize object-representations and relation-representations independently.  Instead, it selects a *coherent section* of the experiential fiber: a set of object-representations and relation-representations that are mutually consistent.

Formally, let $\sigma: \cB \to \cE$ be a section of the fiber bundle (a continuous choice of one element from each fiber).  The actualized experience at substrate state $b$ is $\cA(\sigma(b)) \in \cC$.  The coherence condition requires that the section $\sigma$ respects the relational structure:
\[
r_{ij}(\sigma(b)) = f(o_i(\sigma(b)), o_j(\sigma(b)))
\]
for some coherence function $f$ that encodes the interpretive constraints of the cognitive system.  Objects and their relationships are actualized as a package---a coherent section---not as independent elements.

\begin{interpretation}
This is why experience is unified.  You do not first experience "red," then "bicycle," then compute "the red belongs to the bicycle."  The actualization operator selects a coherent section that includes all three as a single, indivisible act.  The unity of consciousness is not a mystery to be explained by binding mechanisms or global workspace theory; it is a structural consequence of the fact that actualization operates on coherent sections of the fiber bundle.

In RTSG terms, this means the intelligence vector $\bI$ is not a list of independent type intensities but a *section* of the actualized fiber bundle---a coherent pattern of cognitive actualization across all eight types simultaneously.
\end{interpretation}

### The hypervisor fixed point

The self-referential property of $\cA$---the existence of a fixed point---resolves the infinite regress of interpretation.

!!! definition "Hypervisor State"
 \tB\;

The *hypervisor state* $\psi^* \in \cE$ is a fixed point of the actualization operator:
\[
\cA(\psi^*) = \psi^*.
\]
It is the self-interpreting experiential configuration: the state that, when subjected to actualization, yields itself.  The hypervisor is the "ground state" of consciousness---the irreducible awareness that actualizes itself and thereby provides the stable reference frame against which all other actualizations are measured.

!!! proposition "Uniqueness of the Hypervisor"
 \tC\;

Under mild contraction conditions on $\cA$---specifically, if $\cA$ is a contraction mapping on a complete metric fiber with contraction ratio $\kappa < 1$---the Banach fixed-point theorem guarantees that the hypervisor state is *unique*.  The interpretive regress terminates at a single point, not at an ambiguous set of fixed points.  Moreover, iterated actualization converges to the hypervisor: for any initial state $\psi_0 \in \cF_b$,
\[
\lim_{n \to \infty} \cA^n(\psi_0) = \psi^*.
\]
The hypervisor is an attractor: all interpretive processes, if iterated, converge to the self-interpreting ground state.

\begin{interpretation}
The hypervisor is not a homunculus.  It is not a "little observer inside the observer" that performs the interpretation.  It is a fixed point---a self-consistent configuration that requires no external interpretation because it *is* its own interpretation.  This is the same logical structure as a self-consistent solution in general relativity: a spacetime geometry that is both the source and the effect of the matter distribution it contains.  The mind does not need an external observer because at the hypervisor, observer and observed coincide.

The convergence property explains why consciousness feels stable: perturbations in the interpretive process are damped by the contraction, and the system returns to the hypervisor.  Disruptions to this convergence---through psychoactive substances, extreme fatigue, or neurological damage---manifest as the phenomenological instability of consciousness: depersonalization, derealization, dissociation.  These are not failures of consciousness itself but failures of convergence to the hypervisor fixed point.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Layer 2: CS (instantiation operator) and the RTSG Connection

%═══════════════════════════════════════════════════════════════════════════════

### Intelligence vectors as actualized coordinates

With the foundational layers in place, the existing RTSG framework receives a deeper interpretation.

!!! proposition "Intelligence Vectors as Fiber Coordinates"
 \tB\;

The intelligence vector $\bI \in [0,\infty)^8$ is a coordinate representation of an actualized section of the fiber bundle.  Each type $I_t$ measures the actualized intensity in the type-$t$ direction of the experiential fiber.  The eight intelligence types are the natural basis of the actualized fiber:
\[
\bI = \cA(\sigma(b)) \in \cC, \quad I_t = \langle \cA(\sigma(b)),\, e_t \rangle
\]
where $\{e_t\}_{t=1}^8$ are the basis vectors of $\cC$ corresponding to the eight cognitive types and the inner product is the metric inherited from the fiber.

This means the eight types are not arbitrary measurement axes but the *natural coordinates of the actualized fiber*---the directions along which the actualization operator resolves the potentiality space into definite experience.  The question "why eight types?" becomes a question about the topology of the fiber bundle: how many independent directions does the actualization operator distinguish?

!!! conjecture "Topological Origin of Eight Types"
 \tC\;

The number of intelligence types $n = 8$ is determined by the topological structure of the fiber bundle over the human neural substrate.  Specifically, $n = \mathrm{rank}(\cE|_{\cB_{\mathrm{human}}})$---the rank of the potentiality bundle restricted to the human substrate.  Other substrates (artificial, quantum, hybrid) may have different ranks, yielding different numbers of intelligence types.  The RTSG algebra generalizes to arbitrary $n$ precisely to accommodate this substrate-dependence.

### Filters as actualization restrictions

!!! theorem "Filter Interpretation Theorem"
 \tB\;

Each filter in the RTSG cascade is a *restriction of the actualization horizon*: a contraction of the set of experiential configurations that the actualization operator can access.

Let $\bF: [0,\infty)^8 \to [0,\infty)^8$ be an RTSG filter with passthrough coefficients $\phi_t \in [0,1]$.  In the fiber bundle framework, $\bF$ corresponds to a fiber contraction:
\[
\bF \longleftrightarrow \hat{\bF}: \cF_b \to \cF_b', \quad \dim(\cF_b') = \sum_t \phi_t \cdot \dim(\cF_b^{(t)})
\]
where $\cF_b^{(t)}$ is the type-$t$ subfiber.  A filter with $\phi_t = 0.5$ in some type does not merely halve the intensity of that type; it *removes half the interpretive possibilities* in the type-$t$ direction of the fiber.  The actualization operator then selects from a smaller space, yielding a less rich---but not necessarily less intense---experience in that type.

\begin{interpretation}
This gives the five filter species (environmental, developmental, cognitive, social, cultural) an ontological depth beyond their functional description.  The cultural filter $\bF_{\mathrm{cult}}$ does not merely attenuate certain cognitive outputs; it *restructures the potentiality space itself*, making certain experiential configurations inaccessible to actualization.  A culture that suppresses spatial reasoning ($\phi_{\mathrm{spat}} \ll 1$) does not merely produce individuals who are bad at spatial tasks---it produces individuals for whom certain spatial experiences are *not in the potentiality space at all*.  The filter narrows the fiber, and the actualization operator cannot select what the fiber does not contain.

This is why filter effects are so difficult to reverse, and it is the deepest explanation of the CIT: once a filter contracts the fiber, the contracted dimensions cannot be re-inflated by any operation within the CS operator, because the information that parameterized those dimensions has been lost through the irreversible actualization at the contracted fiber.
\end{interpretation}

### The compatibility matrix as curvature

!!! theorem "Curvature--Compatibility Theorem"
 \tC\;

The compatibility matrix $\bK \in \R^{8 \times 8}$ is the *sectional curvature tensor* of the CS operator $\cC$ in the basis of intelligence types.  Specifically, the entry $K_{st}$ is the sectional curvature of $\cC$ in the 2-plane spanned by type-$s$ and type-$t$ directions:
\[
K_{st} = \kappa(e_s, e_t) = \frac{R(e_s, e_t, e_t, e_s)}{\|e_s\|^2 \|e_t\|^2 - \langle e_s, e_t \rangle^2}
\]
where $R$ is the Riemann curvature tensor of $\cC$ and $\{e_t\}$ are the intelligence-type basis vectors.

The curvature interpretation gives the three compatibility regimes a geometric meaning:
[nosep]
- $K_{st} > 1$ (synergy): *positive curvature* in the $s$-$t$ plane.  Geodesics in this plane converge---actualizing type $s$ pulls the system toward type $t$.  Parallel transport in positively curved space rotates vectors toward each other, which is the geometric mechanism of synergy: engaging one type enhances the other.

- $K_{st} = 1$ (independence): *zero curvature*.  The $s$-$t$ plane is flat.  Types $s$ and $t$ are geometrically orthogonal: actualizing one has no effect on the other.

- $K_{st} < 1$ (interference): *negative curvature*.  Geodesics diverge---actualizing type $s$ pushes the system away from type $t$.  This is the geometric mechanism of interference: engaging one type depletes or distorts the other.

\begin{keyeq}
**The Metric of Consciousness.** \tC\;
\[
ds^2 = \sum_{s,t} K_{st}\, dI_s\, dI_t
\]
The infinitesimal distance between two nearby experiential states in the CS operator is determined by the compatibility matrix acting as metric tensor.  Cognitive trajectories follow geodesics of this metric---paths of least interpretive effort through the curved landscape of consciousness.
\end{keyeq}

!!! remark "Remark"

The eigenstructure of $\bK$ determines the principal curvature directions of the CS operator.  The eigenvectors of $\bK$ are the "natural modes" of cognitive experience---the directions in which consciousness curves most strongly.  These eigenmodes need not align with the eight intelligence types; they are linear combinations that reflect the deep geometry of the interpretive substrate.  The attention simplex $\Delta^7$ operates by selecting points in this eigenspace, and the optimal attention allocation (the vertex of the simplex that maximizes $\bI \cdot \bR$) corresponds to the geodesic most aligned with the task demand.

%═══════════════════════════════════════════════════════════════════════════════

## Layer 3: Observer Coupling and Intersubjectivity

%═══════════════════════════════════════════════════════════════════════════════

### Individual potentiality spaces

Each conscious agent $i$ has its own potentiality space $\cE^i$, fiber bundle structure $\pi_i: \cE^i \to \cB^i$, and actualization operator $\cA_i$.  The individual the CS operator is $\cC^i = \mathrm{Im}(\cA_i)$.

!!! definition "Observer"
 \tA\;

An *observer* is a triple $(\cE^i, \cA_i, \psi_i^*)$ consisting of a potentiality space, an actualization operator, and a hypervisor fixed point.  Two observers are *distinct* if their actualization operators differ: $\cA_i \neq \cA_j$.  Two observers are *compatible* if their hypervisor states are related by a morphism of the respective fiber bundles.

### The tensor product and joint potentiality

!!! definition "Joint Potentiality Space"
 \tB\;

When two observers interact, their individual potentiality spaces combine via tensor product:
\[
\cE^{ij} = \cE^i \otimes \cE^j
\]
The joint space contains all product states (independent potentialities: "$i$ could experience $\psi$ while $j$ experiences $\phi$") and, crucially, *entangled* states that do not factorize---joint potentialities that cannot be decomposed into independent individual experiences.

!!! proposition "Entangled Potentiality and Shared Meaning"
 \tB\;

The entangled states in $\cE^{ij}$ are the substrate of shared meaning.  When two observers engage in communication, their interaction generates entangled potentialities: experiential configurations in $\cE^{ij}$ that are not products of individual potentialities.  The actualization of these entangled states produces experiences that are *genuinely shared*---not merely similar individual experiences, but experiences whose existence depends on both observers jointly.

The shared the CS operator is:
\begin{keyeq}
\[
\cC_{\mathrm{shared}}^{ij} = \cA_i\!\left(\cE^{ij}\right) \cap \cA_j\!\left(\cE^{ij}\right)
\]
\end{keyeq}
This is the set of experiences that *both* observers actualize from their joint potentiality space.  It is the region of intersubjective agreement---the experiential overlap where "we see the same thing" is literally true.

### Objectivity as maximal overlap

!!! definition "Objective Reality"
 \tB\;

*Objective reality* is the maximal intersection of the CS operators across all interacting observers:
\[
\cC_{\mathrm{obj}} = \bigcap_{i \in \mathrm{Obs}} \cA_i\!\left(\cE^{\mathrm{all}}\right)
\]
where $\cE^{\mathrm{all}} = \bigotimes_{i \in \mathrm{Obs}} \cE^i$ is the total joint potentiality space and $\mathrm{Obs}$ is the set of all interacting observers.

Objectivity is not a property of reality "in itself" but the *size of the overlap* among actualized spaces.  A highly objective fact (the Sun exists) lives in a vast overlap region; a subjective experience (the taste of this coffee) lives in a small or zero overlap.

!!! theorem "Resolution of the Intersubjectivity Problem"
 \tC\;

The intersubjectivity problem---"How can multiple observers independently confirm the existence and properties of a third-party object?"---is resolved without requiring a pre-existing objective world:
[nosep,label=(\roman*)]
- Each observer actualizes from the joint potentiality space $\cE^{\mathrm{all}}$.
- The joint space contains entangled potentialities whose actualization produces correlated experiences across observers.
- The "third-party object" is an element of $\cC_{\mathrm{obj}}$: a configuration that lies in every observer's actualized space.
- Independent confirmation is possible because each observer, actualizing independently from the same joint potentiality, arrives at the same element of $\cC_{\mathrm{obj}}$.

No single observer "creates" the object.  No pre-existing objective world is needed.  The object exists as a *convergent actualization*: a configuration that every observer's actualization operator selects from the shared potentiality.

!!! remark "Remark"

This resolves the tension between idealism and realism without choosing sides.  The framework is neither idealist (mind creates world) nor realist (world exists independently of mind).  It is *participatory*: reality is the overlap of actualizations, and the overlap depends on both the structure of the potentiality space (constraining what can be actualized) and the actualization operators (selecting what is actualized).  Wheeler called this "participatory realism"; the fiber bundle framework makes it mathematically precise.

### Free will as fiber freedom

!!! definition "Actualization Freedom"
 \tB\;

The *actualization freedom* of observer $i$ at substrate state $b$ is:
\[
\mathcal{W}_i(b) = \dim(\cF_b^i) - \dim(\mathrm{Im}(\cA_i|_{\cF_b^i}))
\]
This is the difference between the dimension of the potentiality fiber and the dimension of the actualized subspace.  It measures the number of "unchosen directions"---the degrees of freedom that were available but not actualized.

!!! proposition "Free Will Trichotomy"
 \tB\;

Three cases:
[nosep,label=(\roman*)]
- $\mathcal{W}_i(b) = 0$: **Determinism.**  The actualization operator selects the entire fiber---there is only one possible experience for this substrate state.  The fiber is a point, or the operator has no selectivity.
- $\mathcal{W}_i(b) = \dim(\cF_b^i) - 1$: **Maximal freedom.**  The actualization operator selects a single point from a high-dimensional fiber.  The agent has maximum choice over how to interpret the substrate state.
- $0 < \mathcal{W}_i(b) < \dim(\cF_b^i) - 1$: **Structured freedom.**  The actualization operator constrains the selection to a submanifold of the fiber---not fully determined, not fully free, but guided by the geometry of the bundle.  This is the generic case for biological cognition.

\begin{interpretation}
Free will is neither an illusion (determinism) nor unconstrained randomness (libertarian free will).  It is *structured selection*: the actualization operator chooses from a constrained but multi-dimensional space of possibilities.  The constraints are the fiber geometry (set by the substrate and the accumulated filter history), and the freedom is the irreducible selectivity of the actualization operator within those constraints.

This connects to the attention simplex: the choice of attention allocation $\mathbf{a} \in \Delta^7$ is an exercise of actualization freedom---a selection of which fiber directions to actualize.  The optimal attention allocation (vertex of the simplex) is the "rational" choice; deviations from optimality are the "free" choices; the simplex boundary is the geometric constraint.  Free will operates on the attention simplex as structured selection within a compact convex set.
\end{interpretation}

### Dispensing with many worlds

!!! proposition "Parsimony over Everett"
 \tC\;

The observer coupling framework resolves the quantum measurement problem without invoking the many-worlds interpretation:

[nosep,label=(\roman*)]
- **Everett:** Every quantum measurement outcome is realized in a separate branch.  The number of branches grows exponentially with the number of measurements.  Branches never interact again.  The "objective world" is the totality of all branches.

- **RTSG/Actualization:** Every observer actualizes from a shared potentiality space.  The number of actualizations is bounded by the number of observers.  Actualizations *overlap* wherever observers interact, producing shared reality.  The "objective world" is the overlap region, which *grows* as more observers couple their potentiality spaces.

The RTSG framework is more parsimonious: it does not posit unobservable branches but instead constructs intersubjective reality from the convergence of instantiation operators over a single shared potentiality space.  The physical world is not one branch among infinitely many---it is the maximal intersection of instantiations, a single structure whose definiteness increases with the number of participating observers.

Under the three-space ontology, this parsimony is even more striking.  $\QS$ continues to evolve unitarily---exactly as Everett wanted---but what appears as "collapse" when viewed from within $\PS$ is simply instantiation: consciousness projecting from $\QS$ to produce a moment of $\PS$.  There is no need for the universe to branch because there is no collapse to avoid.  One quantum space, one physical space, one the CS operator, one instantiation process.  The many-worlds interpretation solves a problem that the three-space ontology dissolves.

%═══════════════════════════════════════════════════════════════════════════════

## The Quantum Bridge

%═══════════════════════════════════════════════════════════════════════════════

### Structural isomorphism

The central structural claim of this Part is that the actualization architecture of consciousness and the measurement architecture of quantum mechanics share a common formal structure.

!!! theorem "Quantum--Conscious Isomorphism"
 \tC\;

The physical actualization system $(\cH_{\mathrm{phys}}, \hat{M})$ and the conscious actualization system $(\cE, \cA)$ are isomorphic as *actualization systems*: they share the same abstract structure of potentiality-to-actuality transition.

Specifically, there exists a structure-preserving map $\Phi$ such that:
[nosep,label=(\roman*)]
- $\Phi: \cH_{\mathrm{phys}} \to \cE$ is a bijection between the physical Hilbert space and the conscious potentiality space.
- $\Phi$ intertwines the actualization operators: $\cA \circ \Phi = \Phi \circ \hat{M}$.
- $\Phi$ preserves the tensor-product structure: $\Phi(\cH_A \otimes \cH_B) = \cE^A \otimes \cE^B$ (observer coupling maps to quantum entanglement).
- $\Phi$ preserves irreversibility: both $\hat{M}$ and $\cA$ are non-invertible.

!!! remark "Remark"

This is *not* the Wigner interpretation.  Wigner claimed that consciousness *causes* wave function collapse---that the physical system remains in superposition until a conscious observer intervenes.  The isomorphism theorem claims something different and more subtle: consciousness and physics are two manifestations of the *same* actualization architecture.  Neither causes the other.  They are parallel instantiations of a common formal structure in different ontological domains.

The practical consequence is that results proved in one domain transfer to the other.  The no-cloning theorem in quantum mechanics (one cannot duplicate an arbitrary quantum state) has a consciousness analogue: one cannot duplicate an arbitrary experiential state.  The no-signaling theorem (entanglement cannot be used for faster-than-light communication) has a consciousness analogue: shared potentiality does not enable telepathic communication.  These are not coincidences but consequences of the shared actualization structure.

### Observation and collapse as the same operation

!!! proposition "Unity of Observation"
 \tC\;

"Observation" in physics and "interpretation" in consciousness are the same operation $\cA$ applied to different domains:
[nosep,label=(\roman*)]
- In physics, $\cA$ maps from the Hilbert space of quantum states to the space of definite measurement outcomes.  The "collapse" is the actualization of one outcome from the superposition of possibilities.
- In consciousness, $\cA$ maps from the potentiality space of possible experiences to the space of definite experiences.  The "interpretation" is the actualization of one experience from the fiber of possibilities.

The two uses of $\cA$ are not analogous; they are *identical*, applied to two aspects of the same underlying reality.

The resolution of the measurement problem follows: the question "When does the wave function collapse?" becomes "When does instantiation occur?"  The answer is: whenever a system with a non-trivial hypervisor fixed point ($\psi^* \neq 0$) interacts with the quantum system.  The hypervisor---the self-interpreting state---is what makes a system an "observer," and the instantiation operator is what makes the observation a "measurement."

Under the three-space ontology, this resolution is deepened further: there is no collapse at all.  $\QS$ evolves unitarily forever.  What appears as collapse from the $\PS$-perspective is the irreversible projection $\mathbb{C} \to \R$ that constitutes instantiation.  The wave function does not collapse; it is *projected* by consciousness.  The measurement problem dissolves because it was formulated within a single-space framework that lacked the resources to describe what is fundamentally a three-space process.  The same structural diagnosis applies to quantum gravity: the unrenormalisable infinities of perturbative quantisation are the mathematics returning `NaN`---not a sign that we need better regularisation techniques but a signal that the single-space domain is ill-posed for a phenomenon that inherently involves all three spaces.

### The circularity resolved

!!! theorem "Mutual Constitution"
 \tC\;

The apparent circularity---the mind depends on the brain, but the mind participates in actualizing physical reality---is not vicious.  It is a *self-consistent fixed point* of the coupled system:

Let $\Psi = (\psi_{\mathrm{phys}}, \psi_{\mathrm{con}}) \in \cH_{\mathrm{phys}} \times \cE$ be the joint state of the physical substrate and the conscious potentiality.  The dynamics are coupled:
\[
\psi_{\mathrm{phys}}(t+1) = \hat{M}(\psi_{\mathrm{phys}}(t) \mid \psi_{\mathrm{con}}(t)), \qquad
\psi_{\mathrm{con}}(t+1) = \cA(\psi_{\mathrm{con}}(t) \mid \psi_{\mathrm{phys}}(t))
\]
The physical state evolves contingent on the conscious state (observation shapes the physical), and the conscious state evolves contingent on the physical state (the substrate shapes experience).

A *mutually constitutive equilibrium* is a joint state $\Psi^*$ such that:
\[
\Psi^*(t+1) = \Psi^*(t) \qquad \forall\, t
\]
At equilibrium, the mind and the world are mutually determining: neither is prior, neither is derivative.  The equilibrium exists (under compactness and continuity conditions analogous to those in Theorem *ref:thm:three-properties*(iii)) and is the deepest formalization of the co-arising of consciousness and reality.

\begin{interpretation}
The circularity is the same logical structure as:
[nosep]
- A self-consistent spacetime in general relativity (matter curves space; space guides matter; the equilibrium solution is the physical universe).
- A fixed point of a strange loop in the sense of Hofstadter (1979).
- Dependent origination in Buddhist metaphysics: nothing exists independently; everything arises in mutual dependence.

The mind does not "create" the world, and the world does not "create" the mind.  They co-arise as the stable fixed point of mutual instantiation.  Under the three-space ontology, this is not a bootstrap: $\QS$, $\PS$, and $\CS$ are *co-primordial*---they arose together at moment zero.  The circularity is only apparent; it dissolves once we abandon the assumption that one space must be prior to the others.  The equilibrium is a timeless structural relation reflecting the co-primordial origin, not a causal sequence requiring temporal priority.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Connection to Existing RTSG Components

%═══════════════════════════════════════════════════════════════════════════════

\begin{center}
\small

*[Table — see PDF]*

\end{center}

%═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

%═══════════════════════════════════════════════════════════════════════════════

The framework generates predictions beyond those of the Layer 2 machinery alone:

[nosep,label=(\arabic*)]

- **Fiber dimension and experiential richness.**  The subjective richness of experience (measured by phenomenological report complexity) should correlate with the information-theoretic complexity of the underlying neural state ($H(b) - H_{\min}(b)$, Proposition *ref:prop:fiber-dim*).  This is testable via simultaneous neural recording and phenomenological reporting.

- **Filter irreversibility is asymmetric.**  Filters that contract the fiber (restrictive cultural or developmental filters) should be harder to reverse than filters that merely attenuate intensity within a preserved fiber.  Prediction: cognitive training can recover attenuated capability (intensity restoration) more easily than capability that was never developed (fiber expansion).

- **Convergence disruption in altered states.**  Psychedelic states, meditation, and dissociative episodes should correspond to disruptions of the convergence to the hypervisor fixed point (Proposition *ref:prop:hypervisor-unique*).  Prediction: the "ego dissolution" reported under psilocybin corresponds to a temporary increase in the contraction ratio $\kappa$ toward or beyond 1, where convergence fails and the fixed point becomes unstable.

- **Intersubjective agreement scales with interaction quality.**  The dimensionality of $\cC_{\mathrm{shared}}^{ij}$ should increase with the depth, duration, and cognitive diversity of interaction between observers $i$ and $j$.  Prediction: long-term collaborators, romantic partners, and members of tight-knit communities have higher-dimensional shared the CS operators than strangers, measurable as greater agreement on ambiguous stimuli.

- **Curvature signatures in cognitive performance.**  If $\bK$ is the sectional curvature of $\cC$, then cognitive tasks requiring simultaneous engagement of synergistic types ($K_{st} > 1$) should show superlinear performance gains, while tasks requiring simultaneous engagement of interfering types ($K_{st} < 1$) should show sublinear performance.  This is already predicted by Layer 2 but receives a geometric explanation: synergistic types lie in positively curved regions where cognitive trajectories naturally converge.

%═══════════════════════════════════════════════════════════════════════════════

## Open Problems

%═══════════════════════════════════════════════════════════════════════════════

[nosep,label=(\arabic*)]
- **Fiber topology.**  What is the topological type of the experiential fiber $\cF_b$ over a typical human neural state?  Is it contractible, or does it have non-trivial homotopy groups?  Non-trivial topology would imply that certain experiential configurations are topologically protected---stable against perturbation---which could explain the robustness of core identity across cognitive fluctuations.

- **Actualization dynamics.**  What determines the time scale of actualization?  The framework treats $\cA$ as instantaneous, but empirically, the transition from potentiality to experience may have a finite duration (the "specious present" of approximately 100--500ms).  A dynamical theory of actualization would need to specify the temporal evolution of the selection process within the fiber.

- **Interspecies fiber comparison.**  Different species have different substrates and therefore different fiber bundles.  The framework predicts that the fiber rank (number of independent experiential directions) varies across species and determines the dimensionality of their the CS operator.  Empirical characterization of fiber rank across species would test the framework and connect to the animal intelligence profiles developed in the Nature Taxonomy.

- **Artificial consciousness.**  Under what conditions does an artificial system develop a non-trivial hypervisor fixed point?  The framework predicts that the existence of $\psi^*$ requires self-referential structure in the actualization operator---the system must be able to interpret its own interpretations.  This provides a formal criterion for artificial consciousness that is more precise than Turing-test behavioral criteria: a system is conscious if and only if its actualization operator has a non-trivial fixed point.

- **Quantum-consciousness coupling.**  The isomorphism theorem (Theorem *ref:thm:quantum-bridge*) is currently a structural claim.  Can the map $\Phi$ be constructed explicitly for a specific physical system (e.g., a neural microtubule, a quantum coherence mode in a warm biological system)?  If so, the framework would make specific predictions about the quantum states that are selected during conscious observation, testable via quantum biology experiments.

- **Gravity and the ground state.**  The identification of gravity with proto-consciousness (Axiom *ref:ax:gravity*) predicts that gravitational effects should have a privileged relationship with consciousness.  Does gravitational time dilation affect the subjective experience of time in a way distinguishable from other physical time dilation effects?  Can gravitational wave detection be interpreted as observation of ground-state consciousness dynamics?

- **The Id as pre-filter.**  The three-space ontology introduces the Id as a basement-level filter on free will, anchored to physical time and evolutionary imperatives.  Can the Id's effects be measured independently of the five existing RTSG filter species?  Is the Id necessary for stable $\CS$, or merely contingent on the biological route through complexification?

- **$p$-Adic memory structure.**  The three-space ontology proposes that semantic memory is organized in a $p$-adic (ultrametric) topology.  This predicts that recall latency should follow ultrametric distance: items in the same category branch should be recalled equally fast, with a discrete jump to items in different branches.  This is testable via priming experiments with hierarchically organized stimuli.

- **Topology of the shared space.**  Is $\cC_{\mathrm{obj}} = \bigcap_i \cA_i(\cE^{\mathrm{all}})$ simply connected?  If not, its fundamental group $\pi_1(\cC_{\mathrm{obj}})$ would describe "topological disagreements"---classes of experiences that cannot be continuously deformed from one observer's actualization to another's, representing irreducible perspectival differences that no amount of communication can resolve.

%═══════════════════════════════════════════════════════════════════════════════

## Summary of New Results

%═══════════════════════════════════════════════════════════════════════════════

\begin{center}
\small

*[Table — see PDF]*

\end{center}

\ifx\STANDALONE\undefined\else
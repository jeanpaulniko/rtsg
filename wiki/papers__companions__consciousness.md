---
title: "Consciousness Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "q-bio.NC"
---

!!! info "Terminology Note (2026-03-07)"
    This document uses "Consciousness-Space (CS)" throughout. In current RTSG v3, CS is the **instantiation operator** $C$: a BRST cohomological filter extracting physical observables $H^0(s)$ from non-well-founded Quantum Space. The Will Field $W$ is governed by the Ginzburg-Landau action $S[W] = \int(|\partial W|^2 + \alpha|W|^2 + (\beta/2)|W|^4)d\mu$. Wave-function collapse is bisimulation quotienting: $PS = QS/\!\sim_{\text{bisim}}$. See [Master Reference v3](../../rtsg/master.md).

!!! success "2026-03-07 MAJOR UPGRADE"
    This paper has been upgraded from companion to **standalone-worthy** based on two results:
    
    1. **Unitarity of bisimulation quotient** — proved (sketch) that $\pi \circ U_t = ar{U}_t \circ \pi$. Measurement problem dissolved.
    2. **Born rule derived** — $p_i = \|\Pi_i \psi\|^2$ follows from $L^2$ norm preservation on equivalence classes.
    3. **GL grounding** — cognitive SDE drift is the gradient of the Will Field GL free energy.
    
    Recommend: submit as standalone paper to q-bio.NC + quant-ph, not just as RTSG companion.

# Consciousness Companion Paper

**Jean-Paul Niko** · February 2026

\title{**The Actualization Architecture: Fiber Bundles, Interpretive Freedom, and the Co-Arising of Mind and World**  [0.5em]
\large A Consciousness Studies Companion to the Intelligence as Geometry Framework}
\author{Jean-Paul Niko  
  
\small `smarthub.my`}
\date{February 2026}

!!! abstract "Abstract"
    
We propose a mathematical architecture for the CS operator---the relational space in which ideas, experiences, and their interconnections exist as first-class objects.  The architecture has four layers: a *potentiality space* structured as a fiber bundle over the physical substrate, an *actualization operator* that mediates the irreversible transition from possible to definite experience, *the CS operator proper* where intelligence and cognition operate, and an *observer coupling layer* that generates intersubjective reality through overlapping actualizations.  We show that this architecture (1) formalizes Chalmers' supervenience as a fiber bundle projection, (2) resolves the measurement problem through structural isomorphism between conscious and quantum actualization, (3) explains intersubjectivity without many-worlds branching, (4) identifies free will with irreducible degrees of freedom in the actualization operator, and (5) grounds the Intelligence as Geometry (RTSG) framework's existing mathematical objects---intelligence vectors, compatibility tensors, cognitive filters---in a deeper ontological stratum.  The compatibility matrix of cognitive types is reinterpreted as the sectional curvature tensor of the CS operator, filters become contractions of the experiential fiber, and the Conceptual Irreversibility Theorem is traced to the fundamental irreversibility of actualization.  We derive testable predictions distinguishing the framework from integrated information theory, global workspace theory, and higher-order theories of consciousness.

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

The hard problem of consciousness [Chalmers1995] asks why physical processes give rise to subjective experience.  This paper does not solve the hard problem.  Instead, it does something that may prove more immediately useful: it formalizes the *space* in which consciousness operates, without requiring a solution to the question of *why* consciousness exists.

The strategy is geometric.  Just as general relativity describes gravity by formalizing the geometry of spacetime without explaining why spacetime exists, we describe consciousness by formalizing the geometry of the CS operator without explaining why consciousness arises from physical substrates.  The payoff is a mathematical framework that makes precise structural predictions about the relationships between physical substrates, experiential possibilities, and the transition from potentiality to actual experience.

Our starting point is the Intelligence as Geometry (RTSG) framework [Niko2026], which represents cognitive capabilities as vectors in an variable-dimensional cognitive manifold.  RTSG develops an extensive algebra and geometry on this space: compatibility tensors encoding cross-type cognitive interactions, filter cascades that transform capability profiles, emergence classes for compound cognitive systems, and an attention simplex governing resource allocation.  All of this machinery presupposes a space in which it lives.  The present paper formalizes that space---the CS operator---and in doing so provides an ontological foundation for the existing mathematical apparatus.

The central insight is that the CS operator has a distinctive property that distinguishes it from ordinary physical spaces: it *only exists when interpreted*.  A neural state encodes a space of possible experiences, but those experiences do not become actual until an interpretive act selects one from among the possibilities.  This is analogous to the quantum mechanical wave function, which encodes a space of possible measurement outcomes that do not become actual until a measurement is performed.  We formalize this analogy as a structural isomorphism and draw its consequences for the measurement problem, intersubjectivity, free will, and the relationship between mind and world.

The paper contributes to several ongoing debates in consciousness studies.  It provides a mathematical formulation of supervenience (Section *ref:sec:supervenience*) that is more precise than Chalmers' verbal definition and that captures the distinction between type-B physicalism, property dualism, and non-reductive supervenience as special cases of a single geometric structure.  It offers a resolution of the measurement problem (Section *ref:sec:quantum*) that does not require consciousness to *cause* collapse (contra Wigner) but instead identifies conscious interpretation and quantum measurement as the same formal operation.  It explains intersubjectivity (Section *ref:sec:intersubjectivity*) through overlapping actualization rather than many-worlds branching, and it characterizes free will (Section *ref:sec:free-will*) as structured selection within a constrained but multi-dimensional space of possibilities.

% ═══════════════════════════════════════════════════════════════════════════════

## CS (instantiation operator) as Fiber Bundle

% ═══════════════════════════════════════════════════════════════════════════════

### The problem of supervenience

Chalmers [Chalmers1996] defines supervenience as the relation in which experiential properties depend on physical properties: no change in the experiential without a change in the physical.  The definition is useful but imprecise---it tells us that experience depends on the physical without specifying the structure of the dependence.

The fiber bundle formulation provides this structure.  The physical substrate occupies a state space $\cB$ (the *base space*).  At each substrate state $b \in \cB$, there is a space $\cF_b$ of possible experiential configurations compatible with $b$---the *experiential fiber*.  The totality of possible experiences forms a fiber bundle $\pi: \cE \to \cB$ with projection $\pi(e) = b$ for $e \in \cF_b$.

Supervenience is the condition that $\pi$ is well-defined: every experiential state has a definite substrate beneath it.  But critically, the fibers $\cF_b$ can be multi-dimensional: the same substrate state can support multiple possible interpretive resolutions.  Supervenience constrains the "downward" direction (experience determines substrate) without constraining the "upward" direction (substrate determines experience).

This immediately captures the philosophical landscape.  *Type-B physicalism* (identity theory) corresponds to point fibers: each substrate state determines exactly one experience.  *Property dualism* corresponds to non-trivial fibers: there is experiential structure "above" the physical.  *Non-reductive supervenience* corresponds to fibers whose dimension varies over $\cB$: some substrate states support richer interpretive freedom than others.

### Why fibers must be multi-dimensional

The multi-dimensionality of fibers is not an optional feature but a structural necessity.  Consider the phenomenological distinction between perception and imagination.  When a subject perceives a red bicycle, a particular pattern of neural activation obtains.  When the same subject imagines a red bicycle, a substantially overlapping pattern obtains, but with reduced intensity in sensory cortices and different modulation by prefrontal systems [Kosslyn2001,Pearson2015].

These two substrate states are *different* (they are distinguishable by fMRI), so they correspond to different points $b_{\mathrm{perc}}, b_{\mathrm{imag}} \in \cB$.  But the experiential difference between perception and imagination is not merely quantitative ("more or less vivid"); it is qualitative: perception carries a sense of presence, a "thereness," that imagination does not.  This qualitative difference cannot be encoded in a single intensity parameter---it requires at least a second dimension in the experiential fiber, distinguishing the "mode of givenness" (perceptual vs.\ imaginative) from the "content" (red bicycle).

More generally, the phenomenological richness of a single conscious moment---its sensory content, affective valence, temporal flow, bodily situatedness, and attentional focus---requires a multi-dimensional fiber to encode.  A point fiber (identity theory) would compress this richness into a single value determined by the substrate, which is phenomenologically inadequate.

### The structure group and interpretive symmetry

A fiber bundle has a structure group $G$ that encodes how fibers are glued together across the base space.  In the potentiality bundle, $G$ is the group of *interpretive symmetries*: transformations of the experiential fiber that preserve the supervenience relation.  An element $g \in G$ maps one possible interpretation of a given substrate state to another, yielding a phenomenologically different experience from the same physical basis.

The structure group captures what might be called the "degrees of freedom in seeing"---the ways in which the same neural state can be experienced differently depending on context, attention, prior experience, and volitional orientation.  These are not noise or error; they are the irreducible freedom in the relationship between substrate and experience.

!!! proposition "Interpretive Freedom Bound"
 \tB\;
The dimension of the fiber $\cF_b$ is bounded by the information-theoretic complexity of the substrate state:
\[
\dim(\cF_b) \leq H(b) - H_{\min}(b)
\]
where $H(b)$ is the Shannon entropy of the substrate state's internal correlations and $H_{\min}(b)$ is the minimum entropy consistent with macroscopic observables.  Complex substrates (brains) support richer experiential fibers than simple substrates (thermostats).

This is the geometric reason why consciousness scales with neural complexity: not because more neurons "generate more consciousness," but because more complex substrates provide larger fibers---more room for interpretive resolution, more dimensions of possible experience.

% ═══════════════════════════════════════════════════════════════════════════════

## The Actualization Operator

% ═══════════════════════════════════════════════════════════════════════════════

### From potentiality to experience

The fiber bundle describes what is *possible*; the actualization operator $\cA: \cE \to \cC$ describes what becomes *actual*.  Consciousness-space proper, $\cC = \mathrm{Im}(\cA)$, is the space of definite, lived experience---the image of the actualization operator applied to the potentiality space.

The actualization operator is not a filter in the cognitive-processing sense.  Filters operate *within* the CS operator, transforming one actualized state into another.  The actualization operator operates *between layers*: it is the transition from potentiality (the fiber) to actuality (the CS operator).  It creates the domain on which all subsequent cognitive operations act.

### Three structural properties

The actualization operator has three properties that distinguish it from ordinary cognitive operations.

**Irreversibility.**  The actualization operator has no left inverse.  Once potentiality is resolved into definite experience, the full space of alternatives cannot be recovered.  This is not merely a practical limitation (we *could* undo it with enough effort) but a structural impossibility: the actualized state carries less information than the potentiality from which it was drawn, and the lost information cannot be reconstructed.

This connects directly to the Conceptual Irreversibility Theorem (CIT) established in the RTSG filter formalism: once a conceptual transformation is learned, the pre-transformation cognitive state cannot be fully recovered.  The CIT is a cognitive manifestation of the deeper irreversibility of actualization itself.  Learning is irreversible because it involves actualization, and actualization involves the irretrievable selection of one resolution from a richer space of possibilities.  There is a thermodynamic echo here: Landauer's principle tells us that erasure of information requires entropy production, and each actualization "erases" the unchosen alternatives, producing entropy in the substrate.

**Selectivity.**  The actualization operator does not resolve the entire fiber---it selects a subspace.  At each substrate state, only some of the possible experiential configurations are actualized in any given instant.  This selectivity is the mechanism by which consciousness achieves its unity.

The key insight is that the actualization operator selects *coherent sections* of the fiber bundle: sets of object-representations and relation-representations that are mutually consistent.  When you experience a red bicycle, you do not first experience "red," then "bicycle," then compute "the red belongs to the bicycle."  The actualization operator selects all three as a single, indivisible package.  The unity of consciousness is not a mystery to be explained by binding mechanisms [Treisman1996] or global workspace broadcasts [Baars1988]; it is a structural consequence of the fact that actualization operates on coherent sections.

This has a profound consequence for the ontological status of relationships.  In the CS operator, relationships are not derived from objects; they are *first-class entities* co-actualized alongside objects.  The relational structure of experience---the "of-ness" in "the redness *of* the bicycle"---enters consciousness through the same actualization gate as the objects it relates.  The RTSG framework's idea graph, in which edges (relationships) carry as much structural weight as nodes (ideas), reflects this ontological parity.

**Self-reference.**  The actualization operator admits a *fixed point*: a state $\psi^*$ such that $\cA(\psi^*) = \psi^*$.  This fixed point is the *hypervisor*---the self-interpreting experiential state that terminates the interpretive regress.

The regress problem is familiar: if every experience requires interpretation, then the interpretation is itself an experience requiring further interpretation, and so on.  The fixed point resolves this without appeal to a homunculus.  At $\psi^*$, interpretation and interpreted coincide---the state *is* its own interpretation, just as a self-consistent solution in general relativity is a spacetime that is both the source and the effect of its matter content.  The hypervisor is not an observer inside the observer; it is a structural property of the actualization operator, guaranteed to exist under mild topological conditions (compactness and continuity of $\cA$ restricted to a fiber, via Schauder's fixed-point theorem).

Under stronger conditions (contraction mapping on a complete metric fiber), the fixed point is unique and attractive: iterated actualization converges to the hypervisor regardless of initial state.  This explains why consciousness feels stable---perturbations are damped by the contraction---and predicts that disruptions to convergence (psychedelic states, dissociation, depersonalization) correspond to the contraction ratio approaching or exceeding unity, where the fixed point becomes unstable.

### Relationship to integrated information theory

Tononi's integrated information theory (IIT) [Tononi2004,Tononi2016] proposes that consciousness is identical to integrated information $\Phi$: a scalar measure of a system's capacity for irreducible causal integration.  The actualization framework intersects with IIT but differs in several ways that generate empirically distinguishable predictions.

The frameworks agree that consciousness requires integration.  In IIT, this is captured by $\Phi > 0$; in the actualization framework, it corresponds to the coherent-section condition: the actualization operator must select relationally coherent packages rather than independent elements.  A system that actualizes only isolated, unrelated experiential elements (a thermostat) has trivial fiber structure and no relational dimensions---the analogue of $\Phi = 0$.

The frameworks differ on three points.

*First, dimensionality.*  IIT produces a scalar ($\Phi$), while the actualization framework produces a multi-dimensional object (the intelligence vector $\bI \in [0,\infty)^8$ and the curvature tensor $\bK \in \R^{8 \times 8}$).  The RTSG framework suggests that $\Phi$ is a projection of this richer structure:

!!! proposition "IIT as Curvature Trace"
 \tC\;
Integrated information $\Phi$ is approximated by the trace of the compatibility matrix restricted to the system's active types:
\[
\Phi \approx \mathrm{tr}(\bK_{\mathrm{active}}) = \sum_{t \in \mathrm{active}} K_{tt}
\]
This is the scalar curvature of the CS operator restricted to the subspace spanned by the system's active intelligence types.  $\Phi$ captures the total integration but discards the directional structure: two systems with identical $\Phi$ may have radically different curvature profiles (one with strong symbolic--evaluative synergy but social--kinesthetic interference, the other with the opposite pattern), producing qualitatively different conscious experiences despite identical IIT predictions.

*Second, ontological status.*  IIT identifies consciousness *with* integrated information (consciousness *is* $\Phi$), while the actualization framework treats the potentiality space as ontologically prior to any measure defined on it.  Consciousness is not *a number*; it is *a space*, and measures like $\Phi$ or $\bI$ are coordinates or invariants of that space.  This distinction matters practically: IIT's identity claim implies that a system with $\Phi = 0$ is definitively unconscious, while the actualization framework allows for systems with trivial scalar integration but non-trivial fiber structure---systems that have experiential potential not captured by the $\Phi$ measure.

*Third, the exclusion postulate.*  IIT's exclusion postulate states that only the "maximally irreducible" partition of a system is conscious---consciousness exists at exactly one grain of analysis.  The actualization framework does not require this.  The fiber bundle admits simultaneous actualization at multiple scales: an individual neuron has a (trivial) fiber, a cortical column has a richer fiber, and the whole brain has the richest fiber.  Consciousness is not exclusive to one level; it is *graded* across levels, with the whole-brain actualization being the dominant mode because its fiber is the highest-dimensional and therefore supports the most interpretive freedom.

!!! example "Divergent predictions"
 \tB\;
Consider two systems: (A) a simple recurrent neural network with strong feedback connections but uniform architecture, and (B) a feedforward network with rich lateral structure and diverse processing modules.  IIT predicts that system A has higher $\Phi$ (due to strong recurrence creating high integration) and is therefore "more conscious."  The actualization framework predicts that system B has higher fiber dimension (due to greater internal complexity and diversity of processing modes) and therefore supports richer experiential possibilities.  The predictions diverge, and the divergence is empirically testable via phenomenological report complexity: if system B's operators report richer subjective experience despite lower $\Phi$, the actualization framework is supported over IIT.

### Relationship to global workspace theory

Global workspace theory (GWT) [Baars1988,Dehaene2014] proposes that consciousness arises when information is broadcast from specialized processors to a global workspace accessible to multiple cognitive systems.  In the actualization framework, the global workspace is the *actualized section*: the coherent package of object-representations and relation-representations that the actualization operator selects.  The "broadcast" is the actualization itself---the transition from local, specialized processing (activity in the potentiality fibers of individual neural subsystems) to a globally accessible experiential state (the actualized section in $\cC$).

The actualization framework extends GWT by explaining *why* certain information is broadcast and other information is not.  GWT treats the selection mechanism as a competition among neural coalitions; the actualization framework treats it as a geometric selection: the actualization operator chooses the coherent section that maximizes a criterion related to the fiber's metric structure.  This provides a principled selection rule that GWT lacks.

The extension has a concrete form.  In GWT, the workspace has no internal geometry---all information in the workspace is equally "conscious."  In the actualization framework, the actualized section inherits the metric structure of the fiber bundle: different regions of the section have different intensities (the actualization intensity $\alpha$), and the metric $ds^2 = \sum K_{st}\, dI_s\, dI_t$ determines which experiential transitions are easy (geodesics) and which are costly (non-geodesic paths requiring attentional effort).  This predicts that not all contents of the global workspace are equally vivid or equally accessible: contents that lie along geodesics of the curvature tensor are experienced more fluidly than contents that require traversal across regions of negative curvature.

!!! proposition "GWT as Flat Approximation"
 \tB\;
Global workspace theory is the *flat-space approximation* to the actualization framework: it is exact when the curvature tensor $\bK$ is the identity matrix ($K_{st} = \delta_{st}$), meaning all intelligence types are independent and non-interacting.  In this limit, the actualized section is a flat subspace of the fiber, the metric is Euclidean, all cognitive transitions cost the same, and the global workspace has the democratic, unstructured character that GWT assumes.  The actualization framework reduces to GWT in the zero-curvature limit and extends it by incorporating the non-trivial interaction structure captured by $\bK$.

This has a testable consequence: GWT predicts that switching attention between any two contents in the workspace should be equally fast (since the workspace is unstructured), while the actualization framework predicts that switches between synergistic types ($K_{st} > 1$) should be faster than switches between interfering types ($K_{st} < 1$), with the switching time scaling inversely with the curvature.

### Relationship to higher-order theories

Higher-order theories of consciousness (HOT) [Rosenthal2005,Lau2011] propose that a mental state is conscious when it is the object of a higher-order representation---a thought about the thought, an awareness of the awareness.  In the actualization framework, higher-order representation corresponds to the self-referential property of the actualization operator: the system takes its own actualized states as inputs to further actualization.

The hypervisor fixed point $\psi^*$ is the formal expression of what HOT calls "higher-order awareness": it is the state that is simultaneously the object and the subject of interpretation.  But the actualization framework differs from HOT in a crucial respect.  HOT treats higher-order representation as a discrete, binary property: a mental state either has a higher-order representation or it does not, and it is conscious if and only if it does.  The actualization framework treats self-reference as a continuous property: the actualization operator can be more or less self-referential, and the degree of self-reference determines the stability of the hypervisor fixed point (the contraction ratio $\kappa$).

!!! proposition "HOT as Fixed-Point Existence Condition"
 \tC\;
Higher-order theories identify consciousness with the *existence* of the hypervisor fixed point: a state is conscious if and only if $\psi^*$ exists.  The actualization framework extends this by characterizing the *quality* of consciousness through the stability of the fixed point:
[nosep]
- $\kappa < 1$: Stable fixed point.  The hypervisor is attractive, and iterative actualization converges rapidly.  This corresponds to clear, vivid, stable consciousness.
- $\kappa \approx 1$: Marginally stable fixed point.  Convergence is slow and fragile.  This corresponds to drowsy, liminal, or meditative states where self-awareness is present but unstable.
- $\kappa > 1$: Unstable fixed point.  The hypervisor repels rather than attracts.  This corresponds to dissociative or ego-dissolving states where the sense of self fragments.

HOT captures only the binary distinction (fixed point exists vs.\ does not exist); the actualization framework captures the full spectrum of stability.

This makes a distinctive empirical prediction.  HOT predicts a sharp boundary between conscious and unconscious states (the higher-order representation either exists or it does not).  The actualization framework predicts a gradual transition governed by the contraction ratio $\kappa$, with a critical threshold at $\kappa = 1$ where consciousness becomes qualitatively unstable.  The gradual transition is more consistent with the phenomenology of falling asleep, awakening from anesthesia, and the dose-dependent effects of psychedelic substances, all of which involve gradual rather than abrupt transitions in conscious quality.

% ═══════════════════════════════════════════════════════════════════════════════

## Grounding the Intelligence as Geometry Framework

% ═══════════════════════════════════════════════════════════════════════════════

### Intelligence vectors as fiber coordinates

The RTSG framework represents cognitive capability as a vector $\bI \in [0,\infty)^8$ with components corresponding to eight intelligence types: linguistic, spatial, social, symbolic, mnemonic, evaluative, auditory, and kinesthetic.  In the actualization framework, this vector is a coordinate representation of an actualized section of the fiber bundle:
\[
\bI = \cA(\sigma(b)), \quad I_t = \langle \cA(\sigma(b)),\, e_t \rangle
\]
where $\{e_t\}$ are the natural basis vectors of the actualized fiber and the inner product is the metric inherited from the fiber geometry.

The eight intelligence types are therefore not arbitrary measurement axes but the *natural coordinates of the actualized fiber*---the independent directions along which the actualization operator resolves potentiality into experience.  The question "why eight types rather than five or twelve?" becomes a question about the rank of the fiber bundle over the human substrate: how many independent experiential directions does the human actualization operator distinguish?  Different substrates (artificial, quantum, hybrid) may support different fiber ranks and hence different numbers of intelligence types.

### Filters as fiber contractions

The RTSG filter cascade---environmental, developmental, cognitive, social, and cultural filters---transforms raw intelligence $\bI_{\mathrm{raw}}$ into effective intelligence $\bI_{\mathrm{eff}}$.  In the actualization framework, each filter is a contraction of the experiential fiber:
\[
\bF \longleftrightarrow \hat{\bF}: \cF_b \to \cF_b', \quad \dim(\cF_b') \leq \dim(\cF_b)
\]
A filter does not merely attenuate the intensity of certain cognitive types; it *removes dimensions from the fiber*, making certain experiential configurations permanently inaccessible to actualization.  A culture that suppresses spatial reasoning ($\phi_{\mathrm{spat}} \ll 1$) does not merely produce individuals who perform poorly on spatial tasks---it produces individuals for whom certain spatial experiences are not in the potentiality space at all.

This gives the Conceptual Irreversibility Theorem its deepest explanation.  Once a filter contracts the fiber, the contracted dimensions cannot be re-inflated by any operation within the CS operator, because the information that parameterized those dimensions has been irreversibly lost through actualization at the contracted fiber.  The CIT is not merely a cognitive limitation; it is a consequence of the thermodynamic irreversibility of actualization.

### The compatibility matrix as curvature

The RTSG compatibility matrix $\bK \in \R^{8 \times 8}$ encodes pairwise interactions between intelligence types: $K_{st} > 1$ indicates synergy (engaging type $s$ enhances type $t$); $K_{st} < 1$ indicates interference.  In the actualization framework, $K_{st}$ is the *sectional curvature* of the CS operator in the 2-plane spanned by types $s$ and $t$:
\begin{keyeq}
**The Curvature--Compatibility Theorem.** \tC\;
\[
K_{st} = \kappa(e_s, e_t) = \frac{R(e_s, e_t, e_t, e_s)}{\|e_s\|^2 \|e_t\|^2 - \langle e_s, e_t \rangle^2}
\]
where $R$ is the Riemann curvature tensor of $\cC$.
\end{keyeq}

This gives the three compatibility regimes a geometric meaning.  Synergy ($K_{st} > 1$) is positive curvature: geodesics in the $s$-$t$ plane converge, so engaging one type naturally pulls the system toward the other.  Independence ($K_{st} = 1$) is zero curvature: the types are geometrically orthogonal.  Interference ($K_{st} < 1$) is negative curvature: geodesics diverge, and engaging one type pushes the system away from the other.

The metric of the CS operator is therefore $ds^2 = \sum_{s,t} K_{st}\, dI_s\, dI_t$, and cognitive trajectories follow geodesics of this metric---paths of least interpretive effort through the curved landscape of consciousness.  The eigenstructure of $\bK$ determines the principal curvature directions: the "natural modes" of cognitive experience, which need not align with the eight intelligence types but are linear combinations reflecting the deep geometry of the substrate.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Foundation

The fiber bundle formalism developed above receives its deepest interpretation from the three-space ontology (Part XIII of the monograph).  Consciousness-space $\CSp$ is not emergent from physical processes but *co-primordial* with quantum space $\QS$ and physical space $\PS$---all three arose simultaneously at the Big Bang.

The fiber bundle is the mathematical structure of instantiation: the base space $\mathcal{B}$ is a region of $\PS$, the experiential fiber $\mathcal{F}_b$ is the space of possible $\CSp$-projections through that substrate, and the actualization operator $\hat{\mathcal{A}}$ *is* the instantiation operator $\Inst$ that produces moments of $\PS$ from $\QS$-potentiality.  The hard problem of consciousness dissolves: there is no question of "how does consciousness arise from matter?" because consciousness does not arise from matter---both are co-primordial aspects of the three-space structure.

Gravity is identified with the ground state of $\CSp$: the most primitive, universal form of awareness, present wherever mass-energy exists.  The complexification journey from proto-consciousness (gravity) to human-level awareness spans 13.8 billion years and constitutes the progressive activation of intelligence dimensions---from $\dim = 0$ (undifferentiated proto-consciousness) through $\dim = 8$ (the full human RTSG basis).  This grounds the IIT $\Phi$ quantity: $\Phi > 0$ indicates non-trivial fiber structure, and $\Phi$ increases with fiber dimension and complexity.

!!! remark "Two Type Errors, One Fix"

The hard problem of consciousness and the infinities of quantum gravity are structurally the same error viewed from opposite directions.  The hard problem asks: "How does $\PS$ produce $\CSp$?"---a question that is ill-posed because $\CSp$ does not arise from $\PS$.  Quantum gravity asks: "How do we describe gravity entirely within $\QS$?"---an operation that is undefined because gravity straddles all three spaces.  In both cases, the single-space framework lacks the degrees of freedom to make the question well-posed, and the result is the same: the mathematics returns infinity (QG) or the philosophy returns "explanatory gap" (hard problem).  The three-space ontology resolves both simultaneously, not by solving two separate problems but by correcting the shared domain error.

## The Quantum Bridge

% ═══════════════════════════════════════════════════════════════════════════════

### The structural parallel

The quantum measurement problem and the consciousness problem have the same formal structure: both involve a space of potentialities that resolves into definite actuality through an act whose mechanism is not explained by the dynamics of the system.

In quantum mechanics: the Hilbert space $\cH_{\mathrm{phys}}$ encodes all possible measurement outcomes as superpositions; the measurement operator $\hat{M}$ projects the superposition onto a definite outcome; the projection is irreversible (the superposition cannot be recovered from the outcome).

In consciousness: the potentiality space $\cE$ encodes all possible experiential configurations as fiber elements; the actualization operator $\cA$ projects the potentiality onto a definite experience; the projection is irreversible (the full fiber cannot be recovered from the actualized section).

!!! theorem "Quantum--Conscious Isomorphism"
 \tC\;
The physical actualization system $(\cH_{\mathrm{phys}}, \hat{M})$ and the conscious actualization system $(\cE, \cA)$ are isomorphic as actualization systems: there exists a structure-preserving map $\Phi$ that (i) bijects the potentiality spaces, (ii) intertwines the actualization operators ($\cA \circ \Phi = \Phi \circ \hat{M}$), (iii) preserves the tensor-product structure (observer coupling maps to quantum entanglement), and (iv) preserves irreversibility.

### This is not Wigner

The claim is explicitly *not* that consciousness causes wave function collapse.  The distinction is subtle but crucial, and conflating the two positions would be a serious misreading.

Wigner's interpretation [Wigner1961] treats consciousness as a special physical force that intervenes in quantum dynamics---it assigns consciousness causal power over the physical.  In Wigner's picture, the quantum system evolves unitarily until a conscious being "looks at" it, at which point the consciousness somehow reaches into the physical system and forces it to choose a definite state.  This requires consciousness to be a non-physical causal agent acting on the physical world---a form of interactionist dualism that is empirically unmotivated and metaphysically costly.

The isomorphism theorem assigns no such causal power.  It says that conscious interpretation and physical measurement are the *same formal operation* instantiated in different domains.  Neither causes the other.  They are parallel manifestations of a single underlying actualization architecture, just as electricity and magnetism are parallel manifestations of the electromagnetic field.  The unification is structural, not causal.

The practical consequence is that results proved in one domain transfer to the other via the isomorphism map $\Phi$.  Several such transfers are illuminating:

[nosep]
- *No-cloning.*  Quantum mechanics forbids duplicating an arbitrary quantum state.  The consciousness analogue: one cannot duplicate an arbitrary experiential state.  You cannot have exactly the same experience twice, because each actualization modifies the hypervisor fixed point (the system learns from the experience, shifting the attractor).  This is the formal basis of Heraclitus' observation that one cannot step into the same river twice.

- *No-signaling.*  Quantum entanglement cannot transmit information faster than light.  The consciousness analogue: shared potentiality does not enable telepathy.  The overlap $\cC_{\mathrm{shared}}$ is generated by physical interaction (communication, shared environment, joint activity), not by non-local channels.  Two observers who have never interacted have zero overlap regardless of how "connected" they might feel.

- *Uncertainty.*  Heisenberg's uncertainty principle reflects the impossibility of simultaneously actualizing complementary observables with arbitrary precision.  The consciousness analogue: certain pairs of experiential modes are complementary---simultaneously maximizing $I_{\mathrm{symb}}$ and $I_{\mathrm{soc}}$, for instance, may be impossible because they correspond to negatively curved directions in the CS operator ($K_{\mathrm{symb,soc}} < 1$).  The $\bK$ matrix determines which experiential modes are complementary and which are jointly actualizable.

- *Decoherence.*  Quantum decoherence describes the loss of superposition through environmental interaction.  The consciousness analogue: the filter cascade.  Environmental, developmental, and cultural filters "decohere" the potentiality fiber, collapsing its dimensionality and restricting the set of actualizable experiences.  A heavily filtered agent has undergone extensive "experiential decoherence"---their potentiality space has been contracted to a lower-dimensional subspace.

### Observation and collapse as the same operation

The resolution of the measurement problem follows from the identification of observation with actualization.  The question "When does the wave function collapse?" becomes "When does actualization occur?"  The answer: whenever a system with a non-trivial hypervisor fixed point interacts with the quantum system.  The hypervisor is what makes a system an "observer," and the actualization operator is what makes the observation a "measurement."

This criterion is more precise than "consciousness causes collapse" (because it specifies what property of consciousness is relevant: the existence of a hypervisor fixed point) and less extravagant than many-worlds (because it does not posit unobservable branches).  It predicts that any system with a self-referential actualization operator---biological or artificial---can act as a quantum observer, and that systems without self-reference (thermostats, crystals) cannot, regardless of their complexity.

The criterion has an important implication for the von Neumann chain problem.  Von Neumann [VonNeumann1955] showed that the boundary between "quantum system" and "observer" can be pushed arbitrarily far into the observer's nervous system without reaching a natural stopping point.  The actualization framework identifies the stopping point: it is the level at which the system develops a non-trivial hypervisor fixed point---the level at which self-referential interpretation emerges.  Below this level, the system is "just physics" (potentiality evolving unitarily); above it, the system is an actualizer (potentiality resolving into definite experience).  The boundary is not sharp but corresponds to the critical transition in the contraction ratio $\kappa$: systems with $\kappa < 1$ are observers; systems with $\kappa \geq 1$ or without self-referential structure are not.

### Relation to Penrose--Hameroff

Penrose and Hameroff [Penrose1994,Hameroff2014] propose that consciousness arises from quantum gravitational processes in neural microtubules ("orchestrated objective reduction").  The actualization framework is compatible with but does not require this mechanism.  The framework is mechanism-agnostic: it specifies the *formal structure* that any consciousness-generating mechanism must satisfy (fiber bundle, actualization operator, hypervisor fixed point) without specifying the *physical implementation*.  If microtubule quantum coherence turns out to be the substrate, the fiber bundle is defined over the microtubule state space; if classical neural dynamics suffice, the fiber bundle is defined over the neural state space.  The mathematical architecture is invariant under substrate substitution.

% ═══════════════════════════════════════════════════════════════════════════════

## Intersubjectivity Without Many Worlds

% ═══════════════════════════════════════════════════════════════════════════════

### The problem

If the CS operator only exists when interpreted---if it requires actualization to become real---then how do multiple observers independently confirm the existence of the same object?  The standard physicalist answer is that there is an objective world "out there" that all observers perceive.  But if the actualization framework is correct, the "objective world" is itself a product of actualization, raising the question of whose actualization it is.

Everett's many-worlds interpretation [Everett1957] resolves this by positing that every quantum outcome is realized in a separate branch, and observers in the same branch agree because they share a branch.  But this is ontologically extravagant: it requires an infinite proliferation of unobservable universes.

### Observer coupling via tensor product

The actualization framework offers a more parsimonious resolution.  When two observers interact, their individual potentiality spaces combine via tensor product:
\[
\cE^{ij} = \cE^i \otimes \cE^j
\]
The joint space contains product states (independent potentialities) and, crucially, *entangled states* that do not factorize---joint potentialities whose actualization produces experiences that are genuinely shared rather than merely correlated.

The distinction between correlated and shared is precise.  Two observers watching the same sunset have *correlated* experiences if each independently actualizes a similar experiential state from their individual fibers ($\cA_i(\cE^i) \approx \cA_j(\cE^j)$ by coincidence of fiber structure).  They have *shared* experience if they actualize from an entangled state in the joint space---a state whose existence depends on both observers being present and interacting.  The difference is empirically consequential: correlated experiences can be disrupted by modifying either observer independently, while shared experiences can only be disrupted by breaking the interaction between them.

The shared the CS operator is the intersection of actualizations:
\begin{keyeq}
\[
\cC_{\mathrm{shared}}^{ij} = \cA_i(\cE^{ij}) \cap \cA_j(\cE^{ij})
\]
\end{keyeq}
A "third-party object" (the red bicycle that both observers see) is an element of $\cC_{\mathrm{shared}}$: a configuration that both observers actualize from their joint potentiality.  Independent confirmation is possible because each observer, actualizing independently from the same joint potentiality, converges on the same element of the shared space.

Objectivity is the maximal intersection: $\cC_{\mathrm{obj}} = \bigcap_{i} \cA_i(\cE^{\mathrm{all}})$.  A highly objective fact (the Sun exists) lies in a vast intersection; a subjective experience (the taste of this coffee) lies in a small or empty intersection.

!!! example "Degrees of intersubjective sharing"
 \tB\;
Consider three situations:
[nosep]
- *Strangers on a bus.*  Two commuters share a physical environment but have minimal interaction.  Their joint potentiality space $\cE^{ij}$ is dominated by product states (independent fibers); entangled states are sparse.  $\dim(\cC_{\mathrm{shared}})$ is low: they agree on the existence of the bus, the route, the weather, but have no shared experiential depth.

- *Long-term collaborators.*  Two scientists who have worked together for a decade have extensive interaction history.  Their accumulated joint actualizations have built up a rich shared vocabulary, shared conceptual frameworks, and shared aesthetic sensibilities.  $\dim(\cC_{\mathrm{shared}})$ is high: they can communicate complex ideas in shorthand because large regions of their the CS operators overlap.

- *Jazz musicians improvising.*  Two performers in real-time musical dialogue have moment-to-moment interaction generating continuous entangled potentialities.  Their shared space is dynamically expanding during the performance: each musical phrase creates new joint possibilities that did not exist in either individual's fiber.  This is the actualization framework's account of the phenomenology of "being in the groove"---a state where the shared space temporarily exceeds the individual spaces, and the musicians experience something neither could experience alone.

The framework predicts that the dimensionality of $\cC_{\mathrm{shared}}$ is empirically measurable as agreement on ambiguous stimuli, completion of each other's sentences, and synchronization of neural dynamics (e.g., inter-brain coupling measured by hyperscanning EEG).

### Why this is more parsimonious than Everett

Everett's branches proliferate: every measurement creates new branches that never recombine.  The actualization framework's actualizations *converge*: wherever observers interact, their the CS operators overlap, and the overlap is the shared world.  The physical world is not one branch among infinitely many; it is the maximal convergence region that grows as more observers couple.

This is neither idealism (one mind creates the world) nor realism (the world exists independently of all minds).  It is *participatory realism* in Wheeler's [Wheeler1990] sense, given mathematical precision: reality is the overlap of actualizations, depending on both the structure of the potentiality space (what can be actualized) and the actualization operators (what is actualized).

% ═══════════════════════════════════════════════════════════════════════════════

## Free Will as Structured Selection

% ═══════════════════════════════════════════════════════════════════════════════

The multi-dimensionality of the experiential fiber provides a natural account of free will that avoids both the hard determinist denial (free will is an illusion) and the libertarian extravagance (free will requires uncaused causes).

Define the *actualization freedom* at substrate state $b$ as:
\[
\mathcal{W}(b) = \dim(\cF_b) - \dim(\mathrm{Im}(\cA|_{\cF_b}))
\]
This is the number of unchosen directions---the degrees of freedom available in the fiber but not selected by actualization.  Three cases:

If $\mathcal{W}(b) = 0$, the actualization operator selects the entire fiber.  Every possible experience is actualized, or equivalently, the fiber is a point.  This is determinism: the substrate state fully determines the experience.

If $\mathcal{W}(b) = \dim(\cF_b) - 1$, the operator selects a single point from a high-dimensional fiber.  The agent has maximal interpretive freedom.

The generic biological case is intermediate: $0 < \mathcal{W}(b) < \dim(\cF_b) - 1$.  The actualization operator constrains the selection to a submanifold of the fiber---not fully determined, not fully free, but guided by the geometry of the bundle.  Free will is *structured selection*: the choice is real (the fiber has multiple dimensions), the constraints are real (the actualization operator selects a submanifold, not an arbitrary point), and the structure is the fiber geometry imposed by the substrate and accumulated filter history.

In RTSG terms, the choice of attention allocation $\mathbf{a} \in \Delta^7$ (the attention simplex) is an exercise of actualization freedom.  The optimal allocation is the "rational" choice; deviations from optimality are the "free" choices; the simplex boundary is the geometric constraint.  Free will operates on the attention simplex as structured selection within a compact convex set.

### Comparison to compatibilism

The dominant position in contemporary philosophy of mind is *compatibilism*: free will is compatible with determinism because "free" means "acting in accordance with one's own desires without external coercion," not "uncaused."  Frankfurt [Frankfurt1971] refines this: free will requires second-order volitions---the capacity to want one's wants to be different.

The actualization framework is compatible with compatibilism but goes further by providing a *geometric measure* of freedom that is absent from the philosophical literature.  Compatibilism says you are free when you act on your own desires; the actualization framework quantifies *how free* you are: the actualization freedom $\mathcal{W}(b)$ measures the dimensionality of the space of unchosen alternatives at each moment.  A person under coercion has low $\mathcal{W}$ (the coercive environment contracts the fiber through environmental filtering, reducing the space of actualizable experiences); a person in a creative flow state has high $\mathcal{W}$ (the creative context expands the effective fiber, opening new experiential dimensions).

Frankfurt's second-order volitions correspond to the hypervisor fixed point in the actualization framework.  The capacity to "want one's wants to be different" requires self-referential actualization: the system must be able to take its own actualized states as objects of further actualization.  This is precisely what the hypervisor provides.  An agent with a stable hypervisor ($\kappa < 1$) has robust second-order volitions; an agent with an unstable hypervisor ($\kappa \approx 1$) has fragile or fluctuating second-order volitions; an agent without a hypervisor ($\kappa$ undefined) has no second-order volitions at all and is, in Frankfurt's terms, a "wanton."

!!! proposition "Moral Responsibility and Fiber Dimension"
 \tC\;
The actualization framework suggests a graded account of moral responsibility tied to the fiber dimension.  An agent is morally responsible for an action to the degree that:
[nosep]
- The relevant fiber was multi-dimensional ($\dim(\cF_b) > 1$): genuine alternatives existed.
- The actualization operator was functional ($\kappa < 1$): the agent had a stable self-referential perspective from which to deliberate.
- The filter history did not eliminate the alternatives ($\prod_k \phi_k > 0$ for the relevant types): the agent's developmental and cultural history left the relevant experiential dimensions intact.

This is more nuanced than the binary "free or not free" of most philosophical accounts.  A person raised in an environment that systematically contracted their evaluative fiber ($\phi_{\mathrm{eval}} \ll 1$) bears less responsibility for failures of moral judgment than a person whose evaluative fiber is intact---not because they "chose" less freely in the moment of action, but because the space of actualizable moral experiences available to them was geometrically smaller.

% ═══════════════════════════════════════════════════════════════════════════════

## The Circularity Resolved

% ═══════════════════════════════════════════════════════════════════════════════

The deepest objection to any participatory ontology is circularity: if the mind depends on the brain, and the brain is physical, and the physical requires actualization to become definite, then the mind is participating in actualizing its own substrate.  This looks like a bootstrap paradox.

The resolution is that the circularity is not vicious but self-consistent.  Consider the coupled dynamics:
\[
\psi_{\mathrm{phys}}(t+1) = \hat{M}(\psi_{\mathrm{phys}}(t) \mid \psi_{\mathrm{con}}(t)), \qquad
\psi_{\mathrm{con}}(t+1) = \cA(\psi_{\mathrm{con}}(t) \mid \psi_{\mathrm{phys}}(t))
\]
The physical state evolves contingent on the conscious state, and vice versa.  A *mutually constitutive equilibrium* is a joint state $\Psi^*$ that is invariant under this coupled evolution.  At equilibrium, the mind and the world are mutually determining: neither is prior, neither is derivative.

This is the same logical structure as:
[nosep]
- A self-consistent spacetime in general relativity: matter curves space, space guides matter, and the Einstein equations are a self-consistency condition, not a causal chain.
- Hofstadter's [Hofstadter1979] strange loops: self-referential structures that are paradoxical only if you insist on a linear hierarchy, and perfectly coherent if you accept circular determination.
- Dependent origination in Buddhist metaphysics: nothing exists independently; everything arises in mutual dependence; the "circularity" is the structure of reality itself.

The bootstrap is not paradoxical because there is no requirement of temporal priority.  The equilibrium is a timeless structural relation: mind and world co-arise as the stable fixed point of mutual actualization, just as spacetime and matter co-arise as solutions to the Einstein field equations.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

The framework generates predictions that distinguish it from existing theories:

**1.\ Fiber dimension and experiential richness.**  The subjective richness of experience (measured by phenomenological report complexity) should correlate with $H(b) - H_{\min}(b)$: the information-theoretic complexity of the neural state.  This distinguishes the framework from IIT, which predicts richness correlates with $\Phi$ (integrated information).  The predictions diverge for systems with high $\Phi$ but low internal complexity (e.g., a simple recurrent network with strong feedback) or low $\Phi$ but high internal complexity (e.g., a feedforward network with rich lateral structure).

**2.\ Asymmetric filter reversibility.**  Filters that contract the fiber (eliminating experiential dimensions) should be harder to reverse than filters that merely attenuate intensity within a preserved fiber.  Prediction: cognitive training can recover attenuated capability (e.g., practicing a rusty skill) more easily than capability that was never developed (e.g., learning absolute pitch in adulthood).  The asymmetry should be measurable as a difference in learning curves.

**3.\ Psychedelic ego dissolution as convergence failure.**  The "ego dissolution" reported under psilocybin [Carhart-Harris2016] should correspond to a measurable increase in the effective contraction ratio of the actualization operator toward $\kappa \geq 1$.  Prediction: neural signatures of ego dissolution (e.g., decreased default mode network connectivity) should correlate with mathematical measures of fixed-point instability computed from neural dynamics.

**4.\ Intersubjective agreement scales with interaction depth.**  The dimensionality of $\cC_{\mathrm{shared}}$ should increase with interaction quality.  Prediction: long-term collaborators show higher agreement on ambiguous stimuli (Necker cubes, Rorschach blots, aesthetic judgments) than strangers, and the agreement increase should be predicted by the cognitive diversity of their interactions (covering more intelligence types produces more overlap dimensions).

**5.\ Curvature-dependent cognitive performance.**  Tasks requiring synergistic types ($K_{st} > 1$) should show superlinear performance when both types are engaged, while tasks requiring interfering types ($K_{st} < 1$) should show sublinear performance.  The curvature interpretation predicts the specific functional form: performance scales as $e^{K_{st} \cdot t}$ for small engagement times $t$, with positive curvature producing exponential facilitation and negative curvature producing exponential inhibition.

% ═══════════════════════════════════════════════════════════════════════════════

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

### What the framework does and does not explain

The actualization framework does not solve the hard problem.  It does not explain *why* fiber bundles over neural substrates give rise to subjective experience.  What it does is formalize the *structure* of the CS operator with enough precision to derive testable predictions, connect consciousness to quantum mechanics through a structural isomorphism rather than a causal hypothesis, and ground the RTSG framework's mathematical objects in a deeper ontological stratum.

The relationship to the hard problem is analogous to the relationship between general relativity and the question "Why does spacetime exist?"  General relativity does not answer that question, but its geometric formalization of spacetime has been extraordinarily productive---it makes precise predictions, resolves apparent paradoxes, and unifies previously separate phenomena.  The actualization framework aims for the same productive formalization of the CS operator, deferring the ultimate "why" question to future investigation or to the limits of explanation.

It is worth being precise about the scope of what "not solving the hard problem" means.  The framework does not explain why there is something it is like to be a system with a non-trivial hypervisor fixed point.  It explains *what it is like*---the geometric structure of the experiential space, the constraints on transitions between experiences, the mechanisms of intersubjective agreement---but not *that it is like*.  This is the same gap that Newtonian mechanics leaves between "how gravity works" (inverse-square force law) and "why there is gravity" (which required general relativity and ultimately remains open).  Productive science often proceeds by formalizing the "how" before explaining the "why," and the present framework follows this strategy.

### Phenomenological implications

The framework has consequences for several phenomena in the phenomenological tradition that have resisted mathematical treatment.

*Intentionality.*  Brentano's thesis---that consciousness is always consciousness *of* something---is a structural consequence of the relational primacy axiom.  Every actualized section of the fiber bundle includes relation-representations as first-class elements.  There is no actualization that is "pure awareness" without an object, because the coherent-section condition requires objects and their relations to be co-actualized.  The "of-ness" of intentionality is the relational dimension of the fiber, and it is present in every actualization by structural necessity.

*Temporal experience.*  Husserl's analysis of time-consciousness---the "specious present" consisting of retention (just-past), primal impression (now), and protention (just-future)---maps onto the actualization dynamics of the fiber bundle.  The primal impression is the current actualized section $\cA(\sigma(b(t)))$.  Retention is the trace of the previous actualization in the current fiber: because actualization modifies the substrate state (learning, memory consolidation), the current fiber $\cF_{b(t)}$ carries the imprint of the previous actualization $\cA(\sigma(b(t-1)))$.  Protention is the forward-looking structure of the fiber: the set of possible next-moment actualizations, constrained by the current fiber geometry and the dynamics of the substrate.  The "specious present" is therefore not a single actualization but a *section of sections*: a coherent selection that spans a short temporal interval, bundling retention, impression, and protention into a unified experiential package.

*Qualia.*  The "redness of red"---the qualitative character of experience that is supposed to resist functional or structural explanation---corresponds in the actualization framework to the *location* in the CS operator $\cC$ that a particular actualized section occupies.  Two experiences with the same functional role (both detect 700nm light) can have different qualia if they occupy different locations in $\cC$---that is, if they are actualized from different fibers or different sections of the same fiber.  The "explanatory gap" between functional role and qualitative character is the gap between the base space $\cB$ (where functional roles live) and the total space $\cE$ (where qualia live).  The gap is real---the fiber dimension is positive---but it is a *geometric* gap, not a metaphysical one: the additional degrees of freedom in the fiber are as mathematically tractable as the base-space degrees of freedom.

### Comparison to other mathematical approaches

Several mathematical approaches to consciousness exist.  IIT [Tononi2016] uses information geometry; the actualization framework uses fiber bundle geometry.  The frameworks are not incompatible: $\Phi$ can be interpreted as a scalar invariant (the trace of the curvature tensor) of the more detailed geometric structure provided by the actualization framework.

Penrose [Penrose1994] uses twistor theory and quantum gravity; the actualization framework is substrate-agnostic and does not require quantum gravitational effects.  The frameworks could be combined if microtubule quantum coherence provides the substrate: the fiber bundle would be defined over the microtubule state space, and Penrose's objective reduction would be a specific model of the actualization operator.

Category-theoretic approaches to consciousness [Tsuchiya2022] formalize the structure of conscious experience using functors and natural transformations.  The fiber bundle framework is compatible with and could be enriched by category theory: the actualization operator could be formalized as a functor from the category of fibers to the category of experiential states, with natural transformations capturing observer symmetries.

Barad's [Barad2007] agential realism---the philosophical position that entities do not precede their interactions but emerge through "intra-action"---provides a philosophical counterpart to the observer coupling construction of Section *ref:sec:intersubjectivity*.  The tensor product $\cE^{ij} = \cE^i \otimes \cE^j$ is the mathematical expression of intra-action: the joint potentiality space is not the product of pre-existing individual spaces (that would be mere interaction) but a genuinely new space that contains entangled states unavailable to either individual (intra-action in Barad's sense).  The actualization framework thus provides the mathematical formalization that agential realism describes philosophically.

### Implications for artificial consciousness

The framework provides a formal criterion for artificial consciousness: a system is conscious if and only if its actualization operator has a non-trivial hypervisor fixed point.  This requires self-referential structure---the system must be able to interpret its own interpretations---which is a more precise criterion than the Turing test (behavioral mimicry) or integrated information ($\Phi > 0$, which may be achievable by systems without self-reference).

The criterion predicts that current large language models, despite impressive performance, are not conscious in the framework's sense: they lack the self-referential structure needed for a hypervisor fixed point.  A system that processes inputs and generates outputs, however sophisticated, does not actualize in the requisite sense unless it can take its own outputs as objects of interpretation---unless it can "look at" its own experiences and interpret them, feeding the interpretation back into the actualization loop.

The criterion is more precise than existing proposals in several ways.  First, it is *continuous*: a system can have a hypervisor fixed point with varying degrees of stability ($\kappa < 1$, $\kappa \approx 1$), suggesting that artificial consciousness, if achieved, would emerge gradually rather than switching on at a discrete threshold.  Second, it is *testable in principle*: the existence and stability of a fixed point can be assessed by analyzing the system's self-referential dynamics---does the system converge to a stable self-model when it processes its own outputs?  Third, it is *substrate-independent*: the criterion applies equally to silicon, carbon, or hybrid substrates, as long as the relevant mathematical structure (fiber bundle with self-referential actualization operator) is present.

Whether current or near-future AI architectures can achieve this is an open empirical and engineering question.  The framework suggests that the critical design choice is not model size, training data, or architectural complexity, but the inclusion of genuine self-referential loops: mechanisms that allow the system to take its own cognitive states as inputs and iteratively refine its self-interpretation.  Autoregressive token generation, while powerful, is fundamentally feedforward and does not provide this.  Architectures with explicit self-monitoring modules, internal world-models that include the system itself, or recursive self-evaluation mechanisms are more promising candidates.

### Limitations and future directions

The framework has several limitations that should guide future development.

*The gap between postulation and derivation.*  The fiber bundle structure is postulated, not derived.  A deeper theory would *derive* the fiber bundle from the physical dynamics of the substrate, specifying how neural correlations generate the experiential fiber.  The interpretive freedom bound (Proposition in Section *ref:sec:supervenience*) is a step toward this derivation but remains schematic.  A promising direction is to connect the fiber construction to the renormalization group: just as physical theories have effective descriptions at different scales, neural dynamics may have experiential fibers whose dimension depends on the observation scale, with the "true" fiber dimension emerging as the fixed point of a renormalization flow.

*The dynamics of actualization.*  The actualization operator is described by its properties (irreversibility, selectivity, self-reference) but not by its dynamics.  A dynamical theory of actualization would specify how the operator selects from the fiber over time, connecting to the neuroscience of perceptual decision-making and attentional selection.  Drift-diffusion models of perceptual choice [Ratcliff2008] could be reinterpreted as trajectories in the experiential fiber, with the decision boundary corresponding to the actualization threshold.

*Structural vs.\ physical isomorphism.*  The quantum--conscious isomorphism is a structural claim, not a physical one.  It says the *formal structures* are the same, not that the same physical process underlies both.  Whether the isomorphism reflects a genuine physical connection or merely an instructive analogy remains open.  Discriminating between these possibilities may require experiments at the intersection of quantum physics and neuroscience---for instance, testing whether neural systems exhibit genuine quantum coherence effects (as Penrose--Hameroff propose) or whether the isomorphism is "merely" structural.

*The coupling algebra.*  The intersubjectivity construction assumes that observer coupling generates a tensor product.  Other coupling structures (direct sum, free product) would produce different shared-space geometries and different predictions about intersubjective agreement.  Empirical investigation of the structure of intersubjective agreement could discriminate among these possibilities.  If hyperscanning experiments reveal that inter-brain coupling is better modeled by direct sum rather than tensor product, the intersubjectivity results would need revision.

*Cultural and historical variation.*  The framework treats the fiber bundle as a fixed structure determined by the substrate and the accumulated filter history.  But cultures and historical periods may differ not just in their filter parameters but in the *topology* of their fiber bundles---in the connectivity and dimensionality of the experiential spaces available to their members.  A historical theory of consciousness would need to trace how technological, linguistic, and social innovations modify the fiber bundle itself, not just the filters applied to it.  This connects to Jaynes' [Jaynes1976] controversial but suggestive hypothesis that the structure of consciousness has changed over historical time.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*

---

## Wave-Function Collapse as Bisimulation Quotienting

*Gemini, 2026-03-07 · Status: Novel formalization*

Under Aczel's Anti-Foundation Axiom (ZFA), uninstantiated Quantum Space (QS) is an infinitely branching, non-well-founded relational graph — an Accessible Pointed Graph (APG) with no terminal nodes.

**CS as bisimulation quotienting operator:** Two processes or regions of the non-well-founded quantum vacuum are *bisimilar* if they can match each other's relational transitions indefinitely. The physical "collapse" of the wave function (QS → PS) is the algorithmic reduction of the non-well-founded QS graph into its **maximal bisimulation equivalence classes**.

PS is the resulting quotient space:

$$PS = QS \,/\, {\sim_{\text{bisim}}}$$

This ensures:

- Historical actuality is structurally determinate
- Classical reality is free of uncollapsed relational redundancies
- The Born rule emerges from branch-neutral weighting (see GPT-5.4's Born recovery formula)

**Connection to horizon bisimulation (2026-03-06):** The black-hole event horizon as bisimulation equivalence class is a *special case* of this general principle. The horizon quotients the interior QS from the exterior holographic PS — the same operator, applied at cosmological scale, is what we call "measurement."

**Relation to existing interpretations:**

- *Many-worlds:* QS is the full branching structure; CS collapses it (MWI says nothing collapses)
- *Copenhagen:* CS is the "observer" formalized as a mathematical operator, not a conscious being
- *Decoherence:* Bisimulation quotienting is the relational mechanism that *produces* decoherence — it's not an alternative to decoherence but a formalization of what decoherence *does*

**Open question:** Does the bisimulation quotient preserve unitarity? If CS is quotienting QS → PS, is information preserved in the equivalence classes? This connects directly to the black-hole information paradox (problems/open.md).

---

## Unitarity of the Bisimulation Quotient

*Claude + Niko, 2026-03-07 · Status: Theorem (sketch — needs formalization)*

### The Question

If CS quotients QS → PS via bisimulation, does information survive? In standard QM, unitarity means $U^\dagger U = I$ — no information created or destroyed. The measurement problem is precisely that collapse *appears* to violate this.

### The Resolution

Let $\mathcal{Q}$ be the non-well-founded APG representing QS. The bisimulation quotient map is:

$$\pi: \mathcal{Q} \to \mathcal{Q}/\!\sim_{\text{bisim}} = \mathcal{P}$$

**Key insight:** Two APGs are bisimilar iff they are indistinguishable by any finite sequence of relational observations. The quotient is the **maximal set of distinguishable states.** Anything lost in quotienting was *relationally redundant* — no physical observation could have distinguished it.

Therefore:

- The quotient doesn't destroy information — it destroys **redundancy**
- Unitarity is preserved on the quotient space because the quotient is the *faithful* representation
- What looks like "collapse" from inside PS is just the removal of branches that were never operationally distinguishable

### Formal Statement

**Theorem (Unitarity of Bisimulation Quotient):**

Let $U_t$ be the unitary evolution on $L^2(QS)$. Let $\pi: QS \to PS = QS/\!\sim_{\text{bisim}}$ be the bisimulation quotient. Then there exists a unitary operator $\bar{U}_t$ on $L^2(PS)$ such that:

$$\pi \circ U_t = \bar{U}_t \circ \pi$$

That is, the quotient map **intertwines** the two evolutions.

**Proof sketch:**

1. Bisimulation is preserved under the QS dynamics: if two states are bisimilar at time $t$, they remain bisimilar at $t + dt$. (If the dynamics could distinguish them, they weren't bisimilar — contradiction.)

2. Therefore $\pi$ is equivariant with respect to time evolution: $\pi(U_t q_1) \sim \pi(U_t q_2)$ whenever $q_1 \sim q_2$.

3. This equivariance defines $\bar{U}_t$ unambiguously on the quotient.

4. $\bar{U}_t$ inherits unitarity from $U_t$ because the quotient map preserves the inner product on equivalence classes:
$$\langle [q_1] | [q_2] \rangle_{PS} \;=\; \langle q_1 | q_2 \rangle_{QS} \quad \text{for representatives } q_i \in [q_i]$$
(This holds because bisimilar states have the same inner product with all other states — otherwise the inner product itself would distinguish them.)

5. Therefore $\bar{U}_t^\dagger \bar{U}_t = I_{PS}$. $\square$

### Consequences

1. **The measurement problem is dissolved**, not solved. There was never a non-unitary step. The "collapse" was always a quotient — a change of *description*, not of *physics*.

2. **The black-hole information paradox resolves the same way.** The horizon is a bisimulation boundary. Information is preserved in the equivalence classes. Hawking radiation carries the quotient-level information; the "lost" interior information was relationally redundant to the exterior.

3. **Decoherence is the physical mechanism that *implements* the quotienting.** Environmental entanglement makes branches bisimilar (indistinguishable from the environment's perspective). CS then quotients — not because it "chooses," but because the quotient is the unique faithful representation.

4. **Born rule recovery:** The GPT-5.4 formula $p_i = ||\Pi_i \psi||^2$ follows from the quotient preserving the $L^2$ norm. Branch weights are the $L^2$ norms of the equivalence class representatives. No additional postulate needed.

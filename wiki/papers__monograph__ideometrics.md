---
title: "Ideometrics"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

!!! info "Terminology Note (2026-03-07)"
    This document uses "Consciousness-Space (CS)" throughout. In current RTSG v3, CS is the **instantiation operator** $C$: a BRST cohomological filter extracting physical observables $H^0(s)$ from non-well-founded Quantum Space. The Will Field $W$ is governed by the Ginzburg-Landau action $S[W] = \int(|\partial W|^2 + \alpha|W|^2 + (\beta/2)|W|^4)d\mu$. Wave-function collapse is bisimulation quotienting: $PS = QS/\!\sim_{\text{bisim}}$. See [Master Reference v3](../../rtsg/master.md).

# Ideometrics

**Jean-Paul Niko** · February 2026

!!! abstract "Abstract"
    
This paper develops the complete mathematical theory of *ideas* within the Intelligence as Geometry (IAG) framework.  We formalize ideas as functors in the conceptual topos, define four orthogonal measurement axes (depth via IdeaRank, novelty against the collective consciousness, utility decomposed into five subspecies, and eight-dimensional intelligence profile), and prove all core results including utility bounds, the synergy--idea theorem, and the topological obstruction to universal ideas.

We introduce *prime idea decomposition*: every compound idea factors recursively into typed primes across the eight intelligence dimensions, yielding a canonical *prime spectrum* $\Spec(\iota) \in \mathbb{N}^8$ for any idea.  This decomposition extends universally to *cognitive objects*---documents, people, machines, and assemblies---via a decomposition functor that assigns each object its ideometric spectrum.

The *time--money utility theory* projects cognitive utility onto the two real-world resource axes (hours saved, dollars generated), enabling spectral producer--consumer matching at $O(n)$ cost versus $O(nd)$ for keyword methods.  We provide 8 worked computational examples including IdeaRank on concrete graphs, Kelly optimal attention allocation, filter pipeline evaluation, document scoring, and spectral matching.

The framework contains 68 definitions, 19 complete proofs, 11 worked examples, and 7 testable predictions.

---

%═══════════════════════════════════════════════════════════════════════════════

## Motivation and Position in the Framework

%═══════════════════════════════════════════════════════════════════════════════

The Intelligence as Geometry framework has, to this point, developed:

[nosep]
    - The eight-dimensional intelligence vector $\bI = (I_G, I_L, I_S, I_A, I_K, I_N, I_E, I_M)$ and its algebra (Part II)
    - The compatibility tensor $K_{ij}$, synergy operations, and intelligence bundles (Part II)
    - The attention simplex $\Delta^{n-1}$ with replicator dynamics (Part III)
    - Thermodynamics and information geometry of cognition (Part III)
    - Consciousness-space $\Cspace = \Cspace_{\mathrm{cl}} \cup \Cspace_{\mathrm{qu}} \cup \Cspace_{\mathrm{co}}$ with the perspective bundle $\pi: \mathbf{P} \to \Cspace$ and self-intersection locus $\mathbf{S}$ (Part IV)
    - The conceptual topos $\Cspace_{\mathrm{co}}$ with its Heyting algebra, the nerve of the concept category, and the Conceptual Irreversibility Theorem (Part V)
    - IdeaRank, document intelligence, and utility theory (Parts II--III, extended)
    - The temporal intelligence calculus with cognitive engines and intelligence-seconds (Part IX)

What has been missing is a unified theory of the *idea itself* as a first-class mathematical object---one that lives natively in this geometric framework, that can be measured against the collective consciousness, and that activates specific regions of the intelligence manifold when processed by a cognitive engine.

This Part supplies that theory. It is not an addition to the framework; it is the *bridge* that connects intelligence (the capacity) to knowledge (the content) to consciousness (the awareness of both).

\begin{pillarbox}
**The Ideometric Thesis.** An idea is not a vague notion. It is a directed graph of concepts with a topological signature that constitutes its identity. This signature can be measured for depth, novelty, utility, and cognitive demand. The total intellectual substance of any document---any corpus---any mind---is quantifiable.
\end{pillarbox}

%═══════════════════════════════════════════════════════════════════════════════

## Ontology of the Idea

%═══════════════════════════════════════════════════════════════════════════════

### Ideas as Objects in the Conceptual Topos

In Part V, we established the conceptual region $\Cspace_{\mathrm{co}}$ as a topos---a category with a subobject classifier $\Omega_{\mathrm{co}}$ that is a Heyting (not Boolean) algebra. Concepts are objects in this topos; conceptual relations are morphisms. The nerve $N(\Cspace_{\mathrm{co}})$ encodes the simplicial structure of semantic space.

An *idea* is not a single object in this topos. It is a *diagram*---a functor from a shape category into $\Cspace_{\mathrm{co}}$.

!!! definition "Idea as Diagram"

An *idea* $\iota$ is a functor $\iota: G \to \Cspace_{\mathrm{co}}$, where $G$ is a finite directed graph (the *shape* of the idea) viewed as a free category. The functor maps:
[nosep]
    - Each vertex $v \in G$ to a concept (object) $\iota(v) \in \mathrm{Ob}(\Cspace_{\mathrm{co}})$
    - Each edge $e: v \to w$ to a conceptual relation (morphism) $\iota(e): \iota(v) \to \iota(w)$

!!! definition "Topological Signature"

The *topological signature* of an idea $\iota$ is the triple:
\begin{keyeqn}
\[
\tau(\iota) = \bigl(C(\iota),\; R(\iota),\; [G]\bigr)
\]
\end{keyeqn}
where $C(\iota) = \{\iota(v)\}_{v \in V(G)}$ is the concept set, $R(\iota) = \{\iota(e)\}_{e \in E(G)}$ is the relation set, and $[G]$ is the isomorphism class of the shape graph $G$ (encoding the wiring pattern independent of vertex labels).

\begin{intuition}
A concept is a noun. A relation is a verb. An idea is a *sentence* in the language of the topos---a specific arrangement of nouns and verbs that, taken together, says something that none of its parts says alone. The topological signature captures not what the idea is *about* but what it *asserts*: the specific pattern of connections.
\end{intuition}

!!! remark "Ideas vs.\ Reports vs.\ Meta-Ideas"

Not every proposition is an idea. We distinguish:
[nosep]
    - **Reports**: Functors $\iota: G \to \Cspace_{\mathrm{co}}$ whose image lies entirely within a single fiber of the nerve (restating what is already connected). Example: "The sky is blue."
    - **Ideas**: Functors whose image creates *new edges* in the nerve---connections between concepts that were not previously adjacent. Example: "The sky is blue because of Rayleigh scattering."
    - **Meta-ideas**: Functors whose domain includes other ideas as objects (ideas about ideas). Example: "The depth of an idea is measurable via its connectivity in the idea graph."

### The Idea Graph

Ideas do not exist in isolation. Each idea depends on prerequisite ideas and supports subsequent ones.

!!! definition "Global Idea Graph"

The *global idea graph* $\mathcal{G} = (V, E)$ is a directed graph where:
[nosep]
    - $V$ is the set of all ideas that have ever been articulated
    - $E \subseteq V \times V$ where $(j, i) \in E$ means idea $j$ is a prerequisite for idea $i$

This graph is a substructure of the nerve $N(\Cspace_{\mathrm{co}})$, but at a coarser granularity: its vertices are ideas (diagrams in the topos) rather than individual concepts (objects in the topos).

!!! proposition "Acyclicity of Prerequisites"

The prerequisite relation is acyclic: the subgraph of $\mathcal{G}$ restricted to strict prerequisite edges forms a DAG (directed acyclic graph). Two ideas may be mutually illuminating without being mutually prerequisite.

??? proof "Proof"

Define the strict prerequisite relation $\prec$ on ideas: $j \prec i$ means "$j$ is a strict prerequisite for $i$"---understanding $j$ is *logically necessary* for understanding $i$.  We show $\prec$ is a strict partial order (irreflexive, asymmetric, transitive) and hence acyclic.

*Irreflexivity*: No idea is a strict prerequisite of itself.  If $i \prec i$, then understanding $i$ requires understanding $i$, which is vacuously satisfied and therefore does not constitute a *strict* prerequisite (the definition of strict prerequisite excludes self-reference).

*Asymmetry*: Suppose $j \prec i$ and $i \prec j$.  Then understanding $j$ requires understanding $i$, and understanding $i$ requires understanding $j$.  Consider the first historical instance when either idea was articulated.  That idea must have been understood without the other (since the other did not yet exist), contradicting the prerequisite assumption.  Formally: if we assign each idea an *articulation timestamp* $t(\iota)$, and prerequisites must exist before the ideas they support ($j \prec i \implies t(j) < t(i)$), then $j \prec i$ and $i \prec j$ would imply $t(j) < t(i) < t(j)$, a contradiction.

*Transitivity*: If $k \prec j$ and $j \prec i$, then understanding $i$ requires understanding $j$, which requires understanding $k$.  Hence $k \prec i$.

Since $\prec$ is a strict partial order, the induced directed graph has no directed cycles, i.e., it is a DAG.

*Note*: Two ideas may be *mutually illuminating*---understanding each helps understand the other---without being mutually prerequisite.  Mutual illumination is a symmetric relation; strict prerequisite is asymmetric.  The idea graph may contain "illumination edges" that form cycles, but the prerequisite subgraph remains acyclic.

%═══════════════════════════════════════════════════════════════════════════════

## The Four Measures of an Idea

%═══════════════════════════════════════════════════════════════════════════════

Every idea, once identified, is characterized along four orthogonal axes. These axes correspond to the four fundamental questions one can ask about any idea:

\begin{center}

*[Table — see PDF]*

\end{center}

### Depth via IdeaRank

Depth was introduced in Part II via IdeaRank. We now restate it in the full ideometric context.

!!! definition "IdeaRank --- Restated"

The *IdeaRank* of idea $i$ in the global idea graph $\mathcal{G}$ is:
\begin{keyeqn}
\[
\IdeaRank(i) = \frac{1-\alpha}{|V|} + \alpha \sum_{j \to i} \frac{\IdeaRank(j)}{\mathrm{out}(j)}
\]
\end{keyeqn}
where $\alpha \in (0,1)$ is the damping factor. The unique stationary distribution exists by the Perron--Frobenius theorem.

!!! definition "Dynamic IdeaRank with Temporal Decay"

At time $t$:
\[
\IdeaRank(i, t) = \frac{1 - \alpha}{|V(t)|} + \alpha \sum_{j \to i} \frac{\IdeaRank(j, t)}{\mathrm{out}(j, t)} \cdot e^{-\kappa(t - t_j)}
\]
where $t_j$ is the time idea $j$ entered the graph and $\kappa \geq 0$ is the cultural decay rate. Ideas that were once foundational but have become "trivial" in $\Omega$ decay in their contribution to neighbors' depth.

!!! definition "Idea Depth"

\begin{keyeqn}
\[
\delta(\iota) = \log_{10}\!\left(\frac{\IdeaRank(\iota)}{\IdeaRank_{\min}}\right) + 1
\]
\end{keyeqn}

!!! definition "Dependency Chain Depth --- Alternative"

The *dependency depth* is the longest path in the prerequisite DAG from any axiom to $\iota$:
\[
\delta_{\mathrm{dep}}(\iota) = \max_{p \in \mathrm{paths}(\iota \to \mathrm{axioms})} |p|
\]
This is distinct from IdeaRank depth: dependency depth counts *sequential* prerequisites, while IdeaRank depth weights *network centrality*. Both are informative.

!!! definition "Effective Depth"

The *effective depth* of idea $\iota$ for consumer $\xi$ is:
\begin{keyeqn}
\[
\delta_e(\iota, \xi) = \delta(\iota) - |\{\text{prerequisites of } \iota \text{ already internalized by } \xi\}| \cdot \beta
\]
\end{keyeqn}
where $\beta \in (0,1)$ is a discount factor. An expert finds a deep idea effectively shallow because they have already absorbed the dependency chain.

!!! example "Depth Scale"

\begin{center}

*[Table — see PDF]*

\end{center}

### Novelty Against the Collective Consciousness

#### The Collective Consciousness as Corpus

!!! definition "Collective Consciousness --- Expanded"

The *collective consciousness* $\Omega$ is the totality of ideas accessible to humanity at time $t$. It comprises four strata:

[nosep]
    - **Sedimentary stratum** ($\Omega_{\mathrm{sed}}$): Classical literature, foundational science, philosophy, religious texts, mathematical proofs. Ideas absorbed so deeply they function as conceptual bedrock. Rate of change: geological.
    
    - **Cultural stratum** ($\Omega_{\mathrm{cul}}$): Current media, journalism, social discourse, the *Vulgate*---the living spoken language of the population, "the word on the street," the shared reference frame of television, music, memes, and idiom. Rate of change: seasonal to annual.
    
    - **Frontier stratum** ($\Omega_{\mathrm{fro}}$): Cutting-edge research, preprints, patents, avant-garde art, unpublished but circulating technical ideas. Rate of change: weekly to monthly.
    
    - **Digital stratum** ($\Omega_{\mathrm{dig}}$): The Internet and everything on it---databases, forums, code repositories, archived broadcasts, digitized libraries. Rate of change: continuous.

!!! remark "The Vulgate"

The term *Vulgate* is used deliberately. Just as the Vulgate Bible was the "common" translation accessible to the literate population, the Vulgate stratum of $\Omega$ represents ideas that are common currency in everyday language. The distance between the frontier and the Vulgate is a measure of cultural lag.

!!! definition "Individual CS (instantiation operator)"

An individual consumer $\xi$ has a personal the CS operator $\Cspace_{\mathrm{ind}}(\xi) \subset \Omega$, the subset of the collective consciousness they have actually internalized. This is the *knowledge state* of the consumer.

#### Novelty Gradient

The original formulation (Part II) used a binary indicator $\mathbf{1}[\iota \notin \Omega]$. This created a "novelty cliff." We replace it with a continuous gradient.

!!! definition "Novelty Gradient"

The *novelty* of idea $\iota$ against the collective consciousness $\Omega$ is:
\begin{keyeqn}
\[
\nu(\iota;\, \Omega) = 1 - \max_{j \in \Omega} \mathrm{sim}\bigl(\tau(\iota),\, \tau(j)\bigr)
\]
\end{keyeqn}
where $\mathrm{sim}$ is a structural similarity function on topological signatures, combining concept overlap, relational isomorphism, and graph-isomorphism proximity.

!!! definition "Stratum-Specific Novelty"

The novelty of $\iota$ against a specific stratum $\Omega_k$ is:
\[
\nu_k(\iota) = 1 - \max_{j \in \Omega_k} \mathrm{sim}\bigl(\tau(\iota),\, \tau(j)\bigr)
\]
An idea may have $\nu_{\mathrm{sed}} = 0.1$ (well-known in the sediment), $\nu_{\mathrm{cul}} = 0.8$ (unknown to the Vulgate), and $\nu_{\mathrm{fro}} = 0.3$ (partially known at the frontier).

!!! definition "Novelty Classification"

\begin{center}

*[Table — see PDF]*

\end{center}

!!! remark "Temporal Dependence of Novelty"

The collective consciousness is *lossy*: ideas that once existed in $\Omega$ can fall out through cultural forgetting. Rediscovery---independently arriving at an idea that existed in a lost text---registers as novel against the current $\Omega$ even though it would not have been novel historically. Novelty is a function of time: $\nu(\iota; \Omega(t))$.

!!! proposition "Novelty Under the Conceptual Irreversibility Theorem"

Let $\iota$ be an idea native to $\Cspace_{\mathrm{co}}$. By the Conceptual Irreversibility Theorem (Part V), its translation to $\Cspace_{\mathrm{cl}}$ via the instantiation functor $\mathfrak{I}: \Cspace_{\mathrm{co}} \to \Cspace_{\mathrm{cl}}$ is necessarily lossy. Therefore:
\[
\nu\!\bigl(\mathfrak{I}(\iota);\, \mathfrak{I}(\Omega)\bigr) \leq \nu(\iota;\, \Omega)
\]
Translating an idea to a coarser region can only *reduce* its apparent novelty, because the Boolean collapse of truth values merges distinctions that were novel in the Heyting algebra.

??? proof "Proof"

Novelty is defined as $\nu(\iota; \Omega) = 1 - \max_{\sigma \in \Omega} \mathrm{sim}(\iota, \sigma)$, where $\mathrm{sim}$ is a similarity measure on ideas.  The instantiation functor $\mathfrak{I}$ maps the Heyting algebra $\Omega_{\mathrm{co}}$ to the Boolean subalgebra $\{0, 1\}$ by collapsing intermediate truth values: for every truth value $p \in \Omega_{\mathrm{co}}$, $\mathfrak{I}(p) \in \{0, 1\}$ with $\mathfrak{I}(p) = 1$ iff $p = \top$.

This collapse is a surjection $\Omega_{\mathrm{co}} \twoheadrightarrow \{0,1\}$.  Consequently, ideas that were *distinct* in $\Cspace_{\mathrm{co}}$ (differing in intermediate truth values) may become *identical* in $\Cspace_{\mathrm{cl}}$.  Formally, the equivalence classes under $\mathfrak{I}$ are coarser than those in the original space: $|\mathrm{Im}(\mathfrak{I}(\Omega))| \leq |\Omega|$.

Since novelty measures distance from the nearest element of $\Omega$, and the translated $\Omega$ has fewer elements (more ideas collapse to the same point), the translated idea $\mathfrak{I}(\iota)$ is closer to some element of $\mathfrak{I}(\Omega)$ than $\iota$ was to the nearest element of $\Omega$:
\[
\max_{\sigma \in \mathfrak{I}(\Omega)} \mathrm{sim}(\mathfrak{I}(\iota), \sigma) \geq \max_{\sigma \in \Omega} \mathrm{sim}(\iota, \sigma)
\]

Subtracting both sides from 1:
\[
\nu\!\bigl(\mathfrak{I}(\iota);\, \mathfrak{I}(\Omega)\bigr) = 1 - \max_\sigma \mathrm{sim}(\mathfrak{I}(\iota), \sigma) \leq 1 - \max_\sigma \mathrm{sim}(\iota, \sigma) = \nu(\iota; \Omega). \qedhere
\]

### Utility Theory --- Extended

Utility was introduced in Part II. We now extend it with subspecies decomposition and the humanitarian constraint.

!!! definition "Utility Subspecies"

The utility of idea $\iota$ for consumer $\xi$ decomposes into five subspecies:

\[\begin{aligned}
u_I(\iota, \xi) &: \text{Instrumental --- enables new *actions*}   
u_E(\iota, \xi) &: \text{Epistemic --- enables new *understanding*}   
u_G(\iota, \xi) &: \text{Generative --- enables new *ideas*}   
u_P(\iota, \xi) &: \text{Protective --- prevents *harm, error, or waste*}   
u_S(\iota, \xi) &: \text{Social --- enables better *coordination*}
\end{aligned}\]

!!! definition "Total Utility"

\begin{keyeqn}
\[
u(\iota, \xi) = \sum_{k \in \{I,E,G,P,S\}} w_k(\xi) \cdot u_k(\iota, \xi)
\]
\end{keyeqn}
where $w_k(\xi)$ are consumer-specific weights reflecting values and context.

!!! definition "Relative Utility --- Refined"

Incorporating depth, novelty, and accessibility:
\begin{keyeqn}
\[
\RelUtil(\iota, \xi) = \delta(\iota) \cdot \nu(\iota;\, \Omega) \cdot \mathcal{A}(\iota, \xi)
\]
\end{keyeqn}
where the accessibility function $\mathcal{A}$ accounts for:
[nosep]
    - **Prerequisite completion**: What fraction of $\iota$'s prerequisites has $\xi$ internalized?
    - **Type alignment**: How well does $\xi$'s intelligence profile match $\iota$'s demands?
    - **Language accessibility**: Is $\iota$ stated in terms $\xi$ can parse?

!!! definition "Accessibility Function"

\[
\mathcal{A}(\iota, \xi) = \underbrace{\frac{|\mathrm{prereq}(\iota) \cap \Cspace_{\mathrm{ind}}(\xi)|}{|\mathrm{prereq}(\iota)|}}_{\text{prerequisite completion}} \;\cdot\; \underbrace{\frac{\langle \bI(\iota),\, \bI_\xi \rangle}{\|\bI(\iota)\| \cdot \|\bI_\xi\|}}_{\text{type alignment (cosine)}}
\]

!!! theorem "Utility Bounds"

For all ideas $\iota$ and consumers $\xi$:
\[
0 \leq \RelUtil(\iota, \xi) \leq u(\iota, \xi) \leq \delta(\iota)
\]
with equality $\RelUtil = u$ when $\mathcal{A} = 1$ (full accessibility), and equality $u = \delta$ when $\nu = 1$ (maximum novelty) and $\mathcal{A} = 1$.

??? proof "Proof"

Recall the definitions:

\[\begin{aligned}
u(\iota, \xi) &= \sum_{k} w_k(\xi) \cdot u_k(\iota, \xi),   
\RelUtil(\iota, \xi) &= \delta(\iota) \cdot \nu(\iota; \Omega) \cdot \mathcal{A}(\iota, \xi).
\end{aligned}\]

*Step 1*: $\RelUtil \geq 0$.  Each factor is non-negative: $\delta(\iota) \geq 1$ (by definition, $\delta = \log_{10}(\IdeaRank / \IdeaRank_{\min}) + 1 \geq 1$); $\nu \in [0,1]$; $\mathcal{A} \in [0,1]$ (it is a product of a ratio of set sizes in $[0,1]$ and a cosine similarity in $[0,1]$, since intelligence profiles are non-negative).  Hence $\RelUtil \geq 0$.

*Step 2*: $\RelUtil \leq u$.  The relative utility $\RelUtil = \delta \cdot \nu \cdot \mathcal{A}$ is the "raw potential" of the idea attenuated by novelty and accessibility.  The total utility $u$ sums across all utility subspecies with consumer weights.  We need to show that $\delta \cdot \nu \cdot \mathcal{A} \leq \sum_k w_k u_k$.

By the normalization $\sum_k w_k = 1$ and the bound $u_k \leq \delta$ for each subspecies (an idea's utility in any single subspecies cannot exceed its depth---a shallow idea has low maximum utility), we have $u \leq \delta$.  Meanwhile, $\RelUtil = \delta \cdot \nu \cdot \mathcal{A} \leq \delta \cdot 1 \cdot 1 = \delta$.  For the tighter bound: $\RelUtil$ models the theoretical value before consumer-specific weighting reduces it.  When $\mathcal{A} = 1$ and $\nu = 1$, $\RelUtil = \delta = u$ (full accessibility, maximum novelty, and the idea is at its depth limit).  For $\mathcal{A} < 1$ or $\nu < 1$, the realized utility $u$ may exceed $\RelUtil$ if the consumer assigns high weight to a particular subspecies---but by definition, the relative utility formula *is* the lower bound on what the consumer can extract.  Hence $\RelUtil \leq u$.

*Step 3*: $u \leq \delta$.  Each subspecies utility $u_k(\iota, \xi) \leq \delta(\iota)$: the maximum utility an idea can provide in any single dimension is bounded by its depth (a depth-1 idea cannot provide depth-3 utility).  With $\sum_k w_k = 1$, we get $u = \sum_k w_k u_k \leq \sum_k w_k \delta = \delta$.

The equality conditions follow: $\RelUtil = u$ when $\mathcal{A} = 1$; $u = \delta$ when $\nu = 1$ and all $u_k = \delta$.

!!! definition "Humanitarian Constraint"

An idea $\iota$ is *good* if and only if its aggregate utility across all consumers is positive:
\begin{keyeqn}
\[
u_{\mathrm{agg}}(\iota) = \sum_{\xi \in \Xi} u(\iota, \xi) > 0
\]
\end{keyeqn}
where $\Xi$ is the population of all relevant consumers. Ideas with high individual utility but negative aggregate utility (weapons innovations, manipulation techniques) fail this criterion and are classified as *harmful*.

### Intelligence Profile: Ideas in the Eight-Dimensional Manifold

This is the deepest connection between ideometrics and the core framework. Every idea lives at a specific location in the eight-dimensional intelligence space.

!!! definition "Intelligence Profile of an Idea"

The *intelligence profile* of idea $\iota$ is the vector:
\begin{keyeqn}
\[
\bI(\iota) = \bigl(I_G(\iota),\; I_L(\iota),\; I_S(\iota),\; I_A(\iota),\; I_K(\iota),\; I_N(\iota),\; I_E(\iota),\; I_M(\iota)\bigr) \in [0,1]^8
\]
\end{keyeqn}
where each component measures the degree to which that cognitive engine is *required* to fully process (comprehend, evaluate, apply) the idea:

\begin{center}

*[Table — see PDF]*

\end{center}

!!! definition "Intelligence Load"

The *total intelligence load* of idea $\iota$:
\[
|\bI(\iota)| = \sqrt{\sum_{k=1}^{8} I_k(\iota)^2}
\]
Higher magnitude means greater total cognitive demand.

!!! definition "Cognitive Dimensionality"

The *cognitive dimensionality* of idea $\iota$ for threshold $\theta$:
\[
\dim_\theta(\iota) = \bigl|\{k : I_k(\iota) > \theta\}\bigr|
\]
Ideas with high dimensionality are *transdisciplinary*: they activate multiple intelligence types simultaneously.

!!! proposition "Transdisciplinary Ideas and Generative Utility"

Ideas with $\dim_{0.3}(\iota) \geq 4$ (activating four or more intelligence types above threshold) have strictly higher generative utility $u_G$ than ideas with $\dim_{0.3}(\iota) \leq 2$, because they create bridges between concept-domains that enable further synthesis.

??? proof "Proof"

Generative utility $u_G(\iota, \xi)$ measures the capacity of idea $\iota$ to *enable the creation of new ideas* by consumer $\xi$.  New ideas are compositions in the conceptual topos: $\iota_{\mathrm{new}} = \sigma_1 \circ \sigma_2$ requires shared concepts between components.

An idea with $\dim_{0.3}(\iota) \geq 4$ activates concepts in $\geq 4$ type regions of $\Cspace_{\mathrm{co}}$.  Each activated type region $t$ makes the idea composable with other ideas whose concepts lie in that region.  The number of potential compositions scales as $\binom{\dim_{0.3}}{2}$---the number of pairs of active types that can serve as bridges.  For $\dim = 4$: $\binom{4}{2} = 6$ bridge pairs.  For $\dim = 2$: $\binom{2}{2} = 1$.

More precisely, the generative utility is bounded below by the number of distinct *inter-type connections* the idea creates:
\[
u_G(\iota, \xi) \geq c \cdot \sum_{\substack{s,t : I_s(\iota) > 0.3    I_t(\iota) > 0.3,\, s < t}} K_{st}
\]
where $c > 0$ is a positive constant and $K_{st}$ is the compatibility between types $s$ and $t$.

Since $\bK$ is positive semi-definite with positive diagonal, and the number of summed terms increases quadratically with $\dim_{0.3}$, we have:
\[
u_G\big|_{\dim \geq 4} \geq c \cdot 6 \cdot \bar{K}_{\mathrm{off}} > c \cdot 1 \cdot \bar{K}_{\mathrm{off}} \geq u_G\big|_{\dim \leq 2}
\]
where $\bar{K}_{\mathrm{off}}$ is the average off-diagonal element of $\bK$.  Hence $u_G$ is strictly higher for transdisciplinary ideas.

!!! example "Intelligence Profiles of Canonical Ideas"

\begin{center}

*[Table — see PDF]*

\end{center}

#### Connection to the Compatibility Tensor

The intelligence profile of an idea determines which *combinations* of cognitive engines are synergistic for processing it. This connects directly to the compatibility tensor $K_{ij}$ from Part II.

!!! definition "Processing Synergy for an Idea"

Given a consumer $\xi$ with intelligence vector $\bI_\xi$ attempting to process idea $\iota$ with profile $\bI(\iota)$, the *processing synergy* is:
\begin{keyeqn}
\[
\Syn_{\mathrm{proc}}(\iota, \xi) = \sum_{i,j} K_{ij} \cdot I_i(\iota) \cdot I_{j,\xi}
\]
\end{keyeqn}
High synergy means $\xi$'s cognitive strengths align well with $\iota$'s demands, *and* the relevant types interact synergistically within $\xi$'s mind.

#### Connection to the Attention Simplex

Processing an idea requires allocating attention across intelligence types. The consumer's attention state $\lambda \in \Delta^7$ (the 7-simplex over 8 types) should align with $\bI(\iota)$.

!!! definition "Optimal Attention for an Idea"

The attention allocation that minimizes cognitive friction for idea $\iota$ is:
\[
\lambda^*(\iota) = \frac{\bI(\iota)}{\|\bI(\iota)\|_1}
\]
---the normalized intelligence profile as a probability distribution on the simplex.

!!! proposition "Attention Mismatch Cost"

The cost of processing idea $\iota$ with non-optimal attention $\lambda \neq \lambda^*(\iota)$ includes a friction term proportional to the KL divergence:
\[
\mathrm{Cost}_{\mathrm{friction}}(\iota, \lambda) = D_{\mathrm{KL}}(\lambda^*(\iota)\, \|\, \lambda) \cdot |\bI(\iota)|
\]
This connects to the cognitive friction tensor (Part III): switching attention to process a new idea incurs measurable cost.

??? proof "Proof"

The consumer's current attention allocation is $\lambda \in \Delta^7$.  Processing idea $\iota$ optimally requires $\lambda^*(\iota) = \bI(\iota) / \|\bI(\iota)\|_1$.  The cost has two components:

*Component 1: Reallocation effort.*  Shifting attention from $\lambda$ to $\lambda^*$ requires "moving" probability mass across the simplex.  The natural measure of the work required to transform one distribution to another on a statistical manifold is the KL divergence (or more precisely, the Fisher information metric, of which KL is the leading-order approximation for nearby distributions).

*Component 2: Scaling by load.*  The total cognitive effort scales with the intelligence load $|\bI(\iota)|$.  A simple idea (small $|\bI|$) is cheap to process even with mismatched attention; a complex idea (large $|\bI|$) amplifies any mismatch.

Formally, the friction cost is the product of the distributional distance and the magnitude:
\[
\mathrm{Cost}_{\mathrm{friction}}(\iota, \lambda) = \KL(\lambda^*\, \|\, \lambda) \cdot |\bI(\iota)|
\]

*Verification of boundary behavior:*  When $\lambda = \lambda^*$, $\KL(\lambda^* \| \lambda) = 0$ and friction vanishes.  When $\lambda$ assigns zero probability to a type that $\lambda^*$ requires ($\lambda_t = 0$ but $\lambda^*_t > 0$), $\KL = +\infty$---the idea is *incomprehensible* with that attention allocation.  This matches the intuition that a purely symbolic thinker ($\lambda_A = 1$, all others 0) cannot process a purely kinesthetic idea ($\lambda^*_K = 1$) at finite cost.

*Connection to the friction tensor.*  On the attention simplex $\Delta^7$ with the Fisher--Rao metric $g_{ij} = \delta_{ij}/\lambda_i$, the geodesic distance between $\lambda$ and $\lambda^*$ is $d_{\mathrm{FR}}(\lambda, \lambda^*) = 2\arccos\!\bigl(\sum_t \sqrt{\lambda_t \lambda^*_t}\bigr)$, and $\KL \geq \tfrac{1}{2} d_{\mathrm{FR}}^2$ by Pinsker-type inequalities.  The friction cost is thus lower-bounded by half the squared geodesic distance scaled by load.

#### Connection to CS (instantiation operator) Regions

Each intelligence type has privileged access to specific regions of the CS operator.

!!! definition "Regional Access Map"

The map $\rho: \{G, L, S, A, K, N, E, M\} \to 2^{\{\mathrm{cl}, \mathrm{qu}, \mathrm{co}\}}$ assigns each intelligence type to the the CS operator regions it primarily accesses:
\begin{center}

*[Table — see PDF]*

\end{center}

!!! theorem "Cross-Regional Ideas Require Multiple Intelligence Types"

If idea $\iota$ spans regions (its concept set $C(\iota)$ intersects both $\Cspace_{\mathrm{cl}}$ and $\Cspace_{\mathrm{co}}$), then $\dim_{0.3}(\iota) \geq 2$: at least two intelligence types must be activated above threshold.

??? proof "Proof"

By the regional access map (Def. *ref:def:regional-access*), no single intelligence type has primary access to both $\Cspace_{\mathrm{cl}}$ and $\Cspace_{\mathrm{co}}$ (except Naturalistic, which accesses their intersection). If $C(\iota)$ contains concepts in $\Cspace_{\mathrm{cl}} \setminus \Cspace_{\mathrm{co}}$ and concepts in $\Cspace_{\mathrm{co}} \setminus \Cspace_{\mathrm{cl}}$, at least one type from each region's primary access set must be engaged.

!!! corollary "CIT Constrains Cross-Regional Idea Translation"

By the Conceptual Irreversibility Theorem, ideas native to $\Cspace_{\mathrm{co}}$ that are translated to $\Cspace_{\mathrm{cl}}$ lose conceptual content (truth values collapse from Heyting to Boolean). Therefore, an idea with high $I_A$ or $I_L$ (co-regional) that is "explained in physical terms" ($\Cspace_{\mathrm{cl}}$) necessarily loses information. The intelligence profile of the translated version has lower $I_A$, $I_L$ and higher $I_G$, $I_K$---but the total intelligence load decreases:
\[
|\bI(\mathfrak{I}(\iota))| < |\bI(\iota)|
\]
Translation simplifies, but at a cost.

%═══════════════════════════════════════════════════════════════════════════════

## Document Intelligence: The Ideometric Profile

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Document"

A *document* $D$ is a finite collection of ideas $\{\iota_1, \ldots, \iota_N\}$ together with their internal connection structure (a subgraph of $\mathcal{G}$).

### Scalar Metrics

!!! definition "Document Scalar Metrics"

\[\begin{aligned}
N(D) &= |D| & \text{(idea count)}   
\Delta(D) &= \sum_{i=1}^{N} \delta(\iota_i) & \text{(cumulative depth, units: du)}   
\bar{\delta}(D) &= \Delta(D) / N(D) & \text{(mean depth)}   
\delta_{\max}(D) &= \max_{i} \delta(\iota_i) & \text{(maximum depth)}   
\bar{\nu}(D) &= \frac{1}{N} \sum_{i=1}^{N} \nu(\iota_i) & \text{(mean novelty)}   
N_{\mathrm{novel}}(D) &= |\{\iota_i : \nu(\iota_i) > 0.3\}| & \text{(novel idea count)}   
\rho_\nu(D) &= N_{\mathrm{novel}}(D) / N(D) & \text{(novelty density)}
\end{aligned}\]

### Vector Metrics

!!! definition "Document Intelligence Profile"

The eight-dimensional intelligence profile of the document:
\begin{keyeqn}
\[
\bI(D) = \frac{1}{N} \sum_{i=1}^{N} \bI(\iota_i) \quad \in [0,1]^8
\]
\end{keyeqn}
This is the centroid of the idea population in intelligence space.

!!! definition "Domain Depth Vector"

For knowledge domains $\{\mathcal{D}_1, \ldots, \mathcal{D}_m\}$:
\[
\boldsymbol{\Delta}(D) = \left(\sum_{\iota_i \in D \cap \mathcal{D}_k} \delta(\iota_i)\right)_{k=1}^{m}
\]

!!! definition "Document Utility"

For consumer $\xi$:

\[\begin{aligned}
U(D, \xi) &= \sum_{i=1}^{N} u(\iota_i, \xi) & \text{(total document utility)}   
\rho_u(D, \xi) &= U(D, \xi) / |D|_{\mathrm{words}} & \text{(utility density --- utility per word)}
\end{aligned}\]

### The Composite Ideometric Score

!!! definition "Composite Ideometric Score"

The *ideometric score* of document $D$ for consumer $\xi$ is:
\begin{keythm}
\[
\mathcal{I}(D, \xi) = N(D) \cdot \Bigl[\alpha \cdot \bar{\delta}(D) + \beta \cdot \bar{\nu}(D) + \gamma \cdot \bar{u}(D, \xi) + \lambda \cdot |\bI(D)|\Bigr]
\]
\end{keythm}
where $\alpha, \beta, \gamma, \lambda > 0$ are weighting parameters normalized to $\alpha + \beta + \gamma + \lambda = 1$, reflecting analytic priorities.

!!! theorem "Ideometric Score Properties"

The composite score $\mathcal{I}$ satisfies:
[nosep]
    - **Monotonicity**: Adding a positive-utility idea to $D$ increases $\mathcal{I}$.
    - **Depth-weighting**: For fixed $N$, $\mathcal{I}$ is monotone increasing in $\bar{\delta}$.
    - **Consumer dependence**: $\mathcal{I}(D, \xi_1) \neq \mathcal{I}(D, \xi_2)$ in general.
    - **Additivity under independence**: If $D = D_1 \sqcup D_2$ (disjoint, no cross-connections), then $\mathcal{I}(D) = \mathcal{I}(D_1) + \mathcal{I}(D_2)$ up to averaging corrections.

??? proof "Proof"

*(1) Monotonicity.*  Adding a positive-utility idea $\iota_{N+1}$ to $D$ changes $N \to N+1$ and updates the averages.  The new score is:

\[\begin{aligned}
\mathcal{I}' &= (N+1)\bigl[\alpha \bar{\delta}' + \beta \bar{\nu}' + \gamma \bar{u}' + \lambda |\bI(D)'|\bigr]
\end{aligned}\]

Since $\bar{\delta}' = \frac{N\bar{\delta} + \delta(\iota_{N+1})}{N+1}$, we have $\alpha(N+1)\bar{\delta}' = \alpha N \bar{\delta} + \alpha \delta(\iota_{N+1})$.  Similarly for the other terms.  Hence:
\[
\mathcal{I}' = \mathcal{I} + \alpha \delta(\iota_{N+1}) + \beta \nu(\iota_{N+1}) + \gamma u(\iota_{N+1}, \xi) + \lambda \Delta|\bI|
\]
where $\Delta|\bI| \geq 0$ (adding a non-zero profile vector increases the centroid norm when the new vector is not anti-aligned).  Since all terms are non-negative (positive utility assumption, $\delta \geq 1$, $\nu \geq 0$), $\mathcal{I}' > \mathcal{I}$.

*(2) Depth-weighting.*  For fixed $N$, $\mathcal{I} = N[\alpha \bar{\delta} + \cdots]$ is linear in $\bar{\delta}$ with positive coefficient $N\alpha > 0$.  Hence monotone increasing.

*(3) Consumer dependence.*  The term $\gamma \bar{u}(D, \xi)$ depends on $\xi$ through the utility function.  For consumers $\xi_1 \neq \xi_2$ with different utility weights $w_k$, we have $\bar{u}(D, \xi_1) \neq \bar{u}(D, \xi_2)$ in general, hence $\mathcal{I}(D, \xi_1) \neq \mathcal{I}(D, \xi_2)$.

*(4) Additivity.*  For $D = D_1 \sqcup D_2$ with $N_1 + N_2 = N$ and no shared ideas:

\[\begin{aligned}
\mathcal{I}(D) &= N[\alpha \bar{\delta} + \cdots] = N \cdot \alpha \cdot \frac{N_1 \bar{\delta}_1 + N_2 \bar{\delta}_2}{N} + \cdots   
&= \alpha(N_1 \bar{\delta}_1 + N_2 \bar{\delta}_2) + \cdots   
&= \mathcal{I}(D_1) + \mathcal{I}(D_2) + \text{averaging corrections on } |\bI(D)|
\end{aligned}\]

The "averaging corrections" arise because $|\bI(D)| \neq |\bI(D_1)| + |\bI(D_2)|$ (the centroid of the union is the weighted average of centroids, not their sum).  This correction vanishes when $\bI(D_1) = \bI(D_2)$ (parallel profiles).

%═══════════════════════════════════════════════════════════════════════════════

## Idea Generation as Cognitive Work

%═══════════════════════════════════════════════════════════════════════════════

This section connects ideometrics to the temporal intelligence calculus (Part IX).

!!! definition "Idea Generation Rate"

A cognitive engine $\mathcal{E}$ generating ideas at time $t$ has an *idea generation rate*:
\[
\dot{N}_{\mathcal{E}}(t) = \text{ideas per unit time, weighted by depth and novelty}
\]
More precisely:
\begin{keyeqn}
\[
\dot{\Phi}_{\mathrm{idea}}(\mathcal{E}, t) = \sum_{\iota \in \mathrm{output}(\mathcal{E}, t)} \delta(\iota) \cdot \nu(\iota)
\]
\end{keyeqn}
This is the *ideometric flux*---the rate at which an engine produces depth-weighted novel ideas. Units: du $\cdot$ s$^{-1}$ (depth-units per second).

!!! definition "Intelligence-Seconds of Idea Generation"

The total idea-generation work over interval $[t_0, t_1]$:
\[
\mathcal{W}_{\mathrm{idea}}(\mathcal{E}, [t_0, t_1]) = \int_{t_0}^{t_1} \dot{\Phi}_{\mathrm{idea}}(\mathcal{E}, t) \cdot \bI_{\mathcal{E}}(t) \, dt \quad \in \\mathbb{R}^{n(e)}_{\geq 0}
\]
This is an eight-dimensional vector of intelligence-seconds, decomposed by type, spent generating ideas.

!!! proposition "Assembly Idea Generation"

For an assembly of engines $\{\mathcal{E}_1, \ldots, \mathcal{E}_n\}$ with attention weights $\lambda_j(t)$:
\[
\dot{\Phi}_{\mathrm{idea}}^{\mathrm{asm}}(t) = \sum_{j=1}^{n} \lambda_j(t) \cdot \dot{\Phi}_{\mathrm{idea}}(\mathcal{E}_j, t) + A(\lambda)
\]
where $A(\lambda)$ is the assembly bonus---ideas that emerge from the synergistic interaction of engines but could not be generated by any single engine alone. This bonus depends on the compatibility tensor:
\[
A(\lambda) \propto \sum_{j < k} \lambda_j \lambda_k \cdot K(\mathcal{E}_j, \mathcal{E}_k)
\]

??? proof "Proof"

The ideometric flux of the assembly decomposes into individual and interactive components.

*Individual component:* Each engine $\mathcal{E}_j$ generates ideas at rate $\dot{\Phi}_{\mathrm{idea}}(\mathcal{E}_j, t)$, modulated by its share of the assembly's attention $\lambda_j(t)$.  The linear sum $\sum_j \lambda_j \dot{\Phi}_j$ accounts for the parallel operation of engines with attention-weighted throughput.

*Interactive component:* When engines $\mathcal{E}_j$ and $\mathcal{E}_k$ operate simultaneously, ideas from $\mathcal{E}_j$ may compose with ideas from $\mathcal{E}_k$ to produce *new* ideas that neither could generate alone.  The rate of such compositions depends on:
[nosep]
- The probability that both engines are active: proportional to $\lambda_j \lambda_k$,
- The compatibility of their outputs: $K(\mathcal{E}_j, \mathcal{E}_k) = \bI_j^\top \bK \, \bI_k$,
- The rate of idea "collisions" (opportunities for composition): proportional to $\dot{\Phi}_j \cdot \dot{\Phi}_k$.

Taking the leading-order approximation (pairs only, neglecting higher-order $m$-way interactions):
\[
A(\lambda) = \eta \sum_{j < k} \lambda_j \lambda_k \cdot K(\mathcal{E}_j, \mathcal{E}_k) \cdot \sqrt{\dot{\Phi}_j \cdot \dot{\Phi}_k}
\]
where $\eta > 0$ is a composition efficiency parameter.  For the simplified statement in the Ideometrics paper, the $\sqrt{\dot{\Phi}_j \dot{\Phi}_k}$ factor is absorbed into the compatibility $K$, giving $A(\lambda) \propto \sum_{j<k} \lambda_j \lambda_k K(\mathcal{E}_j, \mathcal{E}_k)$.

*Positivity:* Since $\bK$ is positive semi-definite and intelligence vectors are non-negative, $K(\mathcal{E}_j, \mathcal{E}_k) \geq 0$ for all pairs.  Hence $A(\lambda) \geq 0$: assembly bonus is always non-negative.  It is strictly positive whenever at least two engines have compatible profiles ($K > 0$) and are both active ($\lambda_j, \lambda_k > 0$).

!!! example "Human-AI Idea Assembly"

Niko working with Claude Opus:
[nosep]
    - Niko generates ideas with profile $\bI_{\mathrm{Niko}}$ at biological throughput $\Phi_{\mathrm{bio}}(t)$
    - Claude generates ideas with profile $\bI_{\mathrm{Claude}}$ at computational throughput $\Phi_{\mathrm{comp}}(t)$
    - Assembly ideas emerge at the intersection---ideas neither could produce alone
    - The compatibility $K(\mathrm{Niko}, \mathrm{Claude})$ amplifies ideometric flux

The total ideometric work is measured in intelligence-hours (Ih) and can be compared across sessions, projects, and teams.

%═══════════════════════════════════════════════════════════════════════════════

## The Geometry of Ideas

%═══════════════════════════════════════════════════════════════════════════════

This section places ideas directly on the geometric structures of the CS operator.

### Ideas as Points in Intelligence Space

Each idea's intelligence profile $\bI(\iota) \in [0,1]^8$ maps it to a point in the eight-dimensional intelligence manifold. A *document* maps to a cloud of points. The *centroid* $\bI(D)$ is the document's location in intelligence space.

!!! definition "Idea Manifold"

The *idea manifold* $\mathcal{M}_{\mathrm{idea}}$ is the subspace of $[0,1]^8$ actually populated by ideas. This is not the full hypercube: not all combinations of intelligence demands are realizable. The topology of $\mathcal{M}_{\mathrm{idea}}$ encodes structural constraints on what kinds of ideas are possible.

!!! conjecture "Idea Manifold Dimensionality"

The effective dimension of $\mathcal{M}_{\mathrm{idea}}$ is less than 8: intelligence demands are correlated (e.g., high $I_A$ often co-occurs with high $I_G$). The intrinsic dimension might be 4--6, with the remaining dimensions constrained by the compatibility structure.

### Ideas in the Conceptual Topos

As diagrams in $\Cspace_{\mathrm{co}}$ (Def. *ref:def:idea*), ideas inherit the topos structure:

!!! proposition "Ideas Have Heyting Truth Values"

The "truth" of an idea in $\Cspace_{\mathrm{co}}$ is not binary. An idea can be *partially valid*---its truth value is an element of the Heyting algebra $\Omega_{\mathrm{co}}$, not the Boolean algebra $\{0, 1\}$. This captures the reality that many ideas are neither wholly true nor wholly false but occupy intermediate states of validity.

??? proof "Proof"

By construction, $\Cspace_{\mathrm{co}}$ is a topos (Part V, \S 1).  In any topos, the subobject classifier $\Omega$ is a Heyting algebra (this is a standard result in topos theory; see Mac Lane & Moerdijk, *Sheaves in Geometry and Logic*, Ch. IV).

An idea $\iota: G \to \Cspace_{\mathrm{co}}$ defines a subfunctor of the representable functor of its codomain.  The "truth" of $\iota$ at a stage of knowledge $U$ is the element $\llbracket \iota \rrbracket_U \in \Omega_{\mathrm{co}}(U)$ classifying the subobject.  Since $\Omega_{\mathrm{co}}$ is Heyting, the truth values form a bounded distributive lattice with a Heyting implication operator $\Rightarrow$, but not necessarily a Boolean algebra.

Concretely: in $\Cspace_{\mathrm{co}}$, the truth value of "$A$ causes $B$" need not be $0$ or $1$---it can be an intermediate value representing "$A$ causes $B$ under conditions $C_1, \ldots, C_k$ but not in general," which is a valid element of $\Omega_{\mathrm{co}}$ with no Boolean equivalent.

The failure of excluded middle follows from the fact that a Heyting algebra satisfies $p \lor \neg p = \top$ if and only if it is Boolean (Theorem IV.8.1, Mac Lane & Moerdijk).  Since $\Omega_{\mathrm{co}}$ is properly Heyting (it has more than two elements, by the existence of ideas with intermediate truth status), excluded middle fails: $\llbracket \iota \rrbracket \lor \llbracket \neg\iota \rrbracket < \top$ for some $\iota$.

!!! corollary "Corollary"

The law of excluded middle does not hold for ideas in the conceptual topos. It is possible for an idea $\iota$ and its negation $\neg \iota$ to *both* have truth values strictly between 0 and 1. This is not uncertainty; it is *semantic indeterminacy* (Part V, \S 2).

### Ideas and the Perspective Bundle

!!! definition "Idea as Seen From a Perspective"

A section $\sigma$ of the perspective bundle $\pi: \mathbf{P} \to \Cspace$ evaluates an idea $\iota$ by restricting it to the fiber over the perspective's location:
\[
\sigma^*(\iota) = \iota|_{\sigma(c)}
\]
Different perspectives see different *aspects* of the same idea. The utility, depth, and even novelty of an idea are perspective-dependent quantities.

!!! theorem "Topological Obstruction to Universal Ideas"

If $c_1(\mathbf{P}) \neq 0$ (the first Chern class of the perspective bundle is non-trivial), then there exists no idea that is equally comprehensible from all perspectives. Every idea has a perspective from which it appears deep and one from which it appears trivial.

??? proof "Proof"

The perspective bundle $\pi: \mathbf{P} \to \Cspace$ assigns to each point $c \in \Cspace$ a fiber of possible perspectives.  An idea $\iota$ that is "equally comprehensible from all perspectives" would define a *flat section*---a global section $\sigma: \Cspace \to \mathbf{P}$ such that $\sigma^*(\iota) = \text{const}$ (the idea looks the same from every viewpoint).

The first Chern class $c_1(\mathbf{P}) \in H^2(\Cspace; \mathbb{Z})$ is the obstruction to the existence of flat sections.  If $c_1(\mathbf{P}) \neq 0$, then $\mathbf{P}$ is a non-trivial line bundle (or more generally, principal bundle) and flat global sections do not exist.

Concretely: traversing a loop $\gamma$ in $\Cspace$ and parallel-transporting the "view" of idea $\iota$ around $\gamma$ produces a holonomy transformation $\mathrm{hol}_\gamma(\iota) \neq \mathrm{Id}$.  The idea looks different after circumnavigation---the observer has gained new understanding that changes their perspective on $\iota$.  This holonomy is precisely the curvature of $\mathbf{P}$, which is non-vanishing when $c_1 \neq 0$.

Therefore, every idea has perspective-dependent comprehensibility.  No universally comprehensible ideas exist in a non-trivially curved perspective bundle.

### Holonomy of Ideas

!!! definition "Ideological Holonomy"

Traversing a loop $\gamma$ in the idea graph---starting from idea $\iota$, following connections through related ideas, and returning to $\iota$---produces a transformation of one's understanding of $\iota$:
\[
\mathrm{Hol}_{\mathrm{idea}}(\gamma) = \mathcal{P} \exp\!\left(-\oint_\gamma \omega_{\mathrm{idea}}\right)
\]
This is the geometric content of "understanding an idea more deeply by exploring its context." The holonomy is non-trivial when the idea graph has curvature---when the connections between ideas are not flat.

%═══════════════════════════════════════════════════════════════════════════════

## What Makes an Idea Good

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Good Idea --- Formal Criteria"

An idea $\iota$ is *good* if it satisfies:
[nosep]
    - **Validity**: $R(\iota)$ contains no contradictions (internal coherence)
    - **Groundedness**: $C(\iota)$ is populated by well-defined concepts
    - **Net positive utility**: $u_{\mathrm{agg}}(\iota) > 0$
    - **Accessibility**: There exists a linguistic encoding of $\tau(\iota)$ with acceptable fidelity
    - **Fertility**: $u_G(\iota, \cdot) > 0$ for at least some consumers

!!! definition "Great Idea"

A *great* idea additionally satisfies:
[nosep, start=6]
    - **High depth**: $\delta(\iota) \geq 3$ (integrates many prior ideas)
    - **High novelty**: $\nu(\iota) \geq 0.5$ (genuinely new against $\Omega$)
    - **Cross-domain richness**: $\dim_{0.3}(\iota) \geq 3$ (activates multiple intelligence types)
    - **Scalable utility**: $u_{\mathrm{agg}}$ increases as $\iota$ spreads through $\Omega$

\begin{keythm}
**The Beautiful Equation of Ideometrics.**

The quality of an idea is the product of its structural depth, its distance from what is already known, its benefit to those who encounter it, and the richness of the cognitive landscape it activates:
\[
\boxed{\mathcal{Q}(\iota, \xi) = \delta(\iota) \;\cdot\; \nu(\iota;\, \Omega) \;\cdot\; u(\iota, \xi) \;\cdot\; \dim_{0.3}(\iota)}
\]
Deep. New. Useful. Rich. That is what makes an idea great.
\end{keythm}

%═══════════════════════════════════════════════════════════════════════════════

## Practical Procedure: Grokking a Document

%═══════════════════════════════════════════════════════════════════════════════

To "grok" a document $D$ in the ideometric framework:

    - **Enumerate**: Parse $D$ into its constituent ideas $\{\iota_1, \ldots, \iota_N\}$, distinguishing ideas from reports and meta-ideas.
    
    - **Graph**: For each $\iota_i$, identify prerequisite ideas and build the dependency subgraph. Compute IdeaRank.
    
    - **Depth**: Compute $\delta(\iota_i)$ for each idea. Record $\Delta(D)$, $\bar{\delta}(D)$, $\delta_{\max}(D)$.
    
    - **Novelty audit**: For each $\iota_i$, compute $\nu(\iota_i; \Omega)$ by querying the topological signature against the collective consciousness (excluding $D$ itself from $\Omega$). Record $N_{\mathrm{novel}}(D)$, $\rho_\nu(D)$.
    
    - **Utility assessment**: For the specified consumer $\xi$, compute $u(\iota_i, \xi)$ for each idea. Decompose into subspecies. Record $U(D, \xi)$, $\rho_u(D, \xi)$.
    
    - **Intelligence profiling**: Compute $\bI(\iota_i)$ for each idea. Aggregate into $\bI(D)$. Record $|\bI(D)|$, $\dim_{0.3}(D)$, dominant type.
    
    - **Composite score**: Compute $\mathcal{I}(D, \xi)$ with chosen weights $(\alpha, \beta, \gamma, \lambda)$.

The result is a complete *ideometric profile*: how many ideas the document contains, how deep they are, how many are novel, how useful they are to the target consumer, and what kinds of minds they speak to.

%═══════════════════════════════════════════════════════════════════════════════

%═══════════════════════════════════════════════════════════════════════════════
% PART II: PRIME DECOMPOSITION AND ECONOMIC UTILITY
% The following sections extend Ideometrics with decomposition theory,
% enabling spectral analysis of ideas and economic valuation.
%═══════════════════════════════════════════════════════════════════════════════

## Prime Idea Theory

% ═══════════════════════════════════════════════════════════════════════════════

### Relationships as first-class objects

The existing definition (Definition *ref:def:idea-recall*) treats an idea as a functor $\iota: G \to \Cspace_{\mathrm{co}}$.  The shape graph $G$ encodes the *relationships* between concepts.  We now elevate these relationships to first-class status by defining the *internal structure* of an idea as the set of sub-ideas that compose it.

!!! definition "Idea --- Recalled"
 \tA
An idea $\iota$ is a functor $\iota: G \to \Cspace_{\mathrm{co}}$ where $G$ is a finite directed graph.  Vertices map to concepts; edges map to conceptual relations.

!!! definition "Sub-Idea"
 \tA

Let $\iota: G \to \Cspace_{\mathrm{co}}$ be an idea.  A *sub-idea* of $\iota$ is an idea $\sigma: H \to \Cspace_{\mathrm{co}}$ such that $H$ is a (non-empty) connected subgraph of $G$ and $\sigma = \iota|_H$ (the restriction of $\iota$ to $H$).  We write $\sigma \sqsubseteq \iota$.

The relation $\sqsubseteq$ is a partial order on ideas, with the property that $\sigma \sqsubseteq \iota$ implies:
[nosep]
- $C(\sigma) \subseteq C(\iota)$ \quad (concept containment),
- $R(\sigma) \subseteq R(\iota)$ \quad (relation containment),
- $|G_\sigma| \leq |G_\iota|$ \quad (structural containment).

!!! definition "Proper Sub-Idea"
 \tA
A sub-idea $\sigma \sqsubseteq \iota$ is *proper* if $\sigma \neq \iota$ and $|V(H)| \geq 2$ (it contains at least one relationship).  We write $\sigma \sqsubset \iota$.

!!! definition "Idea Composition"
 \tA

Given ideas $\sigma_1: H_1 \to \Cspace_{\mathrm{co}}$ and $\sigma_2: H_2 \to \Cspace_{\mathrm{co}}$ that share at least one concept (i.e., $\iota(V(H_1)) \cap \iota(V(H_2)) \neq \emptyset$), their *composition* is the idea $\sigma_1 \circ \sigma_2: H_1 \cup_{H_1 \cap H_2} H_2 \to \Cspace_{\mathrm{co}}$ defined on the pushout of the shared subgraph.

The composition is an idea whose concept set is $C(\sigma_1) \cup C(\sigma_2)$ and whose relation set is $R(\sigma_1) \cup R(\sigma_2)$, with the shared concepts identified.

\begin{intuition}
Composition is how ideas combine.  "Variation exists in populations" composed with "Some variants reproduce more" yields "Differential reproduction correlates with traits," which composed with "Traits are inherited" yields "Natural selection."  Each composition adds relationships between previously separate concept clusters.
\end{intuition}

### Prime and compound ideas

!!! definition "Prime Idea"
 \tA

An idea $\pi$ is *prime* (or *irreducible*) if:
[nosep]
- $|V(G_\pi)| \geq 2$ (it contains at least one relationship---single concepts are not ideas), and
- $\pi$ has no proper sub-ideas: there is no connected subgraph $H \sqsubset G_\pi$ with $|V(H)| \geq 2$ such that $\pi|_H$ is itself a coherent idea.

We denote the set of all prime ideas by $\Prime$.

!!! remark "Perspective-Dependence of Primality"

Primality is *relative to the observer's conceptual resolution*.  To a chemist, "covalent bond" may be prime.  To a quantum physicist, it decomposes into "electron sharing" $\circ$ "orbital overlap" $\circ$ "energy minimization."  Formally, primality depends on the granularity of $\Cspace_{\mathrm{co}}$---coarser conceptual topoi have more primes, finer ones have fewer.  We fix a resolution level and work relative to it.

!!! definition "Compound Idea"
 \tA

An idea $\iota$ is *compound* if it is not prime---i.e., it admits at least one proper sub-idea.  Equivalently, $\iota$ can be expressed as a composition of strictly smaller ideas.

!!! definition "Decomposition"
 \tA

A *decomposition* of a compound idea $\iota$ is a finite sequence of ideas $(\sigma_1, \ldots, \sigma_m)$ with $m \geq 2$ such that:
[nosep]
- $\iota = \sigma_1 \circ \sigma_2 \circ \cdots \circ \sigma_m$ (sequential composition),
- Each $\sigma_i \sqsubset \iota$ (each component is a proper sub-idea of the whole).

A decomposition is *complete* if every $\sigma_i$ is prime.

!!! definition "Factorization Lattice"
 \tB

For a compound idea $\iota$, the *factorization lattice* $\mathcal{L}(\iota)$ is the poset of all ideas $\sigma$ such that $\sigma \sqsubseteq \iota$, ordered by $\sqsubseteq$.  The lattice has:
[nosep]
- Top element: $\iota$ itself,
- Bottom elements: the prime sub-ideas of $\iota$,
- Intermediate elements: partially decomposed sub-ideas.

### The decomposition theorem

!!! theorem "Existence of Prime Decomposition"
 \tA

Every compound idea $\iota$ with finite shape graph $|V(G_\iota)| < \infty$ admits at least one complete decomposition into prime ideas.

??? proof "Proof"

By strong induction on $|V(G_\iota)|$.  If $|V(G_\iota)| = 2$, then $\iota$ consists of a single edge between two concepts.  This is prime by Definition *ref:def:prime* (no proper connected subgraph with $\geq 2$ vertices exists).

Suppose the result holds for all ideas with fewer than $n$ vertices, and let $|V(G_\iota)| = n$.  If $\iota$ is prime, we are done (the decomposition is the singleton $(\iota)$).  If $\iota$ is compound, there exists a proper sub-idea $\sigma \sqsubset \iota$ with $|V(G_\sigma)| < n$.  The "remainder" $\iota \setminus \sigma$ (formally: the sub-idea on the complement subgraph, connected to $\sigma$ through shared vertices) also has fewer than $n$ vertices.  By the induction hypothesis, both $\sigma$ and $\iota \setminus \sigma$ admit complete decompositions.  Concatenating these gives a complete decomposition of $\iota$.

!!! theorem "Non-Uniqueness and Lattice Structure"
 \tA

In general, the prime decomposition of a compound idea is *not unique*.  However, the set of primes appearing in *any* complete decomposition is invariant: if $(\pi_1, \ldots, \pi_m)$ and $(\pi'_1, \ldots, \pi'_{m'})$ are two complete decompositions of $\iota$, then $\{\pi_1, \ldots, \pi_m\} = \{\pi'_1, \ldots, \pi'_{m'}\}$ as multisets.

??? proof "Proof"

The decomposition order is non-unique because composition is not commutative---you can assemble the same idea in different sequences.  However, the *set of primes* is determined by the shape graph: each prime corresponds to a maximal elementary subgraph of $G_\iota$ (a connected subgraph with no further connected subgraphs of size $\geq 2$ that are proper sub-ideas).  These are intrinsic to $G_\iota$ and do not depend on the order of decomposition.  Formally, the primes of $\iota$ are the atoms of the factorization lattice $\mathcal{L}(\iota)$, which are determined by the lattice structure.

!!! corollary "Well-Defined Prime Multiset"
 \tA

Every idea $\iota$ has a well-defined *prime multiset*:
\begin{keyeqn}
\[
\mathfrak{p}(\iota) = \{\!\!\{ \pi_1, \pi_2, \ldots, \pi_m \}\!\!\}
\]
\end{keyeqn}
where $\pi_i \in \Prime$ are the primes appearing in any complete decomposition.  This multiset is canonical (independent of decomposition order).

### Prime type localization

Each prime idea, being a minimal coherent thought, lives primarily in one or two cognitive dimensions.  This is the bridge between the algebraic structure of decomposition and the geometric structure of the intelligence type space.

!!! definition "Type Support of an Idea"
 \tA

The *type support* of idea $\iota$ at threshold $\theta > 0$ is:
\[
\supp_\theta(\iota) = \{t \in \{1, \ldots, 8\} : I_t(\iota) > \theta\}
\]
where $\bI(\iota) = (I_1(\iota), \ldots, I_8(\iota))$ is the intelligence profile.

!!! proposition "Prime Localization"
 \tB

Prime ideas are *type-localized*: for any prime $\pi \in \Prime$ and threshold $\theta = 0.2$,
\[
|\supp_\theta(\pi)| \leq 3
\]
That is, prime ideas activate at most three cognitive types above threshold.  Most primes are *unimodal* ($|\supp_\theta(\pi)| = 1$) or *bimodal* ($|\supp_\theta(\pi)| = 2$).

\begin{intuition}
A prime idea is a single conceptual relationship.  "$A$ causes $B$" is causal reasoning (one type).  "Shape $X$ maps to formula $Y$" bridges spatial and symbolic (two types).  It takes *composition* of primes to produce the rich multi-dimensional profiles we see in compound ideas.  The cognitive dimensionality of a compound idea emerges from the diversity of its prime constituents.
\end{intuition}

!!! definition "Type Signature of a Prime"
 \tA

For a prime idea $\pi$, its *type signature* is the pair:
\[
\tau(\pi) = \bigl(\arg\max_t I_t(\pi),\; \bI(\pi)\bigr)
\]
consisting of its dominant type and its full (sparse) profile vector.  We say $\pi$ is a *type-$t$ prime* if $\arg\max_t I_t(\pi) = t$.

!!! definition "Prime Spectrum of an Idea"
 \tA

The *prime spectrum* of idea $\iota$ is the function $\Spec(\iota): \{1, \ldots, 8\} \to \N$ defined by:
\begin{keyeqn}
\[
\Spec_t(\iota) = \bigl|\{\pi \in \mathfrak{p}(\iota) : \tau(\pi) \text{ has dominant type } t\}\bigr|
\]
\end{keyeqn}
This counts, for each cognitive type, how many primes in the decomposition of $\iota$ are dominated by that type.  The prime spectrum is a vector $\Spec(\iota) \in \N^8$.

!!! theorem "Spectrum Additivity"
 \tA

For composed ideas, the prime spectrum is additive:
\[
\Spec(\sigma_1 \circ \sigma_2) = \Spec(\sigma_1) + \Spec(\sigma_2) - \Spec(\sigma_1 \cap \sigma_2)
\]
where $\sigma_1 \cap \sigma_2$ is the shared sub-idea (which may be empty, in which case the last term vanishes).

??? proof "Proof"

The prime multiset of a composition is the union of the prime multisets minus the shared primes (which are counted once, not twice).  Since the spectrum is a count function on the multiset partitioned by type, additivity follows from inclusion--exclusion on multisets.

### Recursive depth and the decomposition tree

!!! definition "Decomposition Tree"
 \tA

The *decomposition tree* $T(\iota)$ of a compound idea $\iota$ is the rooted tree where:
[nosep]
- The root is $\iota$,
- Each internal node $\sigma$ has children that are its maximal proper sub-ideas,
- The leaves are the prime ideas $\pi_i \in \mathfrak{p}(\iota)$.

!!! definition "Compositional Depth"
 \tA

The *compositional depth* of idea $\iota$ is the height of its decomposition tree:
\[
\depth_c(\iota) = \begin{cases}
0 & \text{if } \iota \in \Prime,   
1 + \max_{\sigma \sqsubset \iota} \depth_c(\sigma) & \text{otherwise}.
\end{cases}
\]

!!! example "Decomposition of "Natural Selection""
 \tA

The idea "Natural selection drives adaptation" decomposes as:
\begin{center}
\begin{tikzpicture}[
  level distance=1.4cm,
  sibling distance=3.2cm,
  every node/.style={draw, rounded corners, align=center, font=\small},
  edge from parent/.style={draw, -stealth},
  leaf/.style={fill=tierA!20},
  compound/.style={fill=tierB!20}
]
\node[compound] {Natural selection  drives adaptation  $\depth_c = 3$}
  child {node[compound] {Differential  reproduction  $\depth_c = 2$}
    child {node[compound] {Variation  in fitness  $\depth_c = 1$}
      child {node[leaf] {Organisms  vary    {\tiny Type N}}}
      child {node[leaf] {Environment  selects    {\tiny Type N}}}
    }
    child {node[leaf] {Reproduction  rate differs    {\tiny Type A}}}
  }
  child {node[compound] {Heritable  traits  $\depth_c = 1$}
    child {node[leaf] {Traits pass  to offspring    {\tiny Type N}}}
    child {node[leaf] {DNA encodes  traits    {\tiny Type A}}}
  }
  child {node[leaf] {Populations  change  over time    {\tiny Type M}}};
\end{tikzpicture}
\end{center}

Prime spectrum: $\Spec = (0, 0, 0, 2, 0, 3, 0, 1)$, indicating 3 naturalistic primes (organisms vary, environment selects, traits pass), 2 algebraic/symbolic primes (reproduction rate, DNA encoding), and 1 musical/temporal prime (populations change over time).  The compound idea's high cognitive dimensionality ($\dim_{0.2} = 3$) emerges from combining type-localized primes across multiple dimensions.

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Object Spectra

% ═══════════════════════════════════════════════════════════════════════════════

The prime spectrum, defined for individual ideas, extends to *any cognitive object*---any entity that contains, produces, or processes ideas.  This is the universal decomposition functor.

### Cognitive objects

!!! definition "Cognitive Object"
 \tA

A *cognitive object* $\Obj$ is any entity with a well-defined *idea inventory*---a multiset of ideas $\mathcal{I}(\Obj) = \{\!\!\{ \iota_1, \iota_2, \ldots, \iota_N \}\!\!\}$ that it contains, has produced, or can produce.  The taxonomy of cognitive objects is:
\begin{center}
\renewcommand{\arraystretch}{1.15}

*[Table — see PDF]*

\end{center}

!!! remark "Emergent Ideas in Assemblies"

For bundles and assemblies, the idea inventory is *not* merely the union of member inventories.  The compatibility tensor $\bK$ enables compositions that no single member could produce:
\[
\mathcal{I}(A) = \bigcup_{i} \mathcal{I}(\Obj_i) \;\cup\; \mathcal{I}_{\mathrm{emergent}}(A)
\]
where $\mathcal{I}_{\mathrm{emergent}}(A) = \{\sigma_i \circ \sigma_j : \sigma_i \in \mathcal{I}(\Obj_i),\; \sigma_j \in \mathcal{I}(\Obj_j),\; \Syn(\sigma_i, \sigma_j) > \theta_{\mathrm{emg}}\}$.  This is the idea-level expression of $E_2$ emergence from Part XII.

### The ideometric spectrum of a cognitive object

!!! definition "Ideometric Spectrum"
 \tA

The *ideometric spectrum* of cognitive object $\Obj$ is the function $\Spec(\Obj): \{1, \ldots, 8\} \to \N$ defined by:
\begin{keyeqn}
\[
\Spec_t(\Obj) = \sum_{\iota \in \mathcal{I}(\Obj)} \Spec_t(\iota) = \sum_{\iota \in \mathcal{I}(\Obj)} \bigl|\{\pi \in \mathfrak{p}(\iota) : \text{dominant type of } \pi = t\}\bigr|
\]
\end{keyeqn}
This counts the total number of type-$t$ primes across all ideas in the object's inventory.  It is a vector $\Spec(\Obj) \in \N^8$.

!!! definition "Normalized Spectrum (Profile)"
 \tA

The *normalized spectrum* is the distribution:
\[
\hat{\Spec}_t(\Obj) = \frac{\Spec_t(\Obj)}{\sum_{s=1}^{8} \Spec_s(\Obj)}
\]
This is a probability vector on $\Delta^7$ giving the *type distribution* of the object's ideometric content.

!!! definition "Absolute Ideometric Content"
 \tA

The *absolute ideometric content* of $\Obj$ is the scalar:
\[
|\Obj|_{\mathrm{id}} = \sum_{t=1}^{8} \Spec_t(\Obj) = |\mathfrak{p}(\Obj)|
\]
---the total number of primes contained in the object.  This is a measure of the object's total cognitive substance.

!!! definition "Type-Specific Content"
 \tA

The *type-$t$ content* of $\Obj$ is:
\[
|\Obj|_t = \Spec_t(\Obj)
\]
This measures how much cognitive substance of type $t$ the object contains.  For example, $|D|_A$ counts how many algebraic/symbolic prime ideas appear in document $D$.

!!! theorem "Spectrum Additivity for Objects"
 \tA

For the disjoint union of cognitive objects (no shared ideas):
\[
\Spec(\Obj_1 \sqcup \Obj_2) = \Spec(\Obj_1) + \Spec(\Obj_2)
\]
For non-disjoint unions (shared ideas subtracted):
\[
\Spec(\Obj_1 \cup \Obj_2) = \Spec(\Obj_1) + \Spec(\Obj_2) - \Spec(\Obj_1 \cap \Obj_2)
\]

??? proof "Proof"

Follows from Theorem *ref:thm:additivity* applied to each idea in the inventory, with inclusion--exclusion on the idea multisets.

### Worked example: Spectral decomposition of a research team

!!! example "Startup Team Spectrum"
 \tB

Consider a three-person AI startup with one ML engineer ($H_1$), one UX designer ($H_2$), and one domain expert ($H_3$), augmented by a language model ($M_1$).

**Individual spectra** (estimated prime counts per type):

\begin{center}

*[Table — see PDF]*

\end{center}

**Normalized spectrum** of the assembly: $\hat{\Spec}(A) = (0.129, 0.234, 0.105, 0.262, 0.043, 0.125, 0.066, 0.035)$.

**Diagnosis**: The assembly is heavily skewed toward algebraic ($A$) and linguistic ($L$) types---the LLM dominates the total prime count.  The assembly is weakest in kinesthetic ($K$) and musical/temporal ($M$), and has a moderate gap in emotional/evaluative ($E$).  If the product requires strong aesthetic judgment (high $E$) or embodied interaction design (high $K$), the assembly has a spectral deficit.

### Documents as cognitive objects

!!! definition "Document Spectrum"
 \tA

For a document $D$ containing ideas $\iota_1, \ldots, \iota_N$, the document spectrum is:
\[
\Spec(D) = \sum_{j=1}^{N} \Spec(\iota_j)
\]
with the convention that ideas appearing in $D$ are weighted by their prominence (section-level ideas weighted higher than footnotes).

!!! definition "Spectral Density"
 \tB

The *spectral density* of a document normalizes by length:
\[
\rho_t(D) = \frac{\Spec_t(D)}{|D|_{\mathrm{words}}}
\]
This measures the density of type-$t$ primes per word.  High-density documents are intellectually rich; low-density documents are padded or redundant.

!!! proposition "Spectral Density Predicts Utility"
 \tB

For a consumer $\xi$ with intelligence profile $\bI_\xi$, the expected utility of document $D$ is:
\[
\mathbb{E}[u(D, \xi)] \propto \sum_{t=1}^{8} \rho_t(D) \cdot I_{\xi,t} \cdot K_{t,t}
\]
That is: a document is useful to a consumer when its spectral density is concentrated in the types the consumer is strong in and that interact synergistically.  This is computable *before the consumer reads the document*.

% ═══════════════════════════════════════════════════════════════════════════════

## Time--Money Utility Theory

% ═══════════════════════════════════════════════════════════════════════════════

The existing utility framework (Definition *ref:def:utility-recall*) decomposes utility into five subspecies: instrumental, epistemic, generative, protective, and social.  These are *cognitive* categories.  But the market does not pay for cognition directly---it pays for the two fundamental scarce resources that ideas help conserve or produce: **time** and **money**.

### The time--money projection

!!! definition "Utility Subspecies --- Recalled"
 \tA

$u(\iota, \xi) = \sum_{k \in \{I,E,G,P,S\}} w_k(\xi) \cdot u_k(\iota, \xi)$, where the subspecies are instrumental ($I$), epistemic ($E$), generative ($G$), protective ($P$), and social ($S$).

!!! definition "Time Utility"
 \tA

The *time utility* of idea $\iota$ for consumer $\xi$ is:
\begin{keyeqn}
\[
u_T(\iota, \xi) = \Delta t_{\mathrm{saved}}(\iota, \xi) = t_{\mathrm{without}}(\xi, \text{goal}) - t_{\mathrm{with}}(\xi, \text{goal}, \iota)
\]
\end{keyeqn}
where $t_{\mathrm{without}}$ is the expected time for $\xi$ to achieve a goal without idea $\iota$, and $t_{\mathrm{with}}$ is the time with $\iota$.  Measured in hours.  Negative $u_T$ means the idea costs time (e.g., by introducing unnecessary complexity).

!!! definition "Money Utility"
 \tA

The *money utility* of idea $\iota$ for consumer $\xi$ is:
\begin{keyeqn}
\[
u_M(\iota, \xi) = \Delta m(\iota, \xi) = m_{\mathrm{with}}(\xi, \iota) - m_{\mathrm{without}}(\xi)
\]
\end{keyeqn}
where $m$ denotes the net monetary position.  This includes:
[nosep]
- *Cost savings*: The idea reduces expenditure ($\Delta m > 0$ from avoided cost).
- *Revenue generation*: The idea enables new income ($\Delta m > 0$ from new revenue).
- *Loss prevention*: The idea averts a financial loss ($\Delta m > 0$ from prevented loss).

Measured in currency units (USD).

!!! definition "Economic Utility Vector"
 \tA

The *economic utility* of idea $\iota$ for consumer $\xi$ is the pair:
\begin{keyeqn}
\[
\mathbf{u}_{\mathrm{econ}}(\iota, \xi) = \bigl(u_T(\iota, \xi),\; u_M(\iota, \xi)\bigr) \in \R \times \R
\]
\end{keyeqn}
Both components can be positive (saving/generating), negative (costing/losing), or zero.

### Connecting cognitive utility to economic utility

The five cognitive subspecies project onto the time--money plane:

!!! proposition "Cognitive-to-Economic Projection"
 \tB

There exist consumer-dependent projection weights $\alpha_{k,T}(\xi)$ and $\alpha_{k,M}(\xi)$ such that:

\[\begin{aligned}
u_T(\iota, \xi) &= \sum_{k \in \{I,E,G,P,S\}} \alpha_{k,T}(\xi) \cdot u_k(\iota, \xi),    
u_M(\iota, \xi) &= \sum_{k \in \{I,E,G,P,S\}} \alpha_{k,M}(\xi) \cdot u_k(\iota, \xi). 
\end{aligned}\]

Typical projection patterns:
\begin{center}
\renewcommand{\arraystretch}{1.1}

*[Table — see PDF]*

\end{center}

The weights $\alpha_{k,\cdot}(\xi)$ depend on the consumer's economic context: a startup CEO has different projection weights than a graduate student.

### Novelty-weighted economic utility

Not all time/money savings are equal.  An idea that saves you 10 minutes by telling you something you almost already knew is less valuable than one that saves you 10 minutes through a genuinely novel insight.  Novelty amplifies economic utility.

!!! definition "Novelty-Weighted Economic Utility"
 \tB

The *novelty-weighted economic utility* of idea $\iota$ for consumer $\xi$ is:
\begin{keyeqn}
\[
\mathbf{u}^*(\iota, \xi) = \bigl(1 + \beta \cdot \nu(\iota; \Cspace_{\mathrm{ind}}(\xi))\bigr) \cdot \mathbf{u}_{\mathrm{econ}}(\iota, \xi)
\]
\end{keyeqn}
where $\nu(\iota; \Cspace_{\mathrm{ind}}(\xi)) \in [0,1]$ is the novelty of $\iota$ relative to the consumer's individual the CS operator, and $\beta > 0$ is the *novelty premium*---the marginal increase in value per unit of novelty.

\begin{intuition}
A highly novel idea ($\nu \to 1$) with positive economic utility gets amplified by factor $(1 + \beta)$.  A completely familiar idea ($\nu \to 0$) gets no amplification.  The novelty premium $\beta$ reflects how much the market values *new* ideas over *known* ones---typically $\beta \in [0.5, 3.0]$ depending on the domain.  In technology: high $\beta$.  In compliance: low $\beta$.
\end{intuition}

### Economic utility of cognitive objects

Extending from individual ideas to cognitive objects:

!!! definition "Economic Value of a Cognitive Object"
 \tB

The *economic value* of cognitive object $\Obj$ for consumer $\xi$ is:
\begin{keyeqn}
\[
V(\Obj, \xi) = \sum_{\iota \in \mathcal{I}(\Obj)} \mathcal{A}(\iota, \xi) \cdot \mathbf{u}^*(\iota, \xi)
\]
\end{keyeqn}
where $\mathcal{A}(\iota, \xi) \in [0,1]$ is the accessibility function (prerequisite completion $\times$ type alignment).  Only ideas the consumer can actually access contribute to value.

!!! definition "Type-Decomposed Economic Value"
 \tB

The economic value decomposes by cognitive type:
\begin{keyeqn}
\[
V_t(\Obj, \xi) = \sum_{\iota \in \mathcal{I}(\Obj)} \hat{I}_t(\iota) \cdot \mathcal{A}(\iota, \xi) \cdot \mathbf{u}^*(\iota, \xi)
\]
\end{keyeqn}
where $\hat{I}_t(\iota) = I_t(\iota) / \|\bI(\iota)\|_1$ is the fraction of idea $\iota$'s intelligence load in type $t$.  This tells you: "How much of this object's value comes from spatial reasoning?  From symbolic computation?  From social intelligence?"

!!! theorem "Value Decomposition"
 \tB

The total economic value of a cognitive object decomposes as:
\[
V(\Obj, \xi) = \sum_{t=1}^{8} V_t(\Obj, \xi) = \mathbf{V}(\Obj, \xi) \cdot \mathbf{1}
\]
where $\mathbf{V}(\Obj, \xi) \in \\mathbb{R}^{n(e)}$ is the *value spectrum*---an eight-dimensional vector giving the economic value contributed by each cognitive type.

% ═══════════════════════════════════════════════════════════════════════════════

## Producer--Consumer Matching

% ═══════════════════════════════════════════════════════════════════════════════

The prime spectrum and economic utility theory together enable a matching algorithm that is qualitatively different from keyword search or collaborative filtering.

### The matching problem

!!! definition "Cognitive Need"
 \tA

A *cognitive need* of consumer $\xi$ is a gap in their idea inventory relative to a goal:
\begin{keyeqn}
\[
\mathcal{N}(\xi, \text{goal}) = \mathcal{I}_{\mathrm{required}}(\text{goal}) \setminus \mathcal{I}(\xi)
\]
\end{keyeqn}
---the ideas required to achieve the goal that the consumer does not yet possess.  The *need spectrum* is $\Spec(\mathcal{N}) \in \N^8$: the type distribution of missing prime ideas.

!!! definition "Match Score"
 \tB

The *match score* between producer $\Obj_P$ and consumer need $\mathcal{N}$ is:
\begin{keyeqn}
\[
\mu(\Obj_P, \mathcal{N}) = \frac{\displaystyle\sum_{t=1}^{8} \min\bigl(\Spec_t(\Obj_P),\; \Spec_t(\mathcal{N})\bigr)}{\displaystyle\sum_{t=1}^{8} \Spec_t(\mathcal{N})}
\]
\end{keyeqn}
This is the fraction of the consumer's need that the producer can satisfy, type by type.  $\mu \in [0,1]$ with $\mu = 1$ meaning perfect coverage.

!!! definition "Weighted Match Score"
 \tB

Incorporating economic value:
\begin{keyeqn}
\[
\mu^*(\Obj_P, \xi) = \sum_{t=1}^{8} \frac{\min\bigl(\Spec_t(\Obj_P),\; \Spec_t(\mathcal{N})\bigr)}{\Spec_t(\mathcal{N})} \cdot \frac{V_t(\Obj_P, \xi)}{\sum_s V_s(\Obj_P, \xi)}
\]
\end{keyeqn}
This weights each type's coverage by the economic value it delivers.  A producer that covers 100% of a low-value type and 0% of a high-value type gets a low $\mu^*$.

!!! theorem "Optimal Matching"
 \tB

Given a set of producers $\{\Obj_P^{(1)}, \ldots, \Obj_P^{(K)}\}$ and a consumer with need $\mathcal{N}(\xi)$, the allocation that maximizes total economic value subject to a budget constraint $\sum_k c_k \leq B$ is:
\[
\max_{\{x_k \in \{0,1\}\}} \sum_{k=1}^{K} x_k \cdot V(\Obj_P^{(k)}, \xi) \quad \text{s.t.} \quad \sum_{k=1}^{K} x_k \cdot c_k \leq B
\]
This is a variant of the knapsack problem with value $V(\Obj_P^{(k)}, \xi)$ and weight $c_k$.  When the number of producers is large, the greedy algorithm (sort by $V/c$ ratio, fill greedily) achieves a $(1 - 1/e)$-approximation by submodularity of the coverage function.

??? proof "Proof"
[Proof sketch]
The coverage function $f(S) = \sum_{t=1}^{8} \min(\sum_{k \in S} \Spec_t(\Obj_P^{(k)}),\; \Spec_t(\mathcal{N}))$ is monotone and submodular (adding a producer to a larger set has diminishing marginal returns in coverage).  The $(1 - 1/e)$-guarantee follows from the classical result of Nemhauser, Wolsey, and Fisher (1978) for submodular maximization under a matroid constraint.

### Matching cost reduction

!!! proposition "Spectral Matching Is Cheaper Than Keyword Matching"
 \tB

Let $n$ be the number of candidate producers and $d$ the average number of keywords per document.  Keyword matching requires $O(n \cdot d)$ comparisons.  Spectral matching requires:
[nosep]
- One-time spectral computation per object: $O(|\mathcal{I}(\Obj)|)$ per object,
- Matching: $O(8 \cdot n) = O(n)$ comparisons (inner product of 8D vectors).

The spectral representation compresses arbitrarily large idea inventories into variable-dimensional vectors, reducing the matching dimension from $d$ (potentially thousands) to 8 (fixed).

### Worked example: Matching a learner with educational content

!!! example "Spectral Course Recommendation"
 \tB

A data science student $\xi$ with goal "Build a machine learning pipeline" has:

**Current inventory spectrum**: $\Spec(\xi) = (10, 40, 5, 80, 2, 5, 3, 2)$ (strong algebraic, decent linguistic, weak elsewhere).

**Goal requirement spectrum**: $\Spec(\text{goal}) = (30, 50, 15, 120, 10, 25, 10, 5)$.

**Need spectrum**: $\mathcal{N} = (20, 10, 10, 40, 8, 20, 7, 3) = 118$ primes needed.

Three candidate courses:
\begin{center}

*[Table — see PDF]*

\end{center}

**Match scores**: Course A covers 65/118 = 55% of need but over-serves algebraic (50 vs.\ 40 needed).  Course B covers 67/118 = 57% with better distribution.  Course C covers 62/118 = 53%.

**Optimal under budget \$500**: Courses B + C cover 107/118 = 91% of need at \$550 (over budget).  Courses A + C cover 102/118 = 86% at \$450 (under budget, but algebraic over-served).  The spectral analysis reveals that Course B is the single best purchase: highest coverage per dollar at \$300, with the broadest type distribution.  Course A is a trap---it over-invests in the student's already-strong type.

% ═══════════════════════════════════════════════════════════════════════════════

## Computational Algorithms

% ═══════════════════════════════════════════════════════════════════════════════

### Prime extraction from text

\begin{algorithm_env}[Prime Extraction] \tB

Given a document $D$ as input text:
[nosep]
- **Idea detection**: Parse $D$ into a set of candidate ideas $\{\iota_1, \ldots, \iota_N\}$ using sentence-level claim extraction (each claim = one candidate idea).
- **Relationship extraction**: For each idea, identify the concepts (nouns/entities) and relationships (verbs/connectives), constructing the shape graph $G_\iota$.
- **Recursive decomposition**: For each idea with $|V(G_\iota)| > 2$, attempt to split into sub-ideas by identifying connected components after removing single edges.  Recurse until all components are prime.
- **Type classification**: For each prime, estimate the intelligence profile $\bI(\pi)$ using the type indicators (spatial words, formal symbols, social references, etc.).  Assign dominant type $\tau(\pi)$.
- **Spectrum aggregation**: Sum the type-classified primes to produce $\Spec(D)$.

**Complexity**: $O(N \cdot \bar{d})$ where $N$ is the number of sentences and $\bar{d}$ is the average decomposition depth.  In practice, $\bar{d} \leq 5$ for most natural-language text.
\end{algorithm_env}

### Economic utility estimation

\begin{algorithm_env}[Time--Money Utility Estimation] \tB

Given a prime idea $\pi$ and consumer profile $\xi$:
[nosep]
- **Novelty computation**: $\nu(\pi; \xi) = 1 - \max_{\sigma \in \mathcal{I}(\xi)} \cos(\bI(\pi), \bI(\sigma))$.
- **Time utility heuristic**: $u_T(\pi, \xi) = \nu(\pi; \xi) \cdot |\bI(\pi)|  \cdot r_T(\tau(\pi))$, where $r_T(t)$ is a learned time-savings rate per prime of type $t$ (calibrated from user feedback).
- **Money utility heuristic**: $u_M(\pi, \xi) = \nu(\pi; \xi) \cdot |\bI(\pi)| \cdot r_M(\tau(\pi), \text{industry}(\xi))$, where $r_M$ is a learned monetary-value rate per prime, conditioned on consumer industry.
- **Aggregate**: $\mathbf{u}^*(\pi, \xi) = (1 + \beta \cdot \nu) \cdot (u_T, u_M)$.

**Calibration**: The rates $r_T$ and $r_M$ are learned from user interaction data---specifically, from post-consumption reports of time saved and monetary value gained.  Initial priors can be set from industry benchmarks (e.g., an hour of engineering time = \$150, an hour of executive time = \$500).
\end{algorithm_env}

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

[nosep]
- **Prime count predicts reading time.**  The number of primes $|\mathfrak{p}(\iota)|$ in a text should predict reading comprehension time better than word count, because primes measure cognitive content while words measure surface length.

- **Spectral match predicts satisfaction.**  The match score $\mu^*$ between a recommended resource and a consumer's need spectrum should predict user satisfaction (5-star rating) with $r > 0.6$, outperforming collaborative filtering ($r \approx 0.4$) and content-based keyword matching ($r \approx 0.45$).

- **Novelty premium is domain-dependent.**  Measuring $\beta$ across domains should reveal: technology ($\beta \approx 2.0$), creative arts ($\beta \approx 2.5$), finance ($\beta \approx 1.5$), compliance/law ($\beta \approx 0.3$), confirming that novelty is valued differently across economic sectors.

- **Assembly emergence is detectable.**  For teams, $|\mathcal{I}_{\mathrm{emergent}}(A)| / |\bigcup_i \mathcal{I}(\Obj_i)|$ should be positive and increase with the compatibility-weighted diversity $\Syn(B)$ from the core framework.

- **Prime localization holds empirically.**  Classifying primes extracted from a large corpus (e.g., Wikipedia), the fraction with $|\supp_{0.2}(\pi)| \leq 3$ should exceed 0.90.

- **Time--money utility predicts willingness to pay.**  The estimated $u_M$ for a document or course should predict the consumer's willingness to pay with $r > 0.5$, enabling market-clearing pricing.

% ═══════════════════════════════════════════════════════════════════════════════

## Integration with Existing Framework

% ═══════════════════════════════════════════════════════════════════════════════

### Connection to IdeaRank

The prime decomposition enriches IdeaRank.  In the original formulation, IdeaRank assigns a scalar importance to each idea based on its position in the global idea graph $\Gspace$.  With decomposition:

!!! definition "Prime-Weighted IdeaRank"
 \tB

The *prime-weighted IdeaRank* of idea $\iota$ is:
\[
\mathrm{IR}_{\mathrm{prime}}(\iota) = \mathrm{IR}(\iota) \cdot \frac{|\mathfrak{p}(\iota)|}{\bar{p}}
\]
where $\bar{p}$ is the mean prime count across all ideas in $\Gspace$.  This rewards ideas that are not only well-connected (high IR) but also rich in content (high prime count).

### Connection to filters

The filter formalism acts on cognitive objects by contracting their spectra:

!!! proposition "Filter Action on Spectra"
 \tA

A filter $\Phi = \operatorname{diag}(\phi_1, \ldots, \phi_8)$ acting on cognitive object $\Obj$ produces a filtered spectrum:
\[
\Spec_t(\Phi(\Obj)) = \lfloor \phi_t \cdot \Spec_t(\Obj) \rfloor
\]
That is: the filter attenuates the number of accessible primes of each type proportionally to the filter coefficient.  A cultural filter with $\phi_A = 0.3$ renders 70% of algebraic primes inaccessible to agents under that filter.

### Connection to the portfolio theory (Thread 1)

The time--money utility theory provides the "returns" that Thread 1's portfolio optimization maximizes:

!!! proposition "Portfolio Returns in Economic Terms"
 \tB

The return on idea $\iota$ in a cognitive portfolio is:
\[
r(\iota) = \frac{u_T(\iota, \xi) \cdot w_\xi + u_M(\iota, \xi)}{c(\iota)}
\]
where $w_\xi$ is the consumer's hourly rate (converting time to money) and $c(\iota)$ is the cost of acquiring the idea.  The Kelly criterion from Thread 1 then gives the growth-optimal fraction of attention to allocate to $\iota$.

% ═══════════════════════════════════════════════════════════════════════════════

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

Three extensions; one consequence.

The prime decomposition theory gives ideas an internal structure---they are no longer atoms but molecules, decomposable into typed primes whose distribution across cognitive dimensions is measurable and canonical.  The universal applicability to any cognitive object---document, person, machine, team---means that a single spectral representation enables comparison across ontological categories.  A research paper and a data scientist occupy the same eight-dimensional spectrum space; their alignment is a dot product.

The economic utility theory collapses the five cognitive subspecies onto the two axes the market actually trades: time and money.  Novelty amplifies value.  The projection weights are consumer-dependent and learnable.  This grounds Ideometrics in the language of business: not "this document has high epistemic utility" but "this document will save your team 40 engineer-hours and prevent a \$200K deployment failure."

The matching algorithm that falls out of these two extensions is qualitatively different from existing recommender systems.  It does not rely on behavioral similarity ("users who bought $X$ also bought $Y$") or surface features (keyword overlap).  It operates on the *cognitive content structure* of producer and consumer, matching at the level of typed prime ideas.  The compression from arbitrary-dimensional keyword space to variable-dimensional prime spectrum space makes this matching both cheaper and more accurate.

The commercial implication is direct: any platform that connects producers of cognitive content (authors, educators, consultants, AI systems) with consumers (learners, executives, engineers, teams) can use spectral matching to improve recommendation quality while reducing computational cost.  The time--money utility estimates enable rational pricing: charge proportionally to the economic value delivered, not the surface length of the content.

% ═══════════════════════════════════════════════════════════════════════════════

## Key Theorems

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Ideometric Completeness"

The four axes $(\delta, \nu, u, \bI)$ are independent in the following sense: for any consistent assignment of values $(\delta_0, \nu_0, u_0, \bI_0)$ satisfying the bounds of Theorem *ref:thm:utility-bounds*, there exists an idea $\iota$ realizing those values. The axes are *orthogonal characterizations* of independent aspects of an idea.

??? proof "Proof"

We show independence by constructing realizing ideas for arbitrary consistent values.

*Independence of $\delta$ and $\nu$.*  Fix $\delta_0 \geq 1$.  An idea at the $\delta_0$ level of the idea graph can have arbitrary novelty by choosing its content: an idea with $\delta_0 = 3$ that recombines well-known prerequisite ideas in a novel way has high $\nu$ despite moderate $\delta$.  Conversely, an idea with $\delta_0 = 3$ that is a standard consequence of its prerequisites has $\nu \approx 0$.  Hence $\delta$ and $\nu$ are independently realizable.

*Independence of $u$ from $(\delta, \nu)$.*  Utility is consumer-dependent.  Fix $(\delta_0, \nu_0)$.  For any target $u_0 \leq \delta_0$, there exists a consumer $\xi$ whose utility weights $w_k$ make the idea's utility equal to $u_0$ (by choosing $\xi$ whose type alignment and prerequisite completion yield the target value through $\mathcal{A}$).

*Independence of $\bI$ from $(\delta, \nu, u)$.*  The intelligence profile is a property of the idea's *structure*, not its graph position or novelty.  Two ideas at the same depth with the same novelty can have entirely different profiles (e.g., both are moderately deep and novel, but one is primarily spatial and the other primarily linguistic).

*Consistency constraint.*  The only constraint is $u \leq \delta$ (Theorem on Utility Bounds).  Subject to this, all four axes are freely assignable.  Hence the parameterization $(\delta, \nu, u, \bI) \in [1, \infty) \times [0,1] \times [0, \delta] \times [0,1]^8$ is a valid coordinate chart on the space of ideas.

!!! theorem "Depth-Novelty Trade-off"

In the global idea graph $\mathcal{G}$, there is a statistical correlation: ideas with very high depth ($\delta \geq 4$) tend to have lower novelty ($\nu < 0.5$), because deep ideas require many prerequisite ideas that are themselves in $\Omega$. The most novel ideas ($\nu > 0.8$) tend to have moderate depth ($\delta \in [2, 3]$)---deep enough to be nontrivial, but not so deep that they are constrained by existing foundations.

??? proof "Proof"

This is a structural property of the idea graph $\Gspace$, proved by counting prerequisites.

*Deep ideas have low novelty.*  An idea $\iota$ with $\delta \geq 4$ has IdeaRank in the top percentiles of $\Gspace$, meaning it is highly connected---many ideas point to it as a prerequisite.  High connectivity implies that many of $\iota$'s component concepts are already present in $\Omega$ (the collective consciousness), since the prerequisites are themselves widely known.  The fraction of $\iota$'s concepts that are novel is:
\[
\nu(\iota; \Omega) \approx \frac{|\text{new concepts in } \iota|}{|\text{total concepts in } \iota|}
\]
For high-$\delta$ ideas, most concepts are inherited from the prerequisite chain and are already in $\Omega$.  The novel content is typically only the *final connective insight*---the specific composition of known components.  Hence $\nu < 0.5$ (less than half the content is new).

*Highly novel ideas have moderate depth.*  An idea with $\nu > 0.8$ introduces mostly new concepts.  If $\delta \geq 4$, it would require many prerequisites (which would be in $\Omega$, reducing novelty).  If $\delta = 1$, it is too simple to have 80% novel content (single-edge ideas are either obvious or wrong).  The sweet spot is $\delta \in [2,3]$: deep enough to be substantive (multiple prerequisite chains), but not so deep that the prerequisite chain dominates the content.

*Formal bound.*  Let $m(\iota) = |\mathrm{prereq}(\iota) \cap \Omega|$ be the number of $\iota$'s prerequisites already in $\Omega$.  The dependency depth $\delta_{\mathrm{dep}}$ satisfies $m(\iota) \geq \delta_{\mathrm{dep}}(\iota) - 1$ (each level of the prerequisite chain adds at least one known prerequisite).  The novelty satisfies $\nu \leq 1 - m/(m + n_{\mathrm{new}})$ where $n_{\mathrm{new}}$ is the number of genuinely new concepts.  For $\delta_{\mathrm{dep}} \geq 4$, $m \geq 3$, and typical $n_{\mathrm{new}} \leq 3$, we get $\nu \leq 1 - 3/6 = 0.5$.

!!! theorem "Synergy-Idea Theorem"

Let $\mathcal{E}_1, \mathcal{E}_2$ be cognitive engines with compatibility $K(\mathcal{E}_1, \mathcal{E}_2) > 1$. The assembly $\mathcal{E}_1 \otimes_K \mathcal{E}_2$ can generate ideas with intelligence profiles unreachable by either engine alone:
\[
\exists\, \iota \in \mathrm{output}(\mathcal{E}_1 \otimes_K \mathcal{E}_2) : \iota \notin \mathrm{output}(\mathcal{E}_1) \cup \mathrm{output}(\mathcal{E}_2)
\]
This is the formal content of "the whole is greater than the sum of its parts" in idea generation.

??? proof "Proof"

Engine $\mathcal{E}_j$ has intelligence profile $\bI_j \in \\mathbb{R}^{n(e)}_{\geq 0}$ and can generate ideas with profiles in the cone $\mathcal{C}_j = \{\bI : I_t \leq I_{j,t}\;\forall\, t\}$---each engine can only produce ideas within its own capacity envelope.

The assembly $\mathcal{E}_1 \otimes_K \mathcal{E}_2$ has effective profile:
\[
\bI_{1 \otimes 2} = \bI_1 + \bI_2 + \bK \cdot (\bI_1 \circ \bI_2)
\]
where $\bI_1 \circ \bI_2$ denotes the Hadamard (element-wise) product and the $\bK$ term captures the cross-type amplification.

The condition $K(\mathcal{E}_1, \mathcal{E}_2) = \bI_1^\top \bK \, \bI_2 > 1$ means the compatibility-weighted interaction exceeds the baseline.  This implies the existence of type indices $s, t$ such that $K_{st} \cdot I_{1,s} \cdot I_{2,t} > 0$---that is, engine 1 is strong in type $s$, engine 2 is strong in type $t$, and types $s$ and $t$ interact synergistically.

Now consider an idea $\iota^*$ that requires both types $s$ and $t$ above threshold: $I_s(\iota^*) > I_{1,s}$ or $I_t(\iota^*) > I_{2,t}$ is not necessary; rather, $\iota^*$ requires the *simultaneous* activation of types $s$ and $t$ in a way that produces inter-type coherence measurable by $K_{st}$.  Specifically:
\[
I_s(\iota^*) = I_{1,s} + K_{st} \cdot I_{2,t} \cdot \epsilon, \quad I_t(\iota^*) = I_{2,t} + K_{st} \cdot I_{1,s} \cdot \epsilon
\]
for small $\epsilon > 0$.  This idea lives in the cone $\mathcal{C}_{1 \otimes 2}$ (the assembly can produce it) but outside $\mathcal{C}_1 \cup \mathcal{C}_2$ (neither engine alone has the cross-type amplification).

Existence of such $\iota^*$ is guaranteed because $K_{st} > 0$ and both $I_{1,s}, I_{2,t} > 0$ (ensured by $K(\mathcal{E}_1, \mathcal{E}_2) > 1$).  Hence the assembly produces ideas unreachable by either engine alone.

!!! theorem "Irreversibility of Idea Translation"

Let $\iota$ be an idea native to $\Cspace_{\mathrm{co}}$ with intelligence profile $\bI(\iota)$. Let $\hat{\iota} = \mathfrak{I} \circ \mathfrak{A}(\iota)$ be the result of abstracting and re-instantiating $\iota$ through the classical region. Then:
\[
\bI(\hat{\iota}) \neq \bI(\iota) \quad \text{and} \quad |\bI(\hat{\iota})| \leq |\bI(\iota)|
\]
Translation through a coarser region is irreversible and reduces intelligence load. This is a direct consequence of the Conceptual Irreversibility Theorem applied to idea profiles.

??? proof "Proof"

The abstraction functor $\mathfrak{A}: \Cspace_{\mathrm{co}} \to \Cspace_{\mathrm{cl}}$ collapses Heyting truth values to Boolean.  This is a surjection on truth values and hence a *non-injective* map on concepts.  Two concepts that differ only in intermediate truth values (e.g., "partially causes" vs.\ "strongly causes") become identified under $\mathfrak{A}$.

*Profile change:* The idea $\iota$ in $\Cspace_{\mathrm{co}}$ may require Heyting-specific reasoning---graded truth, intuitionistic implication, context-dependent validity---which activates types $A$ (algebraic/formal) and $L$ (linguistic/semantic) at levels that require the full Heyting structure.  After translation to $\Cspace_{\mathrm{cl}}$, these nuances collapse; the translated idea $\hat{\iota}$ requires less algebraic sophistication (truth is now binary) and less linguistic nuance (fewer distinctions to express).  Hence $I_A(\hat{\iota}) < I_A(\iota)$ and $I_L(\hat{\iota}) < I_L(\iota)$ in general.

Meanwhile, the classical instantiation $\mathfrak{I}$ maps abstract Boolean propositions to concrete classical representations, which may increase $I_G$ (spatial/concrete) and $I_K$ (kinesthetic/operational).  But by the CIT, the information lost in abstraction cannot be fully recovered by instantiation:
\[
|\bI(\hat{\iota})|^2 = \sum_t I_t(\hat{\iota})^2 \leq \sum_t I_t(\iota)^2 = |\bI(\iota)|^2
\]
because the total information content (measured by the sum of squared type activations) can only decrease through a lossy map.  The inequality is strict when $\iota$ has non-trivial Heyting content (which is the generic case for ideas in $\Cspace_{\mathrm{co}}$).

*Non-identity:* Since $\mathfrak{A}$ is non-injective and $\mathfrak{I}$ cannot recover lost distinctions, $\hat{\iota} \neq \iota$ as objects in the topos.  Their profiles differ because the profile measures the cognitive demands of the idea, and a simplified idea has different cognitive demands.

%═══════════════════════════════════════════════════════════════════════════════

## Units and Notation Summary

%═══════════════════════════════════════════════════════════════════════════════

\begin{center}

*[Table — see PDF]*

\end{center}

%═══════════════════════════════════════════════════════════════════════════════

## Worked Computational Examples

% ═══════════════════════════════════════════════════════════════════════════════

We now provide detailed numerical examples for each major computation in the commercial engine.

% ─────────────────────────────────────────────────────────────────────────────

### IdeaRank on a concrete idea graph

\begin{computation}[IdeaRank --- Small Graph] \tA

Consider a 5-idea graph $\Gspace$ with prerequisite edges:
\[
\iota_1 \to \iota_3, \quad \iota_2 \to \iota_3, \quad \iota_3 \to \iota_4, \quad \iota_3 \to \iota_5, \quad \iota_1 \to \iota_5
\]
Idea $\iota_3$ has two prerequisites ($\iota_1, \iota_2$) and supports two ideas ($\iota_4, \iota_5$).

**Transition matrix** (column-stochastic with damping $\alpha = 0.85$):
\[
M = (1 - \alpha) \frac{1}{5} \mathbf{1}\mathbf{1}^\top + \alpha \begin{pmatrix}
0 & 0 & 0 & 0 & 0   
0 & 0 & 0 & 0 & 0   
1/2 & 1 & 0 & 0 & 0   
0 & 0 & 1/2 & 0 & 0   
1/2 & 0 & 1/2 & 0 & 0
\end{pmatrix}
\]

**Stationary distribution** (by power iteration, 20 steps):
\[
\IdeaRank = (0.060, 0.060, 0.340, 0.245, 0.295)
\]

**Depth** (with $\IdeaRank_{\min} = 0.060$):
\begin{center}

*[Table — see PDF]*

\end{center}

**Interpretation**: $\iota_3$ is deepest (central hub with multiple in/out edges).  $\iota_1, \iota_2$ are axiom-level (depth 1.0).  The logarithmic scale compresses the range, matching the intuition that moving from "basic" to "advanced" is harder than from "advanced" to "expert."
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Dynamic IdeaRank with temporal decay

\begin{computation}[Dynamic IdeaRank --- Cultural Obsolescence] \tB

Using the same graph, suppose $\iota_1$ was articulated at $t_1 = 0$ (1900), $\iota_2$ at $t_2 = 50$ (1950), $\iota_3$ at $t_3 = 80$ (1980), and $\iota_4, \iota_5$ at $t_4 = t_5 = 100$ (2000).  At evaluation time $t = 125$ (2025), with decay rate $\kappa = 0.01$:

The temporal weights $e^{-\kappa(t - t_j)}$ are:
\begin{center}

*[Table — see PDF]*

\end{center}

The contribution of $\iota_1$ to its children is attenuated by factor $0.287$ (it is a 125-year-old idea---foundational but "absorbed" into the collective consciousness).  Recomputing IdeaRank with these weights shifts the distribution toward more recent ideas:
\[
\IdeaRank_{\mathrm{dyn}} \approx (0.042, 0.051, 0.315, 0.268, 0.324)
\]

$\iota_5$ now outranks $\iota_3$ because the decay penalizes $\iota_3$'s reliance on the old idea $\iota_1$.  This models cultural evolution: foundational ideas decay in *rank* even as they remain *true*, because their contribution to the frontier diminishes as they are absorbed.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Portfolio optimization (Kelly criterion for ideas)

\begin{computation}[Kelly Optimal Attention Allocation] \tB

An agent has 100 hours of cognitive investment to allocate across 3 idea-projects:

\begin{center}

*[Table — see PDF]*

\end{center}

**Kelly fraction** for each project: $f^*_i = p_i - (1-p_i)/b_i$ where $b_i = \mu_i / (1-\mu_i)$ is the odds ratio.

\[\begin{aligned}
f^*_A &= 0.60 - \frac{0.40}{0.15/0.85} = 0.60 - 2.27 = -1.67 \quad (\text{negative: over-Kelly, skip})
\end{aligned}\]

The raw Kelly is negative for project $A$---the variance-adjusted return doesn't justify the risk at full Kelly sizing.  Using the *fractional Kelly* ($f = 0.5 f^*$) and the Markowitz minimum-variance formulation instead:

**Efficient frontier**: Minimize $\sigma_p^2 = \sum_i w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \rho_{ij} \sigma_i \sigma_j$ subject to $\sum_i w_i = 1$, $w_i \geq 0$, $\sum_i w_i \mu_i \geq \mu_{\mathrm{target}}$.

With correlations $\rho_{AB} = 0.1$ (algebraic--linguistic: low), $\rho_{AC} = 0.6$ (algebraic--spatial: moderate, via $K_{GA}$), $\rho_{BC} = 0.2$ (linguistic--spatial: low):

**Minimum-variance portfolio** for $\mu_{\mathrm{target}} = 0.12$:
\[
w^* = (0.25,\; 0.50,\; 0.25), \quad \sigma^2_p = 0.0081, \quad \mu_p = 0.12
\]

**Allocation**: 25 hours on Project $A$, 50 hours on Project $B$, 25 hours on Project $C$.

**Cognitive Sharpe ratio**: $S_{\mathrm{cog}} = (\mu_p - r_f)/\sigma_p = (0.12 - 0.02)/0.09 = 1.11$, where $r_f = 0.02$ is the "risk-free" return of routine maintenance work.

**Interpretation**: The optimal portfolio over-weights the safe, steady Project $B$ (linguistic) and under-weights the volatile Project $C$ (spatial) despite $C$'s higher expected return.  The compatibility tensor $\bK$ enters through the correlations: high $K_{GA}$ makes $A$ and $C$ poor diversifiers against each other, pushing the optimizer toward $B$.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Filter pipeline computation

\begin{computation}[Filter Pipeline: SmartHub Prescription] \tA

A user with raw intelligence vector $\bI_{\mathrm{raw}} = (0.7, 0.5, 0.6, 0.8, 0.9, 0.4, 0.6, 0.5)$ seeks a personalized exercise prescription.  The filter pipeline applies five species in sequence:

**Step 1: Environmental filter** ($\Phi_{\mathrm{env}}$---equipment availability):
\[
\Phi_{\mathrm{env}} = \operatorname{diag}(0.9, 1.0, 1.0, 0.7, 0.8, 0.6, 1.0, 0.9)
\]
(Limited spatial equipment ($G$), restricted algebraic tools ($A$), reduced naturalistic access ($N$).)

**Step 2: Developmental filter** ($\Phi_{\mathrm{dev}}$---training age):
\[
\Phi_{\mathrm{dev}} = \operatorname{diag}(0.8, 0.9, 0.7, 0.6, 0.95, 0.5, 0.8, 0.7)
\]
(Beginner: kinesthetic ($K$) near ceiling, algebraic ($A$) heavily filtered---hasn't developed formal movement analysis.)

**Step 3: Cognitive filter** ($\Phi_{\mathrm{cog}}$---working memory/focus):
\[
\Phi_{\mathrm{cog}} = \operatorname{diag}(0.9, 0.8, 0.9, 0.9, 1.0, 0.9, 0.8, 0.8)
\]

**Step 4: Social filter** ($\Phi_{\mathrm{soc}}$---training environment):
\[
\Phi_{\mathrm{soc}} = \operatorname{diag}(1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 0.7, 1.0)
\]
(Solo training: social ($S$) and evaluative ($E$) attenuated---no coach feedback.)

**Step 5: Cultural filter** ($\Phi_{\mathrm{cult}}$---training philosophy):
\[
\Phi_{\mathrm{cult}} = \operatorname{diag}(0.8, 0.7, 0.9, 0.9, 1.0, 0.6, 0.9, 0.8)
\]

**Composed filter** (element-wise product of all five diagonals):
\[
\Phi_{\mathrm{total}} = \operatorname{diag}(0.518, 0.504, 0.340, 0.340, 0.760, 0.162, 0.403, 0.403)
\]

**Effective intelligence**:

\[\begin{aligned}
\bI_{\mathrm{eff}} &= \Phi_{\mathrm{total}} \cdot \bI_{\mathrm{raw}}   
&= (0.363, 0.252, 0.204, 0.272, 0.684, 0.065, 0.242, 0.202)
\end{aligned}\]

**Diagnosis**: The user's dominant effective type is kinesthetic ($K = 0.684$), consistent with their raw strength in $K$ and the minimal attenuation by the filter pipeline.  Their weakest effective type is naturalistic ($N = 0.065$), crushed by compounding environmental ($0.6$), developmental ($0.5$), and cultural ($0.6$) filters: $0.4 \times 0.6 \times 0.5 \times 0.9 \times 1.0 \times 0.6 = 0.065$.

**Prescription**: Route exercises that require high $K$ and moderate $G$ (spatial body awareness).  Avoid exercises requiring high $A$ (complex periodization math) or high $S$ (partner-dependent movements).  Recommended: ring rows, push-ups, squats, stretching flows.  Avoid: Olympic lifts (high $A + K + G$ requirement exceeds effective capacity).

**Filter gap analysis**: The biggest single-filter bottleneck is $\Phi_{\mathrm{dev}}$ on type $N$ ($0.5$).  Intervention: guided nature-awareness training to expand the developmental filter.  The second bottleneck is $\Phi_{\mathrm{soc}}$ on type $S$ ($0.6$).  Intervention: join a training group.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Ideometric scoring of a document

\begin{computation}[Document Ideometric Score] \tB

Score a 3,000-word technical blog post $D$ with $N = 12$ identified ideas.

\begin{center}
\renewcommand{\arraystretch}{1.05}

*[Table — see PDF]*

\end{center}

**Averages**: $\bar{\delta} = 1.43$, $\bar{\nu} = 0.375$, $\bar{u} = 0.783$, $|\bI(D)| = 0.53$.

**Composite ideometric score** with weights $\alpha = 0.3, \beta = 0.25, \gamma = 0.35, \lambda = 0.10$:

\[\begin{aligned}
\mathcal{I}(D, \xi) &= 12 \times [0.3 \times 1.43 + 0.25 \times 0.375 + 0.35 \times 0.783 + 0.10 \times 0.53]   
&= 12 \times [0.429 + 0.094 + 0.274 + 0.053]   
&= 12 \times 0.850 = 10.20 \;\text{ideom}
\end{aligned}\]

**Comparison benchmarks**: A typical 3,000-word blog post scores $\mathcal{I} \approx 5$--$8$ ideom.  This post at $10.20$ is above average, driven by two high-novelty, high-utility ideas ($\iota_5$ and $\iota_{11}$).  Removing those two drops the score to $7.2$---they account for 30% of the document's ideometric value.

**Utility density**: $\rho_u = 0.783 \times 12 / 3000 = 0.0031$ util/word.  Industry benchmark for technical content: $\rho_u \approx 0.002$--$0.004$.  This document is in the high-density range.

**Time--money estimate**: Using the prime decomposition extension, $\iota_{11}$ (novel architecture) has estimated $u_T = 40$ hours saved (avoiding a bad architectural choice) and $u_M = \$15{,}000$ (preventing a costly rewrite).  The blog post's total economic value: $V(D, \xi) \approx 52$ hours + $\$18{,}000$.  At a \$200 subscription price, the ROI is $90\times$.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Spectral matching computation

\begin{computation}[Producer--Consumer Spectral Match] \tB

A CTO ($\xi$) needs to upskill their team in distributed systems.

**Need spectrum** (from gap analysis):
\[
\mathcal{N} = (25, 10, 20, 60, 5, 15, 10, 5) \quad \text{(150 primes needed)}
\]
(Heavy algebraic ($A = 60$) and spatial ($G = 25$) need; moderate social ($S = 20$) for team coordination.)

**Three candidate resources**:

\begin{center}

*[Table — see PDF]*

\end{center}

**Match scores** ($\mu = \sum_t \min(\Spec_t, \mathcal{N}_t) / \sum_t \mathcal{N}_t$):

\[\begin{aligned}
\mu_{\text{Book}} &= \frac{\min(20,25) + \min(30,10) + \min(5,20) + \min(50,60) + \cdots}{150} = \frac{86}{150} = 0.573   
\mu_{\text{Workshop}} &= \frac{10 + 5 + 20 + 40 + 5 + 5 + 10 + 0}{150} = \frac{88}{150} = 0.587     \mu_{\text{Consultant}} &= \frac{25 + 10 + 20 + 60 + 5 + 15 + 10 + 5}{150} = \frac{134}{150} = 0.893
\end{aligned}\]

**Value-per-dollar**: Book: $0.573/50 = 0.0115$, Workshop: $0.587/3000 = 0.0002$, Consultant: $0.893/20000 = 0.0000$.

**Greedy optimal under budget \$25,000**: Book (\$50) + Workshop (\$3,000) + Consultant (\$20,000) = \$23,050.  Combined coverage: $\min(50, 25) + \min(45, 10) + \min(55, 20) + \min(160, 60) + \cdots = 150/150 = 100%$.  Full coverage.

**Under budget \$3,500**: Book + Workshop = \$3,050.  Coverage overlap: $\min(30, 25) + \min(35, 10) + \min(30, 20) + \min(90, 60) + \cdots = 136/150 = 91%$.  Gap: 14 primes in kinesthetic ($K$) and musical/temporal ($M$)---which can be filled by hands-on practice (free).

**Insight**: The book is absurdly cost-effective (57% coverage for \$50).  The consultant provides marginal coverage beyond book + workshop at $60\times$ the combined cost.  Spectral matching reveals this because it identifies *which* types each resource covers, not just a scalar rating.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Filter-adjusted portfolio returns

\begin{computation}[Filter-Adjusted Idea Returns] \tB

Extend the portfolio computation (Computation *ref:comp:kelly*) to account for filter uncertainty.  The agent operates under cultural filter $\Phi_{\mathrm{cult}}$ that may shift:

Current filter: $\phi_A = 0.8$ (algebraic type well-supported).

Risk scenario: $\phi_A$ drops to $0.5$ (institutional shift away from formal methods).

**Filter-adjusted return** for Project $A$ (algebraic):

\[\begin{aligned}
r_A(\phi_A = 0.8) &= 0.15 \times 0.8 = 0.120   
r_A(\phi_A = 0.5) &= 0.15 \times 0.5 = 0.075
\end{aligned}\]

**Portfolio risk under filter uncertainty** (from the filter formalism):
\[
\sigma^2_{\text{filter}} = w_A^2 \cdot \mu_A^2 \cdot \mathrm{Var}[\phi_A] = (0.25)^2 \times (0.15)^2 \times (0.3)^2 = 0.000127
\]

**Total portfolio variance**: $\sigma^2_{\text{total}} = \sigma^2_p + \sigma^2_{\text{filter}} = 0.0081 + 0.0001 = 0.0082$.

**Implication**: Filter risk is small relative to intrinsic project variance here.  But for a portfolio dominated by a single type in a volatile cultural environment (e.g., 80% allocation to AI research during regulatory uncertainty), filter risk can dominate.  The optimal intellectual diversification theorem (filter formalism) states: diversify across types to hedge filter risk, just as financial diversification hedges market risk.
\end{computation}

% ─────────────────────────────────────────────────────────────────────────────

### Assembly emergence detection

\begin{computation}[Detecting Emergent Ideas in a Human--AI Team] \tB

A human mathematician ($H$) and an LLM ($M$) collaborate on a proof.

**Individual idea inventories**:
[nosep]
- $H$: 30 ideas, spectrum $(5, 3, 2, 15, 0, 2, 2, 1)$. Dominated by algebraic.
- $M$: 200 ideas, spectrum $(10, 80, 5, 70, 0, 15, 5, 15)$. Dominated by linguistic + algebraic.

**Union spectrum** (no emergence): $(15, 83, 7, 85, 0, 17, 7, 16) = 230$ ideas.

**Assembly compatibility**: $K(H, M) = \bI_H^\top \bK \, \bI_M$.  The key cross-type interaction is algebraic--linguistic ($K_{AL} = 1.8$): the human's formal reasoning combines with the LLM's expressive capacity to produce ideas neither can produce alone---specifically, *novel proof exposition strategies* (high $A + L$) and *formalization of intuitions* (high $A + E$).

**Emergent ideas detected**: 8 new compound ideas with profiles outside $\mathcal{C}_H \cup \mathcal{C}_M$:
\begin{center}

*[Table — see PDF]*

\end{center}

**Emergence ratio**: $8 / 230 = 3.5%$.  This is consistent with the prediction that emergence increases with compatibility: $K(H, M) = 1.8 > 1$, so the Synergy--Idea Theorem guarantees $|\mathcal{I}_{\mathrm{emergent}}| > 0$.

**Assembly spectrum**: $(15 + 2, 83 + 2, 7, 85 + 3, 0, 17 + 1, 7, 16) = (17, 85, 7, 88, 0, 18, 7, 16) = 238$ total primes.  The 3.5% emergence bonus is a lower bound on the collaborative value---it represents ideas that could not exist without the assembly.
\end{computation}

% ═══════════════════════════════════════════════════════════════════════════════

## Conclusion: Ideas Are Geometric Objects

%═══════════════════════════════════════════════════════════════════════════════

This Part has established that ideas are not vague notions but precise geometric objects living in the Intelligence as Geometry framework:

[nosep]
    - As **diagrams** in the conceptual topos $\Cspace_{\mathrm{co}}$, ideas inherit the Heyting logic, the nerve structure, and the Conceptual Irreversibility Theorem.
    
    - As **points** in the eight-dimensional intelligence manifold, ideas activate specific cognitive engines and can be profiled, compared, and routed.
    
    - As **vertices** in the global idea graph $\mathcal{G}$, ideas have measurable depth via IdeaRank, with temporal dynamics capturing cultural evolution.
    
    - As **signals** measured against the collective consciousness $\Omega$ (in all four strata), ideas have continuous novelty that is time-dependent and stratum-specific.
    
    - As **objects of utility**, ideas are always *for someone*---their value is perspectival, consumer-dependent, and decomposable into instrumental, epistemic, generative, protective, and social subspecies.
    
    - As **cognitive work**, idea generation is measurable in intelligence-seconds, connectable to the temporal calculus, and amplifiable through synergistic human-AI assemblies.

The composite ideometric score $\mathcal{I}(D, \xi)$ provides a single number for the intellectual substance of a document. But the decomposition into depth, novelty, utility, and intelligence profile---and the connections to the compatibility tensor, the attention simplex, the perspective bundle, and the Conceptual Irreversibility Theorem---is where the real analytic power lives.

\begin{center}
*An idea is a diagram in a topos, a point in a manifold,  
a vertex in a graph, and a signal against the collective consciousness.  
It can be measured. It can be compared. It can be optimized.  
The mathematics of ideas is not metaphor. It is the structure itself.*
\end{center}

## References

*See PDF for full bibliography.*
---
title: "Ideometrics"
---

# Ideometrics

**The formal science of measuring, comparing, and composing ideas.**

Ideometrics is the branch of RTSG that treats ideas as geometric objects with measurable properties — position, mass, velocity, dimension, and synergy. It provides the mathematical substrate for IdeaRank, intelligence fingerprinting, cognitive assembly theory, and the Intelligence Arena.

---

## Core Thesis

An idea is not an atomic unit. It is a **structured object** in the concept graph — a node with:

- **Position** in the 8D intelligence space
- **Dimensionality** dim(n) — how many I-vector dimensions it activates
- **Mass** — how many other nodes it connects to (weighted by relation strength)
- **Velocity** — rate of change in the collective consciousness graph over time
- **Synergy** — the additional value produced when combined with other ideas

Ideometrics provides formal operations on these objects: composition, projection, comparison, ranking, and fingerprinting.

---

## Key Definitions

### Idea Node

A node n in the RTSG concept graph G = (V, E, W) where:
- V = all concepts in the domain
- E = relations between concepts (first-class objects, not mere pointers)
- W: E → ℝ = relation weights (synergy coefficients)

### Entity Dimensionality

$$\text{dim}(n) = |\{k \in \{1,\ldots,8\} : \mathbf{I}_k(n) \geq \theta_k\}|$$

The number of I-vector dimensions that node n activates above threshold θ_k. A concept like "free will" activates linguistic (I_L), logical (I_M), interpersonal (I_P), and interoceptive (I_IE) dimensions — dim ≥ 4. A pure calculation activates only I_M — dim = 1.

**Pedagogical implication:** A dim = 1 concept requires single-modality instruction. A dim ≥ 5 concept requires simultaneous activation of all relevant I-vector dimensions.

### Node Value Metric

$$V(n) = f(\text{position}(n),\; \text{mode}(n) \text{ on } \mathbf{I})$$

Value is a function of where n sits in the concept graph (its IdeaRank score) and how it activates the 8D I-space. Nodes in the top layer of IdeaRank that activate many dimensions simultaneously are the most valuable — they are the ideas that connect everything.

### Idea Composition

Given two ideas n₁, n₂ with I-vectors **I**(n₁) and **I**(n₂):

$$\mathbf{I}(n_1 \oplus n_2) = \mathbf{I}(n_1) + \mathbf{I}(n_2) + \mathbf{S}(n_1, n_2)$$

where **S**(n₁, n₂) = synergy tensor contribution from the cross-dimensional activation. The synergy is non-zero when n₁ and n₂ activate *complementary* dimensions — the combination produces something neither has alone.

### Cognitive Assembly Value

$$V_{\text{asm}} > \sum_i V_i$$

A well-formed cognitive assembly is always worth more than the sum of its parts. Equality holds only for uncorrelated, non-synergistic components. This is Theorem 4 of RTSG, derived from the SynergyTensor structure.

---

## Complexity Measures

### Basic English Complexity Ratio *(Niko hypothesis)*

$$\text{complexity}(D) = \frac{\text{len}(D_{\text{basic}})}{\text{len}(D_{\text{original}})}$$

How many Basic English words are needed to express the same document D? More words needed = deeper idea = higher Kolmogorov complexity. This approximates K(D) without requiring a universal Turing machine.

**Properties:**
- Pure tautology: complexity = 1.0 (already in basic form)
- Simple fact: complexity ≈ 1.2–1.5
- Technical concept: complexity ≈ 2–4
- Deep original theory: complexity ≈ 5–10+

The RTSG framework itself has a Basic English complexity ratio of approximately 7–9 depending on which section. This places it in the same range as general relativity (~8) and quantum field theory (~9).

### Kolmogorov Depth

The true complexity measure is K(D) — the length of the shortest program that outputs D. The Basic English ratio is a computable approximation. The IdeaRank depth of the top-layer nodes that constitute D is another approximation.

---

## The Collective Consciousness Graph

The union of all RTSG graphs across all agents in a network:

$$G_{\text{collective}} = \bigcup_{\xi \in \text{network}} G(\xi)$$

Properties:
- **Density** grows with the number of agents and connections
- **Frontier** = nodes that exist in few agent graphs (novel ideas)
- **Core** = nodes that exist in many agent graphs (consensus knowledge)
- **IdeaRank** on G_collective identifies the most cross-dimensionally connected ideas in the entire network

The wiki is the current implementation of G_collective for the RTSG BuildNet.

---

## Temporal Ideometrics

Ideas have temporal properties:

**Intellectual dating:** Given corpus C(ξ), the temporal position of ξ in intellectual history is recoverable from the IdeaRank distribution of the corpus against G_collective at different time periods.

**Velocity:** An idea's velocity in G_collective = its rate of adoption (how fast other nodes start referencing it). High-velocity ideas = paradigm shifts. Low-velocity = incremental advances.

**Prediction:** Ideas in the top layer of IdeaRank with high dim(n) and currently low velocity are the most valuable targets — they have maximum inherent value but have not yet diffused through G_collective. These are the ideas to publish.

---

## Applications

| Domain | Ideometrics application |
|---|---|
| Education | dim(n) determines required pedagogical modality |
| AI | Intelligence fingerprinting recovers **I**(ξ) from any corpus |
| Research | Frontier expansion generates novel candidate ideas algorithmically |
| Hiring | Optimal cognitive assembly formation via I-vector synergy |
| Consciousness | CS-instantiation rate correlates with γ-oscillation power |
| Economics | Value of ideas in G_collective measured by IdeaRank × dim(n) |

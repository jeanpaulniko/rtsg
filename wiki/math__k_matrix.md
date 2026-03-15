# The K-Matrix: Intelligence Dimensions

## Overview

The K-Matrix is RTSG's framework for modeling intelligence as a multi-dimensional tensor rather than a single scalar (IQ). It maps cognitive capability across 8 Gardner dimensions, their 10 compound products, and identifies 3 dimensional holes.

## Gardner Dimensions

The 8 base dimensions, derived from Howard Gardner's multiple intelligences theory and extended by RTSG:

| Dim | Name | Symbol | Status | Knowledge Graph Nodes |
|---|---|---|---|---|
| 1 | Spatial | $d_S$ | Active | 31 |
| 2 | Linguistic | $d_L$ | Active | 2,008 |
| 3 | Logical-Mathematical | $d_M$ | Active | 2,141 |
| 4 | Bodily-Kinesthetic | $d_B$ | Active | 1 |
| 5 | Musical | $d_\mu$ | **Hole** | 0 |
| 6 | Interpersonal | $d_I$ | **Hole** | 0 |
| 7 | Intrapersonal | $d_\iota$ | **Hole** | 0 |
| 8 | Naturalistic | $d_N$ | Active | 22 |

The dominance of Linguistic (2,008) and Logical-Mathematical (2,141) reflects the knowledge graph's current bias toward formal/analytical content. The 3 holes are topological features — their absence *shapes* the structure.

## The K-Matrix Tensor

For an individual, the K-Matrix is:

$$K \in \mathbb{R}^{8 \times 8}$$

where $K_{ij}$ represents the coherence between dimensions $i$ and $j$. The diagonal $K_{ii}$ is raw aptitude in dimension $i$; the off-diagonal $K_{ij}$ measures cross-dimensional integration.

The **K-score** is the spectral radius:

$$\kappa = \max |\lambda_k(K)|$$

This captures the dominant mode of intelligence — the direction in which cognitive energy concentrates most.

## Compound Dimensions

Taking tensor products of active dimension pairs yields 10 compound dimensions:

| Compound | Formula | Interpretation |
|---|---|---|
| Spatial × Linguistic | $d_S \otimes d_L$ | Visual storytelling, spatial metaphor |
| Spatial × Logical-Math | $d_S \otimes d_M$ | Geometric reasoning, topology |
| Spatial × Bodily | $d_S \otimes d_B$ | Proprioceptive navigation, dance |
| Spatial × Naturalistic | $d_S \otimes d_N$ | Ecological mapping, terrain sense |
| Linguistic × Logical-Math | $d_L \otimes d_M$ | Formal proof, mathematical writing |
| Linguistic × Bodily | $d_L \otimes d_B$ | Embodied metaphor, sign language |
| Linguistic × Naturalistic | $d_L \otimes d_N$ | Nature writing, taxonomy |
| Logical-Math × Bodily | $d_M \otimes d_B$ | Algorithmic movement, martial arts |
| Logical-Math × Naturalistic | $d_M \otimes d_N$ | Mathematical biology, ecology models |
| Bodily × Naturalistic | $d_B \otimes d_N$ | Survival skills, animal movement |

These live in the knowledge graph as nodes with `dimensional_product` relations to their parents.

## Dimensional Holes

The 3 missing dimensions create topological holes in the knowledge graph:

$$\beta_0 = 765 \text{ components}, \quad \beta_1 = 2065 \text{ cycles}, \quad \chi = 1$$

The holes represent **structural silence** — what the graph does not say. In Grothendieck filter language, the holes are the negative space of the identity filter.

Filling these holes requires:

- **Musical ($d_\mu$)**: Rhythm, harmony, temporal pattern recognition
- **Interpersonal ($d_I$)**: Social cognition, empathy, theory of mind
- **Intrapersonal ($d_\iota$)**: Self-knowledge, metacognition, introspection

## Cross-Federation Links

The strongest bridge in the knowledge graph:

$$\text{Logical-Mathematical} \leftrightarrow \text{Linguistic} = 3{,}687 \text{ links}$$

This massive cross-federation explains why RTSG naturally produces mathematical writing — the two dominant dimensions are deeply entangled.

## Connection to Fugue

The Fugue methodology (chess + martial arts + cognition) operates primarily in the compound dimension $d_M \otimes d_B$ (Logical-Mathematical × Bodily-Kinesthetic), with Fugue's shape-first evaluation adding $d_S$ (Spatial). The full Fugue K-vector is:

$$K_{\text{Fugue}} = d_S \otimes d_M \otimes d_B$$

## See Also

- [CS Mechanics](cs_mechanics.md)
- [Definitions](definitions.md)
- [RTSG Index](rtsg_index.md)
- [Equations Reference](equations.md)

# NRTE Brain-Graph: Mathematical Specification

**Jean-Paul Niko · RTSG v6.0 · March 2026**

## The Architecture

The brain organizes concepts in a five-layer hierarchy optimized by the principle of least action. The database mirrors this structure exactly.

### Layer 0: Tokens (Free Monoid Σ*)

Tokens are the atomic reusable morphemes — prefixes, suffixes, roots, phonemes. They form a free monoid over a finite alphabet Σ with concatenation as the operation. The key property is **sharing**: the token "un-" participates in hundreds of primes ("undo", "unfair", "universal"), amortizing its storage and retrieval cost.

The assembly of a prime from tokens is a **tropical semiring** problem. In the tropical semiring (ℝ ∪ {∞}, min, +):

    a ⊕ b = min(a, b)       (tropical addition)
    a ⊗ b = a + b           (tropical multiplication)

Finding the cheapest token combination to represent a prime is:

    cost(prime) = min_{paths} Σ c(token_i)

This is a shortest-path problem in the token graph — exactly what the brain's predictive coding optimizes.

### Layer 1: Primes

Irreducible semantic units that cannot be decomposed into simpler concepts within their dimension. Each prime belongs to exactly one of the 12 intelligence dimensions:

    I_L (linguistic), I_M (mathematical), I_S (spatial), I_K (kinesthetic),
    I_N (naturalistic), I_A (abstract), I_P (interpersonal), I_IE (interoceptive),
    I_Pr (proprioceptive), I_Σ (somatic), I_μ (musical), I_E (empathic)

### Layer 2+: Composites

Every composite concept factors uniquely into typed primes:

    concept = ∏_i p_i^{a_i}

yielding a prime spectrum Spec(ι) ∈ ℕ^12 — a 12-dimensional fingerprint.

### Layer 3+: Patterns, Topologies, Geometries

Higher-order structures built from composites. Each layer adds one level of abstraction. A "pattern" is a recurring subgraph. A "topology" is an invariant under continuous deformation of the pattern. A "geometry" adds metric structure.

## The Metric: Not Cosine Similarity

The true distance between concepts in the brain is not Euclidean. It has two non-Euclidean features:

**1. Hierarchy (hyperbolic geometry).** Some concepts contain others ("mammal" contains "dog"). This containment structure is naturally encoded in hyperbolic space — the Poincaré ball model B^n = {x ∈ ℝ^n : ||x|| < 1} — where:

    d_H(x, y) = arcosh(1 + 2||x-y||² / ((1-||x||²)(1-||y||²)))

Distance grows exponentially with depth, so the model has exponentially more "room" at the periphery — exactly matching the exponential branching of taxonomic hierarchies.

**2. Categorical boundaries (ultrametric / p-adic).** "Dog" and "cat" are semantically close, but there is a *sharp categorical boundary* between them. This is captured by ultrametric distance, where:

    d(x, z) ≤ max(d(x, y), d(y, z))    (strong triangle inequality)

Every point inside an ultrametric ball is its center — there are no "partial overlaps", only nested containment. This is the p-adic metric: d_p(x, y) = |x - y|_p = p^{-v_p(x-y)}.

**3. The combined metric (adelic).** The adelic product A = ℝ × ∏_p Q_p combines both:

    d_A(x, y) = d_∞(x_∞, y_∞) × ∏_p d_p(x_p, y_p)

The archimedean place gives continuous similarity. Each prime p gives categorical boundaries at scale p. This is the natural metric for a brain that must simultaneously handle smooth gradients and sharp categories.

**4. The GL Green's function distance.** The true "closeness" of two concepts is determined by the Green's function G(x,y) of the Ginzburg-Landau operator:

    d_GL(x, y) = -log G(x, y)

This distance encodes: "how much activation flows from x to y through the optimal network?" Concepts connected by thick, short tubes have small GL distance.

## The Optimization: Physarum Dynamics

The network structure is optimized by the same dynamics as the slime mold Physarum polycephalum. Each edge (tube) has thickness w that evolves by:

    dw/dt = |Q(w)| - γw

where Q(w) is the flow through the tube and γ is the decay rate. Tubes carrying more flow thicken; unused tubes atrophy. The steady state minimizes the Ginzburg-Landau functional:

    S[W] = ∫ (|∂W|² + α|W|² + (β/2)|W|⁴) dν

where:
- |∂W|² = gradient cost (penalizes long connections, rewards short paths)
- α|W|² = maintenance cost (keeping each tube alive costs metabolic energy)
- (β/2)|W|⁴ = saturation penalty (tubes can't grow infinitely thick)

The minimizer W* is the optimal network configuration — the brain's white matter tract architecture, the slime mold's tube network, and the NRTE database's connection weights.

## Connection Counting

Every entity tracks its connections across all 12 intelligence dimensions plus time:

    connections_by_dim = {
        I_L: 47, I_M: 12, I_S: 23, I_K: 3, ..., temporal: 156
    }

This vector determines:
- **Tube thickness**: proportional to total connections weighted by recency
- **Dominant dimension**: the dimension with most connections (= dominant cognitive channel for this concept)
- **Cross-dimensional richness**: C(k,2) = k(k-1)/2 where k = number of dimensions with connections > 0

The temporal dimension counts time-stamped activations. A concept activated 100 times last week has temporal thickness 100; one not activated in a year has temporal thickness decaying toward zero.

## The Efficiency Principle

Everything is organized so that **traveling along the network to communicate any concept is as fast as possible**. This is the principle of least action applied to cognition:

    min_path ∫ (1/thickness(e)) dl(e)

Traversal cost is inversely proportional to tube thickness. The network self-organizes (via Physarum dynamics) so that frequently co-activated concepts are connected by thick, short tubes — minimizing the total action of cognitive traversal.

## Implementation Notes

- **Token sharing** is implemented via the `prime_tokens` junction table. When a new prime is created, it reuses existing tokens from the pool, only creating new tokens for genuinely novel morphemes.
- **Prime spectrum** is stored as JSONB on each composite, enabling fast factorization queries.
- **Tube thickness** is updated on every traversal via the `traverse_edge()` function, which implements Physarum dynamics.
- **Global decay** runs periodically via `global_decay()`, modeling the forgetting curve.
- **GL action** is computed by `compute_gl_action()`, providing a single scalar measuring total network efficiency.
- **Hyperbolic embeddings** use pgvector with 64 dimensions in the Poincaré ball model.
- **Ultrametric embeddings** store p-adic valuations for the first several primes (2, 3, 5, 7, 11), enabling fast categorical boundary detection.

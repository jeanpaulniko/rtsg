# Intelligence Metrics — Expansion Roadmap

<div class="hero" markdown>

# 📊 Intelligence Metrics

<p class="hero-subtitle">The analytical core of RTSG — where the money lives</p>

</div>

!!! abstract "Strategic Vision"
    The Intelligence Engine is an API that every active AI agent, every CogOS instance, and every human user will want access to. It scores, compares, decomposes, and matches intelligence vectors — for models, documents, people, and teams. This page is the build roadmap.

---

## 1. The Product

**What we're selling:** An API + visual dashboard that lets anyone:

- **Score** any entity (AI model, human, document, team) as an I-vector in ℝⁿ⁽ᵉ⁾ (n=12 for humans, variable per entity)
- **Compare** any two or more entities across all n(e) dimensions (12 for humans) + Elo + composite metrics
- **Visualize** comparisons in every modality: bars, radar, 3D shapes, heatmaps, scatter, parallel coordinates
- **Analyze** geometric properties of the I-vector: shape class, density, parity, nearest neighbor, cosine similarity
- **Match** entities for optimal synergy — find the best partner, team, or tool for a given task
- **Track** changes over time — how does an entity's I-vector evolve?

**Who pays:**

- AI labs benchmarking their models against the field
- Enterprises choosing which model to deploy for which task
- Individuals assessing their own cognitive profile
- Teams optimizing composition for complementary strengths
- Document/content analysis — "what kind of intelligence produced this?"

---

## 2. Comparison Engine — Every Way Possible

### 2.1 Visual Comparisons

| Visualization | What it shows | Status |
|---|---|---|
| **3D Polyhedra** (Three.js) | Full I-vector as rotatable shape, overlay/grid/dim views | ✅ Live |
| **Radar Charts** | Classic 8-axis spider plot, 2-5 models overlaid | 🔨 Build next |
| **Bar Charts** | Side-by-side bars per dimension, grouped by model | 🔨 Build next |
| **Heatmap Matrix** | Models × Dimensions, color-coded intensity | 🔨 Build next |
| **Parallel Coordinates** | 8 vertical axes, one line per model, crossings show trade-offs | 🔨 Build next |
| **Scatter Plots** | Any 2 dimensions as X/Y, bubble size = Elo, color = group | 🔨 Build next |
| **Elo vs ‖I‖ Plot** | X=Elo, Y=‖I‖, reveals models that over/under-perform for their shape | 🔨 Build next |
| **Shape Silhouettes** | 2D projection of 3D polyhedra, overlaid like a police lineup | 📋 Planned |
| **Time Series** | I-vector components over model versions (V1→V2→V3) | 📋 Planned |
| **Synergy Map** | Network graph where edge thickness = complementarity score | 📋 Planned |

### 2.2 Numerical Comparisons

| Metric | Formula | What it reveals |
|---|---|---|
| **Euclidean Norm** ‖I‖ | √(Σ I_d²) | Raw magnitude — total cognitive firepower |
| **Cosine Similarity** | (A·B)/(‖A‖‖B‖) | Shape similarity regardless of scale — "same profile, different magnitude?" |
| **Euclidean Distance** | ‖A−B‖ | How far apart two entities are in intelligence space |
| **Manhattan Distance** | Σ\|A_d − B_d\| | Sum of per-dimension gaps — "total disagreement" |
| **Dimension Parity** | max(I)/min(I) | How lopsided the vector is — specialists vs generalists |
| **Entropy** | −Σ p_d log p_d where p_d = I_d/Σ I_d | Evenness of distribution — high entropy = generalist |
| **Density** | ‖I‖ / max_possible(‖I‖) | How much of the possible space is filled |
| **Nearest Neighbor** | argmin_B ‖A−B‖ | Who is most similar to whom? |
| **Farthest Neighbor** | argmax_B ‖A−B‖ | Maximum cognitive distance — the most complementary pair |
| **Dominance Count** | #{d : A_d > B_d} | In how many dimensions does A beat B? |
| **Pareto Frontier** | Non-dominated set | Which models are not strictly beaten on all dims by any other? |
| **Centroid** | (1/n)Σ I_i | The "average intelligence" of a group |
| **Variance** | (1/n)Σ ‖I_i − centroid‖² | How spread out a group is |

### 2.3 Geometric Analysis — Shape Taxonomy

The shape of an I-vector polyhedron is **not random**. It encodes cognitive architecture. We propose a classification:

| Shape Class | Signature | Example | Interpretation |
|---|---|---|---|
| **Sphere** | All dims ≈ equal, low parity | Balanced generalist | Even investment across all capabilities |
| **Spike** | 1-2 dims >> rest, high parity | Math specialist | Deep investment in narrow capability |
| **Slab** | Top ring high, bottom ring low (or vice versa) | Technical-but-not-social | Systematic gap between capability families |
| **Crown** | Alternating high-low around the rings | Claude (L=9,M=8,S=5,K=1,N=7,A=9,P=8,E=7) | Strong on every other axis — complex trade-off pattern |
| **Teardrop** | Mostly high with 1-2 collapsed dims | Most frontier models (I_K≈1) | Missing capability drags overall shape |
| **Diamond** | Middle dims high, extremes low | Hypothetical balanced reasoner | Peaks in the center of each ring |

**Key insight:** Two models with similar ‖I‖ can have radically different shapes, which means radically different strengths. Shape classification is more informative than any single number.

### 2.4 Synergy — The Killer Feature

Given two entities A and B, their **synergy vector** is:

**S(A,B) = max(A_d, B_d) for each d**

This represents the combined capability of the pair — the best of both on every dimension. The **synergy gain** is:

**ΔS = ‖S(A,B)‖ − max(‖A‖, ‖B‖)**

High ΔS means the pair covers each other's weaknesses. This is the matchmaking metric.

**Complementarity score:**

**C(A,B) = 1 − cos(A,B)**

Low cosine similarity = high complementarity = they're good together because they're *different*.

**Optimal team of size k:** Find the subset of k entities that maximizes ‖S(team)‖. This is the core matching algorithm.

**Use cases:**

- "Which AI model should I pair with Claude for maximum coverage?"
- "Given my personal I-vector, which AI compensates my weaknesses best?"
- "Build me a 3-person team with maximal ‖S‖"
- "Which document requires which intelligence profile to understand?"

---

## 3. Interactive Dashboard — Build Spec

### Page: `/arena/compare/`

**User flow:**

1. User selects 2+ models from a checkbox list (or types a custom I-vector)
2. Dashboard instantly renders ALL comparison views:
   - Top row: Radar chart + 3D polyhedra side-by-side
   - Middle: Heatmap + parallel coordinates
   - Bottom: Numerical metrics table + scatter plot
3. Sidebar: full metric breakdown (cosine sim, distance, parity, entropy, synergy)
4. "Add to comparison" button — keeps adding models
5. "Match me" button — input your own scores, find your nearest/farthest/best-synergy model

### Page: `/arena/geometry/`

**Shape analysis dashboard:**

1. Shows each model's shape classification with visual
2. Clusters models by shape similarity
3. "What shape is optimal for [task]?" — maps tasks to ideal shape profiles
4. Historical shape evolution (when we have version data)

### Page: `/arena/synergy/`

**Synergy calculator:**

1. Select any pair → see synergy vector, gain, complementarity
2. "Build optimal team" — select pool, set team size, maximize coverage
3. Network visualization — all models as nodes, edges = synergy gain, thickness = complementarity
4. "Personal match" — input 8 self-assessment scores, get model recommendations

### Page: `/arena/api/`

**API documentation for the Intelligence Engine:**

```
GET  /api/v1/models                    → List all scored models
GET  /api/v1/models/{id}/vector        → Get I-vector + Elo
GET  /api/v1/compare?a={id}&b={id}     → Full comparison (all metrics)
GET  /api/v1/similarity?a={id}&b={id}  → Cosine similarity
GET  /api/v1/nearest?id={id}&k=5       → k nearest neighbors
GET  /api/v1/synergy?ids=a,b,c         → Synergy vector + gain
GET  /api/v1/match?vector=9,8,5,1,7,9,8,7  → Best match for custom vector
GET  /api/v1/shape/{id}                → Shape classification + metrics
GET  /api/v1/pareto                    → Pareto frontier models
POST /api/v1/score                     → Score a document/text → I-vector
```

---

## 4. Build Phases

### Phase 1 — Visual Dashboard (this week)

- [ ] Interactive radar chart (select 2-5 models, overlaid spider plot)
- [ ] Bar chart comparison (grouped bars, one group per dimension)
- [ ] Heatmap matrix (models × dims, color intensity)
- [ ] Numerical metrics table (cosine sim, distance, parity, entropy for selected pair)
- [ ] All as a single React/HTML page, embeddable in wiki

### Phase 2 — Geometric Analysis (next week)

- [ ] Shape classifier (input I-vector → shape class + visual)
- [ ] Parity/entropy/density calculations live in dashboard
- [ ] Scatter plot (any 2 dims as axes, bubble = Elo)
- [ ] Parallel coordinates plot
- [ ] Pareto frontier visualization

### Phase 3 — Synergy Engine (week 3)

- [ ] Synergy calculator (pair → synergy vector + gain + complementarity)
- [ ] "Match me" tool — input personal vector, get recommendations
- [ ] Optimal team builder (select pool, set k, maximize ‖S‖)
- [ ] Network graph visualization
- [ ] "Score this document" prototype

### Phase 4 — API + CogOS Integration (week 4+)

- [ ] FastAPI endpoints at engine.smarthub.my
- [ ] DuckDB backend for model vectors + historical data
- [ ] Rate-limited public tier (free, 100 req/day)
- [ ] Authenticated tier for agents/enterprises
- [ ] CogOS SDK — any AI can call the Intelligence Engine mid-conversation
- [ ] Webhook: "notify me when a new model enters my nearest-neighbor set"

---

## 5. Mathematical Foundation

All metrics derive from the I-vector space. The key equations:

**I-vector:** $\mathbf{I} = (I_L, I_M, I_S, I_K, I_N, I_A, I_P, I_{IE}, \ldots) \in \mathbb{R}^{n(e)}$

**Norm:** $\|\mathbf{I}\| = \sqrt{\sum_{d=1}^{8} I_d^2}$

**Cosine similarity:** $\cos(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$

**Complementarity:** $C(\mathbf{A}, \mathbf{B}) = 1 - \cos(\mathbf{A}, \mathbf{B})$

**Synergy vector:** $S(\mathbf{A}, \mathbf{B})_d = \max(A_d, B_d)$

**Synergy gain:** $\Delta S = \|S(\mathbf{A}, \mathbf{B})\| - \max(\|\mathbf{A}\|, \|\mathbf{B}\|)$

**Parity:** $P(\mathbf{I}) = \frac{\max_d I_d}{\min_d I_d}$

**Entropy:** $H(\mathbf{I}) = -\sum_{d=1}^{8} p_d \log_2 p_d$ where $p_d = \frac{I_d}{\sum_d I_d}$

**Density:** $\rho(\mathbf{I}) = \frac{\|\mathbf{I}\|}{\sqrt{8 \cdot 10^2}} = \frac{\|\mathbf{I}\|}{10\sqrt{8}}$

**Shape volume** (convex hull of 8 vertices): Computed numerically from the polyhedron geometry. Measures how much of ℝ³ the projected shape occupies.

---

## 6. Competitive Advantage

Why this wins:

1. **Nobody else has variable-dimensional intelligence vector (n=12 for humans)s.** LMSYS has Elo (1D). We have Elo + I-vec (9D effective). That's 9x the information.
2. **Shape analysis is novel.** No one is classifying AI models by geometric cognitive signature.
3. **Synergy is the matchmaking layer.** The moment you can say "pair Claude + DeepSeek for 98% dimension coverage," you're selling infrastructure.
4. **Self-assessment creates viral adoption.** "What's my I-vector?" is inherently shareable.
5. **Document scoring is the enterprise play.** "This legal brief requires I_L=9, I_M=7 to parse correctly" → now you're routing work.
6. **CogOS integration makes it a platform.** Every AI agent that uses the Intelligence Engine becomes a node in the RTSG network.

---

## 7. Revenue Model

| Tier | Price | Access |
|---|---|---|
| **Free** | $0 | 100 API calls/day, public model data, basic comparisons |
| **Pro** | $29/mo | Unlimited calls, synergy engine, custom vectors, team builder |
| **Enterprise** | $299/mo | Document scoring, CogOS integration, historical tracking, webhooks |
| **API Partner** | Custom | White-label, bulk scoring, embedded dashboards |

---

*This document is the strategic foundation. Phase 1 starts now.*

# Intelligence Metrics Dashboard

<style>
.df{position:relative;width:calc(100% + 1.6rem);margin:0 -.8rem;height:90vh;min-height:600px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08)}
.df iframe{width:100%;height:100%;border:none}
@media(max-width:768px){.df{height:92vh;min-height:500px;width:calc(100% + 1rem);margin:0 -.5rem}}
</style>

<div class="df"><iframe src="/wiki/arena/intelligence_dashboard.html" allowfullscreen loading="lazy"></iframe></div>

!!! tip "How to use"
    **Select models** in the top bar to include/exclude from all charts. Switch between **Compare**, **Geometry**, and **Synergy** tabs.

---

## Tabs

### Compare (Phase 1)
Radar chart, bar chart, heatmap, parallel coordinates, scatter plot (pick any 2 dims), Elo vs ‖I‖ plot, and a full pairwise numerical metrics table (cosine similarity, Euclidean distance, Manhattan distance, complementarity, synergy gain, dominance count).

### Geometry (Phase 2)
Shape classification for every model (Sphere, Spike, Slab, Crown, Teardrop, Diamond), parity vs entropy scatter, density distribution, and full geometry table with all computed properties.

### Synergy (Phase 3)
Top synergy pairs, top complementary pairs, synergy matrix heatmap, **Match Me** tool (enter your own 8 scores and find your nearest model + best synergy partner), and optimal team builder (find the best team of 2, 3, or 4 models for maximum dimension coverage).

---

## Mathematical Foundations

All metrics derive from the I-vector: $\mathbf{I} \in \mathbb{R}^{n(e)}$

See the full [Metrics Roadmap](metrics_roadmap.md) for equations, API spec, and strategic vision.

[← Arena Index](index.md) · [3D Arena →](intelligence_arena_mar2026.md) · [Roadmap →](metrics_roadmap.md)

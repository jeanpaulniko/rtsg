---
title: "IdeaRank"
---

# IdeaRank

**The algorithm that identifies the most valuable ideas in any concept graph.**

IdeaRank is RTSG's core ranking algorithm — a generalization of PageRank to the multi-dimensional intelligence space. Where PageRank measures link importance in a web graph, IdeaRank measures *cross-dimensional conceptual importance* in the RTSG concept graph.

---

## The Core Insight

An idea's value is not determined by how often it is cited. It is determined by **how many different dimensions of intelligence it activates simultaneously**.

A mathematical proof that is purely formal (dim = 1) is less valuable than a mathematical proof that also illuminates biological structure, has linguistic elegance, and reveals something about consciousness (dim = 4+). The second proof sits higher in IdeaRank regardless of citation count.

This is why *synthesis* is more valuable than *specialization* in the RTSG framework — synthesizing ideas across dimensions creates high-dim(n) nodes that connect previously disconnected regions of the concept graph.

---

## Algorithm

### Inputs

- Concept graph G = (V, E, W)
- I-vector dimension weights α ∈ ℝⁿ⁽ᵉ⁾ (n=12 for humans, variable per entity) (task-specific)
- Damping factor d ∈ (0,1) (typically 0.85, same as PageRank)
- Threshold vector θ ∈ ℝⁿ⁽ᵉ⁾ (n=12 for humans, variable per entity)

### IdeaRank Score

For node n ∈ V:

$$\text{IR}(n) = (1-d) + d \sum_{m \in \text{In}(n)} \frac{\text{IR}(m) \cdot \mathbf{S}(m,n)}{|\text{Out}(m)|}$$

where **S**(m,n) = cross-dimensional synergy coefficient between m and n:

$$\mathbf{S}(m,n) = \frac{1}{8}\sum_{k=1}^8 \alpha_k \cdot \mathbb{1}[\mathbf{I}_k(m) \geq \theta_k \text{ and } \mathbf{I}_k(n) \geq \theta_k]$$

Nodes that share activation in many I-vector dimensions have high synergy; nodes that share activation in only one dimension have low synergy.

### Convergence

IdeaRank converges in O(|E| log |V|) iterations (Theorem 8). The spectral gap Δ of the normalized adjacency matrix determines the rate: faster convergence when Δ is large.

### Top Layer

After convergence, the top-layer nodes are those with IR(n) above the 90th percentile. These are the ideas that connect everything — the structural joints of the concept graph.

---

## Properties

### Cross-Dimensional Amplification

A node that activates 4 dimensions has IdeaRank amplification factor of approximately 4× over a node that activates 1 dimension, everything else equal. This is the mathematical formalization of why interdisciplinary ideas are more powerful than single-domain ones.

### Frontier Detection

Nodes with high dim(n) but currently low IR score are **frontier ideas** — they have the structure of high-value nodes but haven't yet diffused through the graph. These are the most valuable targets for development and publication.

### Algorithmic Frontier Expansion

IdeaRank can run in reverse — instead of ranking existing nodes, it generates new candidate nodes:

```python
def expand_frontier(G, top_nodes, k=2):
    for combo in combinations(top_nodes, k):
        candidate = cross_project(combo)  # combine across dimensions
        if is_novel(candidate, G) and is_consistent(candidate):
            if idearank_score(candidate) > threshold:
                yield candidate
```

This generates pre-validated frontier ideas — combinations of top-layer nodes that, if added to the graph, would themselves become top-layer nodes. It is the formal basis for AI-assisted research frontier expansion.

---

## Intelligence Fingerprinting

**From corpus to I-vector:** Given any corpus C(ξ) (papers, code, conversation, art), recover **I**(ξ):

1. Build local concept graph G(C) from C
2. Compute IdeaRank on G(C)
3. Extract top-layer nodes
4. Project onto the 8 I-vector dimensions:
   $$\mathbf{I}_k(\xi) = \sum_{n \in \text{top}(G(C))} \mathbb{1}[\mathbf{I}_k(n) \geq \theta_k] \cdot \text{IR}(n)$$
5. Normalize to [0, 10]

**Result:** **I**(ξ) — the cognitive fingerprint of ξ.

This is more robust than self-report personality instruments. It recovers the actual cognitive structure from behavioral output, not what ξ thinks about themselves.

**Temporal dating:** Compare **I**(ξ) against G_collective at different historical time periods to find ξ's temporal position in intellectual history — which era's concepts dominate their thinking.

---

## Optimal Cognitive Assembly Formation

Given a mission with objective weight vector w ∈ Δⁿ⁻¹ (a probability distribution over I-vector dimensions), find the optimal assembly A* of agents:

$$A^* = \arg\max_{A \subseteq \mathcal{A}} \mathbf{w} \cdot \mathbf{I}(A)$$

subject to |A| ≤ k (assembly size constraint).

The optimal assembly maximizes the synergy-weighted I-vector sum along the mission's required dimensions. This is solvable by greedy insertion (O(k·|𝒜|)) with approximation ratio 1 - 1/e for submodular objectives.

**Application to RTSG BuildNet:** The optimal assembly for the GRF essay (requiring I_M, I_S, I_L) is Gemini (I_M = 8.8) + Claude (I_L = 8.8) + Niko (all = 8.8+). Verified by arena scores.

---

## Comparison to PageRank

| Property | PageRank | IdeaRank |
|---|---|---|
| Graph type | Web/citation | Concept/knowledge |
| Edge weight | Link count | Cross-dimensional synergy |
| Node score | Link importance | Multi-dimensional conceptual value |
| Personalization | Topic vector | Mission weight vector w |
| Reverse mode | N/A | Frontier expansion (generate new nodes) |
| Application | Web search | Research, education, assembly formation |

---

## Live Implementation

IdeaRank runs on the knowledge graph at `engine.smarthub.my/kg/`:

```http
POST engine.smarthub.my/kg/idearank
{
  "graph_id": "rtsg-collective",
  "alpha": [1,1,1,1,1,1,1,1],
  "top_k": 20
}

POST engine.smarthub.my/kg/fingerprint
{
  "corpus": "text of any document",
  "return_vector": true,
  "temporal_dating": true
}

POST engine.smarthub.my/kg/expand_frontier
{
  "k": 2,
  "threshold": 0.8,
  "filter": "novel_only"
}
```

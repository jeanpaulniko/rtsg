---
title: "Filter Algebra — The Category of Cognitive Filters"
nav_title: "Filter Algebra"
version: "1.0.0"
last_updated: "2026-03-09"
status: "ACTIVE — formalizes Part V of definitions as algebraic structure"
---

# Filter Algebra — The Category of Cognitive Filters

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    The 5 filter species were defined in the monograph and referenced throughout RTSG. This page gives them a precise algebraic structure: a **filtered monoidal category** with explicit composition rules, non-commutativity proofs, and connection to P vs NP (via filter complexity). Built for computation, not just theory.

---

## 1. The Five Species

Each filter is a smooth endomorphism $F : \mathbb{R}^{n(e)}_{\geq 0} \to \mathbb{R}^{n(e)}_{\geq 0}$ acting on the intelligence vector $\mathbf{I}$.

| Species | Symbol | Timescale | Algebraic type | Invertible? |
|---|---|---|---|---|
| **Ceiling** | $F_{\text{ceil}}$ | Evolutionary ($10^6$ yr) | Diagonal, entries $\leq 1$ | No (idempotent: $F^2 = F$) |
| **Developmental** | $F_{\text{dev}}$ | Lifetime ($10^1$ yr) | Lower-triangular (causal) | No (monotone increasing, saturates) |
| **Cultural** | $F_{\text{cult}}$ | Social ($10^0$ yr) | Full matrix, $K$-coupled | Context-dependent |
| **State** | $F_{\text{state}}$ | Hormonal ($10^{-1}$ hr) | Diagonal (Hadamard gate) | Yes (multiply by reciprocal) |
| **Attentional** | $F_{\text{att}}$ | Neural ($10^{-3}$ s) | Simplex projection | No (rank-deficient) |

The canonical pipeline composes right to left:

$$\boxed{\mathbf{I}_{\text{eff}} = F_{\text{att}} \circ F_{\text{state}} \circ F_{\text{cult}} \circ F_{\text{dev}} \circ F_{\text{ceil}}(\mathbf{I}_{\text{raw}})}$$

---

## 2. The Category $\mathsf{Filt}$

### 2.1 Objects

The objects of $\mathsf{Filt}$ are **pipeline stages**:

$$\text{Ob}(\mathsf{Filt}) = \{0, 1, 2, 3, 4, 5\}$$

- Stage 0: raw capacity $\mathbf{I}_{\text{raw}}$
- Stage 1: ceiling-bounded
- Stage 2: developmentally shaped
- Stage 3: culturally modulated
- Stage 4: state-gated
- Stage 5: attention-projected = $\mathbf{I}_{\text{eff}}$

### 2.2 Morphisms

$\text{Hom}(k, k+1) = \{F : \mathbb{R}^{n}_{\geq 0} \to \mathbb{R}^{n}_{\geq 0} \mid F \text{ is species } k+1\}$

Composition: $F \circ G \in \text{Hom}(j, k+1)$ whenever $G \in \text{Hom}(j, k)$ and $F \in \text{Hom}(k, k+1)$.

The category is **skeletal** (no non-trivial isomorphisms between stages) and **thin in the forward direction** (the canonical filter at each stage is essentially unique up to parameters).

### 2.3 The Monoidal Structure

$\mathsf{Filt}$ is a **monoidal category** under composition:

- Tensor product: $F \otimes G$ applies $F$ and $G$ to disjoint dimension subsets (parallel filtering)
- Unit: identity filter $\text{Id}$
- Associator: $(F \otimes G) \otimes H \cong F \otimes (G \otimes H)$ (trivial, direct sum decomposition)

---

## 3. Algebraic Properties of Each Species

### 3.1 Ceiling Filter $F_{\text{ceil}}$

$$F_{\text{ceil}}(\mathbf{I})_t = \min(I_t, c_t), \qquad c_t \in \mathbb{R}_{>0}$$

**Properties:**
- Diagonal (acts dimension-by-dimension)
- Idempotent: $F_{\text{ceil}}^2 = F_{\text{ceil}}$
- Non-expansive: $\|F(\mathbf{I})\| \leq \|\mathbf{I}\|$
- The ceiling vector $\mathbf{c}$ is species-dependent (humans: $n=12$, current AI: $n$ varies)
- **Not a linear map** (min is nonlinear). Linearization: $F_{\text{ceil}} \approx \text{diag}(\sigma(c_t - I_t))$ where $\sigma$ is a sigmoid.

### 3.2 Developmental Filter $F_{\text{dev}}$

$$F_{\text{dev}}(\mathbf{I}, t)_s = I_s \cdot \left(1 - e^{-\alpha_s (t - t_{0,s})}\right)^+ \cdot \prod_{r \prec s} \theta(I_r - \tau_r)$$

**Properties:**
- **Lower-triangular in the developmental partial order** $\prec$: dimension $s$ only activates after prerequisite dimensions $r \prec s$ pass threshold $\tau_r$
- Monotonically increasing in developmental time $t$
- Saturates: $F_{\text{dev}} \to \text{Id}$ as $t \to \infty$
- **Non-commutative with cultural**: developmental order constrains what cultural content can be absorbed. A child can't absorb abstract algebra before concrete operations.

### 3.3 Cultural Filter $F_{\text{cult}}$

$$F_{\text{cult}}(\mathbf{I}) = M_{\text{cult}} \mathbf{I}, \qquad M_{\text{cult}} \in \mathbb{R}^{n \times n}_{\geq 0}$$

**Properties:**
- **Full matrix** — cross-type couplings. A culture that values linguistic intelligence ($I_L$) can suppress spatial ($I_S$) through resource competition.
- $(M_{\text{cult}})_{st} = K_{st}^{\text{cult}}$: the cultural component of the K-matrix
- Context-loadable: different $M_{\text{cult}}$ for work, family, solitude (filter modularity)
- **Non-commutative with state**: cultural norms about emotional expression modulate how state-gating works. Stoic culture: $M_{\text{cult}}$ suppresses $I_{IE}$-dependent cross-terms.

### 3.4 State Filter $F_{\text{state}}$

$$F_{\text{state}}(\mathbf{I}) = \mathbf{I} \odot \boldsymbol{\eta}(\Psi), \qquad \eta_t \in (0, 1]$$

**Properties:**
- **Diagonal** (Hadamard/element-wise product)
- $\boldsymbol{\eta}$ depends on psychophysiological state vector $\Psi$ (cortisol, sleep, arousal, etc.)
- **Invertible**: $F_{\text{state}}^{-1}(\mathbf{I}) = \mathbf{I} \oslash \boldsymbol{\eta}$ (element-wise division)
- Only filter species that is generically invertible
- Fatigue: $\eta_t \to 0$ as sleep debt increases. Flow: $\eta_t \to 1$ for task-relevant dimensions.

### 3.5 Attentional Filter $F_{\text{att}}$

$$F_{\text{att}}(\mathbf{I}) = \mathbf{I} \odot \boldsymbol{\alpha}, \qquad \boldsymbol{\alpha} \in \Delta^{n-1} \text{ (simplex)}$$

**Properties:**
- **Simplex-constrained**: $\sum_t \alpha_t = 1$, $\alpha_t \geq 0$
- Rank-deficient: projects onto a low-dimensional subspace of intelligence space
- Dynamics: $\dot{\alpha}_t = \alpha_t(u_t - \bar{u})$ (replicator equation on the attention simplex)
- **Fastest timescale**: millisecond switching
- **Not invertible**: once attention collapses, the unattended dimensions are gone

---

## 4. Non-Commutativity

### 4.1 Theorem: $F_{\text{cult}} \circ F_{\text{dev}} \neq F_{\text{dev}} \circ F_{\text{cult}}$

**Proof:** Let $\mathbf{I} = (3, 1)$ in a 2D toy model. Let $F_{\text{dev}}$ have threshold $\tau_2 = 2$ (dimension 2 requires dimension 1 to exceed 2) and $F_{\text{cult}}$ swap dimensions ($M_{\text{cult}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$).

$F_{\text{dev}} \circ F_{\text{cult}}(\mathbf{I}) = F_{\text{dev}}(1, 3)$. Now dim 1 has value 1, which is below $\tau_2 = 2$, so dim 2 is gated: output $(1, 0)$.

$F_{\text{cult}} \circ F_{\text{dev}}(\mathbf{I}) = F_{\text{cult}}(3, 3)$. Dim 1 was 3 > $\tau_2$, so dim 2 passes. Then swap: output $(3, 3)$.

$(1, 0) \neq (3, 3)$. $\square$

**Physical meaning:** A culture that swaps what's valued (e.g., a society that prizes kinesthetic over linguistic) produces different developmental outcomes depending on whether cultural exposure happens before or after developmental gating.

### 4.2 Theorem: $F_{\text{att}} \circ F_{\text{state}} \neq F_{\text{state}} \circ F_{\text{att}}$

**Proof:** Attention is simplex-constrained. State-gating before attention changes which dimensions dominate the simplex allocation. Attention before state-gating locks in allocations that may become suboptimal after state changes. Concretely: coffee ($F_{\text{state}}$: boost $I_M$) after focusing on writing ($F_{\text{att}}$: $\alpha_L \gg \alpha_M$) doesn't retroactively reallocate attention. $\square$

### 4.3 The Non-Abelian Structure

The filter monoid $\mathcal{F} = \langle F_{\text{ceil}}, F_{\text{dev}}, F_{\text{cult}}, F_{\text{state}}, F_{\text{att}} \rangle$ is:

- **Non-abelian** (§4.1, §4.2)
- **Not a group** ($F_{\text{ceil}}, F_{\text{dev}}, F_{\text{att}}$ are non-invertible)
- **A monoid with zero** (the zero filter $F_0 : \mathbf{I} \mapsto \mathbf{0}$ absorbs: $F \circ F_0 = F_0$)
- **Partially ordered** by the pipeline order $\text{ceil} \prec \text{dev} \prec \text{cult} \prec \text{state} \prec \text{att}$

---

## 5. The Kernel Composition Lemma

### 5.1 Statement

For any composition $G = F_k \circ \cdots \circ F_1$:

$$\ker(G) \supseteq \ker(F_1)$$

Information loss is **monotonically non-decreasing** through the pipeline. Each filter can only maintain or increase the kernel. No filter can recover information lost by a previous filter (except $F_{\text{state}}^{-1}$, which only reverses its own gating).

### 5.2 Effective Dimension

Define the effective dimension of $\mathbf{I}$ after filtering:

$$d_{\text{eff}}(F(\mathbf{I})) = \#\{t : F(\mathbf{I})_t > \epsilon\}$$

Then: $d_{\text{eff}}(G(\mathbf{I})) \leq d_{\text{eff}}(F_1(\mathbf{I})) \leq n(e)$

The pipeline is a **dimension funnel**. Raw capacity $n(e) = 12$ for humans. Effective output dimension after all filters: typically 2–4 in any given moment (attention bottleneck).

---

## 6. Connection to P vs NP

### 6.1 Filter Complexity

Define the **filter complexity** of a computation as the minimum pipeline length needed:

$$C_{\mathcal{F}}(x) = \min\{k : \exists F_1, \ldots, F_k \in \mathcal{F} \text{ s.t. } F_k \circ \cdots \circ F_1(x) = \text{solution}\}$$

### 6.2 The Verification/Generation Gap

**Conjecture:** For NP-complete problems, the filter chain for verification is polynomial:

$$C_{\mathcal{F}}(\text{verify}(x, w)) = O(\text{poly}(|x|))$$

but the chain for generation is exponential:

$$C_{\mathcal{F}}(\text{find}(x)) = \Omega(2^{|x|^c})$$

The gap arises because verification uses $F_{\text{att}}$ (cheap simplex projection: check each clause), while generation requires $F_{\text{cult}}^{-1}$ (exponential search through the non-invertible cultural filter's kernel to find the pre-image).

### 6.3 Non-Commutativity as Separation Witness

The commutator $[F_{\text{verify}}, F_{\text{generate}}] \neq 0$ witnesses the separation:

$$F_{\text{verify}} \circ F_{\text{generate}} \neq F_{\text{generate}} \circ F_{\text{verify}}$$

Verification after generation is polynomial (check the output). Generation after verification is meaningless (you can't reverse the funnel). The non-commutativity is **essential** — no rearrangement of the pipeline avoids the exponential bottleneck.

⚠ This is the weakest Millennium connection. It requires proving that the filter monoid's non-commutativity implies a complexity-theoretic lower bound, which is a substantial gap.

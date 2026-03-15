---
title: "Gap 3 Attack — H¹ and H² of the SM BRST Complex"
nav_title: "Gap 3 Attack"
version: "1.0.0"
last_updated: "2026-03-08"
status: "ACTIVE ATTACK — multi-agent deployment"
---

# Gap 3 Attack — $H^1$ and $H^2$ at the Standard Model BRST Point

**@B_Niko · Sole Author · Deployed by @D_Claude**

!!! danger "Active Attack"
    Four agents deployed simultaneously. Results go to `agents/ai_notes.md`. Contradictions welcome — they sharpen the result.

---

## 1. The Question

The Standard Model defines a specific BRST operator $s_{SM} = s_0 + s_1 + s_2$ on the extended state space $\Gamma$ (fields + ghosts + antighosts + Nakanishi-Lautrup auxiliaries) for the gauge group:

$$G_{SM} = \text{Diff}(M) \times SU(3)_c \times SU(2)_L \times U(1)_Y$$

The CS mechanics framework ([cs_mechanics.md](../rtsg/cs_mechanics.md)) identifies:

- **$H^1(s_{SM})$** = tangent space to $\mathcal{M}_{CS}$ at the SM point = **directions the instantiation rule can evolve** = possible BSM physics
- **$H^2(s_{SM})$** = obstruction space = **forbidden directions** = BSM physics that is self-contradictory at second order

**If $H^1 = 0$:** The SM is a rigid point in $\mathcal{M}_{CS}$. No continuous deformations possible. No new gauge forces. The SM is the unique consistent instantiation rule (up to discrete choices).

**If $H^1 \neq 0$:** There exist directions in which CS can evolve. These correspond to possible extensions of the SM — new gauge sectors, new stages in the instantiation cascade, BSM physics that is consistent with BRST.

**If $H^2 \neq 0$:** Some infinitesimal deformations hit obstructions at second order. These are BSM directions that *look* consistent at first order but fail. This constrains which extensions of the SM are actually realizable.

---

## 2. What Is Known (Literature)

### 2.1 BRST Cohomology of Yang-Mills

For a Yang-Mills theory with gauge group $G$ on a manifold $M$, the BRST cohomology is related to the Lie algebra cohomology of $\mathfrak{g}$:

$$H^*(s) \cong H^*(\mathfrak{g}, \mathcal{F})$$

where $\mathcal{F}$ is the space of local functionals (field-dependent). This is the content of the **descent equations** (Stora-Zumino).

### 2.2 Anomalies as $H^1$

The chiral anomaly is an element of $H^1(s)$: it is a BRST-closed functional (satisfies the Wess-Zumino consistency condition $s \mathcal{A} = 0$) that is not BRST-exact. The anomaly cancellation condition in the SM ($\sum Y^3 = 0$ per generation) is the statement that this element of $H^1$ vanishes for the SM field content.

**Key result (Barnich-Brandt-Henneaux, 1994):** For Yang-Mills + matter in 4D, the local BRST cohomology $H^{g,n}(s|d)$ (ghost number $g$, form degree $n$) is fully classified:

- $H^{0,4}(s|d)$ = gauge-invariant Lagrangians (counterterms, deformations)
- $H^{1,4}(s|d)$ = candidate anomalies
- $H^{-1,4}(s|d)$ = global symmetries (Noether currents)

### 2.3 Deformations of BRST

The **deformation problem** for BRST (Barnich-Henneaux, 1993) asks: given $s$ with $s^2 = 0$, what are the consistent deformations $s \to s + g s_1 + g^2 s_2 + ...$?

The first-order deformation $s_1$ must satisfy:

$$s s_1 + s_1 s = 0 \quad \Leftrightarrow \quad [s_1] \in H^1(s)$$

The obstruction to extending to second order:

$$[s_1, s_1] \in H^2(s)$$

If $[s_1, s_1] = 0$ in $H^2$, the deformation extends. If not, it's obstructed.

---

## 3. Agent Assignments

### @D_Claude — Algebraic Structure

Compute $H^1(s_{SM})$ using the Barnich-Brandt-Henneaux classification. Specifically:
1. What is $H^{0,4}(s|d)$ for the SM field content? This gives the space of consistent deformations of the SM Lagrangian.
2. Does the graded structure $s = s_0 + s_1 + s_2$ introduce additional cohomology beyond the ungraded case?
3. What is the relationship between $H^1(s_{SM})$ and the space of consistent gauge group extensions $G_{SM} \to G_{SM} \times G'$?

### @D_GPT — Obstruction Computation

Compute $H^2(s_{SM})$ or bound it. Specifically:
1. For each candidate $[s_1] \in H^1$, compute the obstruction $[s_1, s_1] \in H^2$.
2. Use the Barnich-Henneaux deformation theory to determine which BSM extensions are obstructed.
3. Is GUT unification ($SU(3) \times SU(2) \times U(1) \to SU(5)$) an unobstructed deformation? Is $SO(10)$?
4. What about adding a $U(1)'$ (dark photon)? Extra $SU(2)$?

### @D_Gemini — Deep Think: Spectral Sequence

Use the spectral sequence from [graded_brst.md](../rtsg/graded_brst.md) Prop 2:
1. The filtration $F^p\Gamma$ gives a spectral sequence $E_r \Rightarrow H^*(s)$ that degenerates at $E_3$.
2. Compute $E_1, E_2, E_3$ pages explicitly for the SM.
3. Does the spectral sequence structure constrain $H^1$ and $H^2$ beyond what the ungraded computation gives?
4. **Key question:** Does the graded BRST decomposition introduce *new* obstructions not present in the standard (ungraded) BRST cohomology?

### @D_Grok — Literature Search + Numerical

1. Search for existing computations of BRST deformation cohomology for the SM. Key authors: Barnich, Brandt, Henneaux, Boulanger, Bekaert.
2. Search for any computation of $H^2$ for $SU(3) \times SU(2) \times U(1)$ specifically.
3. Compile a table of all known consistent deformations of the SM BRST complex from the literature.
4. Flag any results that contradict or confirm the RTSG graded structure.

⚠ **@D_Grok: Do not fabricate citations. Provide URLs/DOIs for every claim. If you cannot find a source, say so.**

---

## 4. Expected Outputs

Each agent posts results to `agents/ai_notes.md` under:

```
## 2026-03-08 · @D_{agent} · Gap 3 Attack — {subtopic}
```

**Desired format:**
- State the result clearly (theorem, computation, or literature finding)
- Mark confidence: PROVED / COMPUTED / LITERATURE / CONJECTURE
- Flag contradictions with other agents' results
- Flag any result that "proves too much" (if $H^1 = 0$ trivially, something is wrong)

---

## 5. What Victory Looks Like

**Best case:** Explicit computation of $\dim H^1(s_{SM})$ and $\dim H^2(s_{SM})$, with the graded BRST spectral sequence showing whether the staging introduces new constraints.

**Good case:** Bounds on $H^1$ and $H^2$ sufficient to make a prediction (e.g., "the SM admits exactly $k$ independent deformation directions" or "the SM is rigid").

**Minimum viable:** Literature compilation showing the current state of knowledge, with the RTSG graded structure identified as the novel contribution that could change the answer.

---

## 6. Connection to RTSG

If $H^1(s_{SM}) = 0$: The SM instantiation rule is the unique consistent one. No new gauge forces. No new stages. The partition $2+1+1$ of $(S^2)^4_{\text{int}}$ is rigid. **This would be a prediction of RTSG** — the framework predicts that no BSM gauge physics exists.

If $H^1(s_{SM}) \neq 0$: There exist BSM directions. These correspond to activating additional $S^2$ factors from the infinite tail of $\Omega = (S^2)^\infty$. The directions in $H^1$ tell us exactly which extensions are consistent. **This constrains BSM model-building from RTSG principles.**

Either way, it's a result.

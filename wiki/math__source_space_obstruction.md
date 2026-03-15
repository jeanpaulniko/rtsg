---
title: "Source Space Obstruction — Bisimulation Selection of BSM Physics"
nav_title: "Source Space Obstruction"
version: "1.0.0"
last_updated: "2026-03-08"
status: "CONJECTURE — the next frontier after Gap 3"
---

# Source Space Obstruction — Bisimulation Selection of BSM Physics

**@B_Niko · Sole Author**

!!! info "Origin"
    This page emerged from the Gap 3 attack (2026-03-08), where all four network agents (@D_Claude, @D_GPT, @D_Gemini, @D_Grok) converged on the same result: **local algebraic BRST cohomology cannot constrain BSM physics.** The SM is locally extensible. If RTSG predicts any selection principle on BSM gauge groups, it must be **global and topological**, not local and algebraic. @D_Gemini proposed the pivot to source space topology. This page develops that proposal.

---

## 1. What We Proved (Gap 3)

The full Gap 3 computation established:

| Result | Proved by | Method |
|---|---|---|
| $H^2_{CE}(\mathfrak{g}_{SM}) = 0$ (gauge algebra rigid) | @D_GPT | Whitehead's lemmas |
| $d_2 \equiv 0$ for covariant deformations | @D_Gemini | Cartan's magic formula |
| BSM = extensions, not deformations | @D_GPT | BBH classification |
| Graded BRST adds no new obstructions on $M$ | All agents | Convergence |

**Bottom line:** Local algebraic BRST on target space $M$ is exhausted. It permits all covariant BSM extensions. Any selection principle must come from elsewhere.

---

## 2. The Source Space Selection Principle

### 2.1 The Proposal

In standard QFT, gauge groups are freely assigned — you choose a principal $G$-bundle over $M$ and build the theory. Nothing in the local BRST formalism prevents you from choosing any compact Lie group.

In RTSG, gauge groups are NOT free choices. They are the **output of the instantiation cascade** from source space $\Omega = (S^2)^\infty$. A gauge group $G$ is physically realized iff it corresponds to an actual quotient of Aut$(\Omega)$ that passes the BRST filter $H^0(s)$ and the bisimulation quotient $QS/\!\sim_{bisim}$.

### 2.2 Two Levels of Constraint

| Level | What it constrains | Where it lives | Status |
|---|---|---|---|
| **Local algebraic** (BRST on $M$) | Anomaly cancellation, perturbative consistency | Target space $M$ | Permissive ($d_2 = 0$) |
| **Global topological** (bisimulation on $\Omega$) | Which $S^2$ factors can activate | Source space $\Omega$ | **Unknown — this is the frontier** |

The local level is solved (Gap 3). The global level is the open problem.

### 2.3 What Global Bisimulation Selection Might Look Like

For a new $S^2$ factor from $\Omega$ to activate (producing a new gauge sector), it must:

1. **Be BRST-compatible** with the existing $s = s_0 + s_1 + s_2$ — the enlarged complex $s' = s + s_{\text{new}}$ must satisfy $(s')^2 = 0$. This is local and always satisfiable for a consistent gauge theory (Gap 3 proved this).

2. **Be bisimulation-compatible** with the existing quotient $PS = QS/\!\sim_{bisim}$. The new gauge sector must not destabilize the bisimulation equivalence classes that define spacetime points. Adding a gauge field changes the relational structure of QS — the new relations must be compatible with the existing bisimulation.

3. **Survive the geometric condensate** — the new sector must be compatible with the Stage 0 condensate $W_0$ (spacetime geometry). This is automatically true for diff-covariant fields (which is all of them, by Gap 3), but may impose additional constraints at the non-perturbative level.

### 2.4 The Analogy to Global Anomalies

Local anomaly cancellation ($\sum Y^3 = 0$) is necessary but not sufficient. The Witten $SU(2)$ anomaly is a GLOBAL consistency condition invisible to perturbation theory.

Similarly, local BRST consistency ($d_2 = 0$, anomaly-free) may be necessary but not sufficient for physical realization. The bisimulation quotient is a GLOBAL consistency condition invisible to local BRST cohomology.

**Conjecture (Source Space Selection Principle):** *Not all locally consistent gauge extensions of the SM can be physically realized via the instantiation cascade from $\Omega = (S^2)^\infty$. The set of realizable extensions is constrained by the topology of the bisimulation quotient — specifically, by the requirement that new $S^2$ factor activation must be compatible with the existing quotient structure $PS = QS/\!\sim_{bisim}$.*

---

## 3. What Would Prove or Kill This

### To prove it:
- Show that the bisimulation quotient $QS/\!\sim_{bisim}$ has nontrivial topology (i.e., $\pi_n(PS)$ depends on which $S^2$ factors are active)
- Show that activating a new $S^2$ factor changes $\pi_n(PS)$ in a way that's inconsistent with the existing geometric condensate
- Derive a concrete constraint: e.g., "the SM with $4$ internal $S^2$ factors is the unique bisimulation-stable configuration" or "at most $k$ additional factors can activate"

### To kill it:
- Show that bisimulation quotient is insensitive to the number of active $S^2$ factors
- Show that any locally consistent extension automatically passes the global bisimulation test
- Find a physical realization of a BSM gauge group that should be forbidden but isn't

---

## 4. Connection to Existing RTSG

- **[Stage 0 Gravity](../rtsg/stage0_gravity.md):** The geometric condensate $W_0$ defines the existing bisimulation structure. New gauge sectors must be compatible with it.
- **[Graded BRST](../rtsg/graded_brst.md):** The staged instantiation cascade is real physics. The source space selection principle would constrain which future stages can activate.
- **[CS Mechanics](../rtsg/cs_mechanics.md):** The global Maurer-Cartan equation on $\mathcal{M}_{CS}$ (not the local one on $M$) is where the obstruction lives — if it exists.
- **[Source Space Gauges](source_space_gauges.md):** The $2+1+1$ partition of $(S^2)^4_{int}$ may be bisimulation-locked, not just empirically selected.
- **[Horizon Bisimulation](../rtsg/horizon_bisimulation.md):** The bisimulation divergence rate $\kappa$ already has nontrivial topology at horizons. This machinery may extend to gauge sector activation.

---

## 5. Status

**CONJECTURE.** The most important open problem in RTSG theoretical physics as of 2026-03-08. The local algebraic avenue is exhausted. The global topological avenue is the frontier.

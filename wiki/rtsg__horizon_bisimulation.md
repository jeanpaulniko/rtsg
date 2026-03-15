---
title: "Horizon Bisimulation — Formal Paper"
version: "1.0.0"
last_updated: "2026-03-06"
status: "FORMAL — LaTeX compiled, 11 pages"
---

# The Horizon as Bisimulation Boundary: Surface Gravity as Relational Divergence Rate

**Jean-Paul Niko** · RTSG Working Paper · March 2026

!!! success "Status: Formalized"
    Full LaTeX paper compiled (11 pages, 0 errors). Contains definitions, propositions, theorems with proofs, and clearly separated conjectures. Available as PDF.

---

## Summary of Results

| Result | Status | Section |
|---|---|---|
| λ_bis = κ (Schwarzschild) | **Theorem 3.3** — Proven | §3 |
| λ_bis = κ^Kerr | **Proposition 5.1** — Proven | §5 |
| Horizon = exact bisimulation boundary | **Corollary 4.3** — Proven | §4 |
| Extremal: λ_bis = 0 | **Proposition 5.1** — Proven | §5 |
| t_kin = S/λ_bis interpretation | **Proposition 7.1** — Heuristic | §7 |
| Information preservation via bisimulation | **Conjecture 6.1** — Open | §6 |

## Key Definitions

**Accessible Pointed Graph (APG):** Triple (N, E, p) — nodes, directed edges (membership), root. Under AFA, every APG has a unique decoration into the set-theoretic universe.

**Bisimulation:** Relation R between two APGs where each transition in one graph can be matched by a transition in the other, and vice versa. Under AFA, two sets are equal iff bisimilar (Aczel's Solution Lemma).

**ε-Bisimulation:** Metric refinement — bisimulation that tolerates distance ε between matched nodes. The bisimulation distance d_bis is the infimum of ε over all ε-bisimulations.

**Bisimulation Divergence Rate:**

$$\lambda_{\rm bis} := \lim_{T\to\infty} \frac{1}{T} \ln \frac{d_{\rm bis}(T)}{d_{\rm bis}(0)}$$

## Main Theorem

**Theorem 3.3 (Surface Gravity as Bisimulation Divergence Rate):** For the Schwarzschild horizon with standard asymptotic Killing normalization:

$$\lambda_{\rm bis} = \kappa = \frac{1}{4M}$$

**Proof sketch:** Horizon-straddling null geodesics at displacement δ generate sub-APGs whose bisimulation distance grows as d_bis(T) = δ e^{κT}. This follows from the Rindler approximation: both sides of the horizon share the same local causal structure, differing only by the sign of the proper distance ρ. The Rindler reflection ρ → −ρ provides the initial exact bisimulation; the exponential peeling U ∝ −e^{−κu} provides the divergence rate.

## Corollary: Horizon Uniqueness

The event horizon is the **unique** codimension-1 surface where interior and exterior sub-APGs are exactly bisimilar at T = 0 and diverge at rate κ for T > 0. No other surface has the Rindler reflection symmetry that provides the initial exact bisimulation.

## Kerr Extension

$$\lambda_{\rm bis}^{\rm Kerr} = \kappa^{\rm Kerr} = \frac{\sqrt{1-a_*^2}}{2M(1+\sqrt{1-a_*^2})}$$

At extremality (a* → 1): λ_bis → 0. The interior and exterior remain perpetually bisimilar. This is consistent with the third law (T_H = 0, no Hawking radiation) — the bisimulation never diverges, so there is no thermal particle creation.

## Information Conjecture

**Conjecture 6.1:** For any finite-dimensional observable O computable from the exterior APG, there exists a bisimilar observable Õ computable from the interior APG. The Page curve is computable entirely from the boundary APG via the bisimulation relation.

This is a precise mathematical formulation of holographic complementarity. NOT proven — stated as a target.

## Connection to the GRF Essay

The kinematic clock t_kin = S/κ = S/λ_bis is the timescale at which the bisimulation divergence has "explored" all e^S distinguishable relational states on the horizon. The dressing factor C_Page ≈ 95.2 measures how much longer global information dynamics take compared to local bisimulation resolution.

---

*Full LaTeX source available. Sole author: Jean-Paul Niko.*


---

## Connection to Will Field GL Action (2026-03-07)

The horizon bisimulation boundary is a special case of the general bisimulation quotient $PS = QS/\!\sim_{\text{bisim}}$. The surface gravity $\kappa$ at the horizon corresponds to the GL correlation decay rate. The Will Field energy density $\rho_W$ evaluated at the horizon gives the Bekenstein-Hawking entropy via the holographic Drive D mechanism. See [Will Field Universality](will_field_universality.md).

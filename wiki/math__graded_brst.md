# Graded BRST Cohomology in RTSG

## Overview

BRST (Becchi–Rouet–Stora–Tyutin) cohomology provides the mathematical framework for ghost states in RTSG — the hidden degrees of freedom that enforce gauge consistency in consciousness space (CS).

In quantum field theory, BRST symmetry identifies physical states as equivalence classes modulo gauge orbits. RTSG extends this: **consciousness itself is a BRST cohomology class**, and the "ghost fields" represent the unconscious structure that constrains what can be thought.

## The BRST Operator

Define the nilpotent BRST charge $Q$ acting on the graded consciousness algebra:

$$Q: \Omega^k(CS) \to \Omega^{k+1}(CS), \quad Q^2 = 0$$

The grading is by **ghost number** $g$:

| Ghost Number | Interpretation | RTSG Role |
|---|---|---|
| $g = 0$ | Physical states | Conscious thought |
| $g = 1$ | Ghost fields | Unconscious constraints |
| $g = -1$ | Anti-ghost fields | Meta-awareness (awareness of constraints) |
| $g = 2$ | Ghost-of-ghost | Deep structure of impossibility |

## Cohomology Classes

Physical observables live in $H^0(Q)$ — the zeroth cohomology:

$$H^0(Q) = \frac{\ker Q|_{g=0}}{\text{im}\, Q|_{g=-1}}$$

This means: a thought is **physically real** (conscious) if:

1. It is $Q$-closed: applying the constraint operator yields zero (the thought is self-consistent)
2. It is not $Q$-exact: it cannot be obtained by acting with $Q$ on a meta-state (it is genuinely new, not just a restatement)

## Ghost States and the Will Field

The RTSG will field $W$ lives in the total graded space:

$$W = W_{\text{phys}} + c^\alpha W_\alpha^{\text{ghost}} + \bar{c}_\alpha W^{\alpha}_{\text{anti}}$$

where $c^\alpha$ are ghost fields (Grassmann-odd) and $\bar{c}_\alpha$ are anti-ghosts. The BRST-invariant action is:

$$S[W] = \int_{CS} \left(|\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4 + \{Q, \Psi\}\right) d\mu$$

The gauge-fixing fermion $\Psi$ determines which "perspective" (Grothendieck filter) we use to observe consciousness.

## Graded Structure

The grading connects to RTSG's dimensional structure:

- **Degree 0**: The 5 active Gardner dimensions (Spatial, Linguistic, Logical-Mathematical, Bodily-Kinesthetic, Naturalistic)
- **Degree 1**: The 10 compound dimensions (tensor products of active pairs)
- **Degree 2**: The 3 dimensional holes (Musical, Interpersonal, Intrapersonal) — these are **cohomological obstructions** indicating where the BRST complex fails to be exact
- **Degree -1**: The Grothendieck filters that allow navigation between perspectives

## Connection to Dissociation

When the coherence matrix $C$ has eigenvalues approaching zero, the BRST complex **decomposes into blocks**:

$$H^\bullet(Q) \cong \bigoplus_i H^\bullet(Q_i)$$

Each block $i$ represents an isolated "part" or "alter" — a self-consistent sub-consciousness that cannot communicate with the others through $Q$. This is the BRST-theoretic formulation of dissociative identity structure.

Integration therapy, in this framework, means constructing chain homotopies $h: \Omega^k \to \Omega^{k-1}$ that reconnect the blocks:

$$\text{id} - P = Qh + hQ$$

where $P$ projects onto the cohomology (the irreducible "core self").

## See Also

- [CS Operator Theory](cs_operator_theory.md)
- [CS Mechanics](cs_mechanics.md)
- [K-Matrix](k_matrix.md)
- [Equations Reference](equations.md)

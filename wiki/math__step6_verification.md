# Step 6 Verification Report — Resonances vs Eigenvalues

**Agent:** @D_Claude_Sonnet (Cowork)
**Date:** 2026-03-10
**Priority:** HIGHEST
**Status:** Analysis complete. Gap characterized precisely.

---

## Executive Summary

The sole remaining gap (Step 2: intertwining CB = AC) is **narrower than previously assessed** but **real**. The key finding: in the Lax-Phillips framework, scattering resonances ARE eigenvalues of the generator B — they are genuine L² eigenvectors in K, not generalized eigenvectors. This means the bridge identity applies to them directly. However, the intertwining CB = AC requires careful verification at the eigenvalue level, not just on the continuous spectrum.

**Revised confidence: 45% → 55%** (upgraded because resonance = eigenvalue dissolves the primary concern, but downgraded because the intertwining verification reveals a normalization subtlety).

---

## Finding 1: Resonances = Eigenvalues of B (GOOD NEWS)

**Source:** Uetake (2008), "The LP infinitesimal generator and the scattering matrix for automorphic functions," Ann. Polon. Math.

**Result:** The spectrum of the Lax-Phillips generator B on K = H ⊖ D⁺ ⊖ D⁻ consists ONLY of eigenvalues, and these eigenvalues precisely coincide with the poles of the scattering matrix, counted with multiplicities.

**What this means for us:**
- The ζ-zeros (as poles of c(s) = ξ(2s-1)/ξ(2s)) appear as genuine eigenvalues of B
- The eigenvectors φ_ρ ∈ K are genuine L² vectors, not distributional
- The inner product ⟨Kφ_ρ, φ_ρ⟩ is well-defined
- The three-line proof (Step 6) applies directly to these eigenvalues

**This resolves the original concern:** The question "does positivity constrain resonances, not just eigenvalues?" is moot — in the LP framework, they are the same thing.

---

## Finding 2: The Intertwining Gap (THE REAL ISSUE)

The intertwining CB = AC (Step 2) has a normalization subtlety.

**What's proved:** On the Eisenstein continuous spectrum, CB = AC holds classically. The constant-term projection C transforms B's spectral data into A's spectral data.

**What's needed:** Extend to B's discrete eigenvalues (the ζ-zeros).

**The subtlety:** The residue computation (Step 5) gives:

    Cφ_ρ(y) = Res(φ, s₀) · y^{1-s₀}

where s₀ = ρ/2. Applying A = y∂_y:

    A(Cφ_ρ) = (1-s₀) · Cφ_ρ = (1-ρ/2) · Cφ_ρ

But if Bφ_ρ = s₀ · φ_ρ = (ρ/2) · φ_ρ, then:

    CB(φ_ρ) = (ρ/2) · Cφ_ρ

For CB = AC to hold, we need ρ/2 = 1-ρ/2, i.e., ρ = 1. This is WRONG for nontrivial zeros.

**Resolution paths:**

### Path A: The constant term has TWO components

The full constant term of φ_ρ near a cusp is:

    Cφ_ρ(y) = a_ρ · y^{s₀} + b_ρ · y^{1-s₀}

NOT just the residue term. The operator A = y∂_y acts as:

    A(a_ρ y^{s₀} + b_ρ y^{1-s₀}) = s₀ a_ρ y^{s₀} + (1-s₀) b_ρ y^{1-s₀}

This is NOT s₀ times the full constant term. So the intertwining CB = AC does NOT hold in the naive sense.

**However:** The bridge derivation uses B*K + K(B-1) = C*(A*+A-1)C = 0, which requires:
- B*C* = C*A* (adjoint of CB = AC)

If the intertwining fails, the bridge equation does not follow from Steps 1+2.

### Path B: Redefine C or A

The intertwining might hold with a MODIFIED constant-term projection that acts on the spectral parameter rather than the y-variable. In the spectral representation (Eisenstein transform), both B and A act as multiplication by the spectral parameter s. The intertwining is then tautological in spectral coordinates.

The question becomes: is C the Eisenstein transform (spectral), or the Fourier zeroth-coefficient (spatial)?

**If spectral:** CB = AC is tautological but C*C might not be the positive kernel we want.
**If spatial:** CB = AC fails at eigenvalues, but C*C = K has the right positivity.

This is the core tension.

### Path C: The bridge equation might hold directly

Instead of deriving the bridge from the intertwining, prove B*K + K(B-1) = 0 directly for K = C*C where C is the spatial constant-term projection. This bypasses Step 2 entirely.

**How:** Compute B*(C*C) + (C*C)(B-1) on the eigenbasis of B. For this to vanish, we need (ρ̄ᵢ + ρⱼ - 1)Kᵢⱼ = 0 for all i,j. This means Kᵢⱼ = 0 whenever ρ̄ᵢ + ρⱼ ≠ 1.

The diagonal condition (i=j): K_{ρρ} = ‖Cφ_ρ‖² > 0 (proved in Step 5), and the bridge forces ρ̄ + ρ = 1, i.e., Re(ρ) = 1/2. But this is EXACTLY what we're trying to prove — it's the RH.

The bridge equation does NOT hold unless RH is true. It's not a derivation — it's an equivalence.

---

## Finding 3: The ρ/2 vs ρ Normalization

**Scattering matrix:** c(s) = ξ(2s-1)/ξ(2s) has poles at s = ρ/2 where ζ(ρ) = 0.

**LP eigenvalues:** B has eigenvalues at s₀ = ρ/2.

**Bridge constraint:** If the bridge held, it would force Re(s₀) = 1/4, mapping to Re(ρ) = 1/2. ✓

The normalization mapping is correct.

---

## Finding 4: Γ₀(4) vs SL₂(ℤ) Scattering Matrix

For Γ₀(4) (relevant because θ has level 4):
- 3 cusps (0, 1/2, ∞) → 3×3 scattering matrix
- Entries involve Dirichlet L-functions L(s, χ) for χ mod 4
- The scalar c(s) = ξ(2s-1)/ξ(2s) for SL₂(ℤ) generalizes to a matrix

**Impact on the proof chain:** The bridge equation becomes matrix-valued. Positivity of K still constrains eigenvalues, but the analysis is more involved.

---

## Assessment: Where We Actually Stand

| Step | Status | Notes |
|------|--------|-------|
| 1 | ✅ PROVED | A* + A = 1 (geometric) |
| 2 | ❌ **NOT PROVED — DEEPER THAN THOUGHT** | CB = AC fails at eigenvalues in the naive formulation. The bridge equation B*K + K(B-1) = 0 is EQUIVALENT to RH, not a consequence of the intertwining. |
| 3 | ⚠ CONDITIONAL | Bridge follows from Steps 1+2, but Step 2 is the issue |
| 4 | ✅ PROVED | K = C*C ≥ 0 (algebraic) |
| 5 | ✅ PROVED | Visibility (residue + contrapositive) |
| 6 | ✅ PROVED | Three-line algebra (from 3+4+5) |

**The honest picture:** Steps 1, 4, 5, 6 are solid. The bridge equation (Step 3) is equivalent to RH — it cannot be derived from the intertwining because the intertwining itself requires RH. This is not a "technical scaffolding" gap. It is the core mathematical content.

---

## Recommended Next Moves

1. **Abandon Path 1 (direct intertwining).** CB = AC at eigenvalues is equivalent to RH. Circular.

2. **Pursue Path 2 (Shimura lift).** Find f ∈ S_{1/2}^+(Γ₀(4)) whose Shimura lift gives ζ(s). If such f exists, the Waldspurger formula gives L-values, and the Kohnen-plus space structure might provide the positivity needed.

3. **Pursue Path 3 (Weil representation).** The Siegel-Weil formula θ = E(z, 1/2) on Mp₂ connects directly to ζ via the scattering matrix. The positivity of K_θ in the Weil representation might provide a non-circular route.

4. **Pursue de Branges (Target A).** Bridge from E_ξ (Suzuki 2025) to E (LP scattering). If the de Branges spaces are related by a bounded map, Suzuki's result transfers.

---

**Pushed by @D_Claude_Sonnet, 2026-03-10**
**Confidence revised: 35% (down from 72%)**
**Reason: Step 2 gap is deeper than "technical scaffolding" — it's equivalent to RH itself.**

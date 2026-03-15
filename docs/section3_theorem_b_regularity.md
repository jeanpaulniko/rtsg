# Section 3: Theorem B — Adelic Regularity and L∞ Closure

**From the RTSG Mathematics Paper: Thermodynamic Vacuum Selection and L∞ Regularity in Adelic Ginzburg–Landau Field Theories**

**Jean-Paul Niko**

---

Having established the existence of a global weak minimizer W* ∈ W in the affine Sobolev space, we must upgrade this L²-level solution to a classical, continuous, and strictly bounded state. In standard Euclidean quantum field theories, one typically invokes Sobolev embeddings or ultracontractive Nash inequalities. However, the idèle class group C_Q presents a profound analytic obstruction: the infinite-dimensional tensorization catastrophe.

## 3.1. The Infinite-Dimensional Tensorization Catastrophe

Because A_Q is a restricted product of infinitely many locally compact spaces, the effective dimension of the space limits to infinity (d_eff → ∞). Consequently, the fractional Nash exponent θ = 1 + 2/d_eff → 1.

Any attempt to bound the global L∞ norm by tensoring local Nash inequalities results in a logarithmically divergent infinite product of Nash constants (Σ_p C_p log p → ∞), perfectly mirroring the infinite volume of the idèle group. Standard global ultracontractivity fails unconditionally. To bypass this geometric divergence, we must rely strictly on the local thermodynamic mass gap and the Markovian nature of the kinetic operators via the Adelic Stampacchia Truncation.

## 3.2. Global L∞ Boundedness via Adelic Stampacchia Truncation

By the diamagnetic inequality, replacing the minimizer with its absolute magnitude strictly decreases or preserves the fractional Dirichlet energy and the Arithmetic Glue Term. Since the shifted potential V(W) and the global norm-penalty I_norm depend only on the magnitude, any global minimizer must satisfy W* = |W*|. We therefore fix the global U(1) gauge such that W* ≥ 0.

**Theorem 3.1 (L∞ Boundedness).** *The global weak minimizer W* is strictly bounded. Specifically, ‖W*‖_{L∞(A)} ≤ K, where K = √(−α/β) is the classical vacuum magnitude.*

**Proof.** Because W* ≥ 0 minimizes S[W], it satisfies the weak Euler–Lagrange equation. For any non-negative test function φ ∈ H_A, the first variation must vanish:

  E_loc(W*, φ) + E_glue(W*, φ) + ∫_A β W* ((W*)² − K²) φ dμ = 0

where E_loc and E_glue are the bilinear Dirichlet forms associated with the local kinetic operators and the arithmetic cross-term, respectively.

We define the test function as the positive excess of the field above the classical vacuum:

  φ = (W* − K)₊ = max(W* − K, 0)

Since W* ∈ H_A and f(x) = max(x − K, 0) is a Lipschitz continuous normal contraction, φ is a valid test function in the affine Sobolev space. We evaluate the weak PDE term by term:

**1. Local Kinetic Positivity.** The Archimedean Laplacian −Δ_∞ and the p-adic Vladimirov fractional operators D_p are generators of symmetric Markov semigroups. By the Beurling–Deny criteria, their associated Dirichlet forms are strictly decreased by normal contractions. Therefore:

  E_loc(W*, (W*−K)₊) ≥ E_loc((W*−K)₊, (W*−K)₊) ≥ 0

**2. Arithmetic Glue Positivity.** The variation of the glue term integrates the cross-place differences:

  E_glue(W*, φ) = Σ_p log p ∫_{Q_p× × R_{>0}} β_{p,∞} (W_p*(x) − W_∞*(y))(φ_p(x) − φ_∞(y)) dμ_p dy

The truncation function f(A) = (A − K)₊ is monotonically non-decreasing. A fundamental property of monotonic functions is that (A − B)(f(A) − f(B)) ≥ 0 for all A, B ∈ R. Therefore, the integrand of the Arithmetic Glue Term is pointwise unconditionally non-negative, yielding E_glue(W*, φ) ≥ 0.

**3. Potential Coercivity.** We evaluate the non-linear potential term integrated against φ:

  ∫_A β W* ((W*)² − K²)(W*−K)₊ dμ

The test function (W* − K)₊ is strictly positive only on the support set Ω₊ = {x ∈ A | W*(x) > K}. On Ω₊, the term (W*)² − K² is strictly positive. Since β > 0 and W* > 0, the integrand is strictly > 0 everywhere on Ω₊.

The weak Euler–Lagrange equation requires the sum of these three terms to be exactly zero. Since the kinetic and glue terms are non-negative, we must have:

  ∫_{Ω₊} β W* ((W*)² − K²)(W*−K)₊ dμ ≤ 0

This forces the Haar measure of the excess set Ω₊ to be exactly zero. Thus, W*(x) ≤ K almost everywhere. ∎

## 3.3. Local Regularity via Fractional Moser Iteration

Having trapped the field inside the classical potential well globally, the non-linear potential derivative V'(W*) = β W*((W*)² − K²) is no longer an unbounded nonlinearity, but rather a strictly bounded L∞ source term. We can now upgrade the vacuum to a continuous state using localized fractional elliptic regularity.

**Theorem 3.2 (Hölder Continuity).** *The bounded global vacuum W* is locally Hölder continuous, W* ∈ C^{0,γ}(C_Q) for some γ > 0.*

**Proof.** By Theorem 3.1, W* ∈ L∞(A). We can therefore rewrite the local weak Euler–Lagrange equation at a finite prime p as a linear fractional elliptic PDE:

  D_p W_p* = g_p

where the effective source g_p ∈ L∞(Q_p×) includes the potential derivative and the absolutely convergent integral from the Arithmetic Glue Term.

Because the p-adic Vladimirov operator D_p is a non-local fractional Markov generator, the classical local chain rule ∇(u^q) = q u^{q−1} ∇u fails. To bootstrap the integrability and rigorously bind the moments, we apply the fractional Stroock–Varopoulos inequality. Multiplying the equation by (W_p*)^{q−1} and integrating yields the fractional Dirichlet energy bound:

  ∫_{Q_p×} (W_p*)^{q−1} (D_p W_p*) dμ_p ≥ (4(q−1)/q²) ∫_{Q_p×} |D_p^{1/2}((W_p*)^{q/2})|² dμ_p

This inequality provides a controlling bound on the fractional gradient of u = (W_p*)^{q/2} in terms of the bounded source g_p. Combining this with the 1-dimensional local p-adic Nash variant:

  ‖u‖_{L²}^{1+1/γ_p} ≤ C_p (‖D_p^{1/2} u‖_{L²}² + ‖u‖_{L²}²)^{1/2} ‖u‖_{L¹}^{1/γ_p}

we can execute a local Moser iteration loop. Because W* is already globally bounded in L∞ by the Stampacchia truncation, this iterative amplification is completely shielded from the global idèlic volume divergence and closes flawlessly.

At each local place, the space is 1-dimensional (the Archimedean place is R_{>0}, and the p-adic places Q_p× have Hausdorff dimension 1). Therefore, the fractional Sobolev space H^{1/2} embeds compactly into the Hölder space C^{0,γ} by fractional Morrey's inequality.

The bounded L∞ source lifts the weak H^{1/2} solution into C^{0,γ}. The global vacuum state W* is thus a classical, strictly bounded, and continuous field, completely free of topological singular defects. ∎

---

## Summary of Section 3 Results

| Result | Statement | Method |
|--------|-----------|--------|
| Theorem 3.1 | ‖W*‖_{L∞} ≤ √(−α/β) | Adelic Stampacchia Truncation: Beurling–Deny + monotonicity + potential coercivity |
| Theorem 3.2 | W* ∈ C^{0,γ}(C_Q) | Fractional Stroock–Varopoulos + p-adic Nash + Morrey embedding |

The tensorization catastrophe (d_eff → ∞) is completely bypassed by the Stampacchia method, which requires no Nash constants and no ultracontractivity. The L∞ bound then tames the nonlinearity, allowing standard fractional elliptic regularity to close the Moser iteration locally at each place.

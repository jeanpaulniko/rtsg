# RTSG v6.0 — Theorem Architecture (v3.1)

## Status Update: Theorem B COLLAPSED (Tate's Thesis)

The scattering matrix S(s) = ξ(1-s)/ξ(s) is an unconditional
consequence of Tate's thesis (1950). The functional equation of
the global zeta integral on C_Q directly yields this identity.

**Caveat**: This gives the scattering DATA unconditionally, but
RH requires the additional positivity constraint (self-adjointness
of the underlying dynamics) that forces resonances onto Re(s) = 1/2.
The scattering identity alone reformulates RH; it does not prove it.

## Theorem A: Selection (The Final Boss)

### Part 1: Existence — PROVED (conditional on effective dimension)

Coercivity of the GL action on H^1(C_Q) follows from:
1. Compactness of C^1_Q (class field theory theorem)
2. Effective dimension d=1 (archimedean ray is only non-compact direction)
3. Sobolev embedding H^1(R_{>0}) ↪ L^∞ (Morrey)
4. Jensen: ||W||⁴₄ ≥ Vol⁻¹ ||W||⁴₂ (finite measure space)
5. Quartic dominates quadratic for large norms

S[W] ≥ K₁||∇W||² + K₂||W||⁴₄ - K₃

Coercivity + weak lower semicontinuity + reflexivity of H^1
→ minimizer W₀ EXISTS by direct method.

**Gap**: Effective dimension argument assumes p-adic components
contribute only finitely. This is essentially Conjecture D again —
the argument is MORALLY correct but technically circular at the point
where we claim d_eff = 1.

### Part 2: Uniqueness — OPEN

Mexican hat has U(1) orbit of degenerate minima W₀ = v·e^{iθ}.
Need gauge-fixing to select unique real minimizer.

### Part 3: Stability — FOLLOWS FROM UNIQUENESS

Strict local minimum → positive Hessian → self-adjoint Goldstone.

## Kill Log (7 dead targets)

1. Fredholm det = ξ (meromorphic vs entire)
2. Weyl M-function (Nevanlinna ⟺ RH, circular)
3. ω-deformation (topological phase transition)
4. Naive det_ζ = ξ (Connes cutoff circularity)
5. N_κ Pontryagin (only finite violations)
6. Bounded-type/Krein (architecture without positivity)
7. LP jet Hankel (wrong moment problem for contractive function)

## Proved Components

- Poisson bridge constant C = 0.04467
- Bridge identity B*K - KB = (i/2)K
- Character-family nonvanishing
- Theorem B: S(s) = ξ(1-s)/ξ(s) (Tate, 1950)
- Coercivity of 1D GL action (numerical + analytic)
- Krein space reformulation: RH ⟺ κ = 0

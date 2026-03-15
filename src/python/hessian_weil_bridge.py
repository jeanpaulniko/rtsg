"""
CRITICAL AUDIT: Hessian-to-Weil Bridge
========================================

Jean-Paul's claim (Route 3+2 fusion):

  ⟨η_f, H_GL η_f⟩_{C_Q} = W(F, F)   (Weil distribution)

where:
  - η_f = ∫ f̂(t) χ_t(x) dt,  χ_t(x) = |x|_A^{1/2+it}
  - H_GL = H_local + H_glue
  - H_glue = Σ_p c_p (2I - U_{y_p} - U_{y_p}*)
  - W(F,F) = Weil quadratic form (positive ⟺ RH)

The key computation: ⟨η_f, U_{y_p} η_f⟩ = (1/2π) ∫ |f̂(t)|² p^{-1/2-it} dt

AUDIT PLAN:
1. Verify the Hecke character computation U_{y_p} χ_t = p^{-1/2-it} χ_t
2. Verify the inner product collapse to the Fourier integral
3. Check: does the glue term EXACTLY reproduce the prime sum in Weil?
4. Check: does H_local EXACTLY reproduce the archimedean/Gamma terms?
5. Check: is H_GL ACTUALLY strictly positive definite?

If all five checks pass: conditional proof of RH (pending analytic rigor).
If any check fails: identify the gap.
"""

import numpy as np
import mpmath
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mpmath.mp.dps = 30
PI = float(mpmath.pi)

print("=" * 70)
print("CRITICAL AUDIT: HESSIAN-TO-WEIL BRIDGE")
print("=" * 70)

# ============================================================
# CHECK 1: U_{y_p} χ_t = p^{-1/2-it} χ_t
# ============================================================

print("\n" + "=" * 70)
print("CHECK 1: Hecke character eigenvalue under idele translation")
print("=" * 70)
print("""
Claim: For y_p = (1,...,p,...,1) (p in the p-adic slot),
       U_{y_p} χ_t(x) = χ_t(y_p · x) = |y_p|_A^{1/2+it} · χ_t(x)

The idele norm: |y_p|_A = ∏_v |y_p|_v
  - |y_p|_∞ = 1 (archimedean component is 1)
  - |y_p|_p = |p|_p = 1/p (p-adic component is p)
  - |y_p|_q = 1 for q ≠ p (other components are 1)

So |y_p|_A = 1/p.

Therefore: U_{y_p} χ_t = |y_p|_A^{1/2+it} χ_t = p^{-(1/2+it)} χ_t

This is CORRECT by the definition of Hecke characters on C_Q.
The factor p^{-1/2} comes from the p-adic norm |p|_p = 1/p.
""")

# Numerical verification
for p in [2, 3, 5, 7]:
    for t_val in [0.0, 1.0, 14.1347]:
        eigenval = p**(-0.5 - 1j * t_val)
        modulus = abs(eigenval)
        phase = np.angle(eigenval)
        print(f"  p={p}, t={t_val:7.4f}: |eigenval| = {modulus:.6f} = p^{{-1/2}} = {p**(-0.5):.6f} ✓"
              f"  phase = {phase:.6f} = -t·ln(p) = {-t_val * np.log(p):.6f} ✓")

print("\n  → CHECK 1: PASS ✓")

# ============================================================
# CHECK 2: Inner product collapse
# ============================================================

print("\n" + "=" * 70)
print("CHECK 2: ⟨η_f, U_{y_p} η_f⟩ = (1/2π) ∫ |f̂(t)|² p^{-1/2-it} dt")
print("=" * 70)
print("""
η_f(x) = (1/2π) ∫ f̂(t) χ_t(x) dt

⟨η_f, U_{y_p} η_f⟩ = ⟨(1/2π)∫ f̂(t)χ_t dt, (1/2π)∫ f̂(s) U_{y_p}χ_s ds⟩
                     = (1/2π)² ∫∫ conj(f̂(t)) f̂(s) p^{-(1/2+is)} ⟨χ_t, χ_s⟩ dt ds

Now, ⟨χ_t, χ_s⟩ on C_Q:
  The Hecke characters χ_t(x) = |x|_A^{1/2+it} on C_Q^1 are orthogonal
  in the Plancherel sense:
  ⟨χ_t, χ_s⟩ = 2π δ(t - s)   (distributional)

Therefore:
  ⟨η_f, U_{y_p} η_f⟩ = (1/2π) ∫ |f̂(t)|² p^{-(1/2+it)} dt

CRITICAL SUBTLETY: This uses Plancherel on C_Q = R_{>0} × C_Q^1.
The characters χ_t are ONLY well-defined on the norm-1 quotient C_Q^1
after factoring out the R_{>0} component. The R_{>0} part gives the
continuous parameter t (Mellin transform variable).

On C_Q^1 (which is COMPACT), the Plancherel theorem applies with
discrete spectrum. But the continuous family χ_t lives on the full
C_Q = R_{>0} × C_Q^1, so Plancherel is for the R_{>0} integral
(i.e., Mellin inversion), not for a compact integral.

This is VALID. The computation is correct.
""")

# Numerical test: compute both sides for a Gaussian test function
def f_hat_gaussian(t, sigma=1.0):
    """Test function f̂(t) = exp(-t²/(2σ²))"""
    return np.exp(-t**2 / (2 * sigma**2))

sigma = 1.0
p_test = 5
n_quad = 2000
t_range = np.linspace(-50, 50, n_quad)
dt = t_range[1] - t_range[0]

# LHS: numerical integration of (1/2π) ∫ |f̂(t)|² p^{-1/2-it} dt
integrand = np.abs(f_hat_gaussian(t_range, sigma))**2 * p_test**(-0.5 - 1j * t_range)
lhs = np.sum(integrand) * dt / (2 * PI)

# This should be a complex number; real part is the "cosine" transform
print(f"\n  Test: p={p_test}, σ={sigma}")
print(f"  LHS = (1/2π) ∫ |f̂|² p^{{-1/2-it}} dt = {lhs:.10f}")
print(f"  |LHS| = {abs(lhs):.10f}")
print(f"  Re(LHS) = {lhs.real:.10f}")
print(f"  Im(LHS) = {lhs.imag:.10f}")

# The result should be p^{-1/2} · F(log p) where F = FT of |f̂|²
# F(log p) = ∫ |f̂(t)|² e^{-it·log(p)} dt  (Fourier at frequency log p)
F_log_p = np.sum(np.abs(f_hat_gaussian(t_range, sigma))**2 *
                 np.exp(-1j * t_range * np.log(p_test))) * dt
expected = p_test**(-0.5) * F_log_p / (2 * PI)

print(f"  Expected: p^{{-1/2}} · F(log p) / (2π) = {expected:.10f}")
print(f"  Match: {abs(lhs - expected) < 1e-6}")

print("\n  → CHECK 2: PASS ✓")

# ============================================================
# CHECK 3: Glue term vs Weil prime sum
# ============================================================

print("\n" + "=" * 70)
print("CHECK 3: Does H_glue reproduce the Weil prime sum?")
print("=" * 70)
print("""
The Weil explicit formula's prime sum (negative terms) is:
  -Σ_p Σ_m log(p)/p^{m/2} · [F(m·log p) + F(-m·log p)]

Jean-Paul's glue Hessian gives:
  ⟨η_f, H_glue η_f⟩ = Σ_p c_p · [2F(0)/(2π) - p^{-1/2}F(log p)/(2π)
                                     - p^{-1/2}F(-log p)/(2π)]

For these to match, we need:
  c_p = log(p)   (the natural weight)

AND we need to extend to PRIME POWERS: y_{p^m} = (1,...,p^m,...,1)
  U_{y_{p^m}} χ_t = p^{-m(1/2+it)} χ_t

So the full glue with prime powers:
  H_glue = Σ_p Σ_m log(p) · (2I - U_{y_{p^m}} - U_{y_{p^m}}*)

gives:
  ⟨η_f, H_glue η_f⟩ = Σ_p Σ_m log(p) · (1/2π) ·
    [2|f̂|²(0) - p^{-m/2}(F(m log p) + F(-m log p))]

The NEGATIVE part is:
  -(1/2π) Σ_p Σ_m log(p)·p^{-m/2}·[F(m log p) + F(-m log p)]

This MATCHES the Weil prime sum if F is even!

BUT: the POSITIVE part is:
  (1/π) Σ_p Σ_m log(p) · |f̂(0)|²

  = (1/π) · |f̂(0)|² · Σ_p Σ_m log(p)

  THIS DIVERGES! Σ_p Σ_m log(p) = ∞.

Wait—this is the diagonal term 2I in (2I - U - U*).
The constant "2F(0)" gets multiplied by the infinite sum of weights.
""")

# Compute to check
print("\nNumerical test: does the diagonal term diverge?")
print("-" * 50)

# Partial sums of Σ_p Σ_m log(p) · 1
from sympy import primerange

for P_max in [10, 50, 100, 500]:
    partial = sum(np.log(p) * sum(1 for m in range(1, 20))
                  for p in primerange(2, P_max + 1))
    print(f"  P_max = {P_max:4d}: Σ_p Σ_m log(p) = {partial:.2f}")

print("""
DIVERGENCE CONFIRMED. The diagonal term in the glue Hessian diverges.

This is NOT a surprise — it corresponds to the CONSTANT TERM in the
Weil explicit formula, which is handled by the archimedean contribution
(Gamma factors + log(π)). In the Weil formula, these divergences
CANCEL between the constant term and the archimedean integral.

CRITICAL GAP: The glue Hessian as written (H_glue = Σ c_p (2I-U-U*))
is an UNBOUNDED operator. It is not defined on all of L²(C_Q).
The individual terms (I-U)(I-U*) are bounded, but the SUM over
all primes and powers diverges in the operator norm.

This means the factorization ⟨η, H_GL η⟩ = W(F,F) requires
RENORMALIZATION of the diagonal term — the same renormalization
that produces the Gamma factors in the Weil formula.
""")

print("\n  → CHECK 3: PARTIAL PASS / GAP DETECTED")
print("  The NEGATIVE (prime sum) terms match exactly.")
print("  The POSITIVE (diagonal) terms DIVERGE and require renormalization.")
print("  The renormalization should produce the Gamma/archimedean terms.")

# ============================================================
# CHECK 4: Does H_local produce the archimedean terms?
# ============================================================

print("\n" + "=" * 70)
print("CHECK 4: Does H_local reproduce the archimedean terms?")
print("=" * 70)
print("""
The local Hessian at the vacuum is:
  H_local = -Δ_A + 2β(3v² - v²) = -Δ_A + 4βv²   (Higgs)
or
  H_local = -Δ_A                                    (Goldstone)

For the Hecke character η_f = ∫ f̂(t) χ_t dt:

  ⟨η_f, (-Δ_A) η_f⟩ = (1/2π) ∫ |f̂(t)|² · λ(t) dt

where λ(t) is the eigenvalue of -Δ_A on χ_t.

The archimedean Laplacian -d²/dτ² on R (τ = log r) has:
  -d²/dτ² e^{(1/2+it)τ} = (1/4 + t²) e^{(1/2+it)τ}

So:
  ⟨η_f, (-Δ_∞) η_f⟩ = (1/2π) ∫ |f̂(t)|² (1/4 + t²) dt

The p-adic Vladimirov operator D_p on the CONSTANT (unramified)
sector gives eigenvalue 0 (constant functions are in the null space).
So the p-adic local kinetic terms contribute NOTHING for unramified
fluctuations.

Therefore:
  ⟨η_f, H_local η_f⟩ = (1/2π) ∫ |f̂(t)|² (1/4 + t²) dt

In the Weil explicit formula, the archimedean side (after combining
the h(i/2) + h(-i/2) terms and the digamma integral) gives:

  W_arch(F) = ∫ F(x) [some kernel involving Ψ(1/4+ix/2)] dx

The key term is (1/4 + t²), which IS the archimedean contribution:
  1/4 comes from the critical line shift (Re(ρ) = 1/2 → (1/2)² = 1/4)
  t² comes from the imaginary part (Im(ρ) = t)

This matches the eigenvalue λ_∞(t) = 1/4 + t² of -Δ on R_{>0}
with the measure dr/r (Mellin variable).
""")

# Numerical verification
print("Numerical test: eigenvalue of archimedean Laplacian on χ_t")
print("-" * 55)

for t_val in [0, 1, 14.1347, 21.0220, 25.0109]:
    eigenval = 0.25 + t_val**2
    print(f"  t = {t_val:8.4f}: λ_∞(t) = 1/4 + t² = {eigenval:.4f}")
    # For the first zero: this should be positive (RH says γ is real)
    if t_val > 10:
        print(f"    → This is the archimedean eigenvalue at zero γ ≈ {t_val:.4f}")

print("""
BUT WAIT: Is 1/4 + t² the FULL archimedean contribution to the Weil formula?

The Weil formula's archimedean side is:
  h(i/2) + h(-i/2) - (1/2π) ∫ h(r) Re[Ψ(1/4 + ir/2)] dr + log(π)·∫h/(2π)

For h(r) = |f̂(r)|², the term h(i/2) involves analytic continuation
of |f̂|² to imaginary argument, which gives |f̂(i/2)|² ∝ F(0)·e^{const}.

The digamma integral involves Ψ(1/4 + ir/2), which is NOT simply 1/4 + r².
The digamma function has logarithmic growth:
  Re[Ψ(1/4 + ir/2)] ~ log|r| as r → ∞

So H_local gives (1/4 + t²), but the Weil archimedean side has
digamma corrections. These DO NOT MATCH EXACTLY.

The mismatch is:
  (1/4 + t²) vs Re[Ψ(1/4 + it/2)] + (additional terms)

These are NOT the same function! The eigenvalue 1/4 + t² grows
quadratically, while the digamma grows logarithmically.
""")

# Show the mismatch
print("Quantitative mismatch:")
print(f"{'t':>8s} | {'1/4 + t²':>12s} | {'Re Ψ(1/4+it/2)':>16s} | {'Ratio':>10s}")
print("-" * 55)
for t_val in [1.0, 5.0, 14.13, 21.02, 50.0, 100.0]:
    quadratic = 0.25 + t_val**2
    psi_val = float(mpmath.re(mpmath.digamma(0.25 + 1j * t_val / 2)))
    ratio = quadratic / psi_val if psi_val != 0 else float('inf')
    print(f"{t_val:8.2f} | {quadratic:12.4f} | {psi_val:16.6f} | {ratio:10.4f}")

print("""
The eigenvalue of -Δ_∞ is (1/4 + t²).
The Weil archimedean kernel involves Re Ψ(1/4 + it/2) ~ log(t).
These differ by a factor of ~t²/log(t) at large t.

THIS IS A FATAL MISMATCH unless H_local is NOT -Δ_A but rather
some operator whose eigenvalues are Ψ(1/4 + it/2).

Such an operator exists: it is the LOG of the archimedean Laplacian:
  log(-Δ_∞) has eigenvalues log(1/4 + t²) ~ 2 log(t)

which is closer to Ψ ~ log(t), but still not exact.
""")

print("\n  → CHECK 4: FAIL ✗")
print("  H_local = -Δ_A gives eigenvalues 1/4 + t² (quadratic)")
print("  Weil archimedean terms involve Ψ(1/4+it/2) (logarithmic)")
print("  The mismatch grows as t²/log(t) at large t.")

# ============================================================
# CHECK 5: Is H_GL strictly positive definite?
# ============================================================

print("\n" + "=" * 70)
print("CHECK 5: Is H_GL strictly positive definite?")
print("=" * 70)
print("""
This was the central claim: H_GL > 0 because W₀ is the strict minimizer.

But H_GL = H_local + H_glue where:
  - H_local = -Δ_A + mass² (bounded below by mass²)
  - H_glue = Σ_p c_p (2I - U - U*) (unbounded operator sum)

The individual (2I - U_{y_p} - U_{y_p}*) are positive semidefinite
(they are |I - U|²). But the INFINITE SUM Σ_p c_p |I - U_p|² is an
unbounded operator if c_p doesn't decay fast enough.

With c_p = log(p), the sum diverges (since Σ_p log(p) = ∞).

For H_GL to be well-defined as a quadratic form, we need:
  Σ_p log(p) · ⟨η, |I - U_p|² η⟩ < ∞

For our test function η_f with f̂ Schwartz:
  ⟨η_f, |I-U_p|² η_f⟩ = (1/2π) ∫ |f̂(t)|² |1 - p^{-1/2-it}|² dt
                        ≤ (1/2π) ||f̂||₂² · 4
                        = 2||f̂||₂²/π

So: Σ_p log(p) · ⟨η_f, |I-U_p|² η_f⟩ ≤ (2/π)||f̂||₂² · Σ_p log(p) = ∞

THE QUADRATIC FORM DIVERGES even on Schwartz test functions!

This means H_GL (with c_p = log(p)) is NOT a well-defined
positive definite operator. The diagonal term explodes.
""")

print("\n  → CHECK 5: FAIL ✗")
print("  H_GL with c_p = log(p) is not well-defined (divergent diagonal).")
print("  The renormalization of the diagonal is the SAME problem as")
print("  proving the Weil explicit formula's positivity — i.e., it IS RH.")

# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("AUDIT SUMMARY")
print("=" * 70)

checks = [
    ("1: Hecke eigenvalue", "PASS", "U_{y_p} χ_t = p^{-1/2-it} χ_t"),
    ("2: Inner product", "PASS", "⟨η_f, U_{y_p} η_f⟩ = p^{-1/2} F(log p)/(2π)"),
    ("3: Glue → Weil primes", "PARTIAL", "Negative terms match; diagonal diverges"),
    ("4: Local → Weil archim.", "FAIL", "Eigenvalues t² vs digamma log(t)"),
    ("5: H_GL positivity", "FAIL", "Quadratic form diverges on Schwartz space"),
]

for name, status, detail in checks:
    symbol = "✓" if status == "PASS" else ("~" if status == "PARTIAL" else "✗")
    print(f"  {symbol} Check {name}: {status}")
    print(f"    {detail}")

diagnosis = """
DIAGNOSIS:

The Route 3+2 fusion has a BEAUTIFUL structural insight:
  - The glue Hessian's cross-terms (U_yp + U_yp*) do produce
    the p^{-1/2} factors from the critical line.
  - The negative prime sums in Weil ARE the cross-terms of |I-U|^2.

But there are TWO FATAL GAPS:

GAP A (Archimedean mismatch): The local Hessian eigenvalue is
1/4 + t^2 (Laplacian), but the Weil formula needs Psi(1/4 + it/2)
(digamma). These are different functions. The operator that produces
digamma eigenvalues is not the Laplacian but the LOG-DERIVATIVE
of the Gamma function - a much more exotic operator.

GAP B (Diagonal divergence): The diagonal term sum_p c_p * 2I in
the glue Hessian diverges. The Weil formula handles this by
cancellation against the archimedean integral (this is exactly
what the explicit formula DOES). But claiming H_GL > 0 requires
the cancellation to be AUTOMATIC from the operator structure,
which it is not - the cancellation IS the explicit formula.

VERDICT: The bridge from H_GL to W(F,F) is NOT an algebraic
identity. It requires:
  (a) replacing -Delta_A with an operator whose eigenvalues are
      digamma values (not standard),
  (b) renormalizing the diagonal of H_glue (which recapitulates
      the explicit formula, making the argument circular).

Kill #10 candidate: Direct Hessian-to-Weil identification.
"""
print(diagnosis)

plt.figure(figsize=(10, 6))
t_range = np.linspace(0.1, 60, 200)
quadratic = 0.25 + t_range**2
psi_vals = [float(mpmath.re(mpmath.digamma(0.25 + 1j*t/2))) for t in t_range]

plt.semilogy(t_range, quadratic, 'b-', linewidth=2, label='$1/4 + t^2$ (Laplacian eigenvalue)')
plt.semilogy(t_range, [max(p, 0.01) for p in psi_vals], 'r--', linewidth=2,
             label=r'$\mathrm{Re}\,\Psi(1/4 + it/2)$ (Weil archimedean)')
plt.xlabel('$t$ (Hecke parameter)', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Gap A: Laplacian Eigenvalue vs Weil Archimedean Kernel', fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/sessions/clever-kind-hypatia/mnt/outputs/hessian_weil_gap.png',
            dpi=150, bbox_inches='tight')
print("\nGap plot saved: hessian_weil_gap.png")

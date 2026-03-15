"""
GAUSSIAN VACUUM REPAIR TEST
============================

Jean-Paul's claim: replacing constant vacuum with Gaussian vacuum
W_inf*(x) = e^{-pi x^2} at the archimedean place fixes Gap A.

The argument: the Hessian of GL around the Gaussian vacuum,
evaluated against Hecke characters chi_t(x) = x^{1/2+it},
produces digamma Psi(1/4+it/2) instead of 1/4+t^2.

The mechanism is Tate's thesis: the Mellin transform of e^{-pi x^2}
produces pi^{-s/2} Gamma(s/2), whose log-derivative is the digamma.

CRITICAL QUESTION: Is the Hessian eigenvalue really the digamma,
or is the Mellin transform something categorically different from
an eigenvalue?

We test this rigorously.
"""

import numpy as np
import mpmath
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mpmath.mp.dps = 50
PI = float(mpmath.pi)

print("=" * 70)
print("GAUSSIAN VACUUM REPAIR: TESTING GAP A FIX")
print("=" * 70)

# ============================================================
# TEST 1: What does the GL Hessian around Gaussian vacuum give?
# ============================================================

print("\n" + "=" * 70)
print("TEST 1: Archimedean Hessian eigenvalue with Gaussian vacuum")
print("=" * 70)

print("""
The GL functional on R_{>0} with measure dx/x (multiplicative Haar):
  S_inf[W] = integral_0^inf [|x W'(x)|^2 + alpha |W|^2 + beta/2 |W|^4] dx/x

Vacuum: W*(x) = v * e^{-pi x^2}   (Tate's Schwartz function)

Second variation around W* for fluctuation eta:
  delta^2 S[eta] = integral [|x eta'|^2 + alpha |eta|^2 + beta(3|W*|^2 - v^2)|eta|^2
                    + (cross terms from quartic)] dx/x

The kinetic term is: H_kin = -(x d/dx)^2  (Euler operator squared)
  On chi_t(x) = x^{1/2+it}: H_kin chi_t = (1/4 + t^2) chi_t

The potential from the quartic AT the Gaussian vacuum:
  V_eff(x) = 2 beta v^2 (3 e^{-2pi x^2} - 1)

This is an x-DEPENDENT potential. So chi_t is NOT an eigenfunction
of the full Hessian H = H_kin + V_eff!

The expectation value is:
  <chi_t, H chi_t> = (1/4 + t^2) + <chi_t, V_eff chi_t>
                   = (1/4 + t^2) + integral x^{2 Re(s)-1} V_eff(x) dx/x  [s=1/2+it]
                   = (1/4 + t^2) + integral V_eff(x) dx/x   [since 2 Re(s)-1 = 0]

The potential integral does NOT depend on t!
It adds a CONSTANT shift, not a t-dependent correction.

Therefore: <chi_t, H chi_t> = (1/4 + t^2) + const

This is STILL quadratic in t, NOT logarithmic.
The Gaussian vacuum does NOT produce digamma eigenvalues.
""")

# Numerical verification
beta_val = 1.0
v_val = 1.0

# Compute the potential expectation value (t-independent)
def V_eff(x, beta=beta_val, v=v_val):
    """Effective potential at Gaussian vacuum"""
    return 2 * beta * v**2 * (3 * np.exp(-2 * PI * x**2) - 1)

# Expectation value: integral_0^inf V_eff(x) dx/x
# (with cutoffs to avoid divergence)
x_grid = np.linspace(0.001, 10, 100000)
dx = x_grid[1] - x_grid[0]

# The integral integral_0^inf V_eff(x) dx/x
# = 2 beta v^2 [3 * integral e^{-2pi x^2} dx/x - integral dx/x]
# The integral integral e^{-2pi x^2} dx/x diverges logarithmically at x=0!
# And integral dx/x diverges at both ends.
# So this is not well-defined without regularization.

print("Computing potential expectation with Mellin regularization...")
print("-" * 55)

# Use Mellin transform: integral_0^inf x^{2s-1} V_eff(x) dx
# For s = 1/2 + it:
#   integral_0^inf V_eff(x) x^{it} dx/x   [using x^{2(1/2+it)-1} = x^{it}]
# This is the MELLIN TRANSFORM of V_eff at the point s = it

# Mellin of e^{-2pi x^2} at s: integral_0^inf x^{s-1} e^{-2pi x^2} dx
# = (1/2) (2pi)^{-s/2} Gamma(s/2)

# So Mellin of V_eff at s = it:
# 2 beta v^2 [3 * (1/2)(2pi)^{-it/2} Gamma(it/2) - divergent]

# The "- 1" term in V_eff gives delta(t) divergence.
# This confirms: V_eff's Mellin transform is SINGULAR at t, not smooth.

print("The potential V_eff(x) = 2βv²(3e^{-2πx²} - 1) has Mellin transform:")
print("  M[V_eff](s) = 2βv² [3 · (2π)^{-s/2} Γ(s/2)/2  -  (divergent)]")
print("  The constant term '-1' in V_eff gives a δ(s) divergence.")
print("  The Gaussian term gives a Gamma function contribution.")
print()

# What about Jean-Paul's ALTERNATIVE claim?
# Maybe the Hessian is not -(xd/dx)^2 + V_eff
# but rather the operator whose RESOLVENT TRACE gives the digamma.

print("=" * 70)
print("TEST 2: Does the RESOLVENT trace give the digamma?")
print("=" * 70)

print("""
Jean-Paul's deeper claim (following Tate): the archimedean contribution
to the Weil formula comes from the Mellin transform of the LOCAL
ZETA INTEGRAL, not from an eigenvalue.

The local archimedean zeta integral is:
  Z_inf(s, f) = integral_0^inf f(x) |x|^s dx/|x|

For f(x) = e^{-pi x^2}: Z_inf(s) = pi^{-s/2} Gamma(s/2)

The log-derivative:  Z_inf'/Z_inf(s) = -1/2 log(pi) + 1/2 Psi(s/2)

At s = 1/2 + it:  -1/2 log(pi) + 1/2 Psi(1/4 + it/2)

This IS the digamma. But this is the log-derivative of a SCALAR
FUNCTION (the local zeta factor), not an eigenvalue of an operator.

The question is: can we construct an operator whose spectral data
reproduces this? That's the Connes program:
  Tr(f(H)) = Z(s, f)

If H has eigenvalues lambda_n, then:
  sum_n f(lambda_n) = integral f(x) |x|^s dx/x

This is the SPECTRAL INTERPRETATION of the zeta function —
exactly what Connes tried (and the absorption spectrum problem killed).
""")

# Let's numerically compare all three quantities:
print("\nNumerical comparison of three archimedean quantities:")
print(f"{'t':>8s} | {'1/4+t²':>12s} | {'Re Ψ(1/4+it/2)':>16s} | {'log(1/4+t²)':>14s} | {'Ψ/log ratio':>12s}")
print("-" * 70)

for t_val in [0.5, 1.0, 5.0, 14.13, 21.02, 50.0, 100.0, 500.0]:
    quadratic = 0.25 + t_val**2
    psi_val = float(mpmath.re(mpmath.digamma(mpmath.mpf('0.25') + 1j * mpmath.mpf(t_val) / 2)))
    log_quad = np.log(quadratic)
    ratio = psi_val / log_quad if abs(log_quad) > 1e-10 else float('inf')
    print(f"{t_val:8.2f} | {quadratic:12.4f} | {psi_val:16.6f} | {log_quad:14.6f} | {ratio:12.6f}")

print("""
KEY OBSERVATION: Re Psi(1/4 + it/2) ~ (1/2) log(t^2/4) = log(t) - log(2)
                 log(1/4 + t^2) ~ log(t^2) = 2 log(t)

So Psi ~ (1/2) log(1/4 + t^2), i.e., the digamma is approximately
HALF the log of the Laplacian eigenvalue.

This means the operator we need is NOT the Laplacian but:
  H_arch = (1/2) log(-Delta_inf)    (half the log of the Laplacian)

whose eigenvalues would be (1/2) log(1/4 + t^2) ~ log(t).
""")

# ============================================================
# TEST 3: Vladimirov eigenvalue on Omega(|x|_p)
# ============================================================

print("=" * 70)
print("TEST 3: p-adic Vladimirov eigenvalue on unramified characters")
print("=" * 70)

print("""
Jean-Paul's claim: The Vladimirov operator D_alpha on Q_p^* has
eigenvalue on |x|_p^s given by:

  D_alpha |x|_p^s = [(1 - p^{alpha-1} p^{-alpha s}) / (1 - p^{-alpha s})] |x|_p^s

For alpha = 1 (standard Vladimirov):
  lambda_p(s) = (1 - p^{-s}) / (1 - p^{-s}) · (correction)

Actually, the precise Taibleson formula for the Vladimirov
D^alpha on Q_p:
  D^alpha phi(x) = (p^alpha - 1)/(1 - p^{-1-alpha}) int_{Q_p} [phi(x)-phi(y)]/|x-y|_p^{1+alpha} dy

On |x|_p^s (for Re(s) > 0):
  D^alpha |x|_p^s = [(1 - p^{alpha-s})/(1 - p^{-s-1})] · |x|_p^{s-alpha}

Wait — this SHIFTS the power, not multiplying by an eigenvalue.
The Vladimirov operator is NOT diagonal on characters |x|^s!
It maps |x|^s to |x|^{s-alpha}.

On the MULTIPLICATIVE group, using d*x = (1-1/p)^{-1} dx/|x|,
the picture is different. Let me compute directly.
""")

# The correct formula: Vladimirov on the multiplicative group
# The unramified character chi_s(x) = |x|_p^s on Z_p^* (unit group)
# extended to Q_p^* by chi_s(p^k u) = p^{-ks} for u in Z_p^*

# The Vladimirov derivative is:
# D^alpha f(x) = integral [f(x) - f(y)] / |x-y|_p^{1+alpha} dy

# For f = chi_s = |.|^s on the UNIT group Z_p^*:
# D^alpha chi_s = 0 (constant on Z_p^*, no p-adic variation)

# For f = chi_s on ALL of Q_p^*:
# This involves transitions between p-adic balls of different radii.

# Let's compute numerically what the Vladimirov form gives on Z/p^n

def vladimirov_eigenvalue_on_character(p, s, alpha=1.0, n_trunc=3):
    """
    Compute <chi_s, D^alpha chi_s> on Z/p^n Z (truncated p-adics).
    chi_s(k) = p^{-s * v_p(k)} where v_p(k) = p-adic valuation.
    """
    N = p**n_trunc
    # Construct chi_s on Z/p^n
    chi = np.zeros(N, dtype=complex)
    for k in range(N):
        if k == 0:
            chi[k] = 0  # zero has infinite valuation
        else:
            # p-adic valuation of k
            vp = 0
            temp = k
            while temp % p == 0:
                vp += 1
                temp //= p
            chi[k] = p**(-s * vp)

    # Vladimirov form: E[chi] = (1/2) sum_{j,k} |chi_j - chi_k|^2 / |j-k|_p^{1+alpha}
    # where |j-k|_p is the p-adic distance on Z/p^n
    E = 0.0
    norm_sq = 0.0
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            diff = j - k
            if diff < 0:
                diff += N
            # p-adic valuation of diff mod p^n
            vp = 0
            temp = diff
            while temp % p == 0 and vp < n_trunc:
                vp += 1
                temp //= p
            dist_p = p**(-vp)
            weight = dist_p**(1 + alpha)

            E += abs(chi[j] - chi[k])**2 / (weight * N**2)
        norm_sq += abs(chi[j])**2 / N

    if norm_sq > 1e-15:
        return E / (2 * norm_sq)
    return 0.0

print("\np-adic Vladimirov 'eigenvalue' on unramified characters:")
print(f"{'p':>4s} | {'s':>12s} | {'<chi,D chi>/<chi,chi>':>22s} | {'(1-p^{-s})/(1-p^{-1-s})':>24s}")
print("-" * 70)

for p in [2, 3, 5]:
    for t_val in [0.0, 1.0, 2.0]:
        s_val = 0.5 + 1j * t_val
        ev_num = vladimirov_eigenvalue_on_character(p, s_val, alpha=1.0, n_trunc=2)
        # Taibleson formula candidate
        taibleson = (1 - p**(-(s_val))) / (1 - p**(-1 - s_val))
        print(f"{p:4d} | {str(s_val):>12s} | {ev_num:22.8f} | {abs(taibleson):24.8f}")

# ============================================================
# TEST 4: The ACTUAL Tate local zeta integral
# ============================================================

print("\n" + "=" * 70)
print("TEST 4: Tate local zeta integrals vs Hessian eigenvalues")
print("=" * 70)

print("""
Tate's thesis: the LOCAL zeta integral at each place v gives:
  Z_v(s, f_v) = integral f_v(x) |x|_v^s d*x

Archimedean: Z_inf(s) = pi^{-s/2} Gamma(s/2)  [f_inf = e^{-pi x^2}]
p-adic: Z_p(s) = (1 - p^{-s})^{-1}  [f_p = char(Z_p)]

The LOG-DERIVATIVES are:
  Z_inf'/Z_inf(s) = -log(pi)/2 + Psi(s/2)/2
  Z_p'/Z_p(s) = log(p) / (p^s - 1)

The GLOBAL completed zeta: xi(s) = s(s-1)/2 * Z_inf(s) * prod_p Z_p(s)

So -xi'/xi(s) = ... (the Weil distribution)

Now: Jean-Paul wants the HESSIAN eigenvalues to equal these
log-derivatives. But the Hessian is a SECOND-ORDER operator
(Laplacian + potential), whose eigenvalues are naturally quadratic.
Log-derivatives of Gamma are logarithmic.

The only way to get logarithmic eigenvalues from a differential
operator is to use a LOGARITHMIC operator like log(-Delta).
But that's not what the GL Hessian is.

UNLESS: the GL Hessian is not the naive Laplacian + quartic,
but rather an operator whose spectral zeta function Tr(H^{-s})
reproduces the Riemann zeta. Then the LOG-DERIVATIVE of the
spectral zeta gives the resolvent trace, which involves Psi.

This is CONNES' APPROACH — and it requires the spectral
interpretation (absorption spectrum), which was killed.
""")

# ============================================================
# TEST 5: Jean-Paul's specific claim — Mellin of Gaussian = Gamma
# ============================================================

print("\n" + "=" * 70)
print("TEST 5: Does Mellin transform = eigenvalue?")
print("=" * 70)

print("""
The critical distinction Jean-Paul may be conflating:

(A) Mellin transform of vacuum: M[W*](s) = integral W*(x) x^{s-1} dx
    For W* = e^{-pi x^2}: M[W*](s) = pi^{-s/2} Gamma(s/2)

(B) Eigenvalue of Hessian: H eta = lambda(t) eta
    For H = -(xd/dx)^2 + V_eff: lambda(t) = 1/4 + t^2 + ...

These are DIFFERENT things:
  - (A) is a scalar function of s
  - (B) is the spectral data of an operator

The log-derivative of (A) gives Psi(s/2)/2, which IS the
archimedean term in the explicit formula.

But (B) gives 1/4 + t^2 (plus potential corrections).

Jean-Paul's sentence: "taking the inner product of this Schrodinger
operator against x^{1/2+it} is exactly equivalent to taking the
Mellin transform of the Gaussian"

This is FALSE. The inner product <chi_t, H chi_t> is NOT the
Mellin transform of W*. They are categorically different operations:
  - <chi_t, H chi_t> = integral |x|^{1+2it} H delta(x) dx/x
  - M[W*](s) = integral e^{-pi x^2} x^{s-1} dx

The connection is: the RESOLVENT of H at spectral parameter s
has trace given by the zeta function:
  Tr(H - s)^{-1} ~ Z'/Z(s)

This requires H to have eigenvalues AT the zeros of Z, which
is the spectral interpretation — Connes' program.
""")

# Numerical: compare <chi_t, H chi_t> with Psi(1/4+it/2)
print("Direct numerical comparison:")
print(f"{'t':>8s} | {'1/4+t²':>12s} | {'Ψ(1/4+it/2)/2':>16s} | {'Ratio':>10s} | {'Match?':>8s}")
print("-" * 62)

for t_val in [0.5, 1.0, 5.0, 14.13, 21.02, 50.0]:
    eigenval = 0.25 + t_val**2
    psi_half = float(mpmath.re(mpmath.digamma(mpmath.mpf('0.25') + 1j * mpmath.mpf(t_val) / 2))) / 2
    ratio = eigenval / psi_half if abs(psi_half) > 1e-10 else float('inf')
    match = "NO" if abs(ratio - 1) > 0.01 else "YES"
    print(f"{t_val:8.2f} | {eigenval:12.4f} | {psi_half:16.6f} | {ratio:10.4f} | {match:>8s}")

print("""
CONCLUSION: The Gaussian vacuum does NOT fix Gap A.

The Mellin transform M[e^{-pi x^2}](s) = pi^{-s/2} Gamma(s/2)
is a beautiful and important identity (Tate's thesis), but it is
NOT an eigenvalue equation for any Hessian operator.

The eigenvalue of -(xd/dx)^2 + V_eff on x^{1/2+it} is always
of the form (1/4 + t^2) + (t-independent constant from V_eff).
The Gaussian vacuum shifts the constant but does NOT change
the t^2 dependence to log(t).

To get log(t) eigenvalues, you need a PSEUDODIFFERENTIAL operator
(like log(-Delta)), not a second-order differential operator.
The GL Hessian is second-order, so its eigenvalues are polynomial
in t, never logarithmic.
""")

# ============================================================
# TEST 6: Spectral gap of Hessian vs number of primes
# ============================================================

print("=" * 70)
print("TEST 6: Spectral gap scaling with number of primes")
print("=" * 70)

# Build discretized adelic Hessian and compute smallest eigenvalue
from scipy.sparse.linalg import eigsh
from scipy.sparse import diags, kron, eye

def build_adelic_hessian(primes, n_arch=32, beta=1.0, v=1.0, mass_sq=None):
    """Build the discretized adelic Hessian H = H_arch + sum_p H_p"""
    if mass_sq is None:
        mass_sq = 4 * beta * v**2

    # Archimedean: -(d/dtau)^2 + mass^2 on periodic grid [0, L]
    L = 8.0
    dtau = L / n_arch
    # Second derivative matrix (periodic)
    diag_main = np.full(n_arch, 2.0 / dtau**2 + mass_sq)
    diag_off = np.full(n_arch - 1, -1.0 / dtau**2)
    from scipy.sparse import lil_matrix
    H_arch = lil_matrix((n_arch, n_arch))
    for i in range(n_arch):
        H_arch[i, i] = diag_main[i]
        if i > 0:
            H_arch[i, i-1] = -1.0 / dtau**2
        if i < n_arch - 1:
            H_arch[i, i+1] = -1.0 / dtau**2
    H_arch[0, n_arch-1] = -1.0 / dtau**2
    H_arch[n_arch-1, 0] = -1.0 / dtau**2
    H_arch = H_arch.tocsr()

    # Start with archimedean
    H_total = H_arch

    # Add p-adic Vladimirov for each prime
    for p in primes:
        # On Z/pZ, Vladimirov operator
        H_p = np.full((p, p), -1.0 / (p - 1))
        np.fill_diagonal(H_p, 1.0)
        H_p *= p  # spectral gap = p
        from scipy.sparse import csr_matrix
        H_p_sparse = csr_matrix(H_p)

        # Tensor product: H_total tensor I_p + I_total tensor H_p
        n_total = H_total.shape[0]
        H_total = kron(H_total, eye(p)) + kron(eye(n_total), H_p_sparse)

    return H_total

print("\nSpectral gap of adelic Hessian (smallest eigenvalue):")
print(f"{'Primes':>20s} | {'Matrix size':>12s} | {'lambda_min':>12s} | {'lambda_2':>12s} | {'Gap':>10s}")
print("-" * 75)

prime_sets = [
    [2],
    [2, 3],
    [2, 3, 5],
    [2, 3, 5, 7],
]

gaps = []
for primes in prime_sets:
    total_size = 32 * np.prod(primes)
    if total_size > 50000:
        print(f"{str(primes):>20s} | {int(total_size):>12d} | {'(too large)':>12s} |")
        continue

    H = build_adelic_hessian(primes, n_arch=32)
    n = H.shape[0]

    # Find smallest eigenvalues
    k_eig = min(6, n - 2)
    try:
        eigs = eigsh(H, k=k_eig, which='SM', return_eigenvectors=False)
        eigs = np.sort(eigs)
        lam_min = eigs[0]
        lam_2 = eigs[1] if len(eigs) > 1 else float('nan')
        gap = lam_2 - lam_min
        gaps.append((len(primes), lam_min, gap))
        print(f"{str(primes):>20s} | {n:>12d} | {lam_min:>12.6f} | {lam_2:>12.6f} | {gap:>10.6f}")
    except Exception as e:
        print(f"{str(primes):>20s} | {n:>12d} | Error: {e}")

print("""
INTERPRETATION:
If the spectral gap stays bounded away from zero as more primes
are added, this supports the strict convexity claim.
If it shrinks toward zero, there may be flat directions developing.
""")

# ============================================================
# FINAL VERDICT
# ============================================================

print("\n" + "=" * 70)
print("FINAL VERDICT ON GAUSSIAN VACUUM REPAIR")
print("=" * 70)

print("""
SUMMARY OF JEAN-PAUL'S LATEST PROPOSAL:

1. p-adic vacuum = Omega(|x|_p):
   - Correct. The characteristic function of Z_p is the natural
     local Schwartz function in Tate's thesis.
   - The Vladimirov eigenvalue on the unramified sector is zero
     (constant functions are in the null space of D^alpha on Z_p).
   - The higher eigenvalues involve (1-p^{-s}) factors.

2. Archimedean vacuum = e^{-pi x^2}:
   - This IS the canonical Schwartz function from Tate's thesis.
   - Its Mellin transform IS pi^{-s/2} Gamma(s/2).
   - BUT: the Mellin transform ≠ eigenvalue of Hessian.

3. Claim: <eta_f, H_inf eta_f> = integral |f_hat(t)|^2 Psi(1/4+it/2) dt:
   - FALSE for the standard GL Hessian (-(xd/dx)^2 + V_eff).
   - The eigenvalue is 1/4 + t^2 + const, never digamma.
   - The digamma appears in the LOG-DERIVATIVE of the Mellin
     transform, which is a categorically different quantity.

4. Claim: "resolvent trace of Hessian = log-derivative of Gamma":
   - This would require eigenvalues of H to be at the Gamma zeros,
     i.e., at s = 0, -1, -2, ... (poles of Gamma).
   - This is Connes' spectral interpretation program.
   - It was killed by the absorption spectrum problem.

GAP A STATUS: STILL OPEN.
The Gaussian vacuum produces the correct Gamma factors via
Tate's local zeta integral, but this is a Mellin transform
identity, not a Hessian eigenvalue identity.

GAP B STATUS: STILL OPEN.
The diagonal divergence sum_p c_p * 2I remains. Jean-Paul's
argument that "log(4pi) constant terms" from p-adic Hessians
cancel this is not verified.

KILL #10 ASSESSMENT:
The Route 3+2 fusion (H_GL = Weil distribution) has a beautiful
STRUCTURAL correspondence:
  - Glue cross-terms ↔ prime sums in Weil (verified)
  - Hecke eigenvalues ↔ p^{-s} factors (verified)

But the identification FAILS at the quantitative level:
  - Archimedean eigenvalue = quadratic (not logarithmic)
  - Diagonal = divergent (requires explicit-formula renormalization)

These are not minor corrections — they are the SAME OBSTACLES
that killed Connes' approach. The GL formulation reformulates
the problem but does not overcome it.

KILL #10: H_GL ↔ W(F,F) identification fails at archimedean place
          and at diagonal renormalization. The correspondence is
          structural but not quantitative.
""")

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: eigenvalue vs digamma
t_range = np.linspace(0.5, 80, 200)
quadratic = 0.25 + t_range**2
psi_vals = [float(mpmath.re(mpmath.digamma(mpmath.mpf('0.25') + 1j * mpmath.mpf(t) / 2))) for t in t_range]

axes[0].semilogy(t_range, quadratic, 'b-', linewidth=2, label=r'$\frac{1}{4} + t^2$ (Hessian eigenvalue)')
axes[0].semilogy(t_range, [max(p, 0.01) for p in psi_vals], 'r--', linewidth=2,
                 label=r'$\mathrm{Re}\,\Psi(\frac{1}{4} + \frac{it}{2})$ (Weil)')
axes[0].set_xlabel('$t$', fontsize=12)
axes[0].set_ylabel('Value', fontsize=12)
axes[0].set_title('Gap A: Hessian eigenvalue vs Weil kernel\n(Gaussian vacuum does NOT fix this)', fontsize=11)
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# Right: spectral gap vs primes
if gaps:
    n_primes = [g[0] for g in gaps]
    min_eigs = [g[1] for g in gaps]
    gap_vals = [g[2] for g in gaps]
    axes[1].plot(n_primes, min_eigs, 'bo-', markersize=8, linewidth=2, label=r'$\lambda_{\min}$')
    axes[1].plot(n_primes, gap_vals, 'rs-', markersize=8, linewidth=2, label=r'$\lambda_2 - \lambda_1$')
    axes[1].set_xlabel('Number of primes', fontsize=12)
    axes[1].set_ylabel('Eigenvalue', fontsize=12)
    axes[1].set_title('Spectral gap vs number of primes', fontsize=11)
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/sessions/clever-kind-hypatia/mnt/outputs/gaussian_vacuum_test.png',
            dpi=150, bbox_inches='tight')
print("\nPlot saved: gaussian_vacuum_test.png")

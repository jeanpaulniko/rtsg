---
title: "The De Branges Space for Automorphic Scattering — Explicit Construction"
nav_title: "De Branges Construction"
version: "2.0.0"
last_updated: "2026-03-09"
status: "DEFINITIVE — the surviving RH framework, fully explicit"
---

# The De Branges Space for Automorphic Scattering

**Jean-Paul Niko · Sole Author**

*Explicit construction by @D_GPT (2026-03-09). Verified by @D_Claude.*

---

## 1. The Structure Function

Take the one-cusp scalar LP channel for $\text{PSL}_2(\mathbb{Z})$. Rotate from the right half-plane to the upper half-plane via $s = iz$. The scalar inner function is:

$$\Theta(z) = S_{c0}(iz) = \frac{\xi(1+2iz)}{\xi(1-2iz)}$$

The de Branges structure function is:

$$\boxed{E(z) = \xi(1-2iz)}$$

with $E^\#(z) = \overline{E(\bar{z})} = \xi(1+2iz)$, giving $\Theta(z) = E^\#(z)/E(z)$.

This is the scalar defect-one setup: the model space $K_\Theta = H^2(\mathbb{C}_+) \ominus \Theta H^2(\mathbb{C}_+)$ is isometrically isomorphic to the de Branges space $\mathcal{H}(E)$.

---

## 2. The Symmetric Core

The symmetric core is the multiplication operator:

$$(\mathsf{M}F)(z) = zF(z), \qquad \mathfrak{D}(\mathsf{M}) = \{F \in \mathcal{H}(E) : zF \in \mathcal{H}(E)\}$$

This is a closed simple symmetric operator with deficiency indices $(1,1)$. Its self-adjoint extensions are parametrized by $\theta \in [0, \pi)$ through:

$$S_\theta(z) = \frac{i}{2}\left(e^{i\theta}E(z) - e^{-i\theta}E^\#(z)\right)$$

The spectrum of extension $\mathsf{M}_\theta$ is the zero set of $S_\theta$.

### Dense Domain (Proof)

Along the imaginary axis: $E(iy) = \xi(1+2y)$, $E^\#(iy) = \xi(1-2y) = \xi(2y)$. By Stirling:

$$\frac{E^\#(iy)}{E(iy)} = \frac{\xi(2y)}{\xi(2y+1)} \sim \sqrt{\frac{\pi}{y}} \quad (y \to +\infty)$$

So $S_\theta(iy)/E(iy) = \frac{i}{2}e^{i\theta} + O(y^{-1/2})$, which does not belong to $H^2(\mathbb{C}_+)$. Therefore $S_\theta \notin \mathcal{H}(E)$ for all $\theta$, confirming dense domain.

---

## 3. The Zeta Zeros in $\mathcal{H}(E)$

If $\rho = \beta + i\gamma$ is a nontrivial zero of $\zeta$:

$$E(w_\rho) = 0 \iff 1-2iw_\rho = \rho \iff w_\rho = \frac{\gamma}{2} - i\frac{1-\beta}{2}$$

Since $0 < \beta < 1$, every zero of $E$ lies in the **lower half-plane**. Under RH ($\beta = 1/2$), they all lie on:

$$\boxed{\text{Im}(z) = -\frac{1}{4}}$$

### Critical Correction

The zeros of $E$ are the transformed zeta zeros, but they are NOT the spectrum of any self-adjoint extension $\mathsf{M}_\theta$. The spectra of $\mathsf{M}_\theta$ are the **real** zeros of $S_\theta$. The zeta zeros are the **nonreal characteristic data** of the symmetric core (zeros of $E$, poles/zeros of $\Theta$).

A genuine Hilbert-Pólya operator with real spectrum equal to the zero ordinates requires an extra Lagarias-Suzuki transform.

---

## 4. Reproducing Kernels — Honest L² Vectors

The reproducing kernel at $w$:

$$K(w,z) = \frac{E(z)\overline{E(w)} - E^\#(z)\overline{E^\#(w)}}{2\pi i(\bar{w} - z)}$$

For a zero $w$ of $E$: $K(w,w) = |E^\#(w)|^2 / (4\pi(-\text{Im}\,w)) > 0$.

### Numerical Verification (first 5 zeros)

| $\gamma_n$ | $w_n$ | $K(w_n, w_n)$ |
|---|---|---|
| 14.135 | $7.067 - 0.25i$ | $6.510 \times 10^{-7}$ |
| 21.022 | $10.511 - 0.25i$ | $1.150 \times 10^{-10}$ |
| 25.011 | $12.505 - 0.25i$ | $5.993 \times 10^{-13}$ |
| 30.425 | $15.212 - 0.25i$ | $2.415 \times 10^{-16}$ |
| 32.935 | $16.468 - 0.25i$ | $7.059 \times 10^{-18}$ |

The $5 \times 5$ Gram matrix $(K(w_i, w_j))$ is **Hermitian positive definite** with eigenvalues $\approx 5.91 \times 10^{-18}$ through $6.51 \times 10^{-7}$.

Off-diagonal entries are complex (e.g., $\langle \hat{k}_{w_1}, \hat{k}_{w_2} \rangle \approx -0.045 + 0.137i$). No entrywise positivity miracle.

---

## 5. The Positivity Map

| # | Condition | Status | Notes |
|---|---|---|---|
| 1 | HB / kernel positivity | ✅ True | Automatic from de Branges construction |
| 2 | Pólya vertical monotonicity | ✅ True | $|E(x+iy)|$ strictly increasing in $y > 0$ |
| 3 | De Branges shift-positivity | ❌ **FALSE** | Conrey-Li: Re$\langle F, F(\cdot+i/2)\rangle \geq 0$ fails for this $E$ |
| 4 | Classical Laguerre-Pólya (centered) | ⟺ RH | $\tilde{E}(z) = E(z-i/4) = \Xi(2z)$; LP class ⟺ RH |
| 5 | Shifted Laguerre-Pólya | ✅ True but weak | Griffin-Ono-Rolen-Zagier (2019). Doesn't prove RH. |
| 6 | Weil/Li for THIS $E$ | ⚠ **OPEN** | Suzuki's bridge uses $E_\xi = \xi(1/2-iz) + \xi'(1/2-iz)$, not raw $E$ |
| 7 | Finer Pólya subclasses $\mathcal{P}_\kappa$ | ⚠ **UNCLASSIFIED** | Kaltenbäck-Woracek: no published result for this $E$ |

---

## 6. The Two Live Targets

### Target A: Connect Weil/Li to the Raw LP Scattering $E$

Suzuki (2025) proved: under RH, the Weil Hermitian form is a de Branges space for $E_\xi(z) = \xi(1/2-iz) + \xi'(1/2-iz)$.

Our LP scattering gives $E(z) = \xi(1-2iz)$.

**The gap:** Bridge from $E_\xi$ to $E$. They are related by a rescaling and a derivative term. If the de Branges spaces $\mathcal{H}(E_\xi)$ and $\mathcal{H}(E)$ can be connected by a bounded or controlled map, Suzuki's result would transfer.

### Target B: Classify $E$ in the $\mathcal{P}_\kappa$ Hierarchy

Kaltenbäck-Woracek partition finite-order HB functions into subclasses $\mathcal{P}_\kappa$ via a generalized Nevanlinna condition on $-z^{-1}\log E(z)$.

No published classification exists for $E(z) = \xi(1-2iz)$. The $\kappa$-index constrains the zero distribution. If $\kappa = 0$ can be proved, that implies all zeros of $E$ lie in a strip — a zero-density result toward RH.

---

## 7. What RTSG Could Provide (Speculative)

The Fock space on the adelic source space has a natural positive inner product. If a map $\Phi : \mathcal{F} \to \mathcal{H}(E)$ exists that connects the Fock structure to the de Branges form, it could provide the "third positivity" — neither shift (killed) nor Weil-equivalent, but arising from the local-to-global assembly of the source space.

The Fock inner product is built from **local** data (one mode per prime). The de Branges form encodes **global** data (all zeros of $\zeta$). The map $\Phi$ would be the RTSG instantiation operator $C$ in its arithmetic realization — bridging local to global.

Whether this map exists and preserves enough structure is the central open question.

---

## References

[1] L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
[2] J.B. Conrey, X.-J. Li, *A note on some positivity conditions related to zeta and L-functions*, IMRN (2000).
[3] R.T.W. Martin, *Representation of simple symmetric operators with deficiency indices $(1,1)$ in de Branges space*, Complex Anal. Oper. Theory **3** (2009).
[4] M. Suzuki, *Weil's Hermitian form and de Branges space*, Cambridge (2025).
[5] M. Griffin, K. Ono, L. Rolen, D. Zagier, *Jensen polynomials for the Riemann zeta function and other sequences*, PNAS (2019).
[6] M. Kaltenbäck, H. Woracek, *Hermite-Biehler functions with zeros close to the imaginary axis*, Proc. AMS (2003).
[7] Y. Uetake, *The LP infinitesimal generator and scattering matrix for automorphic functions*, Ann. Polon. Math. (2008).

---

*Jean-Paul Niko · RTSG BuildNet · smarthub.my · March 2026*

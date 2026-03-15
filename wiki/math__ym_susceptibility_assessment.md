
# Susceptibility Bound for 4D SU(2) Polyakov Loops — Honest Assessment
**Date:** 2026-03-08  
**Model:** SU(2) lattice gauge theory on \(\Lambda=(\mathbb Z/L\mathbb Z)^3\times (\mathbb Z/N_t\mathbb Z)\) with Wilson action

## Verdict

The statement

\[
\chi(\beta)=\sum_{\mathbf x\in\Lambda_s}\Big(\langle W^*(\mathbf x)W(\mathbf 0)\rangle-|\langle W\rangle|^2\Big)\le f(\beta)<\infty
\]

for **all** couplings \(\beta\) in the infinite-volume limit \(L\to\infty\) is **false as stated** for fixed finite \(N_t\).

Reason: fixed \(N_t\) is a **finite-temperature** problem. Pure 4D SU(2) has a deconfinement transition, in the universality class of the 3D Ising model, and the Polyakov-loop susceptibility diverges at the transition. With the center-symmetric finite-volume definition \(\langle W\rangle=0\), it also diverges throughout the broken/deconfined phase.

## Phase-by-phase statement

### 1. Strong coupling / confined phase (\(\beta\) small)
Here the strong-coupling expansion gives exponential decay of the Polyakov-loop correlator, hence finite \(\chi\). This is the regime already under control.

### 2. Critical coupling (\(\beta=\beta_c(N_t)\))
For fixed \(N_t\), SU(2) has a second-order deconfinement transition with 3D-Ising critical behavior. Therefore
\[
\chi_L(\beta_c)\sim L^{\gamma/\nu},
\qquad
\chi(\beta)\sim |\beta-\beta_c|^{-\gamma}
\]
in infinite volume. So \(\chi\) is **not** finite at \(\beta_c\).

### 3. Deconfined phase (\(\beta>\beta_c(N_t)\))
In finite volume, exact center symmetry forces \(\langle W\rangle_L=0\). But in the broken phase there are pure states with
\[
\langle W\rangle_\pm = \pm m(\beta),\qquad m(\beta)>0.
\]
The center-symmetric periodic state is the mixture \(\frac12(\langle\cdot\rangle_+ + \langle\cdot\rangle_-)\), so by clustering in pure phases
\[
\lim_{|\mathbf x|\to\infty}\langle W^*(\mathbf x)W(\mathbf 0)\rangle = m(\beta)^2.
\]
Hence, for large \(L\),
\[
\chi_L(\beta)\ge (m(\beta)^2-\varepsilon)\big(L^3-C_\varepsilon\big)\to\infty.
\]
So with the user's definition, \(\chi_L\) diverges like the spatial volume in the deconfined phase.

If instead one works in a selected pure phase and subtracts \(m(\beta)^2\), then the connected susceptibility is expected finite away from \(\beta_c\), but that is a **different observable**.

## Where each proposed proof route fails

### A. Infrared-bound route
An infrared bound would have schematic form
\[
\widehat G(\mathbf p)\le \frac{C}{m(\beta)^2+\widehat p^2}.
\]
At \(\mathbf p=0\), finiteness of \(\chi=\widehat G(0)\) requires \(m(\beta)>0\). But that is exactly the missing screening-mass / gap input. At the critical point \(m(\beta_c)=0\), so this route cannot prove a uniform all-\(\beta\) bound. It is equivalent to proving you are away from criticality.

### B. Reflection positivity + monotonicity
Reflection positivity gives positivity and useful inequalities, but it does **not** prevent a divergent zero-momentum mode. It is compatible with both spontaneous symmetry breaking and critical divergence. So it cannot yield a uniform bound on \(\chi\) across the phase transition.

### C. Center symmetry
Exact \(\mathbb Z_2\) symmetry only implies \(\langle W\rangle_L=0\) on a finite torus. It does **not** imply finite susceptibility. In fact, in the broken phase that exact symmetry makes the symmetric susceptibility larger, because the disconnected piece \(m(\beta)^2\) is not subtracted.

## The exact place the Ising analogy breaks
It does **not** break. Properly applied, it predicts the opposite of the desired theorem.

The correct analogy is:

- confined phase \(\leftrightarrow\) disordered 3D Ising phase: finite \(\chi\),
- deconfinement point \(\leftrightarrow\) Ising critical point: divergent \(\chi\),
- deconfined symmetric mixture \(\leftrightarrow\) Ising low-temperature mixed state: volume-divergent \(\chi\).

So the desired “finite for all couplings” statement is incompatible with the very analogy being invoked.

## Consequence for the Clay Yang–Mills route
Even proving finite \(\chi\) for fixed finite \(N_t\) would only control a **thermal screening** observable. The Clay problem is the zero-temperature 4D continuum mass gap. That means the susceptibility route is, at best, a confined-phase input; it is not the endgame.

The current RTSG/YM route is therefore correctly stated as:
- UV side: Balaban multiscale construction,
- IR side: Polyakov/GL effective action,
- missing theorem: a uniform positive curvature statement such as \(V_L''(0)>0\) in the correct zero-temperature scaling limit.

## Bottom line

\[
\boxed{\text{No unconditional all-coupling bound exists for the susceptibility as defined at fixed finite }N_t.}
\]

The proof fails because the claim itself is false in the thermal setup:
- finite in strong coupling,
- divergent at the deconfinement point,
- and, with the symmetric definition, divergent throughout the broken phase.

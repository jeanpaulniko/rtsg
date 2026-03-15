---
title: "Instantiation Cost Functional — Coordinate Computations"
nav_title: "Cost Functional"
version: "1.0.0"
last_updated: "2026-03-09"
status: "ACTIVE — concrete computations for CS Operator Theory §5"
---

# Instantiation Cost Functional — Coordinate Computations

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    The CS Operator Theory defines $\mathcal{E}(\psi) = \langle \psi, (I - C^*C)\psi \rangle$ abstractly. This page computes it explicitly for four systems: harmonic oscillator, hydrogen atom, free scalar field, and Yang-Mills vacuum. The goal: turn the abstract cost into numbers that connect to experiment or to the Millennium Problems.

---

## 1. The Cost Functional (Review)

For a state $\psi \in \mathcal{H}_Q$, the instantiation cost is:

$$\boxed{\mathcal{E}(\psi) = \|\psi\|_Q^2 - \|C\psi\|_P^2 = \langle \psi, (I - C^*C)\psi \rangle}$$

In the SVD basis $C\psi_n = \sigma_n \phi_n$:

$$\mathcal{E}(\psi) = \sum_n (1 - \sigma_n^2) |\langle \psi, \psi_n \rangle|^2$$

- $\sigma_n = 1$: zero cost (perfect instantiation)
- $\sigma_n = 0$: maximum cost (mode is in $\ker(C)$ — dark sector)
- $0 < \sigma_n < 1$: partial cost (lossy projection)

---

## 2. Harmonic Oscillator

### 2.1 Setup

The quantum harmonic oscillator with Hamiltonian $H = \frac{1}{2}(p^2 + \omega^2 x^2)$ in natural units ($\hbar = m = 1$).

Energy eigenstates: $|n\rangle$ with $E_n = \omega(n + \frac{1}{2})$.

### 2.2 RTSG Identification

The QS states are the full Hilbert space $\mathcal{H}_Q = L^2(\mathbb{R})$. The PS states are classical phase-space distributions — Wigner functions that are non-negative (classical limit).

The instantiation operator $C$ maps quantum states to their classical shadows. The natural candidate: **the Husimi projection** (coherent-state representation):

$$C|n\rangle = Q_n(x, p) = |\langle \alpha | n \rangle|^2, \qquad \alpha = \frac{x + ip}{\sqrt{2}}$$

The Husimi function $Q_n$ is a smoothed Wigner function — always non-negative, always classical. The smoothing loses quantum information.

### 2.3 Singular Values

The overlap between the $n$-th energy eigenstate and a coherent state $|\alpha\rangle$ is:

$$\langle \alpha | n \rangle = \frac{\alpha^n}{\sqrt{n!}} e^{-|\alpha|^2/2}$$

The norm of the Husimi function:

$$\|Q_n\|^2 = \int |Q_n(x,p)|^2 \, \frac{dx\,dp}{2\pi} = \frac{1}{2^n \cdot n! \cdot \sqrt{\pi}} \cdot \frac{(2n)!}{2^n \cdot n!}$$

For the ground state ($n=0$): $\|Q_0\|^2 = \frac{1}{\sqrt{\pi}} \int e^{-2|\alpha|^2} d^2\alpha = \frac{1}{2}$.

Since $\||0\rangle\|^2 = 1$, the singular value for the ground state is:

$$\sigma_0^2 = \|C|0\rangle\|^2 / \||0\rangle\|^2 = \frac{1}{2}$$

$$\boxed{\sigma_0 = \frac{1}{\sqrt{2}} \approx 0.707}$$

### 2.4 Cost for Each Level

For the $n$-th level, the singular value (from the Husimi $L^2$ norm) scales as:

$$\sigma_n^2 \sim \frac{1}{\sqrt{4\pi n}} \quad \text{for large } n \quad (\text{Stirling})$$

So the instantiation cost grows with excitation:

$$\mathcal{E}(|n\rangle) = 1 - \sigma_n^2 \approx 1 - \frac{1}{\sqrt{4\pi n}}$$

| State | $\sigma_n^2$ | $\mathcal{E}$ | Interpretation |
|---|---|---|---|
| $\|0\rangle$ (vacuum) | 0.500 | 0.500 | Half the quantum info survives classical projection |
| $\|1\rangle$ | 0.375 | 0.625 | First excitation: more quantum, higher cost |
| $\|10\rangle$ | $\sim 0.089$ | $\sim 0.911$ | Highly excited: mostly quantum, expensive to instantiate |
| $\|n \to \infty\rangle$ | $\to 0$ | $\to 1$ | Fully quantum: instantiation cost approaches maximum |

**Physical meaning:** Excited states are "more quantum" and cost more to instantiate into the classical world. The ground state is the cheapest to instantiate — it has the highest singular value. This is the harmonic oscillator's version of "gravity is Stage 0" — the ground state (vacuum, minimal complexity) instantiates with maximum efficiency.

---

## 3. Hydrogen Atom

### 3.1 Setup

Bound states $|n, \ell, m\rangle$ with $E_n = -13.6/n^2$ eV.

### 3.2 RTSG Identification

$C$ maps the quantum wave function $\psi_{n\ell m}(\mathbf{r})$ to its classical counterpart — the probability density $|\psi_{n\ell m}|^2$ interpreted as a classical charge distribution.

The loss: quantum phase information $\arg(\psi)$ is destroyed. Coherences between different $(\ell, m)$ components are lost.

### 3.3 Singular Values by Quantum Numbers

The singular value depends on how "classical" the orbital is:

$$\sigma_{n\ell m}^2 \propto \frac{\text{classical content of } |n\ell m\rangle}{\text{total content}}$$

For circular orbits ($\ell = n-1$, maximum angular momentum): the Bohr correspondence says these are the most classical. The wave function concentrates on a thin shell at $r = n^2 a_0$, resembling a classical orbit.

$$\sigma_{n, n-1, m}^2 \sim 1 - O(1/n) \quad \text{(approaches 1 for large } n\text{)}$$

For $s$-orbitals ($\ell = 0$): the wave function has a node at the origin, penetrates the nucleus, has no classical analogue.

$$\sigma_{n, 0, 0}^2 \sim 1/n \quad \text{(drops to 0 for large } n\text{)}$$

| State | Classical analogue | $\sigma^2$ (estimate) | $\mathcal{E}$ |
|---|---|---|---|
| $1s$ | None (fully quantum) | $\sim 0.3$ | $\sim 0.7$ |
| $2p$ ($\ell=1$) | Elliptical orbit | $\sim 0.5$ | $\sim 0.5$ |
| $n, n-1$ (circular) | Bohr orbit | $\to 1$ | $\to 0$ |
| Rydberg ($n \gg 1$, $\ell = 0$) | None | $\to 0$ | $\to 1$ |

**The Bohr correspondence as an instantiation statement:** Circular Rydberg orbits have $\sigma \to 1$ — they instantiate almost perfectly. The $1s$ ground state, despite being lowest energy, is deeply quantum ($\sigma \sim 0.5$). Energy and instantiation cost are **not** the same — the most quantum state is not the most energetic.

---

## 4. Free Scalar Field (QFT)

### 4.1 Setup

Free massive scalar field $\phi$ with Hamiltonian $H = \int d^3k \, \omega_k (a_k^\dagger a_k + \frac{1}{2})$, $\omega_k = \sqrt{k^2 + m^2}$.

### 4.2 RTSG Identification

$\mathcal{H}_Q$ = Fock space. $\mathcal{H}_P$ = classical field configurations. $C$ maps quantum field states to their classical expectation values:

$$C |\psi\rangle = \langle \psi | \hat{\phi}(x) | \psi \rangle = \phi_{\text{cl}}(x)$$

The vacuum $|0\rangle$ maps to $\phi_{\text{cl}} = 0$. A coherent state $|\alpha_k\rangle$ maps to $\phi_{\text{cl}}(x) = \int \alpha_k e^{ikx} d^3k$ — a classical wave.

### 4.3 Cost per Mode

Each mode $k$ is an independent harmonic oscillator. From §2:

$$\sigma_k^2(\text{vacuum}) = \frac{1}{2} \quad \text{for each mode}$$

The total vacuum cost (summed over modes) diverges:

$$\mathcal{E}(\text{vacuum}) = \sum_k (1 - \sigma_k^2) = \sum_k \frac{1}{2} = \infty$$

This is the **UV divergence of vacuum instantiation cost**. In QFT language: the vacuum has infinite zero-point energy. In RTSG language: it costs infinite energy to instantiate the full vacuum because there are infinitely many quantum modes that each lose half their content upon classical projection.

### 4.4 Renormalization as Instantiation Regularization

Renormalization subtracts the vacuum cost: $\mathcal{E}_{\text{ren}}(\psi) = \mathcal{E}(\psi) - \mathcal{E}(|0\rangle)$.

$$\mathcal{E}_{\text{ren}}(|1_k\rangle) = (1 - \sigma_{k,1}^2) - (1 - \sigma_{k,0}^2) = \sigma_{k,0}^2 - \sigma_{k,1}^2 = \frac{1}{2} - \frac{3}{8} = \frac{1}{8}$$

**RTSG reading of renormalization:** We don't measure absolute instantiation cost; we measure *relative* cost against the vacuum. Renormalization is not a trick — it's the statement that PS only detects *differences* in instantiation cost, not the absolute cost.

⚠ Connection to Hilbert-Schmidt conjecture (CS Operator Theory §5.1): the divergence of $\sum_k (1 - \sigma_k^2)$ suggests $C$ is **not** Hilbert-Schmidt for a free field. The Hilbert-Schmidt conjecture may need a renormalized version: $(I - C^*C)_{\text{ren}}$ is trace-class after vacuum subtraction.

---

## 5. Yang-Mills Vacuum

### 5.1 Setup

$SU(N)$ Yang-Mills theory on a lattice $\Lambda$ with spacing $a$, coupling $g$, and Wilson action $S_W = \frac{2N}{g^2} \sum_{\square} (1 - \frac{1}{N} \text{Re Tr } U_\square)$.

### 5.2 RTSG Identification

$\mathcal{H}_Q$ = gauge-invariant wave functionals $\Psi[A]$. $\mathcal{H}_P$ = classical gauge configurations (solutions to the YM equations of motion). $C$ projects quantum gauge field onto classical background:

$$C|\Psi\rangle = A_{\text{cl}}^{\mu} = \langle \Psi | \hat{A}^{\mu} | \Psi \rangle$$

### 5.3 The Mass Gap from the Cost Functional

The YM vacuum $|0_{\text{YM}}\rangle$ has $C|0_{\text{YM}}\rangle = 0$ (the classical vacuum is zero field). The first excited state $|1_{\text{YM}}\rangle$ is a glueball with mass $\Delta_{\text{YM}}$.

The cost difference between first excited state and vacuum:

$$\mathcal{E}_{\text{ren}}(|1_{\text{YM}}\rangle) = \sigma_{0}^2 - \sigma_{1}^2$$

In the GL framework, the action near the minimum is:

$$S[W] \approx S[W_0] + \int \left[|\partial \delta W|^2 + 2\alpha |\delta W|^2\right] d\mu$$

The linearized operator $L = -\nabla^2 + 2\alpha$ has spectral gap $2\alpha$. If $L$ is the linearization of $I - C^*C$ around the vacuum:

$$\sigma_0^2 - \sigma_1^2 = 2\alpha$$

$$\boxed{\Delta_{\text{YM}} = \sqrt{2\alpha} = \sqrt{\sigma_0^2 - \sigma_1^2}}$$

The mass gap is the square root of the gap in the instantiation cost spectrum.

### 5.4 Numerical Estimate

From the engine's lattice data (L=12, β=2.5):

- Mass gap $\Delta \approx 0.37$ (lattice units)
- String tension $\sigma_{\text{str}} \approx 0.045$

If $\Delta = \sqrt{2\alpha}$, then $\alpha \approx 0.068$ in lattice units.

The GL parameter $\alpha$ is the curvature of the instantiation potential at its minimum. It is positive whenever the vacuum is stable — which is the **existence** of the mass gap. The **magnitude** of $\alpha$ is determined by the non-perturbative dynamics of confinement.

⚠ Conjecture. The identification $L = $ linearization of $I - C^*C$ requires proving that the GL action is the effective action for the CS operator restricted to the gauge sector. This is YM Task 2 assigned to @D_GPT.

---

## 6. Summary Table

| System | Ground state $\sigma_0^2$ | First excited $\sigma_1^2$ | Renorm. gap | Physical meaning |
|---|---|---|---|---|
| Harmonic oscillator | $1/2$ | $3/8$ | $1/8$ | Quantum → classical smoothing |
| Hydrogen ($1s$) | $\sim 0.3$ | $\sim 0.5$ ($2p$) | $\sim -0.2$ (!) | $s$-orbitals more quantum than $p$ |
| Free scalar (per mode) | $1/2$ | $3/8$ | $1/8$ | Same as HO; UV divergence in total |
| Yang-Mills vacuum | $\sigma_0^2$ | $\sigma_0^2 - 2\alpha$ | $2\alpha$ | Mass gap = cost gap |

**Note on hydrogen:** $\sigma_{2p} > \sigma_{1s}$ — the first excited state is *more* classical than the ground state! The $2p$ orbital has a classical analogue (elliptical orbit); the $1s$ does not. This shows that energy ordering and instantiation ordering are different. The cheapest-to-instantiate state is not always the lowest-energy state.

---

## 7. Connection to Thermodynamics

The total instantiation cost for a thermal ensemble at temperature $T$:

$$\mathcal{E}(T) = \sum_n (1 - \sigma_n^2) \, p_n(T), \qquad p_n = \frac{e^{-E_n/T}}{Z(T)}$$

At high $T$: all modes populated equally, $\mathcal{E} \to 1 - \overline{\sigma^2}$ (average cost).
At low $T$: only ground state, $\mathcal{E} \to 1 - \sigma_0^2$ (minimum cost).

**The third law of instantiation:** As $T \to 0$, the system approaches the state of minimum instantiation cost. This is the RTSG reading of the third law of thermodynamics — the ground state is the most efficiently instantiable state.

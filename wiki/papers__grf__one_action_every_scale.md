# One Action at Every Scale
## A single Euclidean horizon EFT for \(\kappa\) and \(H\)

**Jean-Paul Niko** · 2026 Gravity Research Foundation Essay  
*Repaired draft after adversarial review*

---

## Abstract

We propose a covariant Ginzburg–Landau effective theory for a complex scalar \(W\) whose **Euclidean horizon sector** yields the characteristic rate of any stationary gravitational horizon. Starting from the Lorentzian action
\[
S_L[W]=\int d^4x\,\sqrt{-g}\left[-g^{\mu\nu}\nabla_\mu \bar W \nabla_\nu W - m_R^2|W|^2 - \frac{\beta}{2}|W|^4\right],
\]
we Wick-rotate to a Euclidean background with thermal period \(\beta_h=2\pi/\kappa_h\), where \(\kappa_h\) is the horizon surface gravity. Bosonic periodicity then quantizes Euclidean frequencies as \(\omega_n=n\kappa_h\). The slowest time-dependent mode has rate
\[
\Gamma_h=\sqrt{m_R^2+\kappa_h^2},
\]
which reduces to \(\Gamma_h=\kappa_h\) in the critical regime \(m_R\ll \kappa_h\). For black-hole horizons this recovers the geometric rate \(\kappa\); for de Sitter horizons, where \(\kappa_h=H\), it yields the cosmological rate \(H\). The proposal unifies the rates kinematically. It does **not** claim a solution of the cosmological-constant problem.

## 1. Two gravitational rates, one thermal mechanism

Black-hole horizons and de Sitter horizons are the two clean cases in gravitation where a horizon carries an intrinsic temperature. For a stationary black hole,
\[
T_{\rm BH}=\frac{\kappa}{2\pi},
\]
while for de Sitter space,
\[
T_{\rm dS}=\frac{H}{2\pi}.
\]
The first rate \(\kappa\) controls black-hole thermodynamics and sets the scale that enters the Maldacena–Shenker–Stanford bound \(\lambda_L\le 2\pi T\). The second rate \(H\) sets the thermal scale of the de Sitter horizon.

The question of this essay is narrower than the original draft: **can one covariant effective action produce the characteristic horizon rate in both settings by the same boundary mechanism?** The answer proposed here is yes. The mechanism is not “vacuum energy \(=T_{\rm CMB}^4\)” and it is not “gravity is confined.” It is the Euclidean thermal circle of a horizon.

## 2. Covariant action and Euclidean horizon sector

Take \(W:\mathcal M\to\mathbb C\) to be a complex scalar field on spacetime with Lorentzian action
\[
S_L[W]=\int d^4x\,\sqrt{-g}\left[-g^{\mu\nu}\nabla_\mu \bar W \nabla_\nu W - m_R^2|W|^2 - \frac{\beta}{2}|W|^4\right]. \tag{1}
\]
Here \(m_R\) is the renormalized quadratic coefficient and \(\beta>0\) stabilizes the theory. We do **not** identify \(W\) with the graviton. \(W\) is an order-parameter EFT defined on spacetime.

Now pass to the Euclidean section of a stationary horizon background. Regularity of the Euclidean metric fixes the imaginary-time period to
\[
\beta_h=\frac{2\pi}{\kappa_h}, \tag{2}
\]
where \(\kappa_h\) is the horizon surface gravity. Expand the bosonic field in Matsubara modes,
\[
W(\tau,x)=\sum_{n\in\mathbb Z} e^{i\omega_n \tau} W_n(x),\qquad \omega_n=\frac{2\pi n}{\beta_h}=n\kappa_h. \tag{3}
\]
The quadratic Euclidean kernel acting on mode \(n\) is
\[
\mathcal K_n=-\nabla_{\Sigma}^2+m_R^2+n^2\kappa_h^2, \tag{4}
\]
where \(\Sigma\) is the spatial section of the Euclidean horizon geometry.

For the homogeneous mode on \(\Sigma\), the lowest spatial eigenvalue is \(\lambda_0=0\). The slowest **time-dependent** fluctuation is therefore the \(n=1\) mode, with rate
\[
\Gamma_h=\sqrt{m_R^2+\kappa_h^2}. \tag{5}
\]
Equation (5) is the central derived statement of this essay. It is not a guess and it is not an identification-by-analogy. It is the lowest nonzero Euclidean thermal frequency dressed by the renormalized mass.

In the critical regime,
\[
m_R\ll \kappa_h,
\]
one finds
\[
\Gamma_h=\kappa_h\left[1+\frac{m_R^2}{2\kappa_h^2}+O\!\left(\frac{m_R^4}{\kappa_h^4}\right)\right]. \tag{6}
\]
Thus the geometric horizon rate is recovered as the leading term of a controlled EFT expansion.

## 3. Black-hole regime

For a stationary black hole, \(\kappa_h=\kappa\), so Eq. (5) becomes
\[
\Gamma_{\rm BH}=\sqrt{m_R^2+\kappa^2}. \tag{7}
\]
In the critical limit \(m_R\ll \kappa\), this reduces to \(\Gamma_{\rm BH}\approx\kappa\).

This has an immediate consequence for any proposal that uses a horizon processing rate. If one adopts the kinematic clock
\[
t_{\rm kin}:=\frac{S_{\rm Wald}}{\Gamma_{\rm BH}}, \tag{8}
\]
then the standard horizon expression
\[
t_{\rm kin}\to \frac{S_{\rm Wald}}{\kappa} \tag{9}
\]
is recovered in the critical regime.

The logic is now clean. The GL action does **not** directly derive the Bekenstein–Hawking or Wald entropy. General relativity gives \(S_{\rm Wald}\). The EFT supplies the rate \(\Gamma_{\rm BH}\). Their ratio defines the kinematic clock. This is all that is claimed.

It is also important to say what is **not** claimed. Equation (7) is not a quasinormal-mode spectrum, not a proof of scrambling saturation, and not a derivation of the black-hole information flux. It is the slowest thermal rate of the Euclidean horizon EFT. Any identification with specific ringdown observables would require a separate perturbation analysis.

## 4. de Sitter regime

For an exact de Sitter static patch, the cosmological horizon has surface gravity
\[
\kappa_h=H,
\]
so the same EFT yields
\[
\Gamma_{\rm dS}=\sqrt{m_R^2+H^2}. \tag{10}
\]
In the same critical regime \(m_R\ll H\),
\[
\Gamma_{\rm dS}\approx H. \tag{11}
\]
This is the cosmological half of the unification. The same action, the same Euclidean thermal circle, and the same mode decomposition produce the black-hole rate \(\kappa\) and the de Sitter rate \(H\).

This statement must be restricted carefully. Generic FRW cosmologies do **not** have an exact equilibrium horizon temperature. The de Sitter claim therefore applies to exact de Sitter space and, at most, to adiabatically quasi-de Sitter regimes where \( |\dot H| \ll H^2\). The essay does not claim that an arbitrary cosmological background has a well-defined horizon thermal circle.

Just as important, this essay does **not** claim that the present dark-energy density is thermal radiation of the \(W\) field. That route confuses a horizon temperature with a cosmological fluid. The present claim is purely kinematic: **once a de Sitter phase exists, its characteristic rate \(H\) is generated by the same Euclidean EFT mechanism that generates \(\kappa\) for black holes.**

## 5. What the model predicts

The repaired proposal makes three sharp statements.

**(i) Universal horizon deformation law.**
For any stationary horizon in the EFT regime,
\[
\Gamma_h^2-\kappa_h^2=m_R^2. \tag{12}
\]
The same renormalized mass \(m_R\) must control departures from the pure geometric rate in every background.

**(ii) Recovery of the one-rate law is conditional, not exact.**
The commonly used horizon law \(\Gamma_h=\kappa_h\) is not fundamental. It is the critical limit of Eq. (5). The first correction is
\[
\Gamma_h-\kappa_h=\frac{m_R^2}{2\kappa_h}+O\!\left(\frac{m_R^4}{\kappa_h^3}\right). \tag{13}
\]
Thus the strongest deviations should occur in low-temperature or near-extremal regimes.

**(iii) The same thermal mechanism governs black-hole and de Sitter horizons.**
The black-hole side and the de Sitter side are not separate assumptions. They are the same Matsubara construction on two different gravitational backgrounds.

## 6. Why the old claims were cut

The previous draft failed because it overclaimed three things.

First, it treated the Hawking temperature at infinity as a local horizon temperature. That is false. The local Tolman temperature near a stationary horizon is redshifted and becomes singular as the horizon is approached.

Second, it tried to identify today’s dark-energy density with a thermal \(T^4\) contribution of a \(W\) field. That does not give a cosmological constant; it gives a radiation-like contribution.

Third, it claimed that gravity is weak because the \(W\) field has a large gap and that this gap implies graviton confinement. None of that follows from Eq. (1). Those claims have been removed.

The present essay survives because it says less and derives more.

## 7. Conclusion

A single covariant Ginzburg–Landau EFT for a complex scalar \(W\) has a Euclidean horizon sector with thermal period \(\beta_h=2\pi/\kappa_h\). Bosonic periodicity then forces the lowest time-dependent mode to carry rate
\[
\Gamma_h=\sqrt{m_R^2+\kappa_h^2}.
\]
In the critical regime this reduces to the geometric horizon rate:
\[
\Gamma_h\approx\kappa_h.
\]
For black-hole horizons, \(\kappa_h=\kappa\). For de Sitter horizons, \(\kappa_h=H\). The same action therefore yields the characteristic gravitational rate in both regimes by the same mechanism: the Euclidean thermal circle of the horizon.

This is not a solution of the cosmological-constant problem and not a theory of graviton confinement. It is a simpler and harder claim: **one Euclidean horizon action, two gravitational rates**.

## References

[1] R. M. Wald, “The Thermodynamics of Black Holes,” *Living Rev. Relativ.* **4**, 6 (2001), arXiv:gr-qc/9912119.

[2] G. W. Gibbons and S. W. Hawking, “Cosmological Event Horizons, Thermodynamics, and Particle Creation,” *Phys. Rev. D* **15**, 2738 (1977).

[3] L. Dolan and R. Jackiw, “Symmetry Behavior at Finite Temperature,” *Phys. Rev. D* **9**, 3320 (1974).

[4] J. Maldacena, S. H. Shenker, and D. Stanford, “A Bound on Chaos,” *JHEP* **08**, 106 (2016), arXiv:1503.01409.

[5] P. C. W. Davies, “Cosmological Event Horizons, Entropy and Quantum Particles,” *Ann. Inst. Henri Poincaré Phys. Théor.* **49**, 297 (1988).
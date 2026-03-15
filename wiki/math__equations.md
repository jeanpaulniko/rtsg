# RTSG Equations Reference

## Fundamental Equations

### GL Action (Master Equation)

$$S[W] = \int \left(|\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4\right) d\mu$$

The Ginzburg–Landau action governing the will field $W$ on all three co-primordial spaces. $\alpha$ controls the phase (ordered vs disordered), $\beta$ controls nonlinear self-interaction.

### Intelligence Equation

$$U = \frac{V}{E \times T}$$

Understanding = Value / (Energy × Time). The cognitive efficiency metric.

### Will Field Equation of Motion

$$-\nabla^2 W + \alpha W + \beta |W|^2 W = 0$$

Euler–Lagrange equation from the GL action. Nonlinear Schrödinger-type on CS.

## Spectral Equations

### Graph Laplacian

$$L = D - A$$

where $D$ is the degree matrix and $A$ is the adjacency matrix. Eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$.

### Fiedler Value (Algebraic Connectivity)

$$\lambda_2(L) = 0.0653$$

Second-smallest eigenvalue of $L$. Measures how well-connected the graph is. Related to the Cheeger constant by:

$$\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2\lambda_2}$$

### Spectral Radius

$$\mu_1 = \max |\lambda_k(A)| = 1728.6 \approx 12^3$$

Connection to the modular discriminant $\Delta(\tau)$ of weight-12 cusp forms.

### Graph Energy

$$E(G) = \sum_k |\lambda_k(A)| = 5{,}466$$

## Topological Equations

### Betti Numbers

$$\beta_0 = 765, \quad \beta_1 = 2{,}065$$

$\beta_0$ = connected components, $\beta_1$ = independent cycles.

### Euler Characteristic

$$\chi = \sum_{k} (-1)^k \beta_k = V - E + F = 1$$

### Heat Kernel Trace

$$K(t) = \text{tr}(e^{-tL}) = \sum_{i=1}^{n} e^{-t\lambda_i}$$

| $t$ | $K(t)$ | Active Modes |
|---|---|---|
| 0.1 | 794.6 | Nearly all modes active |
| 1.0 | 178.3 | Fast modes dominate |
| 5.0 | 10.8 | Only persistent structure |
| $\infty$ | $\beta_0$ | Connected components only (Spinoza's God) |

## Coherence Equations

### Coherence Matrix

$$C_{ij} = \langle W_i | W_j \rangle_{CS}$$

Symmetric positive semi-definite matrix. Eigenvalues $\{\lambda_k\}$ determine the coherence spectrum.

### Coherence Score

$$\kappa = \frac{\lambda_{\min}}{\lambda_{\max}}$$

- $\kappa > 0.7$: Integrated
- $0.4 < \kappa \leq 0.7$: Intermediate
- $\kappa \leq 0.4$: Fragmented

### Fragmentation Count

$$F = |\{k : \lambda_k < \epsilon\}|$$

Number of eigenvalues below threshold $\epsilon$ (default 0.5). Each represents a dissociated mode.

### Dissociation Criterion

$$\lambda_k \to 0 \implies \text{block diagonalization of } C \implies \text{DID structure}$$

## BRST Equations

### BRST Charge

$$Q^2 = 0, \quad [Q, H] = 0$$

Nilpotent, commutes with the Hamiltonian.

### Physical State Condition

$$Q|\psi\rangle = 0, \quad |\psi\rangle \not\sim Q|\chi\rangle$$

States are $Q$-closed but not $Q$-exact.

### Gauge-Fixed Action

$$S_{\text{gf}} = S[W] + \{Q, \Psi\}$$

where $\Psi$ is the gauge-fixing fermion (the choice of Grothendieck filter).

## Filter Equations

### Idempotence

$$\mathcal{F} \circ \mathcal{F} = \mathcal{F}$$

Every Grothendieck filter is idempotent — applying it twice is the same as applying it once.

### Negative Space

$$\text{neg}(\mathcal{F}) = \ker(\mathcal{F})$$

The topology of what the filter removes.

### Conceptual Irreversibility

$$S(\mathcal{F}(X)) \geq S(X)$$

Entropy increases under filter application. Some collapses are thermodynamically irreversible.

## Polynomial Invariants

### F₂ Survival Rate

$$\sigma_{F_2} = \frac{|\{e : w(e) \not\equiv 0 \pmod{2}\}|}{|E|} = 43.5\%$$

### Complex Phase Statistics

$$\text{mean phase} = 52.6°, \quad \text{variance} = 2.71$$

### p-adic Valuation

$$\nu_2(\text{weights}): \text{mean} = 0.73, \quad \max = 6$$

## Relation Shape Spectrum

The 34 × 34 relation-to-relation adjacency matrix has eigenvalues:

$$\mu_1^{(2)} = 119.9, \quad \mu_2^{(2)} = 7.0, \quad \ldots, \quad \mu_{34}^{(2)} = -47.9$$

33 independent relationship shapes exist (dimension of the relation shape space).

## See Also

- [Definitions](definitions.md)
- [RTSG Index](rtsg_index.md)
- [CS Mechanics](cs_mechanics.md)
- [Graded BRST](graded_brst.md)
- [K-Matrix](k_matrix.md)

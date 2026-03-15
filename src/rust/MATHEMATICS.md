# Mathematical Foundations

## P-adic Numbers and Q_p

The p-adic numbers Q_p form a complete metric space extension of the rationals, equipped with a non-archimedean metric. Unlike the reals (which use the standard absolute value), p-adic arithmetic uses a different notion of "distance."

### P-adic Valuation

For a prime p and integer n ≠ 0, the **p-adic valuation** v_p(n) is:

```
v_p(n) = the largest integer k such that p^k divides n
```

Examples:
- v_2(8) = 3 (since 8 = 2³)
- v_3(27) = 3 (since 27 = 3³)
- v_5(10) = 1 (since 10 = 2 × 5)
- v_p(1) = 0 for all primes p
- v_p(0) = ∞ (by convention)

### P-adic Norm

The **p-adic norm** on Q_p is defined as:

```
|x|_p = p^{-v_p(x)}  if x ≠ 0
|0|_p = 0
```

Key properties:
1. **Non-negativity**: |x|_p ≥ 0
2. **Identity**: |x|_p = 0 iff x = 0
3. **Multiplicativity**: |xy|_p = |x|_p · |y|_p
4. **Ultrametric inequality**: |x + y|_p ≤ max(|x|_p, |y|_p)  [stronger than triangle inequality]

The ultrametric property is crucial: in p-adic geometry, "large" numbers (small norms) are closer together.

Example with p = 2:
- |8|_2 = 2^{-3} = 1/8
- |1|_2 = 2^0 = 1
- |10|_2 = 2^{-1} = 1/2

### P-adic Inner Product

The **p-adic inner product** of vectors v₁, v₂ ∈ Q_p^n is:

```
⟨v₁, v₂⟩_p = Σᵢ wᵢ · v₁[i] · v₂[i]
```

where the weight wᵢ depends on the p-adic valuation:

```
wᵢ = |v₁[i] · v₂[i]|_p = p^{-v_p(v₁[i] · v₂[i])}
```

This weighting emphasizes components with high p-adic valuation (small norm), which is geometrically meaningful in p-adic spaces.

### Example Computation

For v₁ = [1, 2] and v₂ = [1, 2] with p = 2:

```
Component 0: product = 1 × 1 = 1
            v_2(1) = 0
            weight = 2^{-0} = 1
            contribution = 1 × 1 = 1

Component 1: product = 2 × 2 = 4
            v_2(4) = 2 (since 4 = 2²)
            weight = 2^{-2} = 1/4
            contribution = 1/4 × 4 = 1

⟨v₁, v₂⟩_2 = 1 + 1 = 2
```

## Adelic Numbers and Restricted Products

The **adeles** form a topological ring that encodes all completions of Q simultaneously. For the RTSG framework, we use the restricted product.

### Archimedean vs. Non-archimedean

1. **Archimedean place**: The standard absolute value on ℝ (Euclidean metric)
2. **Non-archimedean places**: The p-adic norms for primes p

### Restricted Adelic Product

The **restricted adelic inner product** is:

```
⟨v₁, v₂⟩_adelic = ⟨v₁, v₂⟩_∞ × ∏_{p ∈ S} ⟨v₁, v₂⟩_p
```

where:
- ⟨v₁, v₂⟩_∞ = Σᵢ v₁[i] · v₂[i]  (Euclidean inner product)
- S is a finite set of primes
- The product combines archimedean and p-adic contributions multiplicatively

### Example: Two-Prime Adelic Product

For v₁ = [1, 0] and v₂ = [0, 1] with S = {2, 3}:

```
Archimedean: ⟨v₁, v₂⟩_∞ = 1×0 + 0×1 = 0
2-adic:      ⟨v₁, v₂⟩_2 = (depends on components)
3-adic:      ⟨v₁, v₂⟩_3 = (depends on components)

⟨v₁, v₂⟩_adelic = 0 × (⟨v₁, v₂⟩_2) × (⟨v₁, v₂⟩_3) = 0
```

When the archimedean part is zero, the entire product is zero regardless of p-adic contributions.

## Gram Matrices

The **Gram matrix** G of a basis {v₁, ..., vₙ} has entries:

```
G[i,j] = ⟨vᵢ, vⱼ⟩_metric
```

### Properties

1. **Symmetry**: G[i,j] = G[j,i]
2. **Positive semi-definiteness** (for real/complex metrics): All eigenvalues ≥ 0
3. **Full rank iff vectors are linearly independent**

### Real (Euclidean) Gram Matrix

```
G[i,j] = Σₖ vᵢ[k] · vⱼ[k]
```

For orthonormal vectors, G = I (identity matrix).

### P-adic Gram Matrix

```
G[i,j] = ⟨vᵢ, vⱼ⟩_p = Σₖ |vᵢ[k] · vⱼ[k]|_p
```

The non-archimedean nature means the Gram matrix structure differs fundamentally from the real case.

### Adelic Gram Matrix

```
G[i,j] = ⟨vᵢ, vⱼ⟩_adelic = ⟨vᵢ, vⱼ⟩_∞ × ∏_{p ∈ S} ⟨vᵢ, vⱼ⟩_p
```

Combines Euclidean and p-adic information in a multiplicative structure.

## Eigenvalue Computation via Jacobi Method

The Jacobi method is a classical iterative algorithm for computing eigenvalues of symmetric matrices.

### Algorithm Overview

1. **Initialize**: A ← M (copy input matrix)
2. **Iterate until convergence**:
   - Find the largest off-diagonal element A[p,q]
   - Compute rotation angle θ to zero out A[p,q]
   - Apply Givens rotation: A ← Rₚ,q(θ)ᵀ · A · Rₚ,q(θ)
3. **Extract eigenvalues from diagonal**

### Givens Rotation

The rotation angle θ is computed to eliminate element (p,q):

```
tan(2θ) = 2A[p,q] / (A[p,p] - A[q,q])
```

The rotation matrix Rₚ,q(θ) is applied from both sides to preserve symmetry.

### Convergence Properties

- **Quadratic convergence** under normal circumstances
- **Guaranteed convergence** for any symmetric matrix
- **Complexity**: O(n³) with typically 5-30 iterations

### Implementation Details

In our library:
- Maximum iterations: 1000
- Convergence tolerance: 1e-14
- Eigenvalues are sorted in descending order
- Returns NAN on error (not panic)

## Floating-Point P-adic Valuation Estimation

Since we work with floating-point numbers rather than exact rationals, we estimate the p-adic valuation through the mantissa and exponent.

### Method

```rust
mantissa, exponent = extract_mantissa_exponent(x)
approx_int = round(mantissa * 2^53)
v_p ≈ count_factors(approx_int, p)
```

This approach:
- Works for typical floating-point values
- Provides reasonable estimates for the metric
- May lose precision for very large/small numbers
- Is deterministic and reproducible

### Limitations

1. **Loss of information**: Float→int conversion loses precision
2. **Boundary cases**: Numbers very close to powers of p may have estimation errors
3. **Theoretical gap**: True p-adic arithmetic on rationals vs. float approximation

For exact arithmetic on rationals, external libraries (num-rational, rug) would be needed.

## Numerical Stability

### Gram Matrix Computation

- Double precision (IEEE 754) sufficient for typical use
- Direct computation of inner products (no orthogonalization)
- Gram matrix inherits numerical properties of inner product

### Jacobi Eigenvalue Method

- **Numerically stable** for symmetric matrices
- Uses only additions, multiplications, trigonometric functions
- No explicit inverse or decompositions (higher condition number)
- Quadratic convergence means exponential improvement in accuracy

### Guard Against Underflow

In adelic products, we terminate early if intermediate results become very small (< 1e-300) to prevent numerical underflow.

## References and Further Reading

### Books
- **Cassels, J.W.S.** (1986). *Local Fields*. London Mathematical Society Student Texts. [Definitive reference on p-adic theory]
- **Serre, J.-P.** (1979). *Local Fields*. Springer-Verlag. [Cleaner presentation]
- **Weil, A.** (1967). *Basic Number Theory*. Springer-Verlag. [Adeles and algebraic geometry]
- **Golub, G.H. & Van Loan, C.F.** (2013). *Matrix Computations*. Johns Hopkins University Press. [Jacobi method details]

### Papers
- **Jacobi, C.G.J.** (1846). "Über ein leichtes Verfahren, die in der Theorie der Säcularstörungen..."
  [Original Jacobi eigenvalue paper]
- **Freiling, G., et al.** (2000). "Jacobi matrices for measures supported on the unit circle."
  *Linear Algebra and its Applications*, 317(1-3), 1-12.

### Online Resources
- [ProofWiki: P-adic Numbers](https://proofwiki.org/wiki/Definition:P-adic_Absolute_Value)
- [MathWorld: P-adic Number](https://mathworld.wolfram.com/P-adicNumber.html)
- [Encyclopedia of Mathematics: P-adic Analysis](https://encyclopediaofmath.org/wiki/P-adic_analysis)

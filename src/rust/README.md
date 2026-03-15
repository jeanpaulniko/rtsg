# RTSG Framework Compute Library

High-performance p-adic and adelic inner product computations compiled as a C-compatible shared library for the RTSG (Representation Theory Spectral Geometry) framework.

## Overview

This Rust library implements:

- **P-adic arithmetic**: Valuation computation, p-adic norms, and p-adic inner products in Q_p
- **Adelic metrics**: Restricted products combining archimedean (Euclidean) and p-adic components
- **Linear algebra**: Gram matrix computation and eigenvalue calculation via Jacobi iteration
- **C FFI exports**: All functions accessible from Go via standard FFI mechanisms

## Architecture

### Module Structure

```
src/
├── lib.rs          # Main library entry point and exports
├── padic.rs        # P-adic arithmetic (valuation, norms, inner products)
├── adelic.rs       # Adelic metrics and restricted products
├── linalg.rs       # Linear algebra (Gram matrices, Jacobi eigenvalues)
├── ffi.rs          # C-compatible FFI boundary
└── bin/test_lib.rs # Test and demonstration binary
```

### Core Concepts

#### P-adic Numbers (Q_p)

For a prime p and integer n, the **p-adic valuation** v_p(n) is the highest power of p dividing n.

Example: v_2(8) = 3 because 8 = 2³

The **p-adic norm** is |x|_p = p^{-v_p(x)}

The **p-adic inner product** for vectors v₁, v₂ is:
```
⟨v₁, v₂⟩_p = Σᵢ |v₁[i] · v₂[i]|_p · p^{-v_p(v₁[i]·v₂[i])}
```

#### Adelic Metrics

The **adelic inner product** is the restricted product:
```
⟨v₁, v₂⟩_adelic = ⟨v₁, v₂⟩_∞ × ∏_{p ∈ S} ⟨v₁, v₂⟩_p
```

where:
- ⟨v₁, v₂⟩_∞ is the standard Euclidean inner product
- S is a finite set of primes
- The product captures both real and p-adic geometric structure

## Exported Functions

### FFI Boundary (C-compatible)

All functions are marked `extern "C"` and use C-compatible types only.

#### `padic_inner_product`

```c
double padic_inner_product(
    const double *v1,      // First vector
    const double *v2,      // Second vector
    size_t n,              // Dimension
    uint64_t p             // Prime number
);
```

Computes the p-adic inner product ⟨v₁, v₂⟩_p.

**Returns**: f64 (NAN on error)

**Example**:
```c
double v1[3] = {1.0, 2.0, 3.0};
double v2[3] = {1.0, 2.0, 3.0};
double result = padic_inner_product(v1, v2, 3, 2);  // ⟨v₁, v₂⟩_2
```

#### `adelic_inner_product`

```c
double adelic_inner_product(
    const double *v1,       // First vector
    const double *v2,       // Second vector
    size_t n,               // Dimension
    const uint64_t *primes, // Array of primes
    size_t n_primes         // Number of primes
);
```

Computes the restricted adelic inner product.

**Returns**: f64 (NAN on error)

**Example**:
```c
double v1[2] = {1.0, 2.0};
double v2[2] = {3.0, 4.0};
uint64_t primes[3] = {2, 3, 5};
double result = adelic_inner_product(v1, v2, 2, primes, 3);
```

#### `gram_matrix`

```c
double *gram_matrix(
    const double *basis,    // Flattened basis vectors (row-major)
    size_t n_vectors,       // Number of vectors
    size_t dim,             // Dimension of each vector
    uint32_t number_system, // 0=real, 1=complex, 2=padic, 3=adelic
    uint64_t p              // Prime (for padic/adelic)
);
```

Computes the Gram matrix G where G[i,j] = ⟨basis[i], basis[j]⟩.

**Returns**: Pointer to heap-allocated n_vectors × n_vectors matrix (row-major), or NULL on error

**Note**: Must be freed with `free_array()`

**Example**:
```c
double basis[6] = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0};  // Two 3D basis vectors
double *gram = gram_matrix(basis, 2, 3, 0, 0);      // Real metric
// Use gram...
free_array(gram);
```

#### `eigenvalues`

```c
double *eigenvalues(
    const double *matrix,   // Symmetric n×n matrix (row-major)
    size_t n                // Size of matrix
);
```

Computes eigenvalues of a symmetric matrix using the Jacobi method.

**Returns**: Pointer to heap-allocated array of n eigenvalues (sorted descending), or NULL on error

**Note**: Must be freed with `free_array()`

**Example**:
```c
double matrix[4] = {4.0, 2.0, 2.0, 3.0};  // [[4,2],[2,3]]
double *eigs = eigenvalues(matrix, 2);
// eigs[0] ≈ 5.236, eigs[1] ≈ 1.764
free_array(eigs);
```

#### `free_array`

```c
void free_array(double *ptr);
```

Frees heap-allocated arrays from `gram_matrix()` or `eigenvalues()`.

**Safety**: Must be called exactly once per allocated pointer.

### Utility Functions

#### `get_version`

```c
const unsigned char *get_version(void);
```

Returns the library version string.

#### `health_check`

```c
uint32_t health_check(void);
```

Performs a basic sanity check. Returns 1 if functional, 0 otherwise.

## Building

### Prerequisites

- Rust 1.56+ (2021 edition)
- Linux, macOS, or Windows with appropriate toolchain

### Compile as Shared Library

```bash
cargo build --release
```

Produces:
- Linux: `target/release/libsmarthub_compute.so`
- macOS: `target/release/libsmarthub_compute.dylib`
- Windows: `target/release/smarthub_compute.dll`

### Run Tests

```bash
cargo test
```

### Run Test Binary

```bash
cargo run --bin test_lib --features test_binary --release
```

## Go Integration

To call from Go, use `cgo`:

```go
/*
#cgo LDFLAGS: -L. -lsmarthub_compute
#include <stddef.h>
#include <stdint.h>

double padic_inner_product(const double *v1, const double *v2, size_t n, uint64_t p);
double adelic_inner_product(const double *v1, const double *v2, size_t n, const uint64_t *primes, size_t n_primes);
double *gram_matrix(const double *basis, size_t n_vectors, size_t dim, uint32_t number_system, uint64_t p);
double *eigenvalues(const double *matrix, size_t n);
void free_array(double *ptr);
*/
import "C"

// Example: Call p-adic inner product from Go
func PadicInnerProduct(v1, v2 []float64, p uint64) float64 {
    if len(v1) != len(v2) || len(v1) == 0 {
        return math.NaN()
    }

    result := C.padic_inner_product(
        (*C.double)(unsafe.Pointer(&v1[0])),
        (*C.double)(unsafe.Pointer(&v2[0])),
        C.size_t(len(v1)),
        C.uint64_t(p),
    )
    return float64(result)
}
```

## Performance Characteristics

### Computational Complexity

- **P-adic valuation**: O(log n) per component
- **P-adic inner product**: O(n log p) for n-dimensional vectors
- **Adelic inner product**: O(n · k · log p) for k primes
- **Gram matrix**: O(n² · dim · log p)
- **Jacobi eigenvalues**: O(n³) with quadratic convergence

### Numerical Stability

- All floating-point operations use IEEE 754 double precision
- Jacobi method is numerically stable for symmetric matrices
- Returns NAN (not panic) on error conditions for FFI safety

## Design Principles

1. **No external dependencies**: Pure Rust implementation
2. **Safety**: No panics in FFI boundary, proper error handling
3. **Performance**: Optimized for release builds with LTO
4. **Correctness**: Comprehensive test suite included
5. **Compatibility**: C-compatible FFI for universal integration

## Mathematical Formulation

### Gram Matrix Computation

For a basis {v₁, ..., vₙ}, the Gram matrix G is:

```
G[i,j] = ⟨vᵢ, vⱼ⟩
```

In different metrics:
- **Real**: Standard Euclidean inner product
- **Complex**: Hermitian inner product (treated as real for this implementation)
- **P-adic**: ⟨vᵢ, vⱼ⟩_p in Q_p
- **Adelic**: Restricted product of archimedean and p-adic

### Jacobi Eigenvalue Method

Iteratively applies Givens rotations to zero off-diagonal elements until convergence. Guaranteed to converge for symmetric matrices.

Key property: Preserves eigenvalues while diagonalizing the matrix.

## Limitations and Future Work

1. **Floating-point p-adic arithmetic**: Estimates valuation through floating-point representation
2. **Limited prime set for adelic**: Uses hardcoded default primes {2,3,5,7,11}
3. **Single-threaded**: No parallelization in Jacobi method
4. **Fixed-precision eigenvalues**: No arbitrary precision support

## References

- Cassels, J.W.S. (1986). *Local Fields*. London Mathematical Society Student Texts.
- Weil, A. (1967). *Basic Number Theory*. Springer-Verlag.
- Freiling, G., et al. (2000). "Jacobi matrices for measures supported on the unit circle."

## License

Apache License 2.0

## Author

RTSG Framework Team

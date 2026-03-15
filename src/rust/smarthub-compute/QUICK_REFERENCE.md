# Quick Reference Guide

## One-Liner Build and Test

```bash
# Build
cargo build --release

# Test
cargo test --release

# Demo
cargo run --bin test_lib --features test_binary --release
```

## FFI Function Quick Reference

### P-adic Inner Product
```c
double result = padic_inner_product(v1, v2, 3, 2);
// Computes ⟨v1, v2⟩_2 for 3-dimensional vectors
```

### Adelic Inner Product
```c
uint64_t primes[] = {2, 3, 5};
double result = adelic_inner_product(v1, v2, 3, primes, 3);
// Restricted product: Euclidean × p-adic product
```

### Gram Matrix
```c
double *gram = gram_matrix(basis, n, dim, 0, 0);  // Real metric
double *gram = gram_matrix(basis, n, dim, 2, 2);  // P-adic with p=2
double *gram = gram_matrix(basis, n, dim, 3, 0);  // Adelic
if (gram) free_array(gram);
```

### Eigenvalues
```c
double *eigs = eigenvalues(matrix, n);
if (eigs) {
    for (size_t i = 0; i < n; i++)
        printf("λ_%zu = %.6f\n", i+1, eigs[i]);
    free_array(eigs);
}
```

## Go Bindings Template

```go
package compute

/*
#cgo LDFLAGS: -L. -lsmarthub_compute -lm
#include <stddef.h>
#include <stdint.h>
double padic_inner_product(const double *v1, const double *v2, size_t n, uint64_t p);
double adelic_inner_product(const double *v1, const double *v2, size_t n, const uint64_t *primes, size_t n_primes);
double *gram_matrix(const double *basis, size_t n_vectors, size_t dim, uint32_t number_system, uint64_t p);
double *eigenvalues(const double *matrix, size_t n);
void free_array(double *ptr);
*/
import "C"
import "unsafe"

func PadicInnerProduct(v1, v2 []float64, p uint64) float64 {
    return float64(C.padic_inner_product(
        (*C.double)(unsafe.Pointer(&v1[0])),
        (*C.double)(unsafe.Pointer(&v2[0])),
        C.size_t(len(v1)),
        C.uint64_t(p),
    ))
}

// Similar for other functions...
```

## Number System Codes

| Code | System | Usage |
|------|--------|-------|
| 0 | Real (Euclidean) | Standard inner product |
| 1 | Complex | Hermitian (treated as real) |
| 2 | P-adic | Non-archimedean metric |
| 3 | Adelic | Restricted product |

## Error Handling

All FFI functions are safe and return sensible error values:

| Function | Error Return | Notes |
|----------|--------------|-------|
| padic_inner_product | NAN | Check with `isnan()` |
| adelic_inner_product | NAN | Check with `isnan()` |
| gram_matrix | NULL | Check with `if (ptr == NULL)` |
| eigenvalues | NULL | Check with `if (ptr == NULL)` |
| free_array | (void) | Safe to call with NULL |

## Common Mistakes to Avoid

1. **Forgetting to free**: Always free Gram matrices and eigenvalue arrays
   ```c
   double *gram = gram_matrix(...);
   // ... use gram ...
   free_array(gram);  // MUST do this
   ```

2. **Wrong array sizes**: Ensure basis has correct flattened size
   ```c
   // For n_vectors vectors of dim dimensions:
   // basis must have size: n_vectors * dim
   double basis[6];  // 2 vectors × 3 dimensions
   double *gram = gram_matrix(basis, 2, 3, 0, 0);  // ✓ Correct
   ```

3. **Invalid primes**: Use only primes (p ≥ 2)
   ```c
   padic_inner_product(v1, v2, n, 2);  // ✓ Valid (p=2)
   padic_inner_product(v1, v2, n, 0);  // ✗ Invalid (p=0)
   ```

4. **Non-symmetric eigenvalue matrices**: Input must be symmetric
   ```c
   double sym[] = {1, 2, 2, 3};  // [[1,2],[2,3]] ✓ Symmetric
   double non[] = {1, 2, 3, 4};  // [[1,2],[3,4]] ✗ Not symmetric
   ```

## Performance Tips

1. **Batch operations**: Process multiple inner products at once
2. **p-adic choice**: p=2,3,5 are fastest (small primes)
3. **Adelic set size**: Fewer primes = faster computation
4. **Release build**: Always use `cargo build --release`
5. **Jacobi eigenvalues**: Fast for n < 500, slower for larger matrices

## Compilation Targets

```bash
# Linux x86_64
cargo build --release

# macOS (both architectures)
cargo build --release --target aarch64-apple-darwin
cargo build --release --target x86_64-apple-darwin

# Windows
cargo build --release --target x86_64-pc-windows-gnu

# ARM Linux
cargo build --release --target aarch64-unknown-linux-gnu
```

## Linking Libraries

### Linux
```bash
gcc -o program program.c -L./target/release -lsmarthub_compute -lm
LD_LIBRARY_PATH=./target/release ./program
```

### macOS
```bash
clang -o program program.c -L./target/release -lsmarthub_compute -lm
DYLD_LIBRARY_PATH=./target/release ./program
```

### Go
```bash
export LD_LIBRARY_PATH=$(pwd)/target/release:$LD_LIBRARY_PATH
go build
./myapp
```

## Documentation References

- **README.md** - Full API documentation with examples
- **BUILD.md** - Build instructions, cross-compilation, CI/CD
- **MATHEMATICS.md** - Mathematical theory and formulations
- **IMPLEMENTATION_SUMMARY.md** - Architecture and design decisions
- **smarthub_compute.h** - C header with detailed comments
- **examples/*** - Working code examples

## Testing Your Build

```bash
# Run all tests
cargo test --all --release

# Run specific test
cargo test padic_inner_product --release

# Run with output
cargo test --release -- --nocapture

# Build and run example binary
cargo run --bin test_lib --features test_binary --release
```

## Health Check

Always verify library loads correctly:

```c
#include "smarthub_compute.h"

if (!health_check()) {
    fprintf(stderr, "Library check failed\n");
    return 1;
}
printf("Library version: %s\n", (const char *)get_version());
```

## Memory Safety Notes

- **Stack safe**: All internal allocations use stack
- **Heap safe**: Only intentional allocations returned to caller
- **No memory leaks**: Rust ownership guarantees cleanup
- **Thread safe**: Stateless FFI (no global state)

## File Locations

```
smarthub-compute/
├── src/lib.rs              # Library entry (module declarations)
├── src/padic.rs            # P-adic implementation
├── src/adelic.rs           # Adelic implementation
├── src/linalg.rs           # Eigenvalues, Gram matrices
├── src/ffi.rs              # FFI boundary
├── src/bin/test_lib.rs     # Test/demo binary
├── include/smarthub_compute.h  # C header
├── examples/example.c      # C demo
└── examples/example.go     # Go demo
```

## Contact and Support

For issues, questions, or contributions:
1. Check MATHEMATICS.md for theory questions
2. Check examples/ for usage patterns
3. Check BUILD.md for compilation issues
4. Review test cases in src/*.rs for API details

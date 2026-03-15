# Build and Integration Guide

## Quick Start

```bash
# Build the shared library (release optimized)
cargo build --release

# Run the test suite
cargo test --release

# Run the test binary
cargo run --bin test_lib --features test_binary --release
```

## Building for Different Platforms

### Linux (x86_64)

```bash
cargo build --release
# Output: target/release/libsmarthub_compute.so
```

To build for different architectures:

```bash
# ARM64
rustup target add aarch64-unknown-linux-gnu
cargo build --release --target aarch64-unknown-linux-gnu

# ARM32
rustup target add armv7-unknown-linux-gnueabihf
cargo build --release --target armv7-unknown-linux-gnueabihf
```

### macOS

```bash
cargo build --release
# Output: target/release/libsmarthub_compute.dylib

# For ARM64 (Apple Silicon)
rustup target add aarch64-apple-darwin
cargo build --release --target aarch64-apple-darwin

# For Intel (x86_64)
rustup target add x86_64-apple-darwin
cargo build --release --target x86_64-apple-darwin

# Universal binary
cargo install cargo-lipo
cargo lipo --release
```

### Windows

```bash
cargo build --release
# Output: target/release/smarthub_compute.dll

# For 32-bit
rustup target add i686-pc-windows-gnu
cargo build --release --target i686-pc-windows-gnu
```

## Optimizations

The Cargo.toml is configured with aggressive optimizations:

```toml
[profile.release]
opt-level = 3           # Maximum optimization
lto = true              # Link-time optimization
codegen-units = 1       # Single codegen unit for better optimization
strip = true            # Strip symbols for smaller binary
```

For even faster binaries at the cost of larger size:

```bash
cargo build --release -Z build-std=core,alloc --target x86_64-unknown-linux-gnu
```

## Integration with Go

### 1. Setup CGO

Create a Go project structure:

```
myproject/
├── main.go
├── compute/
│   ├── lib.go
│   └── smarthub_compute.h  (if needed for IDE support)
└── libsmarthub_compute.so  (or .dylib/.dll)
```

### 2. Copy the Shared Library

After building, copy the library to your Go project:

```bash
# From the Rust project
cp target/release/libsmarthub_compute.so ../myproject/

# Or if building in a CI/CD pipeline
cp target/release/libsmarthub_compute.* /path/to/deployment/
```

### 3. Write Go Bindings

Create `compute/lib.go`:

```go
package compute

/*
#cgo LDFLAGS: -L. -lsmarthub_compute -lm
#include <stddef.h>
#include <stdint.h>
#include <math.h>

double padic_inner_product(const double *v1, const double *v2, size_t n, uint64_t p);
double adelic_inner_product(const double *v1, const double *v2, size_t n, const uint64_t *primes, size_t n_primes);
double *gram_matrix(const double *basis, size_t n_vectors, size_t dim, uint32_t number_system, uint64_t p);
double *eigenvalues(const double *matrix, size_t n);
void free_array(double *ptr);
const unsigned char *get_version(void);
uint32_t health_check(void);
*/
import "C"

import (
	"fmt"
	"math"
	"unsafe"
)

// PadicInnerProduct computes p-adic inner product
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

// AdelicInnerProduct computes adelic inner product
func AdelicInnerProduct(v1, v2 []float64, primes []uint64) float64 {
	if len(v1) != len(v2) || len(v1) == 0 {
		return math.NaN()
	}
	primesPtr := (*C.uint64_t)(nil)
	if len(primes) > 0 {
		primesPtr = (*C.uint64_t)(unsafe.Pointer(&primes[0]))
	}
	result := C.adelic_inner_product(
		(*C.double)(unsafe.Pointer(&v1[0])),
		(*C.double)(unsafe.Pointer(&v2[0])),
		C.size_t(len(v1)),
		primesPtr,
		C.size_t(len(primes)),
	)
	return float64(result)
}

// GramMatrix computes the Gram matrix
// numberSystem: 0=real, 1=complex, 2=padic, 3=adelic
func GramMatrix(basis []float64, nVectors, dim uint, numberSystem uint32, p uint64) ([][]float64, error) {
	if len(basis) != int(nVectors)*int(dim) {
		return nil, fmt.Errorf("basis size mismatch: expected %d, got %d", nVectors*uint64(dim), len(basis))
	}

	ptr := C.gram_matrix(
		(*C.double)(unsafe.Pointer(&basis[0])),
		C.size_t(nVectors),
		C.size_t(dim),
		C.uint32_t(numberSystem),
		C.uint64_t(p),
	)

	if ptr == nil {
		return nil, fmt.Errorf("gram_matrix returned null")
	}
	defer C.free_array(ptr)

	// Convert to Go slice
	size := int(nVectors) * int(nVectors)
	gramSlice := unsafe.Slice(ptr, size)

	// Convert to 2D matrix
	result := make([][]float64, nVectors)
	for i := 0; i < int(nVectors); i++ {
		result[i] = make([]float64, nVectors)
		copy(result[i], gramSlice[i*int(nVectors):(i+1)*int(nVectors)])
	}

	return result, nil
}

// Eigenvalues computes eigenvalues of a symmetric matrix
func Eigenvalues(matrix []float64, n uint) ([]float64, error) {
	if len(matrix) != int(n)*int(n) {
		return nil, fmt.Errorf("matrix size mismatch")
	}

	ptr := C.eigenvalues(
		(*C.double)(unsafe.Pointer(&matrix[0])),
		C.size_t(n),
	)

	if ptr == nil {
		return nil, fmt.Errorf("eigenvalues returned null")
	}
	defer C.free_array(ptr)

	// Convert to Go slice
	eigs := unsafe.Slice(ptr, n)
	result := make([]float64, n)
	copy(result, eigs)

	return result, nil
}

// GetVersion returns the library version
func GetVersion() string {
	cVersion := C.get_version()
	if cVersion == nil {
		return "unknown"
	}
	return C.GoString((*C.char)(unsafe.Pointer(cVersion)))
}

// HealthCheck performs a sanity check
func HealthCheck() bool {
	result := C.health_check()
	return result == 1
}
```

### 4. Write Tests

Create `compute/lib_test.go`:

```go
package compute

import (
	"math"
	"testing"
)

func TestPadicInnerProduct(t *testing.T) {
	v1 := []float64{1.0, 2.0, 3.0}
	v2 := []float64{1.0, 2.0, 3.0}

	result := PadicInnerProduct(v1, v2, 2)
	if math.IsNaN(result) {
		t.Fatal("Expected finite result, got NaN")
	}
	t.Logf("P-adic inner product: %v", result)
}

func TestGramMatrix(t *testing.T) {
	basis := []float64{1.0, 0.0, 0.0, 1.0}

	gram, err := GramMatrix(basis, 2, 2, 0, 0)
	if err != nil {
		t.Fatalf("GramMatrix failed: %v", err)
	}

	if gram[0][0] != 1.0 || gram[0][1] != 0.0 {
		t.Fatalf("Expected identity matrix, got %v", gram)
	}
}

func TestEigenvalues(t *testing.T) {
	matrix := []float64{2.0, 0.0, 0.0, 3.0}

	eigs, err := Eigenvalues(matrix, 2)
	if err != nil {
		t.Fatalf("Eigenvalues failed: %v", err)
	}

	if math.Abs(eigs[0]-3.0) > 1e-10 || math.Abs(eigs[1]-2.0) > 1e-10 {
		t.Fatalf("Expected [3.0, 2.0], got %v", eigs)
	}
}

func TestHealthCheck(t *testing.T) {
	ok := HealthCheck()
	if !ok {
		t.Fatal("Health check failed")
	}
	t.Logf("Library version: %s", GetVersion())
}
```

### 5. Compile

```bash
# Build with dynamic linking
go build -o myapp main.go

# Run with library in LD_LIBRARY_PATH
LD_LIBRARY_PATH=. ./myapp

# Or embed library path
go build -ldflags="-Wl,-rpath,$(pwd)" -o myapp main.go
```

## Cross-Compilation

To build for a different target:

```bash
# List available targets
rustup target list

# Add target
rustup target add x86_64-pc-windows-gnu

# Build for that target
cargo build --release --target x86_64-pc-windows-gnu
```

## Docker Build

Create a `Dockerfile`:

```dockerfile
FROM rust:1.70

WORKDIR /build
COPY Cargo.toml Cargo.lock* ./
COPY src ./src

RUN cargo build --release

FROM ubuntu:22.04
COPY --from=0 /build/target/release/libsmarthub_compute.so /usr/local/lib/
RUN ldconfig

CMD ["bash"]
```

Build and run:

```bash
docker build -t smarthub-compute .
docker run -v /path/to/go/project:/app smarthub-compute
```

## Benchmarking

Run benchmarks with the test binary:

```bash
cargo run --bin test_lib --features test_binary --release
```

For profiling on Linux:

```bash
# Install perf
sudo apt-get install linux-tools-generic

# Build with debug symbols
cargo build --release

# Profile
perf record -g ./target/release/test_lib
perf report
```

## Troubleshooting

### Symbol not found

```bash
# Check exported symbols
nm target/release/libsmarthub_compute.so | grep padic

# Verify library works
ldd target/release/libsmarthub_compute.so
```

### Linking errors in Go

Ensure library is in LD_LIBRARY_PATH or use absolute path in #cgo directive:

```go
/*
#cgo LDFLAGS: -L/path/to/lib -lsmarthub_compute
*/
```

### NaN results

Check that:
1. Input arrays are valid and non-empty
2. Prime numbers are >= 2
3. Matrix is actually symmetric for eigenvalue computation

## Continuous Integration

Example GitHub Actions workflow:

```yaml
name: Build

on: [push]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: actions/checkout@v2
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
      - run: cargo build --release
      - run: cargo test --release
```

/*
 * Example Go program demonstrating RTSG Compute Library usage
 *
 * Build and run:
 *   go build -o example examples/example.go
 *   LD_LIBRARY_PATH=target/release:. ./example
 *
 * Or with cgo linking directly:
 *   CGO_LDFLAGS="-L$(pwd)/target/release -lsmarthub_compute -lm" go run examples/example.go
 */

package main

import (
	"fmt"
	"math"
	"unsafe"
)

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

// Bindings to library functions

func padicInnerProduct(v1, v2 []float64, p uint64) float64 {
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

func adelicInnerProduct(v1, v2 []float64, primes []uint64) float64 {
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

func gramMatrix(basis []float64, nVectors, dim uint, numberSystem uint32, p uint64) ([][]float64, error) {
	if len(basis) != int(nVectors)*int(dim) {
		return nil, fmt.Errorf("basis size mismatch")
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

	size := int(nVectors) * int(nVectors)
	gramSlice := unsafe.Slice(ptr, size)

	result := make([][]float64, nVectors)
	for i := 0; i < int(nVectors); i++ {
		result[i] = make([]float64, nVectors)
		copy(result[i], gramSlice[i*int(nVectors):(i+1)*int(nVectors)])
	}

	return result, nil
}

func eigenvalues(matrix []float64, n uint) ([]float64, error) {
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

	eigs := unsafe.Slice(ptr, n)
	result := make([]float64, n)
	copy(result, eigs)

	return result, nil
}

func getVersion() string {
	cVersion := C.get_version()
	if cVersion == nil {
		return "unknown"
	}
	return C.GoString((*C.char)(unsafe.Pointer(cVersion)))
}

func healthCheck() bool {
	result := C.health_check()
	return result == 1
}

// Utility functions

func printArray(label string, arr []float64) {
	fmt.Printf("%s: [", label)
	for i, v := range arr {
		if math.IsNaN(v) {
			fmt.Print("NAN")
		} else if math.IsInf(v, 0) {
			fmt.Print("INF")
		} else {
			fmt.Printf("%.6f", v)
		}
		if i < len(arr)-1 {
			fmt.Print(", ")
		}
	}
	fmt.Println("]")
}

func printMatrix(label string, matrix [][]float64) {
	fmt.Printf("%s:\n", label)
	for _, row := range matrix {
		fmt.Print("  [")
		for j, v := range row {
			if math.IsNaN(v) {
				fmt.Print(" NAN  ")
			} else if math.IsInf(v, 0) {
				fmt.Print(" INF  ")
			} else {
				fmt.Printf("%7.3f", v)
			}
			if j < len(row)-1 {
				fmt.Print(",")
			}
		}
		fmt.Println("]")
	}
}

// Main demonstration

func main() {
	fmt.Println("=== RTSG Compute Library Go Example ===\n")

	// Health check
	fmt.Println("1. Health Check")
	fmt.Printf("   Version: %s\n", getVersion())
	fmt.Printf("   Status: %s\n", map[bool]string{true: "OK", false: "FAILED"}[healthCheck()])
	fmt.Println()

	// Example 1: P-adic inner product
	fmt.Println("2. P-adic Inner Product")
	v1 := []float64{1.0, 2.0, 3.0}
	v2 := []float64{1.0, 2.0, 3.0}

	ip2 := padicInnerProduct(v1, v2, 2)
	ip3 := padicInnerProduct(v1, v2, 3)
	ip5 := padicInnerProduct(v1, v2, 5)

	fmt.Println("   v1 = [1, 2, 3], v2 = [1, 2, 3]")
	fmt.Printf("   ⟨v1, v2⟩_2 = %.6f\n", ip2)
	fmt.Printf("   ⟨v1, v2⟩_3 = %.6f\n", ip3)
	fmt.Printf("   ⟨v1, v2⟩_5 = %.6f\n", ip5)
	fmt.Println()

	// Example 2: Adelic inner product
	fmt.Println("3. Adelic Inner Product")
	u1 := []float64{1.0, 0.0}
	u2 := []float64{0.0, 1.0}
	primes := []uint64{2, 3, 5}

	adelicIP := adelicInnerProduct(u1, u2, primes)
	fmt.Println("   u1 = [1, 0], u2 = [0, 1]")
	fmt.Printf("   ⟨u1, u2⟩_adelic (with primes {2,3,5}) = %.6f\n", adelicIP)
	fmt.Println()

	// Example 3: Gram matrix (real/Euclidean)
	fmt.Println("4. Gram Matrix (Real Metric)")
	basisReal := []float64{
		1.0, 0.0, 0.0, // [1,0,0]
		0.0, 1.0, 0.0, // [0,1,0]
		1.0, 1.0, 0.0, // [1,1,0]
	}

	gramR, err := gramMatrix(basisReal, 3, 3, 0, 0)
	if err != nil {
		fmt.Printf("   ERROR: %v\n", err)
	} else {
		printMatrix("   Gram matrix (Euclidean)", gramR)
	}
	fmt.Println()

	// Example 4: Gram matrix (p-adic)
	fmt.Println("5. Gram Matrix (P-adic Metric, p=2)")
	gramP, err := gramMatrix(basisReal, 3, 3, 2, 2)
	if err != nil {
		fmt.Printf("   ERROR: %v\n", err)
	} else {
		printMatrix("   Gram matrix (2-adic)", gramP)
	}
	fmt.Println()

	// Example 5: Eigenvalues of a 2×2 matrix
	fmt.Println("6. Eigenvalues (2×2 Matrix)")
	matrix2 := []float64{4.0, 2.0, 2.0, 3.0} // [[4,2],[2,3]]
	fmt.Println("   Matrix: [[4, 2], [2, 3]]")

	eigs2, err := eigenvalues(matrix2, 2)
	if err != nil {
		fmt.Printf("   ERROR: %v\n", err)
	} else {
		printArray("   Eigenvalues (descending)", eigs2)
		fmt.Println("   (Expected: ~5.236, ~1.764)")
	}
	fmt.Println()

	// Example 6: Eigenvalues of a 3×3 matrix
	fmt.Println("7. Eigenvalues (3×3 Matrix)")
	matrix3 := []float64{
		2.0, 1.0, 0.0,
		1.0, 3.0, 1.0,
		0.0, 1.0, 2.0,
	}
	fmt.Println("   Matrix: [[2, 1, 0], [1, 3, 1], [0, 1, 2]]")

	eigs3, err := eigenvalues(matrix3, 3)
	if err != nil {
		fmt.Printf("   ERROR: %v\n", err)
	} else {
		printArray("   Eigenvalues (descending)", eigs3)
	}
	fmt.Println()

	// Example 7: Error handling
	fmt.Println("8. Error Handling")
	ipEmpty := padicInnerProduct([]float64{}, []float64{}, 2)
	fmt.Printf("   p-adic inner product of empty vectors: ")
	if math.IsNaN(ipEmpty) {
		fmt.Println("NAN (correct error handling)")
	} else {
		fmt.Printf("%f\n", ipEmpty)
	}

	fmt.Println("\n=== Example Complete ===")
}

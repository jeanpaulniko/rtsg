/*
 * RTSG Framework Compute Library - C Header
 * High-performance p-adic and adelic inner product computations
 *
 * This header provides C-compatible function declarations for the Rust library.
 * Link with libsmarthub_compute.so (Linux), libsmarthub_compute.dylib (macOS),
 * or smarthub_compute.dll (Windows).
 */

#ifndef SMARTHUB_COMPUTE_H
#define SMARTHUB_COMPUTE_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/*============================================================================
 * P-ADIC ARITHMETIC
 *============================================================================*/

/**
 * Compute the p-adic inner product in Q_p
 *
 * Computes: ⟨v1, v2⟩_p = Σᵢ |v1[i] · v2[i]|_p
 *
 * @param v1      First vector (array of size n)
 * @param v2      Second vector (array of size n)
 * @param n       Dimension of vectors
 * @param p       Prime number
 *
 * @return        P-adic inner product as double, or NAN on error
 *
 * @note          This function is safe to call from FFI boundaries.
 *                Returns NAN (not panic) on invalid input.
 *
 * Example:
 *   double v1[3] = {1.0, 2.0, 3.0};
 *   double v2[3] = {1.0, 2.0, 3.0};
 *   double result = padic_inner_product(v1, v2, 3, 2);
 */
double padic_inner_product(
    const double *v1,
    const double *v2,
    size_t n,
    uint64_t p
);

/*============================================================================
 * ADELIC ARITHMETIC
 *============================================================================*/

/**
 * Compute the adelic inner product as restricted product
 *
 * Computes: ⟨v1, v2⟩_adelic = ⟨v1, v2⟩_∞ × ∏_{p ∈ S} ⟨v1, v2⟩_p
 * where S is a finite set of primes
 *
 * @param v1          First vector (array of size n)
 * @param v2          Second vector (array of size n)
 * @param n           Dimension of vectors
 * @param primes      Array of prime numbers (size n_primes)
 * @param n_primes    Number of primes
 *
 * @return            Adelic inner product as double, or NAN on error
 *
 * @note              If n_primes is 0, returns the archimedean (Euclidean)
 *                    inner product only.
 *
 * Example:
 *   double v1[2] = {1.0, 2.0};
 *   double v2[2] = {3.0, 4.0};
 *   uint64_t primes[3] = {2, 3, 5};
 *   double result = adelic_inner_product(v1, v2, 2, primes, 3);
 */
double adelic_inner_product(
    const double *v1,
    const double *v2,
    size_t n,
    const uint64_t *primes,
    size_t n_primes
);

/*============================================================================
 * LINEAR ALGEBRA
 *============================================================================*/

/**
 * Compute Gram matrix for a set of basis vectors
 *
 * Computes G[i,j] = ⟨basis[i], basis[j]⟩ in the specified metric
 *
 * @param basis         Flattened array of vectors (row-major, size n_vectors * dim)
 * @param n_vectors     Number of vectors
 * @param dim           Dimension of each vector
 * @param number_system Metric type: 0=real, 1=complex, 2=padic, 3=adelic
 * @param p             Prime number (ignored for real/complex metrics)
 *
 * @return              Pointer to n_vectors × n_vectors matrix (row-major, heap-allocated)
 *                      Returns NULL on error
 *
 * @note                Caller must free the returned pointer with free_array()
 *
 * Example:
 *   double basis[6] = {1, 0, 0, 0, 1, 0};  // Two 3D basis vectors
 *   double *gram = gram_matrix(basis, 2, 3, 0, 0);  // Real metric
 *   if (gram != NULL) {
 *       printf("gram[0][0] = %f\n", gram[0]);
 *       free_array(gram);
 *   }
 */
double *gram_matrix(
    const double *basis,
    size_t n_vectors,
    size_t dim,
    uint32_t number_system,
    uint64_t p
);

/**
 * Compute eigenvalues of a symmetric matrix
 *
 * Uses the Jacobi eigenvalue method (no external dependencies).
 * Iteratively applies Givens rotations to diagonalize the matrix.
 *
 * @param matrix    Symmetric n×n matrix in row-major order
 * @param n         Size of the matrix
 *
 * @return          Pointer to array of n eigenvalues (sorted descending, heap-allocated)
 *                  Returns NULL on error
 *
 * @note            Caller must free the returned pointer with free_array()
 *                  Input matrix must be symmetric within floating-point tolerance
 *
 * Example:
 *   double matrix[4] = {4, 2, 2, 3};  // [[4,2],[2,3]]
 *   double *eigs = eigenvalues(matrix, 2);
 *   if (eigs != NULL) {
 *       printf("λ1 = %f, λ2 = %f\n", eigs[0], eigs[1]);
 *       free_array(eigs);
 *   }
 */
double *eigenvalues(
    const double *matrix,
    size_t n
);

/*============================================================================
 * MEMORY MANAGEMENT
 *============================================================================*/

/**
 * Free a heap-allocated array
 *
 * Deallocates memory allocated by gram_matrix() or eigenvalues()
 *
 * @param ptr   Pointer to array (from gram_matrix or eigenvalues)
 *
 * @note        Safe to call with NULL pointer
 *              Do NOT call multiple times on the same pointer
 *
 * Example:
 *   double *gram = gram_matrix(...);
 *   if (gram != NULL) {
 *       // use gram...
 *       free_array(gram);
 *   }
 */
void free_array(double *ptr);

/*============================================================================
 * UTILITY FUNCTIONS
 *============================================================================*/

/**
 * Get the library version string
 *
 * @return  Version string (e.g., "0.1.0")
 *
 * Example:
 *   printf("Library version: %s\n", (const char *)get_version());
 */
const unsigned char *get_version(void);

/**
 * Perform a health check on the library
 *
 * Runs a simple sanity check to verify the library is functional
 *
 * @return  1 if library is healthy, 0 otherwise
 *
 * Example:
 *   if (health_check() == 0) {
 *       fprintf(stderr, "Library health check failed!\n");
 *       return -1;
 *   }
 */
uint32_t health_check(void);

#ifdef __cplusplus
}
#endif

#endif /* SMARTHUB_COMPUTE_H */

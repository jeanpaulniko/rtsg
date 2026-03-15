/*
 * Example C program demonstrating RTSG Compute Library usage
 *
 * Compile with:
 *   gcc -o example examples/example.c -L. -lsmarthub_compute -lm
 *
 * Run with:
 *   LD_LIBRARY_PATH=target/release:. ./example
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../include/smarthub_compute.h"

void print_array(const char *label, double *arr, size_t len) {
    printf("%s: [", label);
    for (size_t i = 0; i < len; i++) {
        if (isnan(arr[i])) {
            printf("NAN");
        } else if (isinf(arr[i])) {
            printf("INF");
        } else {
            printf("%.6f", arr[i]);
        }
        if (i < len - 1) printf(", ");
    }
    printf("]\n");
}

void print_matrix(const char *label, double *matrix, size_t n) {
    printf("%s:\n", label);
    for (size_t i = 0; i < n; i++) {
        printf("  [");
        for (size_t j = 0; j < n; j++) {
            double val = matrix[i * n + j];
            if (isnan(val)) {
                printf(" NAN  ");
            } else if (isinf(val)) {
                printf(" INF  ");
            } else {
                printf("%7.3f", val);
            }
            if (j < n - 1) printf(",");
        }
        printf("]\n");
    }
}

int main(void) {
    printf("=== RTSG Compute Library C Example ===\n\n");

    // Health check
    printf("1. Health Check\n");
    printf("   Version: %s\n", (const char *)get_version());
    printf("   Status: %s\n", health_check() ? "OK" : "FAILED");
    printf("\n");

    // Example 1: P-adic inner product
    printf("2. P-adic Inner Product\n");
    double v1[] = {1.0, 2.0, 3.0};
    double v2[] = {1.0, 2.0, 3.0};
    size_t n = 3;

    double ip2 = padic_inner_product(v1, v2, n, 2);
    double ip3 = padic_inner_product(v1, v2, n, 3);
    double ip5 = padic_inner_product(v1, v2, n, 5);

    printf("   v1 = [1, 2, 3], v2 = [1, 2, 3]\n");
    printf("   ⟨v1, v2⟩_2 = %.6f\n", ip2);
    printf("   ⟨v1, v2⟩_3 = %.6f\n", ip3);
    printf("   ⟨v1, v2⟩_5 = %.6f\n", ip5);
    printf("\n");

    // Example 2: Adelic inner product
    printf("3. Adelic Inner Product\n");
    double u1[] = {1.0, 0.0};
    double u2[] = {0.0, 1.0};
    uint64_t primes[] = {2, 3, 5};
    size_t n_primes = 3;

    double adelic_ip = adelic_inner_product(u1, u2, 2, primes, n_primes);
    printf("   u1 = [1, 0], u2 = [0, 1]\n");
    printf("   ⟨u1, u2⟩_adelic (with primes {2,3,5}) = %.6f\n", adelic_ip);
    printf("\n");

    // Example 3: Gram matrix (real/Euclidean)
    printf("4. Gram Matrix (Real Metric)\n");
    double basis_real[] = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0};
    // Three 3D basis vectors: [1,0,0], [0,1,0], [1,1,0]
    size_t n_vectors = 3;
    size_t dim = 3;

    double *gram_r = gram_matrix(basis_real, n_vectors, dim, 0, 0);
    if (gram_r != NULL) {
        print_matrix("   Gram matrix (Euclidean)", gram_r, n_vectors);
        free_array(gram_r);
    } else {
        printf("   ERROR: gram_matrix returned NULL\n");
    }
    printf("\n");

    // Example 4: Gram matrix (p-adic)
    printf("5. Gram Matrix (P-adic Metric, p=2)\n");
    double *gram_p = gram_matrix(basis_real, n_vectors, dim, 2, 2);
    if (gram_p != NULL) {
        print_matrix("   Gram matrix (2-adic)", gram_p, n_vectors);
        free_array(gram_p);
    } else {
        printf("   ERROR: gram_matrix returned NULL\n");
    }
    printf("\n");

    // Example 5: Eigenvalues of a 2×2 matrix
    printf("6. Eigenvalues (2×2 Matrix)\n");
    double matrix2[] = {4.0, 2.0, 2.0, 3.0}; // [[4,2],[2,3]]
    printf("   Matrix: [[4, 2], [2, 3]]\n");

    double *eigs2 = eigenvalues(matrix2, 2);
    if (eigs2 != NULL) {
        print_array("   Eigenvalues (descending)", eigs2, 2);
        // Theoretical eigenvalues: λ₁ ≈ 5.236, λ₂ ≈ 1.764
        printf("   (Expected: ~5.236, ~1.764)\n");
        free_array(eigs2);
    } else {
        printf("   ERROR: eigenvalues returned NULL\n");
    }
    printf("\n");

    // Example 6: Eigenvalues of a 3×3 matrix
    printf("7. Eigenvalues (3×3 Matrix)\n");
    double matrix3[] = {
        2.0, 1.0, 0.0,
        1.0, 3.0, 1.0,
        0.0, 1.0, 2.0
    };
    printf("   Matrix: [[2, 1, 0], [1, 3, 1], [0, 1, 2]]\n");

    double *eigs3 = eigenvalues(matrix3, 3);
    if (eigs3 != NULL) {
        print_array("   Eigenvalues (descending)", eigs3, 3);
        free_array(eigs3);
    } else {
        printf("   ERROR: eigenvalues returned NULL\n");
    }
    printf("\n");

    // Example 7: Error handling
    printf("8. Error Handling\n");
    double empty[] = {};
    double ip_empty = padic_inner_product(empty, empty, 0, 2);
    printf("   p-adic inner product of empty vectors: ");
    if (isnan(ip_empty)) {
        printf("NAN (correct error handling)\n");
    } else {
        printf("%f\n", ip_empty);
    }

    double *null_gram = gram_matrix(NULL, 0, 0, 0, 0);
    printf("   gram_matrix with NULL input: %s\n",
           null_gram == NULL ? "NULL (correct)" : "non-NULL (error)");

    printf("\n=== Example Complete ===\n");

    return 0;
}

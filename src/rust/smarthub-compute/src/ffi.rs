/// FFI (Foreign Function Interface) module
/// Provides C-compatible exports for the RTSG framework

use crate::adelic;
use crate::linalg;
use crate::padic;
use core::slice;

/// Compute p-adic inner product in Q_p
///
/// # Parameters
/// - v1: pointer to first vector
/// - v2: pointer to second vector
/// - n: dimension of vectors
/// - p: prime number for p-adic arithmetic
///
/// # Returns
/// The p-adic inner product as f64, or NAN on error
///
/// # Safety
/// Caller must ensure:
/// - v1 and v2 point to valid arrays of at least n elements
/// - n > 0
/// - p is a prime number
#[no_mangle]
pub extern "C" fn padic_inner_product(
    v1: *const f64,
    v2: *const f64,
    n: usize,
    p: u64,
) -> f64 {
    if v1.is_null() || v2.is_null() || n == 0 || p < 2 {
        return f64::NAN;
    }

    let v1_slice = unsafe { slice::from_raw_parts(v1, n) };
    let v2_slice = unsafe { slice::from_raw_parts(v2, n) };

    padic::padic_inner_product(v1_slice, v2_slice, p)
}

/// Compute adelic inner product as restricted product
///
/// Computes: ⟨v1, v2⟩_∞ × ∏_{p ∈ primes} ⟨v1, v2⟩_p
///
/// # Parameters
/// - v1: pointer to first vector
/// - v2: pointer to second vector
/// - n: dimension of vectors
/// - primes: pointer to array of prime numbers
/// - n_primes: number of primes in the array
///
/// # Returns
/// The adelic inner product as f64, or NAN on error
///
/// # Safety
/// Caller must ensure:
/// - v1 and v2 point to valid arrays of at least n elements
/// - primes points to valid array of at least n_primes elements
/// - n > 0 and n_primes >= 0
#[no_mangle]
pub extern "C" fn adelic_inner_product(
    v1: *const f64,
    v2: *const f64,
    n: usize,
    primes: *const u64,
    n_primes: usize,
) -> f64 {
    if v1.is_null() || v2.is_null() || n == 0 {
        return f64::NAN;
    }

    let v1_slice = unsafe { slice::from_raw_parts(v1, n) };
    let v2_slice = unsafe { slice::from_raw_parts(v2, n) };

    let primes_slice = if n_primes > 0 && !primes.is_null() {
        unsafe { slice::from_raw_parts(primes, n_primes) }
    } else {
        &[]
    };

    adelic::adelic_inner_product(v1_slice, v2_slice, primes_slice)
}

/// Compute Gram matrix for a basis of vectors
///
/// # Parameters
/// - basis: pointer to flattened array of vectors (row-major)
/// - n_vectors: number of vectors
/// - dim: dimension of each vector
/// - number_system: number system type (0=real, 1=complex, 2=padic, 3=adelic)
/// - p: prime for p-adic computations (ignored for real/complex)
///
/// # Returns
/// Pointer to heap-allocated n_vectors × n_vectors Gram matrix (row-major order)
/// Returns NULL on error. Caller must free with free_array().
///
/// # Safety
/// Caller must ensure:
/// - basis points to valid array of n_vectors * dim elements
/// - n_vectors > 0 and dim > 0
/// - Returned pointer is freed with free_array()
#[no_mangle]
pub extern "C" fn gram_matrix(
    basis: *const f64,
    n_vectors: usize,
    dim: usize,
    number_system: u32,
    p: u64,
) -> *mut f64 {
    if basis.is_null() || n_vectors == 0 || dim == 0 {
        return core::ptr::null_mut();
    }

    let basis_slice = unsafe { slice::from_raw_parts(basis, n_vectors * dim) };

    let result = match number_system {
        0 => {
            // Real (Euclidean) metric
            linalg::gram_matrix_real(basis_slice, n_vectors, dim)
                .unwrap_or_else(|_| vec![f64::NAN; n_vectors * n_vectors])
        }
        1 => {
            // Complex (Euclidean, ignoring imaginary part)
            // For this implementation, we treat as real
            linalg::gram_matrix_real(basis_slice, n_vectors, dim)
                .unwrap_or_else(|_| vec![f64::NAN; n_vectors * n_vectors])
        }
        2 => {
            // P-adic
            if p < 2 {
                return core::ptr::null_mut();
            }
            compute_gram_matrix_padic(basis_slice, n_vectors, dim, p)
        }
        3 => {
            // Adelic
            compute_gram_matrix_adelic(basis_slice, n_vectors, dim, p)
        }
        _ => vec![f64::NAN; n_vectors * n_vectors],
    };

    let mut boxed = result.into_boxed_slice();
    let ptr = boxed.as_mut_ptr();
    core::mem::forget(boxed);
    ptr
}

/// Compute Gram matrix using p-adic inner product
fn compute_gram_matrix_padic(
    basis: &[f64],
    n_vectors: usize,
    dim: usize,
    p: u64,
) -> Vec<f64> {
    let mut gram = vec![0.0; n_vectors * n_vectors];

    for i in 0..n_vectors {
        for j in 0..n_vectors {
            let v_i = &basis[i * dim..(i + 1) * dim];
            let v_j = &basis[j * dim..(j + 1) * dim];
            gram[i * n_vectors + j] = padic::padic_inner_product(v_i, v_j, p);
        }
    }

    gram
}

/// Compute Gram matrix using adelic inner product
fn compute_gram_matrix_adelic(
    basis: &[f64],
    n_vectors: usize,
    dim: usize,
    p: u64,
) -> Vec<f64> {
    let mut gram = vec![0.0; n_vectors * n_vectors];

    // Default: use small set of common primes for adelic metric
    let default_primes = [2u64, 3, 5, 7, 11];

    for i in 0..n_vectors {
        for j in 0..n_vectors {
            let v_i = &basis[i * dim..(i + 1) * dim];
            let v_j = &basis[j * dim..(j + 1) * dim];
            gram[i * n_vectors + j] = adelic::adelic_inner_product(v_i, v_j, &default_primes);
        }
    }

    gram
}

/// Compute eigenvalues of a symmetric matrix
///
/// Uses the Jacobi eigenvalue method (no external dependencies).
///
/// # Parameters
/// - matrix: pointer to symmetric n×n matrix in row-major order
/// - n: size of the matrix
///
/// # Returns
/// Pointer to heap-allocated array of n eigenvalues (sorted in descending order)
/// Returns NULL on error. Caller must free with free_array().
///
/// # Safety
/// Caller must ensure:
/// - matrix points to valid array of n*n elements
/// - n > 0
/// - matrix is symmetric (within floating-point tolerance)
/// - Returned pointer is freed with free_array()
#[no_mangle]
pub extern "C" fn eigenvalues(matrix: *const f64, n: usize) -> *mut f64 {
    if matrix.is_null() || n == 0 {
        return core::ptr::null_mut();
    }

    let matrix_slice = unsafe { slice::from_raw_parts(matrix, n * n) };

    let result = linalg::jacobi_eigenvalues(matrix_slice, n)
        .unwrap_or_else(|_| vec![f64::NAN; n]);

    let mut boxed = result.into_boxed_slice();
    let ptr = boxed.as_mut_ptr();
    core::mem::forget(boxed);
    ptr
}

/// Free a heap-allocated array
///
/// # Parameters
/// - ptr: pointer to array allocated by gram_matrix() or eigenvalues()
///
/// # Safety
/// Caller must ensure:
/// - ptr was allocated by this library
/// - ptr is not used after this call
/// - ptr is only freed once
#[no_mangle]
pub extern "C" fn free_array(ptr: *mut f64) {
    if ptr.is_null() {
        return;
    }

    unsafe {
        // This is safe because we know the memory was allocated by this library
        // We reconstruct the boxed slice and let it drop
        let _ = Box::from_raw(ptr);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_padic_inner_product_ffi() {
        let v1 = vec![1.0, 2.0];
        let v2 = vec![3.0, 4.0];

        let result = padic_inner_product(v1.as_ptr(), v2.as_ptr(), 2, 2);
        assert!(!result.is_nan());
    }

    #[test]
    fn test_gram_matrix_ffi() {
        let basis = vec![1.0, 0.0, 0.0, 1.0]; // Identity basis
        let gram = gram_matrix(basis.as_ptr(), 2, 2, 0, 0);

        assert!(!gram.is_null());

        unsafe {
            let gram_array = slice::from_raw_parts(gram, 4);
            // Should be identity for orthonormal basis
            assert!((gram_array[0] - 1.0).abs() < 1e-10);
            free_array(gram);
        }
    }

    #[test]
    fn test_eigenvalues_ffi() {
        let matrix = vec![2.0, 0.0, 0.0, 3.0]; // Diagonal matrix
        let eigvals = eigenvalues(matrix.as_ptr(), 2);

        assert!(!eigvals.is_null());

        unsafe {
            let eigs = slice::from_raw_parts(eigvals, 2);
            // Should be 3.0 and 2.0 in descending order
            assert!((eigs[0] - 3.0).abs() < 1e-10);
            assert!((eigs[1] - 2.0).abs() < 1e-10);
            free_array(eigvals);
        }
    }

    #[test]
    fn test_free_array_null() {
        // Should not crash
        free_array(core::ptr::null_mut());
    }
}

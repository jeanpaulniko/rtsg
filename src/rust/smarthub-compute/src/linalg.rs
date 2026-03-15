/// Linear algebra module
/// Implements Gram matrix computation and eigenvalue calculation using Jacobi iteration

use core::f64;

/// Compute the Gram matrix for a set of vectors in a specified number system
///
/// # Parameters
/// - basis: flattened array of n_vectors x dim vectors
/// - n_vectors: number of vectors
/// - dim: dimension of each vector
/// - inner_product_fn: function to compute inner products
///
/// # Returns
/// Flattened n_vectors × n_vectors Gram matrix stored in row-major order
#[inline]
pub fn compute_gram_matrix<F>(
    basis: &[f64],
    n_vectors: usize,
    dim: usize,
    inner_product_fn: F,
) -> Result<Vec<f64>, &'static str>
where
    F: Fn(&[f64], &[f64]) -> f64,
{
    if n_vectors == 0 || dim == 0 {
        return Err("Empty vectors or dimension");
    }

    if basis.len() != n_vectors * dim {
        return Err("Basis size mismatch");
    }

    let mut gram = vec![0.0; n_vectors * n_vectors];

    // Compute each entry of the Gram matrix
    for i in 0..n_vectors {
        for j in 0..n_vectors {
            let v_i = &basis[i * dim..(i + 1) * dim];
            let v_j = &basis[j * dim..(j + 1) * dim];

            let ip = inner_product_fn(v_i, v_j);

            if ip.is_nan() {
                return Err("NaN in inner product");
            }

            gram[i * n_vectors + j] = ip;
        }
    }

    Ok(gram)
}

/// Real symmetric Gram matrix using Euclidean inner product
#[inline]
pub fn gram_matrix_real(basis: &[f64], n_vectors: usize, dim: usize) -> Result<Vec<f64>, &'static str> {
    compute_gram_matrix(basis, n_vectors, dim, euclidean_inner_product)
}

/// Euclidean inner product
#[inline]
fn euclidean_inner_product(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len() {
        return f64::NAN;
    }
    v1.iter().zip(v2.iter()).map(|(x, y)| x * y).sum()
}

/// Compute eigenvalues of a symmetric matrix using Jacobi iteration
///
/// This implements the Jacobi eigenvalue method:
/// 1. Find the largest off-diagonal element
/// 2. Apply a Givens rotation to zero it out
/// 3. Repeat until convergence
///
/// # Parameters
/// - matrix: symmetric n×n matrix in row-major order
/// - n: size of the matrix
///
/// # Returns
/// Vector of n eigenvalues, sorted in descending order
///
/// # Note
/// The method is O(n^3) and converges quadratically. For n < 100, this is typically
/// faster than other methods due to low overhead.
#[inline]
pub fn jacobi_eigenvalues(matrix: &[f64], n: usize) -> Result<Vec<f64>, &'static str> {
    if n == 0 {
        return Err("Empty matrix");
    }

    if matrix.len() != n * n {
        return Err("Matrix size mismatch");
    }

    // Verify symmetry (within tolerance)
    for i in 0..n {
        for j in i + 1..n {
            let diff = (matrix[i * n + j] - matrix[j * n + i]).abs();
            if diff > 1e-10 * (matrix[i * n + j].abs().max(matrix[j * n + i].abs())) {
                return Err("Matrix is not symmetric");
            }
        }
    }

    // Copy matrix to working array
    let mut a = matrix.to_vec();

    const MAX_ITERATIONS: usize = 1000;
    const TOLERANCE: f64 = 1e-14;

    for iteration in 0..MAX_ITERATIONS {
        // Find the largest off-diagonal element
        let (p, q, max_elem) = find_max_off_diagonal(&a, n);

        // Check convergence
        if max_elem.abs() < TOLERANCE {
            break;
        }

        // Compute the rotation angle
        let (cos_theta, sin_theta) = compute_rotation_angle(&a, n, p, q);

        // Apply Givens rotation
        apply_givens_rotation(&mut a, n, p, q, cos_theta, sin_theta);
    }

    // Extract eigenvalues from the diagonal
    let mut eigenvalues = Vec::with_capacity(n);
    for i in 0..n {
        eigenvalues.push(a[i * n + i]);
    }

    // Sort in descending order
    eigenvalues.sort_by(|a, b| b.partial_cmp(a).unwrap_or(core::cmp::Ordering::Equal));

    Ok(eigenvalues)
}

/// Find the largest off-diagonal element in a symmetric matrix
#[inline]
fn find_max_off_diagonal(matrix: &[f64], n: usize) -> (usize, usize, f64) {
    let mut max_p = 0;
    let mut max_q = 1;
    let mut max_elem = 0.0;

    for i in 0..n {
        for j in i + 1..n {
            let elem = matrix[i * n + j].abs();
            if elem > max_elem {
                max_elem = elem;
                max_p = i;
                max_q = j;
            }
        }
    }

    (max_p, max_q, matrix[max_p * n + max_q])
}

/// Compute the Givens rotation angle to zero out element (p, q)
#[inline]
fn compute_rotation_angle(matrix: &[f64], n: usize, p: usize, q: usize) -> (f64, f64) {
    let app = matrix[p * n + p];
    let aqq = matrix[q * n + q];
    let apq = matrix[p * n + q];

    let theta = if (app - aqq).abs() < 1e-14 {
        // Special case: a_pp ≈ a_qq
        core::f64::consts::PI / 4.0
    } else {
        0.5 * ((2.0 * apq) / (app - aqq)).atan()
    };

    (theta.cos(), theta.sin())
}

/// Apply a Givens rotation to a symmetric matrix
#[inline]
fn apply_givens_rotation(
    matrix: &mut [f64],
    n: usize,
    p: usize,
    q: usize,
    cos_theta: f64,
    sin_theta: f64,
) {
    // Cache frequently accessed values
    let c = cos_theta;
    let s = sin_theta;

    // Rotate all elements
    for i in 0..n {
        if i != p && i != q {
            let aip = matrix[i * n + p];
            let aiq = matrix[i * n + q];

            let new_aip = c * aip - s * aiq;
            let new_aiq = s * aip + c * aiq;

            matrix[i * n + p] = new_aip;
            matrix[p * n + i] = new_aip;
            matrix[i * n + q] = new_aiq;
            matrix[q * n + i] = new_aiq;
        }
    }

    // Update diagonal and off-diagonal (p, q)
    let app = matrix[p * n + p];
    let aqq = matrix[q * n + q];
    let apq = matrix[p * n + q];

    let new_app = c * c * app - 2.0 * s * c * apq + s * s * aqq;
    let new_aqq = s * s * app + 2.0 * s * c * apq + c * c * aqq;
    let new_apq = s * c * (app - aqq) + (c * c - s * s) * apq;

    matrix[p * n + p] = new_app;
    matrix[q * n + q] = new_aqq;
    matrix[p * n + q] = new_apq;
    matrix[q * n + p] = new_apq;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gram_matrix_real() {
        // Two orthonormal vectors
        let basis = vec![1.0, 0.0, 0.0, 1.0]; // [1,0] and [0,1]
        let gram = gram_matrix_real(&basis, 2, 2).unwrap();

        // Gram matrix should be identity
        assert!((gram[0] - 1.0).abs() < 1e-10); // ⟨v1, v1⟩
        assert!((gram[1] - 0.0).abs() < 1e-10); // ⟨v1, v2⟩
        assert!((gram[2] - 0.0).abs() < 1e-10); // ⟨v2, v1⟩
        assert!((gram[3] - 1.0).abs() < 1e-10); // ⟨v2, v2⟩
    }

    #[test]
    fn test_jacobi_eigenvalues() {
        // Diagonal matrix: eigenvalues are the diagonal elements
        let matrix = vec![2.0, 0.0, 0.0, 3.0]; // 2x2 diagonal matrix
        let eigvals = jacobi_eigenvalues(&matrix, 2).unwrap();

        assert!((eigvals[0] - 3.0).abs() < 1e-10);
        assert!((eigvals[1] - 2.0).abs() < 1e-10);
    }

    #[test]
    fn test_jacobi_eigenvalues_non_diagonal() {
        // 2x2 symmetric matrix: [[4, 2], [2, 3]]
        let matrix = vec![4.0, 2.0, 2.0, 3.0];
        let eigvals = jacobi_eigenvalues(&matrix, 2).unwrap();

        // Eigenvalues of [[4,2],[2,3]]: λ ≈ 5.236 and 1.764
        assert!(eigvals[0] > 5.0 && eigvals[0] < 5.5);
        assert!(eigvals[1] > 1.5 && eigvals[1] < 2.0);
    }
}

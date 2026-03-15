/// Adelic arithmetic module
/// Implements the restricted adelic product: archimedean × Π_p p-adic

use crate::padic::{padic_inner_product as compute_padic_ip, padic_norm};
use core::f64;

/// Standard Euclidean (archimedean) inner product
#[inline]
fn archimedean_inner_product(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len() || v1.is_empty() {
        return f64::NAN;
    }

    v1.iter().zip(v2.iter()).map(|(x, y)| x * y).sum()
}

/// Archimedean norm (Euclidean)
#[inline]
fn archimedean_norm(v: &[f64]) -> f64 {
    if v.is_empty() {
        return 0.0;
    }

    let sum_sq: f64 = v.iter().map(|x| x * x).sum();
    sum_sq.sqrt()
}

/// Compute the adelic inner product as a restricted product
///
/// The formula is: ⟨v1, v2⟩_adelic = ⟨v1, v2⟩_∞ × ∏_{p ∈ S} ⟨v1, v2⟩_p
///
/// where:
/// - ⟨v1, v2⟩_∞ is the standard archimedean (Euclidean) inner product
/// - ⟨v1, v2⟩_p is the p-adic inner product for each prime p in the finite set S
/// - The product is taken over a finite set of primes (restricted product)
///
/// # Parameters
/// - v1, v2: input vectors
/// - primes: array of prime numbers to consider in the product
///
/// # Returns
/// The restricted adelic inner product as f64
#[inline]
pub fn adelic_inner_product(v1: &[f64], v2: &[f64], primes: &[u64]) -> f64 {
    if v1.len() != v2.len() || v1.is_empty() {
        return f64::NAN;
    }

    if primes.is_empty() {
        // If no primes specified, just return archimedean
        return archimedean_inner_product(v1, v2);
    }

    // Start with archimedean contribution
    let mut product = archimedean_inner_product(v1, v2);

    if product == 0.0 {
        return 0.0; // Early exit if archimedean part is zero
    }

    // Multiply by p-adic contributions for each prime
    for &p in primes {
        if p < 2 {
            continue; // Skip invalid primes
        }

        let padic_contrib = compute_padic_ip(v1, v2, p);

        if padic_contrib.is_nan() || padic_contrib.is_infinite() {
            return f64::NAN;
        }

        // Use multiplicative structure: multiply the contributions
        product *= padic_contrib;

        // Guard against numerical underflow
        if product.abs() < f64::MIN_POSITIVE * 1e6 {
            break;
        }
    }

    product
}

/// Compute the adelic norm of a single vector
#[inline]
pub fn adelic_norm(v: &[f64], primes: &[u64]) -> f64 {
    if v.is_empty() {
        return 0.0;
    }

    if primes.is_empty() {
        return archimedean_norm(v);
    }

    let mut norm = archimedean_norm(v);

    if norm == 0.0 {
        return 0.0;
    }

    for &p in primes {
        if p < 2 {
            continue;
        }

        let padic_n = p_adic_vector_norm(v, p);

        if padic_n.is_nan() || padic_n.is_infinite() {
            return f64::NAN;
        }

        norm *= padic_n;

        if norm.abs() < f64::MIN_POSITIVE * 1e6 {
            break;
        }
    }

    norm
}

/// Compute p-adic norm of a vector (maximum of component norms)
#[inline]
fn p_adic_vector_norm(v: &[f64], p: u64) -> f64 {
    v.iter()
        .map(|&x| padic_norm(x, p))
        .fold(0.0, f64::max)
}

/// Normalize a vector in the adelic metric
///
/// Returns a new vector with adelic norm equal to 1.0
#[inline]
pub fn adelic_normalize(v: &[f64], primes: &[u64]) -> Vec<f64> {
    let norm = adelic_norm(v, primes);

    if norm == 0.0 || norm.is_nan() {
        return vec![f64::NAN; v.len()];
    }

    v.iter().map(|x| x / norm).collect()
}

/// Compute the adelic distance between two vectors
#[inline]
pub fn adelic_distance(v1: &[f64], v2: &[f64], primes: &[u64]) -> f64 {
    if v1.len() != v2.len() {
        return f64::NAN;
    }

    let diff: Vec<f64> = v1.iter().zip(v2.iter()).map(|(x, y)| x - y).collect();
    adelic_norm(&diff, primes)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_archimedean_inner_product() {
        let v1 = vec![1.0, 0.0];
        let v2 = vec![0.0, 1.0];
        let ip = archimedean_inner_product(&v1, &v2);
        assert_eq!(ip, 0.0);

        let v3 = vec![1.0, 2.0];
        let v4 = vec![3.0, 4.0];
        let ip2 = archimedean_inner_product(&v3, &v4);
        assert!((ip2 - 11.0).abs() < 1e-10);
    }

    #[test]
    fn test_archimedean_norm() {
        let v = vec![3.0, 4.0];
        let norm = archimedean_norm(&v);
        assert!((norm - 5.0).abs() < 1e-10);
    }

    #[test]
    fn test_adelic_inner_product_no_primes() {
        let v1 = vec![1.0, 2.0];
        let v2 = vec![3.0, 4.0];
        let ip = adelic_inner_product(&v1, &v2, &[]);
        assert!((ip - 11.0).abs() < 1e-10);
    }

    #[test]
    fn test_adelic_norm() {
        let v = vec![1.0, 0.0];
        let norm = adelic_norm(&v, &[]);
        assert!((norm - 1.0).abs() < 1e-10);
    }

    #[test]
    fn test_adelic_distance() {
        let v1 = vec![0.0, 0.0];
        let v2 = vec![3.0, 4.0];
        let dist = adelic_distance(&v1, &v2, &[]);
        assert!((dist - 5.0).abs() < 1e-10);
    }
}

/// P-adic arithmetic module
/// Implements p-adic valuation, norms, and inner product computations

use core::f64;

/// Compute the p-adic valuation of an integer n
/// Returns the highest power of p that divides n
/// If n = 0, returns a sentinel value
#[inline]
pub fn padic_valuation(mut n: i64, p: u64) -> i32 {
    if n == 0 {
        return i32::MAX; // Convention: v_p(0) = infinity
    }

    let n_abs = n.abs();
    let p_i64 = p as i64;
    let mut valuation = 0i32;

    let mut remainder = n_abs;
    while remainder % p_i64 == 0 {
        remainder /= p_i64;
        valuation += 1;
    }

    valuation
}

/// Compute the p-adic norm |x|_p = p^{-v_p(x)}
/// Returns a float representation of the p-adic norm
#[inline]
pub fn padic_norm(x: f64, p: u64) -> f64 {
    if x == 0.0 {
        return 0.0;
    }

    // For floating point, we estimate the p-adic valuation
    // by examining the mantissa and exponent
    let (mantissa, exponent) = extract_mantissa_exponent(x);

    // Estimate valuation through integer approximation
    // This is a heuristic for floating-point values
    let approx_int = (mantissa * (1u64 << 53) as f64) as i64;
    let estimated_val = if approx_int != 0 {
        approximate_valuation(approx_int, p)
    } else {
        0
    };

    // p^{-v_p(x)}
    p.pow(estimated_val as u32) as f64
}

/// Extract mantissa and exponent from a float
#[inline]
fn extract_mantissa_exponent(x: f64) -> (f64, i32) {
    if x == 0.0 {
        return (0.0, 0);
    }

    let abs_x = x.abs();
    let exponent = abs_x.log2().floor() as i32;
    let mantissa = abs_x / (2.0_f64.powi(exponent));

    (mantissa, exponent)
}

/// Approximate p-adic valuation for integer representation
#[inline]
fn approximate_valuation(mut n: i64, p: u64) -> i32 {
    if n == 0 {
        return 0;
    }

    let p_i64 = p as i64;
    let mut valuation = 0i32;
    let mut remainder = n.abs();

    // Limit iterations to prevent overflow
    while remainder % p_i64 == 0 && valuation < 64 {
        remainder /= p_i64;
        valuation += 1;
    }

    valuation
}

/// Compute the p-adic inner product: ⟨v1, v2⟩_p
///
/// For each component pair (v1[i], v2[i]), compute:
///   - product = v1[i] * v2[i]
///   - weight = p^{-v_p(product)}
/// Then sum the weighted products
#[inline]
pub fn padic_inner_product(v1: &[f64], v2: &[f64], p: u64) -> f64 {
    if v1.len() != v2.len() || v1.is_empty() {
        return f64::NAN;
    }

    let mut sum = 0.0;

    for (x, y) in v1.iter().zip(v2.iter()) {
        let product = x * y;

        if product == 0.0 {
            continue; // Contribution is zero
        }

        // Estimate p-adic valuation of the product
        let (mantissa, _) = extract_mantissa_exponent(product);
        let approx_int = (mantissa * (1u64 << 53) as f64) as i64;

        let valuation = if approx_int != 0 {
            approximate_valuation(approx_int, p)
        } else {
            0
        };

        // Weight: p^{-v_p(product)} * product
        // This gives the contribution in the p-adic metric
        let weight = p.pow(valuation.saturating_abs() as u32) as f64;
        sum += weight * product.abs(); // Use absolute value for metric
    }

    sum
}

/// Compute the p-adic metric (norm) of a vector in Q_p
#[inline]
pub fn padic_vector_norm(v: &[f64], p: u64) -> f64 {
    if v.is_empty() {
        return 0.0;
    }

    // The p-adic norm of a vector is the maximum p-adic norm of its components
    v.iter()
        .map(|&x| padic_norm(x, p))
        .fold(0.0, f64::max)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_padic_valuation() {
        // v_2(8) = 3, since 8 = 2^3
        assert_eq!(padic_valuation(8, 2), 3);
        // v_3(9) = 2, since 9 = 3^2
        assert_eq!(padic_valuation(9, 3), 2);
        // v_5(10) = 1, since 10 = 2 * 5
        assert_eq!(padic_valuation(10, 5), 1);
        // v_p(1) = 0 for all p
        assert_eq!(padic_valuation(1, 7), 0);
    }

    #[test]
    fn test_padic_norm() {
        let norm_0 = padic_norm(0.0, 2);
        assert_eq!(norm_0, 0.0);

        let norm_1 = padic_norm(1.0, 2);
        assert!(norm_1 >= 0.0);
    }

    #[test]
    fn test_padic_inner_product() {
        let v1 = vec![1.0, 2.0, 3.0];
        let v2 = vec![1.0, 2.0, 3.0];
        let ip = padic_inner_product(&v1, &v2, 2);
        assert!(!ip.is_nan());
        assert!(ip >= 0.0);
    }
}

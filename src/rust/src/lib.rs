//! RTSG Framework High-Performance Compute Library
//!
//! This library provides p-adic and adelic inner product computations optimized for the
//! RTSG (Representation Theory Spectral Geometry) framework.
//!
//! ## Architecture
//!
//! The library is organized into several modules:
//!
//! - **padic**: P-adic arithmetic operations including valuation and inner products
//! - **adelic**: Adelic metrics as restricted products of p-adic and archimedean components
//! - **linalg**: Linear algebra operations (Gram matrices, eigenvalues via Jacobi method)
//! - **ffi**: C-compatible FFI exports for Go integration
//!
//! ## Features
//!
//! - Zero external dependencies (pure Rust)
//! - Production-grade error handling
//! - High-performance implementations with no panics in FFI boundary
//! - Jacobi eigenvalue method for symmetric matrices
//! - Support for multiple number systems (real, complex, p-adic, adelic)
//!
//! ## Usage from C/Go
//!
//! The library exports the following functions:
//!
//! - `padic_inner_product(v1, v2, n, p) -> f64`
//! - `adelic_inner_product(v1, v2, n, primes, n_primes) -> f64`
//! - `gram_matrix(basis, n_vectors, dim, number_system, p) -> *mut f64`
//! - `eigenvalues(matrix, n) -> *mut f64`
//! - `free_array(ptr)`

#![no_std]
#![allow(unsafe_code)] // FFI requires unsafe code

extern crate alloc;

pub mod adelic;
pub mod ffi;
pub mod linalg;
pub mod padic;

/// Library version
pub const VERSION: &str = "0.1.0";

/// Get library version string
#[no_mangle]
pub extern "C" fn get_version() -> *const u8 {
    VERSION.as_ptr()
}

/// Library health check
///
/// # Returns
/// 1 if library is functional, 0 otherwise
#[no_mangle]
pub extern "C" fn health_check() -> u32 {
    // Perform a simple sanity check
    let v1 = [1.0, 2.0];
    let v2 = [3.0, 4.0];
    let ip = padic::padic_inner_product(&v1, &v2, 2);

    if ip.is_finite() {
        1
    } else {
        0
    }
}

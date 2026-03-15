//! Test binary for the smarthub-compute library
//!
//! This demonstrates the library's capabilities and can be used for benchmarking

#[cfg(feature = "test_binary")]
fn main() {
    use smarthub_compute::padic;
    use smarthub_compute::adelic;
    use smarthub_compute::linalg;

    println!("=== RTSG Compute Library Test ===\n");

    // Test 1: P-adic valuation
    println!("Test 1: P-adic Valuation");
    println!("  v_2(8) = {}", padic::padic_valuation(8, 2));
    println!("  v_3(27) = {}", padic::padic_valuation(27, 3));
    println!("  v_5(100) = {}", padic::padic_valuation(100, 5));
    println!();

    // Test 2: P-adic inner product
    println!("Test 2: P-adic Inner Product");
    let v1 = vec![1.0, 2.0, 3.0];
    let v2 = vec![1.0, 2.0, 3.0];
    let ip_2 = padic::padic_inner_product(&v1, &v2, 2);
    let ip_3 = padic::padic_inner_product(&v1, &v2, 3);
    println!("  ⟨[1,2,3], [1,2,3]⟩_2 ≈ {:.6}", ip_2);
    println!("  ⟨[1,2,3], [1,2,3]⟩_3 ≈ {:.6}", ip_3);
    println!();

    // Test 3: Adelic inner product
    println!("Test 3: Adelic Inner Product");
    let v3 = vec![1.0, 0.0];
    let v4 = vec![0.0, 1.0];
    let primes = vec![2u64, 3, 5];
    let adelic_ip = adelic::adelic_inner_product(&v3, &v4, &primes);
    println!("  ⟨[1,0], [0,1]⟩_adelic (p ∈ {{2,3,5}}) = {:.6}", adelic_ip);
    println!();

    // Test 4: Gram matrix (Euclidean)
    println!("Test 4: Gram Matrix (Real)");
    let basis = vec![1.0, 0.0, 0.0, 1.0]; // [1,0] and [0,1]
    match linalg::gram_matrix_real(&basis, 2, 2) {
        Ok(gram) => {
            println!("  Gram matrix for orthonormal basis:");
            println!("    [[ {:.2}, {:.2} ]", gram[0], gram[1]);
            println!("     [ {:.2}, {:.2} ]]", gram[2], gram[3]);
        }
        Err(e) => println!("  Error: {}", e),
    }
    println!();

    // Test 5: Eigenvalues
    println!("Test 5: Eigenvalues (Jacobi method)");
    let matrix = vec![4.0, 2.0, 2.0, 3.0]; // [[4,2],[2,3]]
    match linalg::jacobi_eigenvalues(&matrix, 2) {
        Ok(eigvals) => {
            println!("  Eigenvalues of [[4,2],[2,3]]:");
            for (i, &ev) in eigvals.iter().enumerate() {
                println!("    λ_{} = {:.6}", i + 1, ev);
            }
        }
        Err(e) => println!("  Error: {}", e),
    }
    println!();

    // Test 6: P-adic norm
    println!("Test 6: P-adic Norm");
    let norm_2 = padic::padic_norm(8.0, 2);
    let norm_3 = padic::padic_norm(9.0, 3);
    println!("  |8|_2 = {:.6}", norm_2);
    println!("  |9|_3 = {:.6}", norm_3);
    println!();

    println!("=== All Tests Complete ===");
}

#[cfg(not(feature = "test_binary"))]
fn main() {
    println!("Run with --features test_binary to enable tests");
}

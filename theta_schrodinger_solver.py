import numpy as np
import matplotlib.pyplot as plt

# Generate theta function

def theta_function(z):
    return 0.5 * (z + np.sign(z) * np.sqrt(z**2))

# Compute potential

def potential(x):
    return np.sin(np.pi * x)**2

# Spectral method solver

def schrodinger_solver(n, x_min, x_max):
    x = np.linspace(x_min, x_max, n)
    V = potential(x)
    H = np.diag(V) + np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)
    H[0, 0] += 1e10  # Boundary condition
    H[-1, -1] += 1e10  # Boundary condition
    eigenvals, _ = np.linalg.eigh(H)
    return eigenvals

# Compare with zeta zero

def zeta_zero_comparison(eigenvals):
    zeta_zeros = np.array([14.134725141734693790457251983243, 21.022039638771554992628479423493, 
                           25.01085758014568850])  # Early zeta zeros
    plt.plot(eigenvals, 'o', label='Eigenvalues')
    plt.plot(zeta_zeros, 'x', color='red', label='Zeta Zeros')
    plt.xlabel('Eigenvalue Index')
    plt.ylabel('Value')
    plt.title('Comparison of Eigenvalues and Zeta Zeros')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == '__main__':
    eigenvals = schrodinger_solver(100, 0, 1)
    print('Eigenvalues:', eigenvals)
    zeta_zero_comparison(eigenvals)
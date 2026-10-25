# omp_reconstruction.py
# Implementation of Orthogonal Matching Pursuit (OMP) for Compressive Sensing.
# This is a major step forward from simple linear interpolation.

import numpy as np
import matplotlib.pyplot as plt

def generate_mock_ecg(duration=5, sampling_rate=250):
    t = np.linspace(0, duration, duration * sampling_rate)
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))
    return t, signal

def omp_algorithm(y, A, sparsity_k):
    """
    Orthogonal Matching Pursuit (OMP) Algorithm.
    y: Compressed measurements
    A: Sensing matrix (Phi * Psi)
    sparsity_k: Number of non-zero elements (sparsity level)
    """
    m, n = A.shape
    x_hat = np.zeros(n) # Reconstructed sparse vector
    residual = y.copy() # Initial residual
    index_set = []      # Indices of selected columns
    
    for _ in range(sparsity_k):
        # 1. Find the column most correlated with the residual
        correlations = np.abs(A.T @ residual)
        
        # Ignore already selected indices
        if len(index_set) > 0:
            correlations[index_set] = -1
            
        best_index = np.argmax(correlations)
        index_set.append(best_index)
        
        # 2. Solve the least squares problem to update the coefficients
        A_subset = A[:, index_set]
        x_subset, _, _, _ = np.linalg.lstsq(A_subset, y, rcond=None)
        
        # 3. Update residual
        residual = y - A_subset @ x_subset
        
    x_hat[index_set] = x_subset
    return x_hat

if __name__ == "__main__":
    print("--- OMP Reconstruction Demo ---")
    time, ecg = generate_mock_ecg()
    n = len(ecg)
    m = int(n * 0.4) # Keep 40% of samples (Measurement size)
    
    # Create a random sensing matrix (Phi) and a sparse basis (Psi)
    Phi = np.random.randn(m, n) / np.sqrt(m)
    
    # For simplicity, let's assume the signal itself is sparse (Identity basis Psi = I)
    # So A = Phi * I = Phi
    A = Phi
    
    # Create compressed measurements
    y = Phi @ ecg
    
    # Run OMP
    sparsity_level = 20 # Assume the signal has 20 main components
    print(f"Running OMP with sparsity level {sparsity_level}...")
    reconstructed_ecg = omp_algorithm(y, A, sparsity_level)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(time, ecg, label="Original Signal", color='blue', alpha=0.5)
    plt.plot(time, reconstructed_ecg, label="OMP Reconstructed", color='red', linestyle='dashed')
    plt.title("Signal Reconstruction using OMP")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("OMP Algorithm executed successfully.")

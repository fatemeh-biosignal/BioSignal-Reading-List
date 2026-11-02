# performance_evaluation.py
# Evaluates the performance of OMP vs. Linear Interpolation.
# This is crucial for the ICEE 2027 paper.

import numpy as np
import matplotlib.pyplot as plt
from reconstruction_demo import simple_reconstruction
from omp_reconstruction import omp_algorithm

def generate_mock_ecg(duration=5, sampling_rate=250):
    t = np.linspace(0, duration, duration * sampling_rate)
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))
    return t, signal

if __name__ == "__main__":
    print("--- Performance Evaluation: Interpolation vs. OMP ---")
    
    time, ecg = generate_mock_ecg()
    n_samples = len(ecg)
    n_measurements = int(n_samples * 0.4) # Keep 40%
    
    # Create compressed measurements
    indices = np.random.choice(n_samples, n_measurements, replace=False)
    compressed = ecg[indices]
    
    # 1. Linear Interpolation
    interp_reconstructed = simple_reconstruction(n_samples, indices, compressed)
    mse_interp = np.mean((ecg - interp_reconstructed) ** 2)
    
    # 2. OMP Algorithm
    # For OMP, we need a sensing matrix (Phi)
    Phi = np.random.randn(n_measurements, n_samples) / np.sqrt(n_measurements)
    y = Phi @ ecg
    omp_reconstructed = omp_algorithm(y, Phi, sparsity_k=20)
    mse_omp = np.mean((ecg - omp_reconstructed) ** 2)
    
    print(f"MSE (Linear Interpolation): {mse_interp:.6f}")
    print(f"MSE (OMP Algorithm): {mse_omp:.6f}")
    
    # Plotting the comparison
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(time, ecg, color='blue')
    plt.title("Original Signal")
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(time, interp_reconstructed, color='orange')
    plt.title(f"Linear Interpolation (MSE: {mse_interp:.4f})")
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(time, omp_reconstructed, color='green')
    plt.title(f"OMP Reconstruction (MSE: {mse_omp:.4f})")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    print("Performance evaluation completed.")

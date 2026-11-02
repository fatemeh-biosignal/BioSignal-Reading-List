# test_pipeline.py
# A simple automated test to ensure the core components of the project work correctly.

import numpy as np
from ecg_processor import ECGProcessor
from omp_reconstruction import omp_algorithm

def test_ecg_processor():
    print("Testing ECGProcessor class...")
    processor = ECGProcessor(duration=2, sampling_rate=250)
    signal = processor.generate_signal()
    assert len(signal) == 500, "Signal length is incorrect!"
    
    filtered = processor.apply_moving_average_filter()
    assert len(filtered) == 500, "Filtered signal length is incorrect!"
    print("✅ ECGProcessor test passed.")

def test_omp_algorithm():
    print("Testing OMP Algorithm...")
    # Create a simple sparse signal
    n = 100
    x_true = np.zeros(n)
    x_true[10] = 1.0  # One spike
    
    # Create a sensing matrix
    m = 40
    A = np.random.randn(m, n) / np.sqrt(m)
    y = A @ x_true
    
    # Reconstruct
    x_reconstructed = omp_algorithm(y, A, sparsity_k=1)
    
    # Check if the spike is in the right place
    assert np.argmax(np.abs(x_reconstructed)) == 10, "OMP failed to find the correct spike!"
    print("✅ OMP Algorithm test passed.")

if __name__ == "__main__":
    print("--- Running Automated Tests ---")
    test_ecg_processor()
    test_omp_algorithm()
    print("\n🎉 All tests passed successfully! The pipeline is ready.")

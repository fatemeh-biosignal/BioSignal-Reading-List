# reconstruction_demo.py
# A basic demonstration of signal reconstruction from compressed samples.
# This shows how to recover the original ECG signal from 30% of measurements.

import numpy as np

def generate_mock_ecg(duration=5, sampling_rate=250):
    t = np.linspace(0, duration, duration * sampling_rate)
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))
    return t, signal

def simple_reconstruction(original_length, indices, compressed_signal):
    """
    A very basic (naive) reconstruction: placing the known values back 
    and using interpolation for the missing parts.
    (In a real project, we would use OMP or FISTA here).
    """
    # Create an empty array of the original length
    reconstructed = np.zeros(original_length)
    
    # Place the known (compressed) values back
    reconstructed[indices] = compressed_signal
    
    # For the missing points, we can just use linear interpolation as a placeholder
    # (This is not Compressive Sensing reconstruction, but a simple fill-in)
    x_known = indices
    y_known = compressed_signal
    x_all = np.arange(original_length)
    
    reconstructed = np.interp(x_all, x_known, y_known)
    
    return reconstructed

if __name__ == "__main__":
    print("--- Reconstruction Demo ---")
    time, ecg = generate_mock_ecg()
    
    # Compress (keep 30%)
    n_samples = len(ecg)
    n_measurements = int(n_samples * 0.3)
    indices = np.random.choice(n_samples, n_measurements, replace=False)
    compressed = ecg[indices]
    
    print(f"Original samples: {n_samples}")
    print(f"Compressed samples: {n_measurements}")
    
    # Reconstruct
    print("Reconstructing signal...")
    reconstructed = simple_reconstruction(n_samples, indices, compressed)
    
    # Calculate error
    error = np.mean((ecg - reconstructed) ** 2)
    print(f"Mean Squared Error (MSE): {error:.4f}")
    print("Reconstruction complete. Next step: Implement OMP algorithm.")

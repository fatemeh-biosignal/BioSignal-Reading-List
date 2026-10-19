# compressed_sensing_demo.py
# A basic demonstration of Compressive Sensing for ECG signals.
# This is the core algorithm for my Khwarizmi Award project.

import numpy as np
import matplotlib.pyplot as plt

def generate_mock_ecg(duration=5, sampling_rate=250):
    t = np.linspace(0, duration, duration * sampling_rate)
    # Simple synthetic signal
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))
    return t, signal

def apply_compressive_sensing(signal, compression_ratio=0.3):
    """
    Simulates taking fewer measurements (compression).
    We take only 30% of the original samples.
    """
    n_samples = len(signal)
    n_measurements = int(n_samples * compression_ratio)
    
    # Randomly select indices to keep (simulating a sensing matrix)
    indices = np.random.choice(n_samples, n_measurements, replace=False)
    compressed_signal = signal[indices]
    
    return indices, compressed_signal

if __name__ == "__main__":
    print("Generating mock ECG...")
    time, ecg = generate_mock_ecg()
    
    print("Applying Compressive Sensing (keeping 30% of data)...")
    indices, compressed = apply_compressive_sensing(ecg, compression_ratio=0.3)
    
    print(f"Original samples: {len(ecg)}")
    print(f"Compressed samples: {len(compressed)}")
    
    # In the next phase, I will add the reconstruction algorithm (like OMP or FISTA)
    # to recover the full signal from these 30% measurements.

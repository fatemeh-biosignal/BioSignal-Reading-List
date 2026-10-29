# compressed_sensing_demo.py
# A basic demonstration of Compressive Sensing for ECG signals.
# This is the core algorithm for my Khwarizmi Award project.

import numpy as np
import matplotlib.pyplot as plt
from ecg_processor import ECGProcessor
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
    # --- Plotting the results ---
    plt.figure(figsize=(10, 6))

    # 1. Plot the original signal
    plt.subplot(2, 1, 1)
    plt.plot(time, ecg, label="Original ECG", color='blue')
    plt.title("Original Signal (100% samples)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    # 2. Plot the compressed signal (sub-sampled)
    plt.subplot(2, 1, 2)
    # Show the original signal in the background (faded)
    plt.plot(time, ecg, label="Original ECG (faded)", color='lightblue', alpha=0.5) 
    # Show the compressed points in red
    plt.scatter(time[indices], compressed, color='red', label="Compressed Samples (30%)")
    plt.title("Compressed Signal (Sub-sampled)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    print("Plot generated. In a real environment, a graph window would open here.")
    # --- Testing the new Object-Oriented Approach ---
    print("\n--- Testing ECGProcessor Class ---")
    processor = ECGProcessor(duration=5, sampling_rate=250)

    # Generate and filter using the class
    raw_class_signal = processor.generate_signal()
    filtered_class_signal = processor.apply_moving_average_filter()

    # Compress using the class
    indices_class, compressed_class = processor.compress_signal(compression_ratio=0.3)

    print(f"Class-based compressed samples: {len(compressed_class)}")
    print("ECGProcessor class integrated successfully.")

# real_ecg_analysis.py
# This script demonstrates how to handle real ECG data and apply noise.
# In a real scenario, we would load data from the MIT-BIH Arrhythmia Database.

import numpy as np
import matplotlib.pyplot as plt

def load_mock_real_data():
    """
    Simulates loading a real ECG record (e.g., from MIT-BIH database).
    For now, it generates a more realistic-looking ECG with baseline wander.
    """
    fs = 360  # Sampling frequency of MIT-BIH database (360 Hz)
    duration = 5  # seconds
    t = np.linspace(0, duration, duration * fs)
    
    # Simulate a more complex signal (base + wander + noise)
    base_signal = np.sin(2 * np.pi * 1.2 * t)  # Heart rate
    baseline_wander = 0.2 * np.sin(2 * np.pi * 0.3 * t) # Low-frequency noise (breathing)
    noise = 0.05 * np.random.randn(len(t))
    
    signal = base_signal + baseline_wander + noise
    return t, signal

def apply_noise_filter(signal):
    """
    Applies a simple moving average filter to remove high-frequency noise.
    """
    window_size = 5
    filtered_signal = np.convolve(signal, np.ones(window_size)/window_size, mode='same')
    return filtered_signal

if __name__ == "__main__":
    print("--- Real ECG Signal Analysis ---")
    time, raw_signal = load_mock_real_data()
    
    print("Applying moving average filter to remove noise...")
    filtered_signal = apply_noise_filter(raw_signal)
    
    # Plotting the comparison
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, raw_signal, color='red', label="Raw Signal (with noise)")
    plt.title("Raw ECG Signal (Simulating Real-World Conditions)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time, filtered_signal, color='green', label="Filtered Signal")
    plt.title("Filtered ECG Signal (Noise Removed)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print("Analysis complete. This is a crucial step before applying Compressive Sensing.")

# wavelet_analysis.py
# Applying Wavelet Transform to the ECG signal to show sparsity.
# Wavelets are crucial for Compressive Sensing because they make the signal sparse.

import numpy as np
import matplotlib.pyplot as plt
import pywt  # PyWavelets library

def generate_mock_ecg(duration=5, sampling_rate=250):
    t = np.linspace(0, duration, duration * sampling_rate)
    # Create a slightly more complex ECG-like signal
    signal = (
        np.sin(2 * np.pi * 1.2 * t) + 
        0.5 * np.sin(2 * np.pi * 5 * t) + 
        0.05 * np.random.randn(len(t))
    )
    return t, signal

if __name__ == "__main__":
    print("--- Wavelet Analysis ---")
    time, ecg = generate_mock_ecg()
    
    # Perform Discrete Wavelet Transform (DWT)
    # 'db4' is a common wavelet for ECG analysis
    wavelet_name = 'db4'
    coeffs = pywt.wavedec(ecg, wavelet_name, level=4)
    
    print(f"Original signal length: {len(ecg)}")
    print(f"Number of wavelet coefficient arrays: {len(coeffs)}")
    
    # Plotting the signal and its wavelet coefficients
    plt.figure(figsize=(10, 6))
    
    # 1. Original Signal
    plt.subplot(2, 1, 1)
    plt.plot(time, ecg, color='blue')
    plt.title("Original ECG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # 2. Wavelet Coefficients (Approximation)
    plt.subplot(2, 1, 2)
    plt.plot(coeffs[0], color='green')
    plt.title(f"Approximation Coefficients (Wavelet: {wavelet_name})")
    plt.xlabel("Coefficient Index")
    plt.ylabel("Value")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    print("Wavelet transform completed successfully.")

# advanced_filtering.py
# Implementing advanced filtering techniques for ECG signals.
# This goes beyond the simple moving average filter.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def generate_noisy_ecg(duration=5, sampling_rate=250):
    """Generates an ECG signal with baseline wander and high-frequency noise."""
    t = np.linspace(0, duration, duration * sampling_rate)
    # Base ECG (simulated)
    ecg = np.sin(2 * np.pi * 1.2 * t) 
    # Baseline wander (low frequency)
    baseline = 0.5 * np.sin(2 * np.pi * 0.1 * t)
    # High-frequency noise (e.g., muscle artifacts)
    noise = 0.2 * np.random.randn(len(t))
    
    noisy_ecg = ecg + baseline + noise
    return t, noisy_ecg

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    """Applies a Butterworth bandpass filter to remove baseline wander and high-frequency noise."""
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

if __name__ == "__main__":
    print("--- Advanced Filtering Demo ---")
    fs = 250 # Sampling rate
    time, raw_signal = generate_noisy_ecg(sampling_rate=fs)
    
    # Apply bandpass filter (0.5 Hz to 40 Hz is typical for ECG)
    filtered_signal = butter_bandpass_filter(raw_signal, lowcut=0.5, highcut=40.0, fs=fs, order=4)
    
    print("Filtering complete. Generating plot...")
    
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, raw_signal, color='red')
    plt.title("Raw ECG with Noise and Baseline Wander")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(time, filtered_signal, color='green')
    plt.title("Filtered ECG (Butterworth Bandpass 0.5-40 Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    print("Advanced filtering completed successfully.")

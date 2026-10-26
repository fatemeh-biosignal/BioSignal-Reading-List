# load_real_data.py
# This script demonstrates how to load and process a real ECG dataset.
# In the future, this will be connected to the MIT-BIH Arrhythmia Database.

import numpy as np
import matplotlib.pyplot as plt

def simulate_loading_mitbih():
    """
    Simulates loading a record from the MIT-BIH Arrhythmia Database.
    Real MIT-BIH data has a sampling rate of 360 Hz and is often 30 minutes long.
    Here, we simulate a 10-second window.
    """
    fs = 360  # Sampling frequency (Hz)
    duration = 10  # seconds
    num_samples = fs * duration
    
    # Simulate time vector
    t = np.linspace(0, duration, num_samples)
    
    # Simulate a more realistic ECG shape using a combination of functions
    # (This is just a placeholder until the real dataset is loaded)
    baseline = 0.1 * np.sin(2 * np.pi * 0.2 * t) # Baseline wander
    heart_rate = 1.2 # Hz (approx 72 bpm)
    ecg_wave = np.sin(2 * np.pi * heart_rate * t)
    
    # Add some sharp peaks (simulating QRS complexes)
    qrs_peaks = np.zeros(num_samples)
    for i in range(int(duration * heart_rate)):
        peak_idx = int((i / heart_rate) * fs)
        if peak_idx < num_samples:
            qrs_peaks[peak_idx] = 1.5 # Sharp spike
            
    signal = ecg_wave + baseline + qrs_peaks
    return t, signal, fs

if __name__ == "__main__":
    print("--- Loading Real ECG Data (Simulation) ---")
    time, signal, fs = simulate_loading_mitbih()
    
    print(f"Sampling Rate: {fs} Hz")
    print(f"Total Samples: {len(signal)}")
    print(f"Signal Duration: {len(signal) / fs} seconds")
    
    # Plot a small window (first 5 seconds)
    plt.figure(figsize=(10, 4))
    plt.plot(time[:5*fs], signal[:5*fs], color='purple')
    plt.title("Simulated MIT-BIH ECG Record (First 5 seconds)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True)
    plt.show()
    
    print("Data loaded successfully. Ready for preprocessing.")

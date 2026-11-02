# r_peak_detection.py
# A simple algorithm to detect R-peaks (heartbeats) in an ECG signal.
# This is a crucial step for calculating Heart Rate (BPM).

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def generate_mock_ecg(duration=10, sampling_rate=250):
    """Generates a synthetic ECG signal with sharp R-peaks."""
    t = np.linspace(0, duration, duration * sampling_rate)
    # Base wave
    signal = 0.1 * np.sin(2 * np.pi * 1.2 * t)
    
    # Add sharp R-peaks at regular intervals (e.g., every 0.8 seconds for 75 BPM)
    for i in range(int(duration / 0.8)):
        peak_time = i * 0.8
        peak_idx = int(peak_time * sampling_rate)
        if peak_idx < len(signal):
            # Create a sharp spike
            signal[peak_idx:peak_idx+5] += 1.0 
            
    # Add noise
    signal += 0.05 * np.random.randn(len(t))
    return t, signal

if __name__ == "__main__":
    print("--- R-Peak Detection ---")
    time, ecg = generate_mock_ecg()
    
    # Use scipy's find_peaks to detect the R-peaks
    # height=0.5 ensures we only detect the tall spikes (R-peaks)
    # distance=100 ensures we don't detect peaks too close to each other
    peaks, _ = find_peaks(ecg, height=0.5, distance=100)
    
    # Calculate Heart Rate (BPM)
    if len(peaks) > 1:
        # Time difference between peaks
        rr_intervals = np.diff(time[peaks])
        avg_rr = np.mean(rr_intervals)
        heart_rate = 60 / avg_rr
        print(f"Detected {len(peaks)} beats.")
        print(f"Estimated Heart Rate: {heart_rate:.2f} BPM")
    else:
        print("Not enough peaks detected.")
    
    # Plotting
    plt.figure(figsize=(10, 4))
    plt.plot(time, ecg, label="ECG Signal", color='blue', alpha=0.6)
    plt.plot(time[peaks], ecg[peaks], "x", label="Detected R-Peaks", color='red', markersize=10)
    plt.title("ECG Signal with Detected R-Peaks")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("R-Peak detection completed.")

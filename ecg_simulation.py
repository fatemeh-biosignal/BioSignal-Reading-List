# ecg_simulation.py
# My first Python script to generate a mock ECG signal.
# This is a placeholder code for my future Compressive Sensing project.

import numpy as np
import matplotlib.pyplot as plt

def generate_mock_ecg(duration=5, sampling_rate=250):
    # Create a time array
    t = np.linspace(0, duration, duration * sampling_rate)
    
    # Create a simple synthetic signal (sine wave + noise)
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.05 * np.random.randn(len(t))
    
    return t, signal

if __name__ == "__main__":
    print("Generating mock ECG signal...")
    time, ecg = generate_mock_ecg()
    print(f"Generated {len(ecg)} samples.")
    
    # Note: I will run this code later to plot the graph.

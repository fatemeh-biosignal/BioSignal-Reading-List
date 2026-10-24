# Project Progress Report

**Date:** November 2026
**Project:** Low-Power Wearable ECG Monitoring using Compressive Sensing

## 🎯 Objective
To simulate an ECG signal, apply noise (simulating real-world conditions), compress the signal using Compressive Sensing (CS), and reconstruct it.

## 🧪 Methodology & Simulations (What I have done so far)

1. **Signal Generation (`ecg_simulation.py`):**
   - Generated a synthetic ECG signal with a sampling rate of 250 Hz.
   - Added Gaussian noise to simulate real-world artifacts.

2. **Noise Filtering (`real_ecg_analysis.py`):**
   - Simulated baseline wander (low-frequency noise from breathing).
   - Applied a Moving Average filter to remove high-frequency noise.

3. **Compressive Sensing (`compressed_sensing_demo.py`):**
   - Sub-sampled the signal, keeping only **30%** of the original data points.
   - Demonstrated how data volume can be reduced while maintaining the core structure.

4. **Signal Reconstruction (`reconstruction_demo.py`):**
   - Applied a basic linear interpolation to recover the missing 70% of the data.
   - Calculated the Mean Squared Error (MSE) as a baseline metric.

## 🚀 Next Steps
- Implement the **OMP (Orthogonal Matching Pursuit)** algorithm for a more accurate reconstruction.
- Integrate TinyML for on-device arrhythmia detection.
- Write the manuscript for the ICEE 2027 conference.

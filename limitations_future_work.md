# Limitations and Future Work

This document outlines the current limitations of the project and the planned steps to overcome them.

## 1. Current Limitations
- **Synthetic Data:** The current algorithms are tested on synthetic ECG signals, not real patient data.
- **Simplified Model:** The TinyML classifier uses a simplified Random Forest model. A more complex neural network (like a 1D-CNN) might yield higher accuracy.
- **Hardware Prototype:** The system has not yet been tested on a physical microcontroller (STM32) with real sensors.

## 2. Future Work
- **Real-World Testing:** Integrate the MIT-BIH Arrhythmia Database to validate the algorithms on real clinical data.
- **Deep Learning:** Explore 1D-CNNs (Convolutional Neural Networks) for better feature extraction from the ECG signal.
- **Hardware Implementation:** Port the C-code to an STM32 microcontroller and design the PCB for a wearable patch.
- **Clinical Trials:** Collaborate with cardiologists to test the device on actual patients.

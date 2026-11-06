# Literature Review

This document summarizes the existing research and identifies the gap that our project addresses.

## 1. Compressive Sensing in ECG
- **Paper:** *Compressive Sensing in ECG Signal Processing: A Review*.
- **Key Finding:** CS can reduce the sampling rate of ECG by 70% without losing diagnostic information, which is crucial for wearable devices.
- **Our Project's Approach:** We implemented a 30% compression ratio and used the OMP algorithm for reconstruction.

## 2. Hardware Implementation of CS
- **Paper:** *ADC-Assisted Random Sampler Architecture for Efficient Sparse Signal Acquisition* (by Safarpour, Charmi, et al.).
- **Key Finding:** The paper proposes a custom SAR ADC architecture for efficient sampling, reducing power consumption to less than 25 µW.
- **Our Project's Approach:** While they focused on the hardware implementation, our project focuses on the software and TinyML aspect. Future work will integrate our algorithms with their hardware design.

## 3. Machine Learning for Arrhythmia Detection
- **Paper:** *TinyML for Healthcare: A Survey*.
- **Key Finding:** Lightweight models (like Random Forest or 1D-CNN) can run on microcontrollers, enabling real-time detection without cloud dependency.
- **Our Project's Approach:** We successfully implemented a Random Forest classifier on synthetic data and are preparing to test it on the MIT-BIH dataset.

## 4. The Research Gap
Most existing works either focus only on the hardware (ADC design) or only on the software (AI algorithms). **Our project bridges this gap by providing a complete end-to-end simulation**, from CS to TinyML, tailored for a low-power wearable device.

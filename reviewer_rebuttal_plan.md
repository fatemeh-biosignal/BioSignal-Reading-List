# Anticipated Reviewer Questions & Rebuttal Plan

This document prepares the responses to potential questions from reviewers during the peer-review process for ICEE 2027.

## Q1: "Why did you use a Random Forest classifier instead of a Deep Neural Network (DNN)?"
- **Response:** While DNNs (like 1D-CNNs) can achieve high accuracy, they require significant memory and computational power. Our target platform is an STM32 microcontroller with only 1MB of Flash and 192KB of RAM. A Random Forest model, after quantization, fits perfectly within these constraints and provides real-time inference (< 50ms), making it the optimal choice for TinyML.

## Q2: "Your data is synthetic. How can you prove this works on real patients?"
- **Response:** We acknowledge this limitation in our "Threats to Validity" section. The current synthetic data allowed us to establish the mathematical model and the pipeline. In the next phase (post-ICEE), we will validate the system using the real-world MIT-BIH Arrhythmia Database and conduct a pilot clinical trial at a hospital in Zanjan.

## Q3: "Compressive Sensing is known to be computationally expensive for reconstruction. How does this save power?"
- **Response:** We do not reconstruct the signal on the device. The device only performs compression (which is computationally cheap) and runs the TinyML model on the compressed data. The expensive OMP reconstruction is only performed on a powerful PC or server (e.g., at the hospital) if the doctor requests the full ECG.

## Q4: "How do you handle motion artifacts in a wearable device?"
- **Response:** Motion artifacts are a major challenge. We use a 4th-order Butterworth bandpass filter (0.5 - 40 Hz) to remove high-frequency muscle noise. Additionally, the TinyML model is trained to be robust against this noise. If the signal is too corrupted, the device detects it and alerts the patient to adjust the patch.

## Q5: "What is the novelty of your work compared to existing literature?"
- **Response:** Most existing works focus either on hardware (ADC design) or software (AI). Our novelty lies in providing a complete, end-to-end, open-source simulation pipeline that integrates CS, OMP reconstruction, and TinyML specifically tailored for a low-power, cost-effective wearable patch (~$33).

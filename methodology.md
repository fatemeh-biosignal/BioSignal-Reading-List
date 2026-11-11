# Methodology

This document outlines the step-by-step pipeline used in the BioSignal project, from raw data acquisition to final classification.

## Step 1: Data Acquisition
- The ECG signal is collected using the **AD8232** Analog Front-End (AFE) sensor.
- The signal is sampled at **250 Hz** with a 12-bit resolution using the ADC.

## Step 2: Signal Preprocessing (Noise Reduction)
- Raw ECG signals contain baseline wander (low frequency) and muscle noise (high frequency).
- We apply a **Butterworth Bandpass Filter** (0.5 Hz to 40 Hz) using `scipy.signal.butter` to isolate the clean ECG signal.

## Step 3: Compressive Sensing (Data Compression)
- To save battery and transmission bandwidth, the signal is compressed using a **Random Gaussian Sensing Matrix**.
- The compression ratio is set to **30%**, meaning only 30% of the original samples are retained.

## Step 4: Signal Reconstruction (For Validation)
- To prove the compressed data is sufficient, we use the **Orthogonal Matching Pursuit (OMP)** algorithm (`omp_reconstruction.py`).
- OMP solves the L1-minimization problem to reconstruct the full signal from the 30% compressed measurements.

## Step 5: Machine Learning (TinyML)
- The raw (or reconstructed) signal is fed into a **Random Forest Classifier** (`tinyml_classifier.py`).
- The model is trained to classify the heartbeat as **Normal** or **Arrhythmia**.
- The model's feature importances are analyzed to ensure it focuses on the QRS complex.

## Step 6: Alert System
- If the Heart Rate (BPM) is below 60 (Bradycardia) or above 100 (Tachycardia), an alert is triggered (`heart_rate_alert.py`).
- The alert is sent via BLE to the patient's mobile app.

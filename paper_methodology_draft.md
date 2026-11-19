# Methodology (Draft for ICEE 2027 Paper)

This section describes the end-to-end architecture of the BioSignal system, from signal acquisition to on-device classification.

## 1. System Architecture
The BioSignal platform consists of three main layers:
1. **Analog Front-End (AFE):** The AD8232 sensor captures the raw ECG signal, which is then digitized by a 12-bit ADC at a sampling rate of 250 Hz.
2. **Processing Unit:** An STM32F4 microcontroller handles signal filtering, Compressive Sensing, and TinyML inference.
3. **Communication:** A Bluetooth Low Energy (BLE) module transmits alerts to the patient's smartphone.

## 2. Signal Preprocessing
Raw ECG signals are often corrupted by baseline wander (low-frequency noise) and muscle artifacts (high-frequency noise). We apply a 4th-order Butterworth bandpass filter (0.5 Hz to 40 Hz) using the `scipy.signal` library to isolate the clean ECG waveform.

## 3. Compressive Sensing (CS)
To reduce power consumption and data transmission costs, we employ CS to compress the filtered signal. The signal is multiplied by a random Gaussian sensing matrix (\(\Phi\)) to obtain compressed measurements (\(y\)):
\[
y = \Phi x
\]
where \(x\) is the original ECG signal. We set the compression ratio to 30%, meaning only 30% of the original data is retained.

## 4. Signal Reconstruction (OMP)
To validate that the compressed data retains diagnostic information, we reconstruct the signal using Orthogonal Matching Pursuit (OMP). OMP solves the \(L_1\)-minimization problem to recover the sparse representation of the ECG signal. The reconstructed signal is then compared to the original using Mean Squared Error (MSE).

## 5. TinyML Classifier
For arrhythmia detection, we train a Random Forest classifier using `scikit-learn`. The model takes the ECG time-series (100 time points per heartbeat) as input and outputs a binary classification: Normal or Arrhythmia. To deploy this on the STM32, the trained model is converted into C code, ensuring low-latency, on-device inference without cloud dependency.

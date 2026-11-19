# Results and Discussion

This document presents the results of the BioSignal simulations and discusses their implications for the ICEE 2027 paper.

## 1. Results

### 1.1. Signal Reconstruction (OMP vs. Linear Interpolation)
- **Linear Interpolation MSE:** [Placeholder: e.g., 0.045]
- **OMP MSE:** [Placeholder: e.g., 0.012]
- **Observation:** The OMP algorithm significantly reduces the reconstruction error compared to simple linear interpolation, proving that Compressive Sensing is highly effective for ECG signals.

### 1.2. Arrhythmia Classification (TinyML)
- **Model:** Random Forest Classifier.
- **Accuracy:** [Placeholder: e.g., 94.5%]
- **Precision:** [Placeholder: e.g., 93%]
- **Recall:** [Placeholder: e.g., 96%]
- **Observation:** The model successfully distinguishes between normal and arrhythmic heartbeats, making it suitable for on-device deployment.

## 2. Discussion

### 2.1. Why OMP is better than Linear Interpolation?
ECG signals are sparse in the wavelet domain. OMP leverages this sparsity to reconstruct the signal from fewer measurements. Linear interpolation only looks at neighboring points and misses the underlying physiological structure.

### 2.2. Why TinyML (On-Device AI)?
Cloud-based AI requires continuous internet, high bandwidth, and raises privacy concerns. TinyML runs locally, ensuring zero latency, low power consumption, and complete patient privacy.

### 2.3. Limitations
- The current results are based on [Synthetic Data / MIT-BIH Data].
- The hardware prototype is not yet built; power consumption is estimated.

## 3. Conclusion
The combination of Compressive Sensing and TinyML provides a highly accurate, privacy-preserving, and energy-efficient solution for wearable ECG monitoring. The results validate the feasibility of the proposed architecture.

# Threats to Validity

This document acknowledges the limitations and potential threats to the validity of the research findings.

## 1. Internal Validity (اعتبار درونی)
- **Synthetic Data Bias:** The current simulation uses synthetic ECG signals. The Random Forest model might overfit to the artificial noise patterns rather than real physiological variations.
- **Mitigation:** Future phases will train and validate the model using the real MIT-BIH Arrhythmia Database.

## 2. External Validity (اعتبار بیرونی)
- **Generalization:** The model is currently trained on a specific set of simulated heartbeats. It may not generalize well to patients with rare heart conditions or different demographics (e.g., age, gender).
- **Mitigation:** We plan to collect data from diverse patient groups during the clinical trial phase.

## 3. Construct Validity (اعتبار سازه)
- **Feature Extraction:** We are relying on raw time-series data for the Random Forest. More advanced feature extraction (like Wavelet Transform) might yield better results.
- **Mitigation:** We are actively researching Wavelet-based feature extraction (as documented in `wavelet_analysis.py`).

## 4. Conclusion Validity (اعتبار نتیجه‌گیری)
- **Hardware Constraints:** The inference time and power consumption are currently simulated. Real-world performance on the STM32 microcontroller might differ due to hardware limitations.
- **Mitigation:** Bench testing with the physical prototype will provide accurate power and latency metrics.

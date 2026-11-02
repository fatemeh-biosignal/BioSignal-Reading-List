# Paper Draft (For ICEE 2027)

**Title:** Low-Power Wearable ECG Monitoring using Compressive Sensing and TinyML for Real-Time Arrhythmia Detection

## 1. Introduction
- **Background:** Cardiovascular diseases are the leading cause of death globally. Early detection of arrhythmias is crucial.
- **Problem:** Continuous ECG monitoring is limited by battery life and data transmission bandwidth.
- **Proposed Solution:** A wearable system using Compressive Sensing (CS) for data reduction and TinyML for on-device classification.

## 2. Methodology
### 2.1. Signal Acquisition
- Used the AD8232 sensor and STM32 microcontroller.
### 2.2. Compressive Sensing
- Compressed the ECG signal to 30% of its original size using a random Gaussian matrix.
### 2.3. TinyML Classifier
- Trained a Random Forest model to classify Normal vs. Arrhythmia.
### 2.4. OMP Reconstruction
- Used the Orthogonal Matching Pursuit algorithm for signal recovery when needed.

## 3. Results
- **Accuracy:** (To be filled after running the final tests)
- **Power Consumption:** (To be evaluated on hardware)
- **MSE Comparison:** OMP outperformed Linear Interpolation in reconstruction accuracy.

## 4. Conclusion
- The proposed system provides a practical, low-power, and privacy-preserving solution for continuous cardiac monitoring.
- Future work includes testing on the MIT-BIH database and clinical trials.

## References
1. (To be added)

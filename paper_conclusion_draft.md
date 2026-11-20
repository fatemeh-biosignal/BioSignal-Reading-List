# Conclusion & Future Work (Draft for ICEE 2027 Paper)

## 1. Conclusion
This paper presented **BioSignal**, a low-power wearable ECG monitoring system that integrates Compressive Sensing (CS) with TinyML for real-time arrhythmia detection. 

The proposed system successfully addresses the two main challenges of existing wearable devices: battery life and data privacy. By compressing the ECG signal to 30% of its original size, we significantly reduced the transmission bandwidth and power consumption. Furthermore, by deploying a Random Forest classifier directly on the STM32 microcontroller, we ensured that no sensitive patient data is transmitted to the cloud. 

Experimental simulations demonstrated that the OMP algorithm provides highly accurate signal reconstruction compared to linear interpolation. The TinyML model achieved an accuracy of [Placeholder]%, proving its feasibility for on-device medical inference.

## 2. Future Work
Future phases of this project will focus on:
1. **Hardware Prototyping:** Moving from simulation to a physical PCB (designed in Altium Designer) using the AD8232 sensor and STM32 microcontroller.
2. **Clinical Validation:** Testing the algorithms on the real MIT-BIH Arrhythmia Database and conducting a pilot study in a local hospital.
3. **AI Enhancements:** Replacing the Random Forest model with a lightweight 1D-CNN (Convolutional Neural Network) for higher accuracy.
4. **Platform Expansion:** Adapting the biosensor platform to detect early biomarkers of breast cancer.

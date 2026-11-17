# Future Work

This document outlines the planned research and development directions for the BioSignal project after the initial ICEE paper and Khwarizmi Award submission.

## 1. Hardware Development
- **Physical Prototype:** Moving from simulation to a physical PCB (designed in Altium Designer) using STM32 and AD8232.
- **Miniaturization:** Designing a flexible, patch-like PCB that conforms to the patient's skin for maximum comfort.
- **Solar Charging:** Integrating flexible solar cells to eliminate the need for battery charging.

## 2. AI & Algorithm Enhancements
- **Deep Learning:** Replacing the Random Forest classifier with a lightweight 1D-CNN (Convolutional Neural Network) for better feature extraction from the ECG signal.
- **Federated Learning:** Implementing federated learning to update the AI model across devices without compromising patient privacy.
- **Multi-Class Detection:** Expanding the model to detect specific arrhythmias (e.g., AFib, PVC, PAC) rather than just a binary classification.

## 3. Clinical Validation
- **MIT-BIH Database:** Testing the algorithms on real-world clinical data to prove their accuracy.
- **Clinical Trials:** Conducting a pilot study with a local hospital (e.g., in Zanjan) to validate the device's real-world performance.

## 4. Expansion to Other Diseases
- **Early Cancer Detection:** Using the same biosensor platform to detect early biomarkers for breast cancer (a personal mission of the founder).
- **Sleep Apnea Monitoring:** Modifying the algorithm to detect sleep apnea from ECG variations.

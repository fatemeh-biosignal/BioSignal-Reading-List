# Patent Strategy

This document outlines the strategy for protecting the novel aspects of the BioSignal project through patents.

## 1. Patentable Innovations
Not everything can be patented. We have identified the following novel aspects of our project that have patent potential:
- **The Integrated CS-TinyML Pipeline:** A specific method for reducing data size (CS) and immediately classifying it (TinyML) on a low-power MCU for ECG monitoring.
- **Dynamic Power Management:** A method where the device switches between "high-resolution mode" and "compressed sensing mode" based on the patient's activity level or heart rate variability.
- **The Form Factor:** The specific mechanical design of the reusable core and the disposable patch.

## 2. Patent Type
- **Utility Patent:** We will apply for a utility patent for the algorithm and the electronic circuit.
- **Provisional Patent Application (PPA):** Before public disclosure (e.g., at the Khwarizmi Award), we will file a PPA to secure an early filing date.

## 3. Patent Timeline
1. **Now (Pre-Exam):** Document all innovations (this file).
2. **Post-Exam (Hardware Phase):** Build the prototype and test the algorithm.
3. **Before Khwarizmi Submission:** Consult with a patent attorney and file the PPA.
4. **After Clinical Trials:** Convert the PPA to a full non-provisional patent.

## 4. Open-Source vs. Patent
- **Code:** The Python simulation and GUI will remain open-source (MIT License).
- **Hardware & Algorithm:** The physical device and the optimized C-code for TinyML will be proprietary and covered by the patent.

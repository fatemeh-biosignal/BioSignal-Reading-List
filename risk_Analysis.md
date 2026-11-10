# Risk Analysis & FMEA (Failure Mode and Effects Analysis)

This document identifies potential failure modes in the wearable ECG device and outlines mitigation strategies to ensure patient safety.

## 1. Risk Assessment Table

| Failure Mode | Potential Cause | Potential Effect | Severity (1-10) | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Sensor Detachment** | Loose adhesive / Sweat | Loss of ECG signal (False Alarm) | 6 | Leads-off detection (LO+ / LO-) using AD8232. Send immediate alert to app. |
| **Battery Depletion** | High power consumption | Loss of continuous monitoring | 7 | Implement Compressive Sensing (CS) and BLE sleep modes to extend battery life to 3 days. |
| **False Negative (Missing Arrhythmia)** | AI model limitation | Missed critical event | 9 | Human-in-the-loop: Raw data is stored and reviewed by a doctor. Use high-sensitivity model. |
| **False Positive (False Alert)** | Motion artifacts / Noise | Unnecessary panic for the patient | 4 | Implement Butterworth bandpass filter (0.5-40 Hz) to remove noise before AI inference. |
| **BLE Data Interception** | Unsecured wireless connection | Privacy breach | 8 | AES-128 encryption for all BLE communications. |

## 2. Risk Priority Number (RPN)
- **Formula:** RPN = Severity × Occurrence × Detection (To be fully calculated during hardware testing phase).
- **Current Focus:** The highest severity risk is the **False Negative (Severity 9)**. Therefore, the device is designed as a "screening tool," not a replacement for a doctor, ensuring human review of the data.

## 3. Safety Standards Compliance
- Design adheres to **IEC 60601-1** for electrical safety.
- Materials adhere to **ISO 10993** for biocompatibility.

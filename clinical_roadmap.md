# Clinical Validation Roadmap

This document outlines the steps required to validate the wearable ECG device for real-world clinical use.

## Phase 1: Bench Testing (تست روی میز آزمایشگاه)
- **Goal:** Verify that the hardware and software work together.
- **Method:** Use a signal generator to simulate ECG signals and feed them into the device.
- **Output:** Ensure the device correctly filters, compresses, and classifies the signal.

## Phase 2: Pre-clinical Testing (تست پیش‌بالینی)
- **Goal:** Test the device on healthy volunteers (non-patients).
- **Method:** Attach the device to 5-10 healthy individuals and compare the recorded ECG with a standard hospital ECG machine.
- **Output:** Validate the accuracy of the signal acquisition and the battery life.

## Phase 3: Clinical Trials (کارآزمایی بالینی)
- **Goal:** Test the device on actual patients with known arrhythmias.
- **Method:** Collaborate with cardiologists at a hospital (e.g., in Zanjan). Record the patient's ECG using both the device and the gold-standard Holter monitor.
- **Output:** Prove that the TinyML algorithm can detect arrhythmias with high sensitivity and specificity.

## Phase 4: Regulatory Approval (تاییدیه‌های قانونی)
- **Goal:** Obtain medical device certification.
- **Method:** Submit the clinical trial results to regulatory bodies (e.g., FDA in the US, CE in Europe, or IRC in Iran).
- **Output:** Official approval to market and sell the device.

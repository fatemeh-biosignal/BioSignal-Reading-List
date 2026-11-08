# Data Management Plan (DMP)

This document outlines how patient data is handled, stored, and protected throughout the research lifecycle.

## 1. Data Collection
- **Source:** ECG signals collected via the AD8232 sensor.
- **Format:** Digital time-series data (CSV/JSON).
- **Volume:** Approximately 250 samples per second per patient.

## 2. Data Storage & Security
- **Local Storage:** Data is temporarily stored on the STM32 microcontroller's internal flash memory.
- **Encryption:** All stored data is encrypted using AES-128.
- **Cloud Policy:** Raw data is **never** sent to the cloud. Only anonymized alerts (e.g., "Arrhythmia detected at 14:30") are shared with the doctor.

## 3. Data Sharing & Access
- **Patient Access:** Patients can view their own heart rate history through the mobile app.
- **Doctor Access:** Doctors can access the data only after the patient grants explicit digital consent via the app.
- **Research Use:** Anonymized datasets may be used for training future AI models, in compliance with GDPR and HIPAA.

## 4. Data Retention & Destruction
- Data is retained on the device for a maximum of 30 days (to save battery and storage).
- After 30 days, the oldest data is automatically overwritten.
- If a patient deletes their account, all their data is permanently erased from the device and the doctor's dashboard.

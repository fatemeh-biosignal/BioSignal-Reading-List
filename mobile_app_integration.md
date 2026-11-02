# Mobile App Integration (BLE)

This document describes how the wearable ECG device communicates with a smartphone application via Bluetooth Low Energy (BLE).

## 1. Communication Protocol
- **BLE Service:** Custom ECG Service
- **Data Characteristics:**
  - `ECG_Data`: Sends compressed ECG data (or raw data if requested).
  - `Alert_Status`: Sends an alert (e.g., "Arrhythmia Detected", "High Heart Rate").
  - `Battery_Level`: Sends the current battery percentage.

## 2. Mobile App Features
- **Real-time Dashboard:** Shows the patient's heart rate (BPM) in real-time.
- **Alert Notifications:** Pushes a notification to the user's phone if an arrhythmia is detected.
- **Data History:** Stores the patient's ECG records for the doctor's review.
- **Emergency Call:** Automatically calls a family member or emergency services if a critical event occurs.

## 3. Privacy & Security
- **Data Encryption:** All BLE communication is encrypted using AES-128.
- **Local Processing:** Only alerts and summaries are sent to the cloud; raw data stays on the device unless the patient explicitly consents.

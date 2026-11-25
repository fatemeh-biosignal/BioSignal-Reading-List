# Cybersecurity Threat Model (STRIDE)

This document outlines the potential cybersecurity threats to the BioSignal device and the mitigation strategies, based on the FDA cybersecurity guidelines for medical devices.

## 1. STRIDE Threat Analysis

### 1.1. Spoofing (جعل هویت)
- **Threat:** An attacker pretends to be the BioSignal device to send fake ECG data to the doctor's dashboard, or a fake doctor dashboard requests patient data.
- **Mitigation:** Mutual Authentication. The device and the server must verify each other's digital certificates before exchanging any data.

### 1.2. Tampering (دستکاری داده‌ها)
- **Threat:** A hacker intercepts the BLE communication and modifies the ECG data (e.g., changing a normal heartbeat to look like an arrhythmia).
- **Mitigation:** Message Integrity Codes (MAC). Every BLE packet is signed with AES-128 encryption. Any tampered packet is immediately rejected.

### 1.3. Repudiation (انکار)
- **Threat:** A doctor denies receiving a critical alert, leading to legal issues.
- **Mitigation:** Secure Audit Logs. The server logs every action (who viewed the data and when) with a cryptographic timestamp that cannot be altered.

### 1.4. Information Disclosure (افشای اطلاعات)
- **Threat:** A hacker steals the patient's personal health information (PHI) from the cloud.
- **Mitigation:** Data Anonymization and Encryption. Patient IDs are stored separately from ECG data, and all data at rest on the cloud is encrypted using AES-256.

### 1.5. Denial of Service (DoS) (حمله انسداد سرویس)
- **Threat:** An attacker floods the BLE connection with junk data, draining the device's battery or preventing the real alert from reaching the phone.
- **Mitigation:** BLE Rate Limiting. The firmware limits the number of connection requests per minute. If a DoS attack is detected, the device enters a safe mode and sounds a local alarm.

### 1.6. Elevation of Privilege (ارتقای سطح دسترسی)
- **Threat:** A normal user (patient) finds a bug in the app to gain admin access to the doctor's dashboard.
- **Mitigation:** Role-Based Access Control (RBAC). The server strictly checks user roles (Patient vs. Doctor) for every API request.

## 2. Secure Update Process
- **OTA (Over-The-Air) Updates:** Firmware updates are cryptographically signed by the BioSignal team. The STM32 Secure Boot will reject any unsigned firmware.

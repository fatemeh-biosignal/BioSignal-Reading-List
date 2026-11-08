# Security Policy

This document outlines the security architecture and policies for the BioSignal wearable ECG device.

## 1. Supported Versions
Currently, only the latest version (v1.0.0) is supported with security updates.

## 2. Security Architecture
Because this is a medical device handling sensitive patient data, we implement the following security measures:
- **On-Device Processing:** The TinyML classifier runs locally on the microcontroller. Raw ECG data is never sent to the cloud, minimizing data interception risks.
- **Data Encryption:** All Bluetooth Low Energy (BLE) communications between the device and the mobile app are encrypted using **AES-128**.
- **Authentication:** The mobile app requires a secure login (biometric or password) before pairing with the device.

## 3. Reporting a Vulnerability
If you discover a security vulnerability in this project, please do not disclose it publicly. Instead, please send an email to the project maintainer (Fatemeh Karimi) directly. We will acknowledge your report within 48 hours and work on a fix.

## 4. Future Security Enhancements
- Implementation of Secure Boot on the STM32 microcontroller.
- Regular security audits of the TinyML model against adversarial attacks.

# Software Requirements Specification (SRS)

This document defines the functional and non-functional requirements for the BioSignal wearable ECG device.

## 1. Functional Requirements (نیازمندی‌های عملکردی)
- **FR1:** The system must sample ECG signals at a rate of 250 Hz with 12-bit resolution.
- **FR2:** The system must apply a bandpass filter (0.5 Hz to 40 Hz) to remove baseline wander and high-frequency noise.
- **FR3:** The system must compress the signal to 30% of its original size using Compressive Sensing.
- **FR4:** The system must reconstruct the full signal using the OMP algorithm when requested by the doctor.
- **FR5:** The system must run a TinyML classifier to detect Arrhythmia in real-time.
- **FR6:** The system must send an alert to the mobile app if Bradycardia (< 60 BPM) or Tachycardia (> 100 BPM) is detected.

## 2. Non-Functional Requirements (نیازمندی‌های غیرعملکردی)
- **NFR1 (Battery Life):** The device must operate for at least 3 days on a single charge under normal usage.
- **NFR2 (Latency):** The TinyML classifier must detect an arrhythmia within 1 second of its occurrence.
- **NFR3 (Privacy):** All BLE communication must be encrypted using AES-128.
- **NFR4 (Safety):** The device must comply with IEC 60601-1 electrical safety standards.

## 3. Hardware Constraints (محدودیت‌های سخت‌افزاری)
- **MCU:** STM32F4 series (or RP2350).
- **AFE:** AD8232 ECG sensor.
- **Power:** 3.7V Li-Po battery.

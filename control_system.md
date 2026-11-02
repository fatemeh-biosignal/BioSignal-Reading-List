# Control System & State Machine

This document outlines the logic and state machine for the low-power wearable ECG device.

## 1. State Machine (وضعیت‌های دستگاه)
To maximize battery life, the device operates in different states:
- **Sleep Mode:** The MCU is in deep sleep, drawing minimal current. The AFE is off.
- **Wear Detection:** A capacitive sensor detects if the device is on the patient's skin.
- **Acquisition Mode:** The AFE and ADC are active, sampling ECG at 250 Hz.
- **Processing Mode:** The MCU runs the Compressive Sensing algorithm and the TinyML classifier.
- **Alert Mode:** If an arrhythmia is detected, the BLE module wakes up and sends an alert to the smartphone.

## 2. Power Management Strategy
- **Dynamic Voltage Scaling:** Reducing the MCU clock speed when not processing data.
- **Duty Cycling:** The device only samples ECG for 10 seconds every minute (unless an anomaly is detected).
- **BLE Optimization:** The BLE module remains off most of the time and only activates during an alert or scheduled sync.

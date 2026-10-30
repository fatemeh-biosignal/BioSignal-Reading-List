# Hardware Specifications (Bill of Materials)

This document outlines the hardware components required to build the physical prototype of the low-power wearable ECG device.

## 1. Core Processing Unit (MCU)
- **Component:** STM32F4 Series (e.g., STM32F407) or RP2350
- **Why:** High processing power for TinyML algorithms, with low-power sleep modes.
- **Role:** Runs the Compressive Sensing algorithm and the Random Forest classifier.

## 2. Analog Front-End (AFE)
- **Component:** AD8232 (ECG Sensor Module)
- **Why:** Specifically designed for ECG, low noise, and includes built-in filtering.
- **Role:** Captures the raw electrical signals from the heart.

## 3. Analog-to-Digital Converter (ADC)
- **Component:** SAR ADC (built into the MCU or external low-power ADC)
- **Specs:** 12-bit resolution, sampling rate of 250 Hz.
- **Role:** Converts the analog ECG signal into digital data for the MCU.

## 4. Power Management
- **Component:** Li-Po Battery (3.7V) + Low-Dropout Regulator (LDO)
- **Why:** To ensure stable power supply and maximize battery life.
- **Role:** Provides power to all components while maintaining low quiescent current.

## 5. Wireless Communication
- **Component:** BLE (Bluetooth Low Energy) Module (e.g., nRF52 or ESP32-C3)
- **Role:** Sends the final alert (Arrhythmia detected) to the patient's smartphone without sending raw data.

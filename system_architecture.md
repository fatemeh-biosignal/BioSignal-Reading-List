# System Architecture (High-Level)

This document provides a high-level overview of how the hardware, software, and AI components of the BioSignal system interact.

## 1. Hardware Layer
- **Sensor:** AD8232 Analog Front-End (AFE) for capturing ECG.
- **Microcontroller:** STM32F4 series for processing.
- **Communication:** BLE module (e.g., nRF52) for wireless data transfer.

## 2. Software Layer (On-Device)
- **Firmware (C):** Handles ADC sampling, Butterworth filtering, and BLE communication.
- **TinyML (C/Python):** Random Forest model compiled into C for on-device arrhythmia detection.

## 3. Software Layer (Off-Device)
- **Python Simulation:** Used for algorithm development, testing, and validation (Compressive Sensing, OMP).
- **GUI Dashboard (Tkinter):** For clinical visualization and demonstration.

## 4. Data Flow
1. The **AD8232** captures the analog ECG signal.
2. The **STM32** converts it to digital (via ADC) and applies noise filtering.
3. The **TinyML model** runs on the STM32 to classify the heartbeat (Normal vs. Arrhythmia).
4. If an anomaly is detected, the **BLE module** sends an alert to the patient's smartphone.
5. For research purposes, the **Compressive Sensing** and **OMP** algorithms are simulated in Python to prove data reduction efficiency.

## 5. Design Principles
- **Modularity:** Each layer (hardware, firmware, AI, UI) can be developed and tested independently.
- **Privacy:** Raw data never leaves the device; only alerts are transmitted.
- **Energy Efficiency:** Compressive Sensing and low-power hardware are used to maximize battery life.

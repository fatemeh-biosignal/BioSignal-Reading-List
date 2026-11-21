# Firmware Architecture (STM32)

This document describes the software architecture of the firmware running on the STM32 microcontroller.

## 1. Execution Model (Bare-Metal with Interrupts)
To ensure maximum power efficiency, the system uses a **Bare-Metal** architecture without an operating system. 
- **Timer Interrupt (250 Hz):** Triggers the ADC to sample the ECG signal.
- **Main Loop:** Processes the data, runs the AI inference, and manages BLE communication.

## 2. Data Flow Pipeline
1. **Acquisition:** The ADC reads the analog voltage from the AD8232 at 250 samples per second.
2. **Ring Buffer:** The samples are stored in a circular buffer to prevent data loss.
3. **Preprocessing:** A digital Butterworth filter (implemented in C) removes baseline wander and high-frequency noise.
4. **Compression (CS):** The filtered signal is multiplied by the sensing matrix to reduce the data size.
5. **AI Inference:** The TinyML model (optimized C code) analyzes the compressed data.
6. **Action:**
   - If Normal: Data is stored or discarded to save power.
   - If Arrhythmia: The BLE module wakes up and sends an alert to the phone.

## 3. Power Management States
- **Active Mode:** When the AFE is sampling and the MCU is processing.
- **Sleep Mode:** The MCU sleeps between timer interrupts (approx. 3.9 ms) to save power.
- **Deep Sleep:** If no movement is detected (via an accelerometer), the device enters deep sleep.

## 4. Memory Management
- **Flash (1MB):** Stores the firmware code, the TinyML model weights, and the CS sensing matrix.
- **RAM (192KB):** Used for the ring buffer, stack, and temporary AI variables.

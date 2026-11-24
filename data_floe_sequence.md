# Data Flow Sequence Diagram

This diagram illustrates the step-by-step interaction between the hardware and software components during an arrhythmia event.

```mermaid
sequenceDiagram
    participant Patient
    participant AD8232 as ECG Sensor (AD8232)
    participant STM32 as STM32 MCU
    participant BLE as BLE Module
    participant App as Mobile App
    participant Doctor

    Patient->>AD8232: Heart beats (Electrical signal)
    AD8232->>STM32: Analog Voltage
    STM32->>STM32: ADC Sampling (250 Hz)
    STM32->>STM32: Butterworth Filtering
    STM32->>STM32: Compressive Sensing (Compression)
    STM32->>STM32: TinyML Inference (Arrhythmia detected)
    STM32->>BLE: Trigger Alert
    BLE->>App: Send BLE Notification
    App->>Patient: Display Warning ("Sit down")
    App->>Doctor: Send Emergency Alert (Cloud)
    Doctor->>App: Review Compressed ECG Data
    Doctor->>Patient: Call patient for consultation

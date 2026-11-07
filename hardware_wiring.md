# Hardware Wiring Diagram (Block Level)

This document illustrates the connections between the different hardware modules of the wearable ECG device.

```mermaid
graph LR
    %% Power Supply
    Battery[Li-Po Battery 3.7V] -->|Power| LDO[LDO Regulator]
    LDO -->|3.3V| MCU[STM32 / RP2350]
    LDO -->|3.3V| AFE[AD8232 AFE]
    LDO -->|3.3V| BLE[BLE Module]

    %% Signal Flow
    Patient[Patient's Chest] -->|ECG Signal| AFE
    AFE -->|Analog Output| MCU
    MCU -->|Digital Data| BLE
    BLE -->|Wireless| Phone[Mobile App]

    %% Styling
    classDef power fill:#f9f,stroke:#333,stroke-width:2px;
    classDef signal fill:#bbf,stroke:#333,stroke-width:2px;
    class Battery,LDO,MCU,AFE,BLE power;
    class Patient,Phone signal;

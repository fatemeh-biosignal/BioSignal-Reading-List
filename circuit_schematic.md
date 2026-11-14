# Circuit Schematic (Block Level)

This document provides a block-level schematic of the electronic components and their connections.

```mermaid
graph TD
    %% Power Supply
    Battery[3.7V Li-Po Battery] -->|VIN| LDO[LDO Regulator 3.3V]
    LDO -->|3.3V| MCU_VDD[STM32 VDD]
    LDO -->|3.3V| AFE_VDD[AD8232 VDD]
    LDO -->|3.3V| BLE_VDD[BLE VDD]
    
    %% Decoupling Capacitors
    MCU_VDD -->|C1: 100nF| GND[Ground]
    AFE_VDD -->|C2: 100nF| GND
    
    %% ECG Signal Path
    Electrodes[Patient Electrodes] -->|IN+| AFE[AD8232 AFE]
    Electrodes -->|IN-| AFE
    AFE -->|OUT| MCU_ADC[STM32 ADC Pin]
    
    %% Leads-off Detection
    AFE -->|LO+| MCU_GPIO1[STM32 GPIO]
    AFE -->|LO-| MCU_GPIO2[STM32 GPIO]
    
    %% Communication
    MCU_UART[STM32 UART TX/RX] <-->|Data| BLE[BLE Module]

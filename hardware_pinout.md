# Hardware Pinout Configuration

This document defines the pin mapping between the STM32 microcontroller, the AD8232 ECG sensor, and the BLE module.

## 1. STM32 to AD8232 (Analog Front-End)
| STM32 Pin | AD8232 Pin | Function |
| :--- | :--- | :--- |
| PA0 (ADC1_IN0) | OUTPUT | Analog ECG Signal |
| PA1 (GPIO) | LO+ | Leads-off detection (+) |
| PA2 (GPIO) | LO- | Leads-off detection (-) |
| 3.3V | 3.3V | Power Supply |
| GND | GND | Ground |

## 2. STM32 to BLE Module (e.g., nRF52 or HC-08)
| STM32 Pin | BLE Pin | Function |
| :--- | :--- | :--- |
| PA9 (USART1_TX) | RX | UART Transmit (STM32 -> BLE) |
| PA10 (USART1_RX) | TX | UART Receive (BLE -> STM32) |
| 3.3V | VCC | Power Supply |
| GND | GND | Ground |

## 3. Power Management
| Component | Pin | Function |
| :--- | :--- | :--- |
| Li-Po Battery | VCC | 3.7V Input |
| LDO Regulator | VIN | 3.7V Input |
| LDO Regulator | VOUT | 3.3V Output to MCU/AFE/BLE |

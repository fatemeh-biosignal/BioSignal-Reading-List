# Bill of Materials (BOM) & Cost Estimate

This document provides an estimated cost for building the first hardware prototype (Version 1.0).

## 1. Component List
| Component | Description | Quantity | Est. Unit Price (USD) | Total (USD) |
| :--- | :--- | :--- | :--- | :--- |
| STM32F407 | Main Microcontroller | 1 | $8.00 | $8.00 |
| AD8232 | ECG Analog Front-End | 1 | $5.00 | $5.00 |
| BLE Module | e.g., nRF52832 | 1 | $4.00 | $4.00 |
| Li-Po Battery | 3.7V, 500mAh | 1 | $3.00 | $3.00 |
| PCB | Custom 2-layer board | 5 | $2.00 | $10.00 |
| Passives | Resistors, Capacitors | 1 set | $2.00 | $2.00 |
| Enclosure | 3D printed plastic | 1 | $1.00 | $1.00 |

## 2. Total Estimated Cost
- **Total per prototype:** ~$33.00 USD (Approx. 20,000,000 IRR based on current exchange rates).
- **Note:** This is a very low-cost estimate for the MVP (Minimum Viable Product). Mass production will significantly reduce the cost per unit.

## 3. Future Cost Reduction Strategies
- Using a custom ASIC instead of an off-the-shelf MCU.
- Integrating the AD8232 and BLE into a single System-on-Chip (SoC).

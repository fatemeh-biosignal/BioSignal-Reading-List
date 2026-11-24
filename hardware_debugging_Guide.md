# Hardware Debugging Guide

This document provides a systematic approach to troubleshooting the BioSignal hardware prototype during the testing phase.

## 1. Essential Tools
- **Digital Multimeter:** For checking voltage levels, continuity, and short circuits.
- **Oscilloscope:** For visualizing the analog ECG signal and checking digital communication (SPI, I2C, UART).
- **Logic Analyzer (Optional):** For debugging complex BLE or SPI communication protocols.

## 2. Common Issues & Solutions

### Issue 1: The device does not power on.
- **Check:** Measure the battery voltage (should be ~3.7V).
- **Check:** Measure the LDO output (should be exactly 3.3V). If it's 0V, check for a short circuit or a blown LDO.
- **Check:** Verify the polarity of the decoupling capacitors.

### Issue 2: STM32 cannot be programmed.
- **Check:** Ensure the ST-Link is properly connected to SWDIO, SWCLK, GND, and 3.3V.
- **Check:** Press the "Reset" button on the board right before flashing.
- **Check:** Verify the BOOT0 pin is pulled to GND.

### Issue 3: The ECG signal is noisy or flat.
- **Check:** Ensure the AD8232 is receiving 3.3V power.
- **Check:** Verify the electrode connections (LO+ and LO- pins should detect if electrodes are off).
- **Check:** Probe the analog output pin with an oscilloscope. If it's flat, check the filter capacitors.

### Issue 4: BLE module is not discoverable.
- **Check:** Ensure the BLE module is receiving power.
- **Check:** Verify the UART TX/RX lines are not swapped.
- **Check:** Ensure the firmware is actively sending advertising packets.

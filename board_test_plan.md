# Board Test Plan (Hardware Validation)

This document outlines the step-by-step procedure to test the physical PCB prototype before connecting it to a patient.

## 1. Visual Inspection
- **Tool:** Magnifying glass or microscope.
- **Action:** Check for cold solder joints, short circuits between adjacent pins, and correct component orientation (especially the STM32 and AD8232).

## 2. Power Supply Test (Before inserting the MCU)
- **Tool:** Multimeter.
- **Action:** 
  - Connect the 3.7V Li-Po battery.
  - Measure the output of the LDO regulator. It must be exactly **3.3V** (± 0.1V).
  - Ensure there is no short circuit between 3.3V and GND.

## 3. Microcontroller Test
- **Tool:** ST-Link programmer and STM32CubeIDE.
- **Action:** 
  - Try to connect to the STM32 via the debug port.
  - Flash a simple "Blink LED" code to ensure the MCU is alive and the clock is working.

## 4. Analog Front-End (AFE) Test
- **Tool:** Signal generator and Oscilloscope.
- **Action:** 
  - Inject a known 1 mV, 1 Hz sine wave into the AD8232 input (simulating an ECG).
  - Probe the AFE output pin. The signal should be amplified (approx. 1000x) and centered at 1.65V (VCC/2).

## 5. ADC Test
- **Tool:** STM32CubeIDE (Debug mode).
- **Action:** 
  - Read the ADC values from the STM32 registers.
  - Verify that the digital values change smoothly as the input signal changes.

## 6. BLE Communication Test
- **Tool:** Smartphone with a BLE scanner app (e.g., nRF Connect).
- **Action:** 
  - Power on the BLE module.
  - Scan for the device name "BioSignal" on the phone.
  - Connect and verify that basic data packets are being received.

# Hardware Assembly Guide

This document outlines the step-by-step procedure for assembling the BioSignal prototype PCB.

## 1. Safety & Preparation
- **ESD Protection:** Always wear an anti-static wrist strap to prevent damage to the STM32 and AD8232.
- **Tools:** Temperature-controlled soldering iron, lead-free solder, flux, tweezers, and a magnifying glass.
- **Cleanliness:** Clean the PCB with isopropyl alcohol before starting.

## 2. Assembly Order (Solder Smallest to Largest)
1. **Power Supply (LDO & Capacitors):** Solder the 3.3V LDO regulator and the 100nF decoupling capacitors first. *Do not insert the battery yet.*
2. **Microcontroller (STM32):** Solder the STM32 (use a stencil and hot air rework station for the QFP package if possible, otherwise drag-solder with a fine tip).
3. **Analog Front-End (AD8232):** Solder the AD8232 chip and its associated resistors/capacitors.
4. **BLE Module:** Solder the BLE module (e.g., nRF52).
5. **Connectors:** Solder the battery connector and the ECG electrode snap connectors.

## 3. Smoke Test (Before connecting the battery)
- **Visual Inspection:** Check for solder bridges between adjacent pins under a magnifying glass.
- **Continuity Test:** Use a multimeter to check for short circuits between 3.3V and GND.
- **Power Test:** Connect a bench power supply (set to 3.3V with a 100mA current limit) instead of the battery. Check if the LDO is outputting a stable 3.3V.

## 4. Initial Firmware Flash
- Connect the ST-Link programmer to the SWD pins.
- Flash a simple "Hello World" or "Blink LED" code to verify that the STM32 is alive.

## 5. Final ECG Test
- Connect the patient simulator (or a human volunteer).
- Observe the analog output on an oscilloscope to verify the ECG waveform is clean.

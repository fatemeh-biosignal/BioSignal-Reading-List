# PCB Design Plan (Post-Exam Phase)

This document outlines the step-by-step plan for designing the physical Printed Circuit Board (PCB) for the wearable ECG device.

## 1. Software & Tools
- **Primary Tool:** Altium Designer (or KiCad as an open-source alternative).
- **3D Modeling:** SolidWorks (for designing the device enclosure).

## 2. Design Process
1. **Schematic Capture:** Translating the `hardware_wiring.md` and `hardware_pinout.md` into a formal schematic.
2. **Component Selection:** Choosing exact footprints for the STM32, AD8232, and BLE module.
3. **PCB Layout:**
   - Separating analog (ECG) and digital (MCU/BLE) grounds to reduce noise.
   - Keeping the ECG traces as short as possible.
4. **Design Rule Check (DRC):** Ensuring the design meets manufacturing standards.
5. **Gerber Generation:** Exporting files for manufacturing (e.g., JLCPCB).

## 3. Form Factor
- **Shape:** Flexible circular patch (similar to a band-aid).
- **Layers:** 2-layer board (Top and Bottom) to keep costs low.

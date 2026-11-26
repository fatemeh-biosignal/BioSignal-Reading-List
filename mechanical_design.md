# Mechanical & Enclosure Design

This document outlines the mechanical design, material selection, and ergonomics for the BioSignal wearable patch.

## 1. Form Factor & Ergonomics
- **Shape:** A rounded, ergonomic patch that conforms to the contour of the left chest.
- **Thickness:** The reusable core should be less than 10mm thick to avoid discomfort during sleep.
- **Weight:** Total weight (including battery) should be under 15 grams.
- **Flexibility:** The disposable electrode part will use a flexible polyimide substrate to move with the patient's skin.

## 2. Material Selection
- **Skin-Contact Layer:** Medical-grade, hypoallergenic silicone (ISO 10993 certified) to prevent skin irritation.
- **Enclosure Shell:** Biocompatible polycarbonate (PC) or ABS plastic for the reusable core. 
- **Waterproofing:** The enclosure must achieve an **IP67 rating** (dust-tight and protected against water immersion up to 1 meter) to withstand sweat and accidental washing.

## 3. Thermal Management
- The electronic components (STM32, BLE) generate heat during operation.
- The enclosure will include a thin thermal pad to distribute heat evenly and ensure the surface temperature never exceeds 41°C (safe for human skin).

## 4. Manufacturing Process
- **Prototyping Phase:** The enclosure will be 3D printed using biocompatible resin (SLA/DLP printing) for initial fit testing.
- **Mass Production Phase:** Injection molding will be used for the plastic shell to reduce costs and ensure high precision.

## 5. User Interaction (Buttons & LEDs)
- The enclosure will feature a single, easy-to-press button for power and pairing.
- A small, light-pipe LED will indicate device status (Green = Connected, Red = Low Battery / Alert).

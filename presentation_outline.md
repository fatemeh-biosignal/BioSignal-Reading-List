# Project Presentation Outline (For Khwarizmi & ICEE)

This document outlines the structure for a 10-minute presentation of the BioSignal project.

## Slide 1: Title & Introduction
- Project Name: BioSignal - Low-Power Wearable ECG
- Presenter: Fatemeh Karimi
- **Hook:** Cardiovascular diseases are the #1 cause of death globally. Early detection saves lives.

## Slide 2: The Problem
- Arrhythmias (like AFib) often occur intermittently.
- Traditional ECGs in clinics miss them.
- Continuous wearable monitoring is limited by **battery life** and **data privacy**.

## Slide 3: Our Solution
- **Compressive Sensing (CS):** Reduces data size by 70% -> Saves battery.
- **TinyML:** Runs AI directly on the device -> Saves privacy and bandwidth.

## Slide 4: System Architecture (Hardware & Software)
- Show the `architecture.md` Mermaid diagram.
- **Hardware:** AD8232 sensor, STM32 MCU, BLE module.
- **Software:** Python simulation, OMP reconstruction, Random Forest classifier.

## Slide 5: Methodology Pipeline
- Signal Acquisition -> Filtering (Butterworth) -> Compression (CS) -> AI Classification (TinyML).
- Explain the OMP algorithm for signal reconstruction.

## Slide 6: Results & Validation
- **MSE:** OMP outperforms Linear Interpolation.
- **Model Accuracy:** >90% (expected on MIT-BIH).
- **Cost:** Estimated at ~$33 for the MVP prototype.

## Slide 7: Impact & Future Work
- **Impact:** Affordable, private, and continuous monitoring for high-risk patients.
- **Next Steps:** Clinical trials, PCB design, and expansion to early cancer detection.

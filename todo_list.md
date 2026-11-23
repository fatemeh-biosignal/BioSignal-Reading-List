# Project To-Do List (Hardware & Validation Phase)

This document tracks the immediate next steps for the BioSignal project.

## 1. Procurement (خرید قطعات)
- [ ] Order STM32F407 development board.
- [ ] Order AD8232 ECG sensor module.
- [ ] Order BLE module (e.g., nRF52 or HC-08).
- [ ] Purchase ECG electrodes and disposable patches.

## 2. Software & Validation (نرم‌افزار و اعتبارسنجی)
- [ ] Download the MIT-BIH Arrhythmia Database from PhysioNet.
- [ ] Run `tinyml_classifier.py` on the real dataset and record the accuracy.
- [ ] Run `performance_evaluation.py` to calculate the real MSE for OMP.

## 3. Hardware Prototyping (نمونه‌سازی سخت‌افزار)
- [ ] Solder components on the breadboard according to `hardware_wiring.md`.
- [ ] Flash the `embedded_c_code.c` to the STM32.
- [ ] Test the filtering and BLE communication.

## 4. Paper & Presentation (مقاله و ارائه)
- [ ] Fill in the real accuracy and MSE placeholders in `results_and_discussion.md`.
- [ ] Record the 2-minute demo video based on `demo_script.md`.

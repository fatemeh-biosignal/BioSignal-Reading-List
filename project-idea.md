# Project Idea: Low-Power Wearable ECG System

## The Problem
Continuous ECG monitoring outside hospitals is limited by battery life and data transmission costs. 

## My Proposed Solution
Designing a low-power wearable ECG system using:
- **Compressive Sensing (CS):** To reduce the number of samples and save power.
- **TinyML:** To detect arrhythmias directly on the microcontroller (on-device inference) without sending raw data to the cloud.
- **Low-power Hardware:** Using efficient Analog Front-Ends (AFE) and SAR ADCs.

## Why this matters
This connects my background in Electrical Engineering with my future in Medicine. It aims to create a practical, low-cost solution for remote healthcare.
## 🫀 Target Medical Condition: Atrial Fibrillation (AFib)

While my system aims to detect general arrhythmias, my primary target is **Atrial Fibrillation (AFib)**. 

**Why AFib?**
- It is the most common serious heart rhythm abnormality.
- It often occurs intermittently (Paroxysmal AFib), meaning a standard 10-second ECG at a clinic might miss it entirely.
- Continuous monitoring with a low-power wearable (like my proposed device) is the most effective way to catch it.
- Early detection of AFib can prevent strokes.

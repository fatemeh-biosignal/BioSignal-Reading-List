# Introduction (Draft for ICEE 2027 Paper)

## 1. Background and Motivation
Cardiovascular diseases (CVDs) remain the leading cause of death globally, accounting for approximately 17.9 million deaths annually (WHO, 2021). Among these, arrhythmias—such as Atrial Fibrillation (AFib)—are particularly dangerous because they often occur intermittently. A standard 10-second ECG recorded at a clinic frequently misses these silent events, making continuous monitoring essential for early diagnosis and stroke prevention.

## 2. Problem Statement
Despite the availability of wearable ECG monitors, two major challenges hinder their widespread adoption:
1. **Battery Life:** Continuous transmission of raw ECG data to the cloud rapidly drains the battery, making long-term monitoring impractical.
2. **Privacy:** Sending sensitive patient data to centralized cloud servers raises significant privacy and security concerns.

## 3. Proposed Solution
To address these challenges, this paper proposes **BioSignal**, a low-power wearable ECG monitoring system that integrates **Compressive Sensing (CS)** with **TinyML** (on-device machine learning).
- CS reduces the data volume by 70%, significantly lowering power consumption.
- TinyML runs a lightweight Random Forest classifier directly on the STM32 microcontroller, ensuring real-time arrhythmia detection without transmitting raw data to the cloud.

## 4. Contributions
The main contributions of this paper are:
1. An end-to-end simulation pipeline (Python and C) integrating CS, OMP reconstruction, and TinyML.
2. A comparative analysis proving the superiority of OMP reconstruction over linear interpolation for ECG signals.
3. A privacy-preserving, low-cost hardware architecture (~$33) tailored for developing countries.

## 5. Paper Organization
The remainder of this paper is organized as follows: Section II reviews related work. Section III describes the methodology and experimental setup. Section IV presents the results, and Section V concludes the paper and discusses future work.

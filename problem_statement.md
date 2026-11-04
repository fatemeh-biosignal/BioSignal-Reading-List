# Problem Statement & Proposed Solution

## 1. The Problem
Cardiovascular diseases (CVDs) are the leading cause of death globally. According to the World Health Organization (WHO), an estimated 17.9 million people died from CVDs in 2019, representing 32% of all global deaths. 

- **Arrhythmias:** Conditions like Atrial Fibrillation (AFib) often occur intermittently. A standard 10-second ECG at a clinic can easily miss these events.
- **Battery Life:** Continuous monitoring requires wearable devices. However, sending raw ECG data continuously drains the battery quickly.
- **Privacy:** Sending sensitive patient data to the cloud raises privacy concerns.

## 2. The Proposed Solution
We propose a **low-power wearable ECG device** that integrates **Compressive Sensing (CS)** and **TinyML**.

- **Compressive Sensing (CS):** Reduces the data size by 70%, significantly saving battery life.
- **TinyML:** Runs a lightweight Random Forest model directly on the device. This means the AI detects arrhythmias in real-time without sending raw data to the cloud, preserving patient privacy.
- **OMP Reconstruction:** Advanced algorithms ensure the full signal can be reconstructed when needed by a doctor.

## 3. Why This Matters
This solution enables long-term, continuous monitoring for high-risk patients. By detecting arrhythmias earlier, we can prevent strokes and save lives.

# Executive Summary: Low-Power Wearable ECG Monitoring

## 🎯 The Problem
Cardiovascular diseases are the leading cause of death globally. Continuous ECG monitoring outside hospitals is crucial for early detection of arrhythmias (like Atrial Fibrillation). However, existing wearable devices face a major challenge: **battery life**. Sending raw ECG data continuously drains the battery quickly and requires large storage.

## 💡 Our Solution
This project proposes a novel wearable ECG system that combines **Compressive Sensing (CS)** and **TinyML**:
1. **Compressive Sensing:** Reduces the amount of data sampled from the heart by 70% (keeping only 30%), significantly lowering power consumption.
2. **TinyML (On-Device AI):** Instead of sending raw data to the cloud, a lightweight Random Forest model runs directly on the microcontroller (e.g., STM32) to detect arrhythmias in real-time.
3. **OMP Reconstruction:** Advanced algorithms are used to reconstruct the full signal when needed.

## 🚀 Why This Matters
- **Energy Efficiency:** Reduces power consumption by minimizing data transmission.
- **Privacy:** Patient data is processed locally on the device, not in the cloud.
- **Clinical Impact:** Enables long-term, continuous monitoring for high-risk patients, leading to earlier medical intervention.

## 🏆 Goals
- Submit a research paper to the **ICEE 2027** conference.
- Present the prototype at the **Khwarizmi International Award (2027)**.

# Key Concepts for My Project

This file contains the core concepts I am learning and how they apply to my wearable ECG project.

---

## 1. Compressive Sensing (CS)
- **What it is:** A technique to sample signals at a lower rate than the Nyquist rate, assuming the signal is sparse.
- **Why it matters for ECG:** ECG signals have a sparse representation in certain domains (like wavelet). By using CS, we can reduce the number of samples, which directly saves battery power.
- **How I will use it:** I will implement a CS matrix on a low-power microcontroller to compress the ECG signal before transmission or processing.

## 2. TinyML (On-Device Machine Learning)
- **What it is:** Running lightweight machine learning models directly on microcontrollers (like RP2350 or STM32) instead of sending data to the cloud.
- **Why it matters for ECG:** Instead of sending raw ECG data to a phone, the device can detect arrhythmias (like AFib) locally and only send an alert. This saves power and protects privacy.
- **How I will use it:** I will deploy a lightweight classifier (e.g., SVM or a small Neural Network) to detect abnormal beats on the edge.

## 3. Low-Power Hardware Design
- **What it is:** Choosing components (ADC, AFE, MCU) and designing circuits that consume minimal power.
- **Why it matters:** Wearable devices need to last for days or weeks on a single battery charge.
- **How I will use it:** I will select a low-power Analog Front-End (AFE) and a SAR ADC to acquire the ECG signal efficiently.
- ## 4. Arrhythmia (آریتمی قلبی)
- **What it is (چیست؟):** Arrhythmia is an irregular heartbeat (heart rhythm disorder). It means the heart beats too fast, too slow, or with an irregular pattern.
- **Why it matters (چرا مهم است؟):** Many arrhythmias are harmless, but some can lead to serious complications like stroke or heart failure. Early detection is crucial for saving lives.
- **How my project helps (پروژه من چطور کمک می‌کند؟):** By using a low-power wearable ECG device with on-device TinyML, we can monitor the heart continuously. The device can detect abnormal rhythms (like Atrial Fibrillation) in real-time and alert the patient or doctor before a critical event occurs.

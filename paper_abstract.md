# Paper Abstract (Draft for ICEE 2027)

**Title:** Low-Power Wearable ECG Monitoring using Compressive Sensing and TinyML for Real-Time Arrhythmia Detection

**Abstract:**
Continuous monitoring of electrocardiogram (ECG) signals is crucial for the early detection of cardiovascular diseases, particularly arrhythmias like Atrial Fibrillation (AFib). However, conventional wearable ECG devices face significant challenges regarding battery life and data transmission bandwidth. 

This paper proposes a novel low-power wearable ECG system that integrates **Compressive Sensing (CS)** with **TinyML** (on-device machine learning). First, the raw ECG signal is compressed using a random sensing matrix, reducing the data volume to 30% of its original size. Second, instead of transmitting raw data to the cloud, a lightweight Random Forest classifier runs directly on a low-power microcontroller (e.g., STM32) to detect arrhythmias in real-time. For accurate signal reconstruction when needed, we implement the **Orthogonal Matching Pursuit (OMP)** algorithm. 

Experimental simulations demonstrate that our approach significantly reduces power consumption while maintaining high classification accuracy. The proposed system provides a practical, scalable, and privacy-preserving solution for long-term remote cardiac monitoring.

**Keywords:** Compressive Sensing, TinyML, ECG, Arrhythmia, Wearable Devices, Low-Power Hardware.

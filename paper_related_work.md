# Related Work (Draft for ICEE 2027 Paper)

This section reviews the existing literature on ECG monitoring, Compressive Sensing (CS), and TinyML.

## 1. Compressive Sensing in Biomedical Signals
Compressive Sensing (CS) has been widely adopted for ECG compression due to the signal's inherent sparsity in the wavelet domain [Candès et al., 2008]. Recent studies have shown that CS can reduce the sampling rate by up to 70% without compromising diagnostic quality. However, most of these studies focus purely on the mathematical reconstruction algorithms and do not address the practical integration with on-device AI.

## 2. TinyML and Edge Computing in Healthcare
The integration of Machine Learning on low-power microcontrollers (TinyML) has opened new avenues for real-time health monitoring. For instance, [PhysioEdge, 2025] introduced a multimodal compressive sensing platform for wearable health, demonstrating the feasibility of embedded AI. However, the specific combination of CS-based data reduction with a lightweight Random Forest classifier on an STM32 microcontroller for arrhythmia detection remains largely unexplored.

## 3. Hardware Implementations of CS
From a hardware perspective, [Safarpour et al., 2024] proposed an ADC-Assisted Random Sampler Architecture for efficient sparse signal acquisition. While this work provides an excellent hardware foundation for CS (reducing power consumption to < 25 µW), it does not include the software pipeline for on-device classification. 

## 4. Research Gap
Most existing works either focus exclusively on **hardware** (designing better ADCs) or **software** (optimizing AI models). There is a lack of a holistic, end-to-end framework that bridges the gap between CS hardware sampling and on-device TinyML classification. **BioSignal** addresses this gap by providing a complete, low-power, and privacy-preserving pipeline tailored for wearable ECG monitoring.

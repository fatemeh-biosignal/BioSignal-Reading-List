# Scientific and Engineering Contributions

This document summarizes the key contributions of the BioSignal project to the fields of biomedical engineering and artificial intelligence.

## 1. Engineering Contributions
- **End-to-End Open-Source Pipeline:** We provide a complete, open-source simulation pipeline (Python and C) that integrates signal processing, Compressive Sensing, and TinyML.
- **Hardware-Aware Algorithm Design:** The CS and TinyML algorithms are specifically optimized for low-power microcontrollers (e.g., STM32), bridging the gap between theoretical algorithms and practical hardware.

## 2. Scientific Contributions
- **Integrated CS-TinyML Framework:** We demonstrate that combining Compressive Sensing for data reduction with TinyML for on-device classification is a viable strategy for wearable ECG devices.
- **Comparative Analysis:** We provide a detailed comparison between OMP reconstruction and Linear Interpolation, proving the superiority of OMP in preserving diagnostic information.

## 3. Clinical Contributions
- **Low-Cost Solution for Developing Countries:** The project proposes a medical-grade ECG patch with an estimated prototype cost of ~$33, making continuous cardiac monitoring accessible to low-income patients.
- **Privacy-Preserving Design:** By keeping the AI inference on the device, we eliminate the need to transmit sensitive patient data to the cloud.

## 4. Open Science Contributions
- All code, documentation, hardware specifications, and clinical roadmaps are publicly available on GitHub to encourage further research in the open-source medical community.

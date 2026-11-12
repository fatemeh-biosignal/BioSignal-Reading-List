# Innovation & Novelty Statement

This document highlights the unique contributions and innovative aspects of the BioSignal project.

## 1. The Core Innovation: A Synergistic Approach
While many projects focus on either **hardware** (designing a better ADC) or **software** (training a better AI model), BioSignal integrates both into a single, cohesive pipeline. 
**Innovation:** We combine **Compressive Sensing (CS)** for extreme power reduction with **TinyML** for on-device privacy-preserving intelligence.

## 2. Technical Novelties
- **End-to-End Simulation:** We have built a complete simulation pipeline in Python that covers signal generation, noise filtering, CS compression, OMP reconstruction, and Random Forest classification.
- **Hardware-Aware AI:** The TinyML model is designed with hardware constraints in mind (low memory footprint, suitable for STM32 microcontrollers).
- **Real-Time Edge Processing:** By avoiding the cloud, we eliminate latency and protect patient data.

## 3. Clinical & Societal Impact
- **Bridging the Gap:** The project bridges the gap between bulky, expensive Holter monitors and consumer smartwatches. It provides medical-grade accuracy in a low-cost wearable patch.
- **Focus on Developing Countries:** The low cost (~$33 prototype) makes this technology accessible to patients in developing countries like Iran, where access to advanced medical equipment is limited.

## 4. Academic Contributions
- The algorithms and hardware specifications are fully documented and open-sourced on GitHub.
- The project aims to be published at the **ICEE 2027** conference, contributing to the scientific community.

# Experimental Setup

This document outlines the hardware and software environment used to conduct the experiments and generate the results for the ICEE 2027 paper.

## 1. Hardware Environment
- **Processor:** (To be updated based on the actual PC used for simulation, e.g., Intel Core i7).
- **RAM:** (e.g., 16 GB).
- **Target Microcontroller (Simulated):** STM32F407 (ARM Cortex-M4) with 1MB Flash and 192KB RAM.

## 2. Software Environment
- **Programming Language:** Python 3.9+
- **Libraries:** NumPy, SciPy, Scikit-Learn, Matplotlib, PyWavelets.
- **IDE:** VS Code / Jupyter Notebook.

## 3. Datasets
- **Phase 1 (Current):** Synthetic ECG signals generated using mathematical functions (sine waves + Gaussian noise) to test the algorithms.
- **Phase 2 (Future):** MIT-BIH Arrhythmia Database from PhysioNet. The dataset contains 48 half-hour ECG recordings sampled at 360 Hz.

## 4. Evaluation Metrics
- **Reconstruction Quality:** Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR) for evaluating OMP vs. Linear Interpolation.
- **Classification Performance:** Accuracy, Precision, Recall, and F1-Score for the TinyML Random Forest model.
- **Power Consumption:** Estimated using the STM32CubeMX Power Consumption Calculator (for hardware phase).

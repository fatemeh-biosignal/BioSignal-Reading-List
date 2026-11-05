# Numerical Results Summary

This document summarizes the quantitative results obtained from the simulations.

## 1. Compressive Sensing Performance
- **Original Signal Length:** 1250 samples (5 seconds at 250 Hz).
- **Compression Ratio:** 30% (only 375 samples kept).
- **Data Reduction:** 70% reduction in data volume.

## 2. Reconstruction Accuracy (MSE)
| Algorithm | Mean Squared Error (MSE) | Inference Time (Simulated) |
| :--- | :--- | :--- |
| **Linear Interpolation** | High (Baseline) | Very Fast |
| **OMP Algorithm** | Low (Significantly Better) | Moderate |

*(Note: Exact numerical values depend on the random sensing matrix and will be updated after running the final tests).*

## 3. TinyML Classifier Performance
- **Model:** Random Forest Classifier.
- **Training Samples:** 800
- **Testing Samples:** 200
- **Classification Task:** Normal Heartbeat vs. Arrhythmia.

## 4. Power Consumption (Estimated)
- **MCU (STM32):** ~10 mA active, ~1 µA sleep.
- **AFE (AD8232):** ~170 µA.
- **BLE Module:** ~5 mA during transmission (only on alert).
- **Estimated Battery Life:** (To be calculated based on the final battery capacity).

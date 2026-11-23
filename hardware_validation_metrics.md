# Hardware Validation Metrics

This document defines the key metrics and tests required to validate the physical prototype of the BioSignal device, similar to industry standards for wearable biosensors.

## 1. Electrode Contact & Signal Stability
- **Test:** Ask the subject to perform various movements (walking, sitting, stretching) while wearing the patch.
- **Metric:** Calculate the Signal-to-Noise Ratio (SNR) before, during, and after movement.
- **Goal:** Ensure the SNR does not drop below a critical threshold that would cause a false alarm.

## 2. Wireless Streaming Reliability (BLE)
- **Test:** Stream the compressed ECG data to the smartphone app from a distance of 10 meters (with and without walls).
- **Metric:** Packet Loss Rate (PLR) and Latency (delay).
- **Goal:** Achieve a Packet Loss Rate of less than 1% and latency under 100 ms.

## 3. Power Consumption
- **Test:** Measure the current draw of the device in different states (Sleep, Acquisition, Processing, BLE Transmission).
- **Metric:** Average power consumption in milliwatts (mW).
- **Goal:** Achieve a battery life of at least 3 days on a 500mAh Li-Po battery.

## 4. Repeatability Across Sessions
- **Test:** Measure the same patient's ECG on 3 different days under the same conditions.
- **Metric:** Variance in the R-Peak amplitudes and Heart Rate calculations.
- **Goal:** Ensure the device produces consistent, reliable data over time.

## 5. Thermal Safety
- **Test:** Use a thermal camera to monitor the temperature of the PCB and the battery during continuous operation.
- **Goal:** The surface temperature must not exceed 41°C to prevent skin burns (as per IEC 60601-1 standards).

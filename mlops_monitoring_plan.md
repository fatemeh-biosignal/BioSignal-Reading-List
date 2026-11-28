# MLOps & Model Monitoring Plan (SaMD)

This document outlines the strategy for monitoring the TinyML model after deployment to ensure it remains accurate and safe (Software as a Medical Device - SaMD).

## 1. The Challenge: Data & Model Drift
- **Data Drift:** Patient demographics, sensor aging, or environmental changes can cause the incoming ECG signals to look different from the training data.
- **Model Drift:** Over time, the AI model's accuracy may decrease, leading to false negatives (missing a real arrhythmia) or false positives (unnecessary alarms).

## 2. Real-Time Monitoring Metrics
The mobile app and hospital dashboard will track:
- **Confidence Score Distribution:** If the model's confidence in its predictions drops significantly, it may indicate data drift.
- **False Positive Rate (FPR):** If the number of alerts increases unexpectedly, doctors will flag it.
- **Signal Quality Index (SQI):** Monitoring the raw signal quality to distinguish between a sick patient and a broken sensor.

## 3. Continuous Learning Strategy (Federated Learning)
- To avoid privacy issues, raw patient data will **not** be sent to the cloud.
- We will use **Federated Learning**: The model learns from local data on the device, and only the *model weights* (not the data) are sent back to the server to create an updated global model.

## 4. Over-The-Air (OTA) Update Protocol
- If a new, improved model (e.g., Model v2.0) is trained, it will be signed digitally.
- The STM32 Secure Boot will verify the signature and install the update over BLE.
- A/B Testing: The new model will be rolled out to 10% of users first to ensure safety before a full release.

## 5. Post-Market Surveillance (PMS) Integration
- Any drop in model accuracy will trigger a CAPA (Corrective and Preventive Action) investigation, as outlined in our QMS plan.

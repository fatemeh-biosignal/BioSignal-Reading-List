# Multi-Modal Sensing Strategy

Inspired by recent Google Research published in Nature (regarding hypertension screening via PPG and ACC), this document outlines the strategy for expanding BioSignal's sensing modalities.

## 1. The "Screen, Don't Measure" Paradigm
Like the Google study, BioSignal is not designed to replace clinical gold standards (like 12-lead ECG or a blood pressure cuff). Instead, we aim to **screen** for physiological anomalies in daily life, prompting the patient to seek professional medical help early.

## 2. Expanding Beyond Single-Lead ECG
Currently, BioSignal relies on ECG (electrical). To create a holistic health profile, we will integrate:
- **PPG (Photoplethysmography):** To measure blood volume changes. This allows us to estimate Heart Rate Variability (HRV), SpO2 (blood oxygen), and potentially screen for hypertension signs.
- **ACC (Accelerometer):** To track physical activity and posture. This is crucial for **motion artifact rejection** (separating actual heart anomalies from noise caused by running or falling).
- **Temperature Sensor:** For detecting fever or local skin inflammation.

## 3. Multi-Modal AI Fusion
By fusing data from ECG, PPG, and ACC, the TinyML model becomes much smarter:
- *Scenario A:* High heart rate (from ECG) + High movement (from ACC) = Normal exercise.
- *Scenario B:* High heart rate (from ECG) + Zero movement (from ACC) = Potential Tachycardia at rest -> Trigger Alert.
- *Scenario C:* Low SpO2 (from PPG) + Irregular ECG = Potential sleep apnea or heart failure -> Trigger Alert.

## 4. Hardware Evolution
The future BioSignal 2.0 patch will feature an integrated AFE (Analog Front-End) that supports both ECG and PPG, along with a 3-axis accelerometer, all managed by the STM32 microcontroller.

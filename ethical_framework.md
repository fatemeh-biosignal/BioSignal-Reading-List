# Ethical Framework for AI in Healthcare

This document outlines the ethical principles guiding the development and deployment of the BioSignal device.

## 1. Human-in-the-Loop (حضور انسان در چرخه تصمیم‌گیری)
- **Principle:** AI is a tool, not a replacement for a doctor.
- **Implementation:** The TinyML model only generates an "alert" (e.g., suspected arrhythmia). The final diagnosis and treatment decision always rest with a licensed physician. We do not allow autonomous medical interventions.

## 2. Beneficence and Non-Maleficence (سودمندی و عدم ضرر رساندن)
- **Principle:** The device must do good and avoid harm.
- **Implementation:** The device is designed as a "screening tool" to catch anomalies early. To avoid harm (false alarms causing panic), the device uses high-specificity thresholds before sending an alert.

## 3. Patient Autonomy and Privacy (استقلال و حریم خصوصی بیمار)
- **Principle:** Patients have the right to control their own data.
- **Implementation:** As outlined in our Data Management Plan, patients must grant explicit consent for their data to be shared with their doctor. The AI runs on the device (Edge AI), so raw data is not uploaded to the cloud.

## 4. Equity and Accessibility (عدالت و دسترسی‌پذیری)
- **Principle:** Medical advancements should benefit everyone, not just the rich.
- **Implementation:** By keeping the hardware cost low (~$33), we aim to make this life-saving technology accessible to low-income patients and rural areas in Iran.

## 5. Transparency (شفافیت)
- **Principle:** The AI should not be a "black box."
- **Implementation:** The Random Forest model allows us to extract "feature importances," showing exactly which parts of the ECG signal led to the AI's decision. The entire source code is open-source on GitHub.

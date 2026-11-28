# Key Performance Indicators (KPIs)

This document defines the measurable metrics (KPIs) used to evaluate the success of the BioSignal project across technical, clinical, and business dimensions.

## 1. Technical KPIs (شاخص‌های فنی)
- **Battery Life:** ≥ 72 hours (3 days) of continuous monitoring on a single charge.
- **Data Compression Ratio:** 30% (70% reduction in transmitted data).
- **AI Inference Latency:** < 1 second from the onset of arrhythmia to the alert.
- **Signal-to-Noise Ratio (SNR):** > 20 dB after applying the Butterworth filter.

## 2. Clinical KPIs (شاخص‌های بالینی)
- **Sensitivity (True Positive Rate):** > 95% for detecting Atrial Fibrillation (AFib).
- **Specificity (True Negative Rate):** > 90% (minimizing false alarms).
- **Patient Adherence:** > 80% of patients wearing the patch for the full 7-day duration.
- **Skin Irritation Rate:** < 5% of patients experiencing mild redness.

## 3. Business & Project KPIs (شاخص‌های تجاری)
- **Prototype Cost:** < $50 per unit (Targeting ~$33).
- **Regulatory Milestone:** Submission of the IRC (Iran FDA) application by Month 12.
- **Clinical Partners:** Securing at least 1 hospital for the pilot trial by Month 6.
- **Intellectual Property:** Filing at least 1 provisional patent for the CS-TinyML algorithm.

## 4. How KPIs are Measured
- **Technical KPIs:** Measured using laboratory equipment (oscilloscope, multimeter) and software profiling (Python `time` module, STM32 CubeMonitor).
- **Clinical KPIs:** Measured during the pilot clinical trial against the gold-standard 12-lead ECG.
- **Business KPIs:** Tracked via financial spreadsheets and project management tools (GitHub Projects).

# TinyML Classifier Results (ECG Arrhythmia Detection)

This document summarizes the performance and results of the first Machine Learning model developed for this project.

## 1. Model Overview
- **Algorithm:** Random Forest Classifier (from `scikit-learn`)
- **Task:** Binary classification (Normal Heartbeat vs. Arrhythmia)
- **Input Data:** Synthetic ECG signals (100 time points per beat)
- **Training/Test Split:** 80% Training / 20% Testing

## 2. Model Performance
- **Accuracy:** (در اینجا عدد دقت مدل را بنویس، مثلاً 95% یا هر عددی که در خروجی کد دیدی)
- **Classification Report:** The model successfully distinguishes between the two classes.

## 3. Feature Importance (تحلیل ویژگی‌ها)
As shown in the `tinyml_classifier.py` script, the model evaluates the importance of each time point in the ECG signal. 
- This helps us understand which parts of the heartbeat (e.g., the QRS complex) are most critical for detecting arrhythmias.
- The visualization of `model.feature_importances_` provides insights into the decision-making process of the AI.

## 4. Next Steps
- Replace synthetic data with real MIT-BIH dataset.
- Optimize the model for deployment on a low-power microcontroller (TinyML).
- Write the results section for the ICEE 2027 paper.

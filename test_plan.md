# Test Plan

This document outlines the testing strategy to ensure the reliability and accuracy of the BioSignal device.

## 1. Unit Testing (تست واحد)
- **Objective:** Test individual components in isolation.
- **Method:** Use Python's `unittest` or `pytest` to test functions in `ecg_processor.py` and `omp_reconstruction.py`.
- **Success Criteria:** All test cases (in `test_pipeline.py`) must pass without errors.

## 2. Integration Testing (تست یکپارچگی)
- **Objective:** Ensure different modules work together correctly.
- **Method:** Run `main.py` to test the entire pipeline from signal generation to TinyML classification.
- **Success Criteria:** The pipeline runs without crashing, and the 4-panel dashboard is generated correctly.

## 3. Hardware Testing (تست سخت‌افزار)
- **Objective:** Validate the physical prototype.
- **Method:** 
  - Measure power consumption using a multimeter.
  - Inject a known ECG signal using a signal generator to test the ADC and AFE.
- **Success Criteria:** Power consumption is below the SRS threshold, and the recorded signal matches the input.

## 4. Clinical Validation (اعتبارسنجی بالینی)
- **Objective:** Prove the AI's accuracy on real patient data.
- **Method:** Test the TinyML model on the MIT-BIH Arrhythmia Database.
- **Success Criteria:** Achieve an accuracy of >90% in detecting arrhythmias.

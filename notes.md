# Research Notes

Short notes and observations from my daily reading on biomedical signal processing.

---

## October 15, 2026

- Started my GitHub research journal today.
- Focus areas: Compressive Sensing, ECG, TinyML, SAR ADC.
- Next: reading about FISTA vs OMP for on-device ECG reconstruction.

---
## October 16, 2026

- Reviewed README structure and added "Files in this repo" section.
- Next: reading about Compressive Sensing matrices for ECG.

---
## October 20, 2026
- Successfully added plotting code to `compressed_sensing_demo.py`.
- Learned how to use `plt.subplot` to show two graphs side-by-side.
- The red dots will represent the 30% of samples we kept, while the blue line is the original.

## October 22, 2026
- Created `reconstruction_demo.py` to demonstrate how to recover a signal from compressed samples.
- Learned how `np.interp` works in Python (Linear interpolation for missing points).
- Note: Linear interpolation is just a temporary placeholder. In the next phase, I will implement the OMP algorithm for more accurate reconstruction.
## October 23, 2026
- Created `real_ecg_analysis.py` to simulate real-world ECG data and apply noise filtering.
- Learned how `np.convolve` works in Python (Moving average filter for noise reduction).
- Note: Filtering is a necessary step before applying Compressive Sensing to ensure data quality.
## October 24, 2026
- Created `results_report.md` to summarize the simulations and algorithms implemented so far.
- This report will be the foundation for the ICEE 2027 paper and the Khwarizmi proposal.
- Created `math_model.md` documenting the core mathematical equations of Compressive Sensing (y = Phi * x, L1-minimization).
- This document will be the theoretical foundation for the OMP algorithm implementation.
## October 25, 2026
- Created `omp_reconstruction.py` to implement the Orthogonal Matching Pursuit (OMP) algorithm.
- This is a major upgrade from linear interpolation, using least squares optimization to recover the signal.
- Learned how to use `np.linalg.lstsq` in Python for solving matrix equations.
## October 26, 2026
- Created `load_real_data.py` to simulate loading a real MIT-BIH ECG record.
- The script accounts for the 360 Hz sampling rate used in standard medical datasets.
- Note: Next step is to integrate the `wfdb` library to read actual PhysioNet data.
## October 27, 2026
- Created `wavelet_analysis.py` to apply Discrete Wavelet Transform (DWT) using PyWavelets.
- Learned how wavelets (like 'db4') make the ECG signal sparse, which is a crucial step before applying Compressive Sensing.
- Updated `requirements.txt` to include `PyWavelets`.
## October 28, 2026
- Created `tinyml_classifier.py`, my first Machine Learning model for ECG analysis.
- Used `scikit-learn` (Random Forest) to classify between Normal and Arrhythmia heartbeats.
- Note: This is the foundational step for implementing TinyML on a low-power microcontroller.
- Added feature importance visualization to the TinyML classifier.
- This helps in understanding which parts of the ECG signal the Random Forest model focuses on for arrhythmia detection.
- Learned how to extract and plot `model.feature_importances_` in scikit-learn.
## October 29, 2026
- Created `main.py`, a central dashboard script that runs the entire pipeline.
- Integrated the `ECGProcessor` class, signal filtering, and the TinyML Random Forest model into one execution file.
- This script generates a 4-panel visualization showing raw, filtered, compressed signals, and AI feature importance.
## October 30, 2026
- Created `documentation.md` to provide a technical overview of all project modules.
- This file will serve as the foundation for the "Methodology" section of the ICEE 2027 paper.
- Created `architecture.md` to visualize the data flow from the ECG sensor to the TinyML classifier.
- Used Mermaid syntax in Markdown to generate a professional system architecture diagram.
- Created `hardware_specs.md` outlining the required components for the physical prototype.
- Selected the AD8232 for the Analog Front-End and STM32 for the core processing unit.
- This bridges the gap between the software simulation and the actual wearable device.
- Created `executive_summary.md` to provide a high-level overview of the project for reviewers and award committees.
- This document will be the first thing judges read for the Khwarizmi Award.
## October 31, 2026
- Added `ai_competitions.md` to track future AI competitions and medical datasets.
- This will help me plan my future research and portfolio after the entrance exam.
## November 1, 2026
- Created `future_roadmap.md` outlining the path from software simulation to hardware prototyping and commercialization.
- This document is crucial for the Khwarizmi Award, showing the practical and commercial potential of the project.
- Created `paper_abstract.md` as a draft for the ICEE 2027 paper.
- The abstract summarizes the entire project (CS, TinyML, OMP) in a professional academic format.
## November 2, 2026
- Created `control_system.md` to define the state machine and power management strategy for the wearable device.
- This ensures the device operates efficiently and maximizes battery life.
- Created `embedded_c_code.c` to demonstrate how the filtering logic can be implemented in C for microcontrollers.
- This bridges the gap between the Python simulation and the actual hardware implementation.
- Created `r_peak_detection.py` to identify heartbeats using `scipy.signal.find_peaks`.
- This allows the system to calculate the Heart Rate (BPM) from the ECG signal.
- Next step: Integrate this with the TinyML classifier to detect if the heart rate is abnormal.
- Created `heart_rate_alert.py` to define the medical alert logic (Bradycardia < 60 BPM, Tachycardia > 100 BPM).
- This brings the system closer to a real-world medical device.
- Created `limitations_future_work.md` to document the current boundaries of the project and plan the next steps.
- This shows scientific honesty and a clear vision for the future of the research.
- Created `performance_evaluation.py` to numerically compare OMP and Linear Interpolation.
- This provides quantitative proof (MSE) that OMP is superior for signal reconstruction.
- Created `graphical_abstract.md` to provide a quick visual overview of the system's data flow.
- This is a standard requirement for scientific papers and presentations.
- Created `test_pipeline.py` to add automated testing for the core algorithms.
- This ensures the reliability of the code and follows professional software engineering practices.
- Created `mobile_app_integration.md` to design the BLE communication between the wearable device and the smartphone app.
- Emphasized data encryption (AES-128) and patient privacy.
- Created `paper_draft.md` to outline the full structure of the ICEE 2027 paper.
- This will serve as the main skeleton for writing the final manuscript.

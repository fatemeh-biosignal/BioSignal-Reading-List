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
## October 26, 2026
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

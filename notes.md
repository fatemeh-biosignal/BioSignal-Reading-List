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
### November 1, 2026
- Created `real_ecg_analysis.py` to simulate real-world ECG data and apply noise filtering.
- Learned how `np.convolve` works in Python (Moving average filter for noise reduction).
- Note: Filtering is a necessary step before applying Compressive Sensing to ensure data quality.

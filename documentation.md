# Project Documentation

This file provides a technical overview of the Python scripts and modules in this repository.

## 1. `ecg_processor.py` (Object-Oriented Core)
- **Purpose:** Encapsulates the core signal processing tasks into a reusable class.
- **Class `ECGProcessor`:**
  - `generate_signal()`: Creates a synthetic ECG with noise.
  - `apply_moving_average_filter()`: Removes high-frequency noise.
  - `compress_signal()`: Simulates Compressive Sensing by keeping 30% of the data.

## 2. `tinyml_classifier.py` (Machine Learning)
- **Purpose:** Trains a Random Forest model to detect Arrhythmia.
- **Key Functions:**
  - `generate_synthetic_ecg_data()`: Creates labeled data (Normal vs. Arrhythmia).
  - Uses `scikit-learn` to train and evaluate the model.
  - Extracts `feature_importances_` to show which signal parts matter most.

## 3. `omp_reconstruction.py` (Advanced Algorithm)
- **Purpose:** Implements the Orthogonal Matching Pursuit (OMP) algorithm.
- **Key Functions:**
  - `omp_algorithm(y, A, sparsity_k)`: Reconstructs the original signal from compressed measurements using Least Squares optimization.

## 4. `main.py` (Pipeline Dashboard)
- **Purpose:** The main execution script that runs the entire pipeline from start to finish.
- **Output:** Generates a 4-panel visualization (Raw, Filtered, Compressed, and Feature Importance).

## 5. Other Files
- `wavelet_analysis.py`: Applies Discrete Wavelet Transform for sparsity.
- `load_real_data.py`: Simulates loading MIT-BIH datasets.
- `requirements.txt`: Lists all necessary Python libraries.

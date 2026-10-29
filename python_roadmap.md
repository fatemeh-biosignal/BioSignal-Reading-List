# My Python Learning Roadmap

This file documents my step-by-step journey learning Python for Biomedical Signal Processing.

## Phase 1: Basics
- **Variables:** Storing data (e.g., heart rate, patient name).
- **Libraries:** Importing pre-written code (e.g., `import numpy as np`).

## Phase 2: Simulation & Plotting
- **NumPy (`np.linspace`, `np.sin`):** Generating synthetic ECG signals.
- **Matplotlib (`plt.plot`, `plt.show`):** Visualizing the signals.
- **Noise Addition (`np.random.randn`):** Simulating real-world noise.

## Phase 3: Filtering & Preprocessing
- **Moving Average (`np.convolve`):** Removing high-frequency noise from the signal.
- **Subplots (`plt.subplot`):** Comparing raw vs. filtered signals side-by-side.

## Phase 4: Compressive Sensing (Compression)
- **Random Sampling (`np.random.choice`):** Selecting only a percentage of data points (e.g., 30%).
- **Scatter Plot (`plt.scatter`):** Visualizing the compressed points.

## Phase 5: Signal Reconstruction
- **Linear Interpolation (`np.interp`):** A basic method to guess missing points.
- **OMP Algorithm (`np.linalg.lstsq`):** Advanced reconstruction using Least Squares optimization.
- **MSE Calculation:** Evaluating the reconstruction accuracy (Mean Squared Error).

## Phase 6: Advanced Analysis (Wavelets)
- **Discrete Wavelet Transform (`pywt.wavedec`):** Decomposing the signal to make it sparse before compression.

## Phase 7: Machine Learning (TinyML)
- **Scikit-Learn:**
  - `train_test_split`: Splitting data into training and testing sets.
  - `RandomForestClassifier`: Training a lightweight AI model for classification.
  - `accuracy_score`: Evaluating the model's performance.
  - `feature_importances_`: Analyzing which parts of the signal the model finds most important.

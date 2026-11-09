# Software Design Document (SDD)

This document describes the architecture and design of the Python software modules in the BioSignal project.

## 1. System Architecture
The software is divided into four main modules, following a modular and object-oriented approach:
1. **Signal Processing (`ecg_processor.py`)**
2. **Compression & Reconstruction (`compressed_sensing_demo.py`, `omp_reconstruction.py`)**
3. **Machine Learning (`tinyml_classifier.py`)**
4. **User Interface (`gui_dashboard.py`)**

## 2. Module Design Details

### 2.1. Signal Processing (ECGProcessor Class)
- **Design Pattern:** Object-Oriented (OOP).
- **Attributes:** `duration`, `sampling_rate`, `raw_signal`, `filtered_signal`.
- **Methods:** `generate_signal()`, `apply_moving_average_filter()`, `compress_signal()`.
- **Purpose:** Encapsulates all signal manipulation logic in a reusable class.

### 2.2. Compression & Reconstruction
- **Algorithm:** Orthogonal Matching Pursuit (OMP).
- **Input:** Compressed measurements (`y`) and Sensing Matrix (`A`).
- **Output:** Reconstructed sparse vector (`x_hat`).
- **Dependencies:** `numpy.linalg.lstsq` for least-squares optimization.

### 2.3. Machine Learning (TinyML Classifier)
- **Model:** Random Forest (Scikit-Learn).
- **Data Split:** 80% Training / 20% Testing.
- **Output:** Binary classification (0 = Normal, 1 = Arrhythmia) and feature importances.

### 2.4. User Interface (GUI Dashboard)
- **Framework:** Tkinter.
- **Design Pattern:** Event-Driven Programming (buttons trigger functions).
- **Integration:** Embeds Matplotlib figures into the Tkinter window using `FigureCanvasTkAgg`.

## 3. Data Flow
1. `ECGProcessor` generates and filters the signal.
2. The signal is compressed using a random sensing matrix.
3. `omp_algorithm` reconstructs the signal (for validation).
4. `tinyml_classifier` analyzes the signal for arrhythmias.
5. `gui_dashboard` visualizes the results for the user.

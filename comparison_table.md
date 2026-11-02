# Comparative Analysis of Reconstruction Methods

This document compares different signal reconstruction methods used in this project.

## 1. Linear Interpolation vs. OMP

| Feature | Linear Interpolation | Orthogonal Matching Pursuit (OMP) |
| :--- | :--- | :--- |
| **Algorithm Type** | Simple mathematical fill-in | Sparse recovery optimization |
| **Computational Cost** | Very Low (O(N)) | Medium/High (Iterative) |
| **Accuracy (MSE)** | Higher Error | Lower Error (More Accurate) |
| **Handling Noise** | Poor | Better (Due to sparsity constraints) |
| **Use Case** | Quick visual check | Real medical reconstruction |

## 2. Why OMP is better for ECG?
ECG signals have a sparse representation in certain domains (like wavelets). OMP exploits this sparsity to reconstruct the signal with fewer measurements, which is the core principle of Compressive Sensing. Linear interpolation does not use any structural information of the signal, hence it is less accurate.

# Mathematical Model of Compressive Sensing

To implement Compressive Sensing (CS) effectively in my project, I need to understand the mathematical foundation. This file documents the core equations.

## 1. The Sensing Equation
Instead of measuring the signal $x$ (which has length $N$), we take $M$ measurements, where $M < N$. 
The measurement vector $y$ is obtained by:

$$y = \Phi x$$

- $x$: The original signal (e.g., ECG signal) of length $N$.
- $\Phi$: The measurement matrix (or sensing matrix) of size $M \times N$.
- $y$: The compressed measurements of length $M$.

## 2. Sparsity
CS relies on the assumption that the signal is *sparse* in some domain (like Wavelet or Fourier). If the signal is sparse in a basis $\Psi$, we can write:

$$x = \Psi s$$

Where $s$ is the sparse representation of $x$. Combining this with the first equation:

$$y = \Phi \Psi s = A s$$

Where $A = \Phi \Psi$ is the recovery matrix.

## 3. The Reconstruction Problem
To recover the original signal $x$, we need to find the sparsest vector $s$ that satisfies $y = As$. This is an optimization problem:

$$\min \|s\|_1 \quad \text{subject to} \quad y = As$$

This is known as $L_1$-norm minimization, which can be solved using algorithms like **Orthogonal Matching Pursuit (OMP)** or **FISTA**.

## Next Steps for Implementation
- Implement a random Gaussian matrix for $\Phi$.
- Write the OMP algorithm in Python to solve the $L_1$ minimization problem.

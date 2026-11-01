# OMP Algorithm Flowchart

This diagram shows the step-by-step process of the Orthogonal Matching Pursuit (OMP) algorithm for signal reconstruction.

```mermaid
graph TD
    A[Input: Compressed Signal y] --> B[Initialize Residual r = y]
    B --> C[Set Sparse Vector x = 0]
    C --> D{Is Sparsity Level Reached?}
    D -- No --> E[Find Column with Max Correlation to r]
    E --> F[Add Index to Active Set]
    F --> G[Solve Least Squares: A_subset * x_subset = y]
    G --> H[Update Residual: r = y - A_subset * x_subset]
    H --> D
    D -- Yes --> I[Output: Reconstructed Signal x]

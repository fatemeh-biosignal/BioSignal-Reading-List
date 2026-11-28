# Release & Versioning Strategy

This document outlines the versioning scheme and release process for the BioSignal project, ensuring stability and transparency for researchers and developers.

## 1. Semantic Versioning (SemVer)
We follow the standard **MAJOR.MINOR.PATCH** versioning scheme:
- **MAJOR (e.g., 1.0.0):** Incompatible API changes or major hardware redesigns.
- **MINOR (e.g., 1.1.0):** Adding new features (e.g., adding PPG integration or a new AI model) in a backward-compatible manner.
- **PATCH (e.g., 1.1.1):** Bug fixes and minor performance improvements.

## 2. AI Model Versioning
The machine learning model is versioned separately from the software code to ensure reproducibility:
- **Model v1.0:** Random Forest trained on synthetic data.
- **Model v2.0:** 1D-CNN trained on the MIT-BIH dataset.
*Note: The specific model version used in a clinical study must be documented in the `model_card.md`.*

## 3. Release Cycle
- **Alpha Releases:** Internal testing by the core team. (e.g., v0.1.0-alpha)
- **Beta Releases:** Shared with partner hospitals for pilot testing. (e.g., v1.0.0-beta)
- **Stable Releases:** Publicly available for research and clinical use. (e.g., v1.0.0)

## 4. Documentation Updates
- Every new release must be accompanied by an update to the `CHANGELOG.md`.
- The `README.md` must be updated if the installation process or new features change.

## 5. Backward Compatibility
- We aim to maintain backward compatibility for at least one major version to ensure that ongoing clinical trials are not disrupted by software updates.

# Usability Engineering Plan (IEC 62366-1)

This document outlines the usability engineering process to ensure the BioSignal device is safe and effective for its intended users, minimizing the risk of use errors.

## 1. Intended User Profiles
- **Primary User:** Elderly patients (65+ years) with limited technical literacy. They may have visual or hearing impairments.
- **Secondary User:** Cardiologists and nurses who need to interpret the data quickly in a busy clinical environment.

## 2. Use Scenarios & Hazards
- **Hazard 1:** Patient accidentally detaches the patch (e.g., pulling a shirt off).
  - *Mitigation:* The app sends an immediate "Patch Detached" alert with a loud sound.
- **Hazard 2:** Patient ignores a critical alert because they don't understand it.
  - *Mitigation:* Use clear, non-medical language (e.g., "Sit down immediately") and a red flashing screen.
- **Hazard 3:** Doctor misinterprets the AI's alert as a confirmed diagnosis.
  - *Mitigation:* The app clearly states "AI Screening Alert - Requires Clinical Confirmation."

## 3. Formative Evaluation (During Design)
- We will create low-fidelity prototypes (paper mockups) of the mobile app.
- We will ask 5 non-technical people to perform tasks (e.g., "Find your heart rate history") and observe where they struggle.

## 4. Summative Evaluation (Final Validation)
- Before market release, we will conduct a usability test with 15 participants representing the target user group.
- **Success Criteria:** 95% of users must be able to complete the setup and understand the alerts without any assistance.

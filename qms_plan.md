# Quality Management System (QMS) Plan (ISO 13485)

This document outlines the Quality Management System (QMS) for the BioSignal project, ensuring compliance with ISO 13485 (Medical Devices - Quality Management Systems).

## 1. Purpose & Scope
The QMS ensures that the BioSignal wearable ECG device consistently meets regulatory requirements and patient safety standards throughout its lifecycle (from design to commercialization).

## 2. Document Control
- All project documentation (code, schematics, risk analysis) is maintained in this GitHub repository.
- Version control is managed via Git commits, providing a full audit trail of all changes.

## 3. Design Controls (کنترل طراحی)
The design process follows a structured approach:
- **Design Input:** User needs and clinical requirements (see `user_personas.md` and `srs.md`).
- **Design Output:** System architecture, hardware schematics, and software code.
- **Design Verification:** Testing the software and hardware against the requirements (see `test_plan.md`).
- **Design Validation:** Clinical trials to ensure the device meets the actual clinical needs (see `clinical_trial_protocol.md`).

## 4. Risk Management (ISO 14971)
- A comprehensive FMEA (Failure Mode and Effects Analysis) has been conducted to identify and mitigate risks (see `risk_analysis.md`).

## 5. Corrective and Preventive Actions (CAPA)
- **Corrective Action:** If a bug or hardware failure is detected (e.g., in GitHub Issues), a root-cause analysis is performed and a fix is implemented.
- **Preventive Action:** Code reviews and automated testing (`test_pipeline.py`) are used to prevent future issues.

## 6. Traceability
- Every feature and component can be traced from the initial user requirement to the final implementation in the code.

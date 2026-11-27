# Biocompatibility Testing Plan (ISO 10993)

This document outlines the testing strategy to ensure that the BioSignal wearable patch is safe for prolonged skin contact, in compliance with ISO 10993 standards.

## 1. Material Selection (Pre-emptive Measures)
Before testing, we will select materials known for their biocompatibility:
- **Skin Adhesive:** Medical-grade silicone or acrylic adhesives (hypoallergenic).
- **Electrodes:** Hydrogel electrodes (standard for ECG).
- **Enclosure:** Medical-grade polycarbonate (PC) or biocompatible 3D printing resin (for prototypes).
- **PCB Coating:** Parylene coating to prevent skin contact with electronic components and solder.

## 2. Required Tests (Based on Contact Duration)
Since the BioSignal patch is designed for continuous wear (up to 7 days), it falls under the category of **"Prolonged Surface Contact"** (24 hours to 30 days).

### 2.1. Cytotoxicity (ISO 10993-5)
- **Purpose:** Ensure that the materials do not kill cells.
- **Method:** In-vitro testing using mammalian cell cultures (e.g., L929 mouse fibroblasts).
- **Success Criteria:** No more than a Grade 1 reaction (slight reactivity).

### 2.2. Sensitization and Irritation (ISO 10993-10)
- **Purpose:** Ensure the device does not cause allergic reactions or skin irritation.
- **Method:** In-vivo testing on animal models (or human patch tests in the final phase).
- **Success Criteria:** No erythema (redness) or edema (swelling) after 72 hours of exposure.

### 2.3. Extractables and Leachables (E&L)
- **Purpose:** Ensure no harmful chemicals (e.g., plasticizers) leak from the plastic shell or adhesive onto the patient's skin.
- **Method:** Chemical analysis using Gas Chromatography-Mass Spectrometry (GC-MS).

## 3. Testing Roadmap
1. **Phase 1 (Prototype):** Test the 3D-printed enclosure and hydrogel electrodes.
2. **Phase 2 (Pilot):** Conduct a 7-day patch test on 10 healthy volunteers to observe for any skin irritation.
3. **Phase 3 (Commercial):** Partner with an ISO 17025-accredited laboratory for official certification.

## 4. Risk Mitigation
If a patient develops skin irritation (reported via the mobile app), the CAPA system (as defined in the QMS plan) will be triggered to investigate whether the adhesive or the enclosure material is the cause.

# Metabolic Wearables Integration (Beyond ECG)

Inspired by 2026 FDA-cleared technologies (like Abbott Libre Duo and Biolinq Shine), this document outlines the roadmap for integrating metabolic (biochemical) sensing into the BioSignal platform.

## 1. The Shift from Electrical to Biochemical
- **Current State:** BioSignal focuses on **electrical signals** (ECG) to monitor heart rhythm.
- **Future Trend:** The next generation of wearables will use **microneedles or sweat-based biosensors** to monitor metabolic markers like glucose, ketones, and lactate in real-time, without drawing blood.

## 2. Why Integrate Metabolic Sensing?
Cardiovascular health is deeply connected to metabolic health:
- **Diabetes & Heart Disease:** High glucose levels damage blood vessels, increasing the risk of arrhythmias and heart failure.
- **Ketones & Arrhythmias:** Abnormal ketone levels (e.g., in diabetic ketoacidosis) can cause severe cardiac arrhythmias.
- **Lactate & Sepsis:** High lactate levels can indicate sepsis or tissue hypoxia, which can lead to rapid heart rate and cardiac arrest.

## 3. The Ultimate Multi-Modal Patch
The BioSignal 3.0 concept will feature a **hybrid sensor array**:
1. **ECG Electrodes:** For heart rhythm (Gold standard).
2. **PPG Sensor:** For SpO2 and heart rate variability.
3. **Sweat-Based Biosensor:** To monitor glucose and lactate via microfluidics.

## 4. AI Data Fusion
With multiple data streams, the TinyML model becomes much more powerful:
- *Example:* If ECG shows an arrhythmia **AND** the sweat sensor detects low glucose (hypoglycemia), the AI can alert the patient to eat sugar immediately, preventing a cardiac event.

## 5. Engineering Challenges
- **Sweat Stimulation:** Using iontophoresis (a mild electrical current) to stimulate sweat production without exercise.
- **Sensor Degradation:** Ensuring the enzymes in the biosensor remain stable for at least 7 days of continuous wear.

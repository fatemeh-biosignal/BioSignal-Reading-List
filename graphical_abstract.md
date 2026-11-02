# Graphical Abstract

This is a visual summary of the project's workflow.

```text
[Patient's Heart] 
      │
      ▼
[ECG Sensor (AD8232)] ──> Captures raw analog signal
      │
      ▼
[Analog Front-End & ADC] ──> Converts to digital (250 Hz)
      │
      ▼
[Compressive Sensing] ──> Compresses data to 30%
      │
      ├─────────────────────────────────┐
      ▼                                 ▼
[OMP Reconstruction]             [TinyML Classifier]
(Recovers full signal)           (Detects Arrhythmia on-device)
      │                                 │
      ▼                                 ▼
[Data Visualization]             [Heart Rate Alert]
                                 (BPM < 60 or > 100)
                                        │
                                        ▼
                                 [Alert Patient/Doctor]

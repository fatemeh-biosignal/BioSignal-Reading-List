# System Architecture

This diagram shows the data flow and architecture of my wearable ECG monitoring system.

```mermaid
graph TD
    A[ECG Sensor] -->|Raw Analog Data| B(Analog Front-End & ADC)
    B -->|Digital Raw Signal| C{ECGProcessor Class}
    C -->|Filtered Signal| D[Compressive Sensing]
    D -->|30% Compressed Data| E(OMP Reconstruction)
    D -->|Compressed Data| F{TinyML Classifier}
    F -->|Classification| G[Arrhythmia Detected?]
    E -->|Reconstructed Signal| H[Data Visualization]
    G -->|Yes| I[Alert Patient/Doctor]
    G -->|No| J[Normal Heartbeat]

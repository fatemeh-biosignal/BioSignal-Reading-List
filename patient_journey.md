# Patient Journey Map

This document illustrates how the BioSignal device fits into the daily life of a patient and their doctor.

```mermaid
journey
    title Patient Journey with BioSignal
    section Daily Life
      Wakes up and attaches the ECG patch: 5: Patient
      Goes about daily activities: 4: Patient
    section Anomaly Detection
      Device detects irregular heartbeat: 3: Patient
      TinyML classifies as Arrhythmia: 1: Device
      Alert sent to mobile app: 2: Patient
    section Medical Intervention
      Patient contacts doctor: 2: Patient, Doctor
      Doctor reviews the compressed ECG data: 3: Doctor
      Doctor prescribes medication or visit: 4: Doctor, Patient
    section Recovery
      Patient feels safe and monitored: 5: Patient

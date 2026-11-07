# Medical Data Standards (HL7 / FHIR)

This document outlines how the BioSignal device integrates with hospital information systems using international medical data standards.

## 1. Why HL7 FHIR?
HL7 (Health Level Seven) and FHIR (Fast Healthcare Interoperability Resources) are the global standards for exchanging healthcare information electronically. Using FHIR ensures that our device can communicate with any modern Electronic Health Record (EHR) system.

## 2. Data Structure (FHIR Resources)
Our system uses the following FHIR resources:
- **Patient:** Stores the patient's demographic information (Name, ID, Age).
- **Observation:** Stores the ECG data and Heart Rate (BPM). It includes the timestamp and the device ID.
- **Alert:** If an arrhythmia is detected, an alert is generated and sent to the doctor's dashboard.

## 3. Example JSON Payload (Heart Rate Observation)
```json
{
  "resourceType": "Observation",
  "status": "final",
  "category": [
    {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/observation-category",
          "code": "vital-signs"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "system": "http://loinc.org",
        "code": "8867-4",
        "display": "Heart rate"
      }
    ]
  },
  "subject": {
    "reference": "Patient/12345"
  },
  "valueQuantity": {
    "value": 72,
    "unit": "beats/minute",
    "system": "http://unitsofmeasure.org",
    "code": "/min"
  }
}

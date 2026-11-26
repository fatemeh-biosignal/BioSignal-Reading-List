# Data Dictionary

This document defines the structure, data types, and constraints for the key data elements used in the BioSignal system (both in the code and the database).

## 1. Patient Data
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `patient_id` | String (UUID) | Unique identifier for the patient. | Primary Key, Anonymized |
| `age` | Integer | Patient's age in years. | 18 - 100 |
| `gender` | String | Patient's gender. | "Male", "Female", "Other" |
| `medical_history` | String | Brief history of cardiac issues. | Max 500 characters |

## 2. ECG Signal Data (Raw & Filtered)
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `record_id` | String (UUID) | Unique ID for the ECG recording session. | Primary Key |
| `timestamp` | DateTime | Date and time of the recording. | ISO 8601 format |
| `sampling_rate` | Integer | Sampling rate of the ECG. | Default: 250 (Hz) |
| `signal_array` | Float Array | The actual ECG voltage values. | Length: 1250 (for 5 sec) |
| `compression_ratio` | Float | Ratio of compressed data. | Default: 0.3 (30%) |

## 3. AI Classification Data
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `prediction_id` | String (UUID) | Unique ID for the AI prediction. | Primary Key |
| `record_id` | String (UUID) | Foreign key linking to the ECG record. | Foreign Key |
| `predicted_class` | Integer | 0 = Normal, 1 = Arrhythmia. | 0 or 1 |
| `confidence_score` | Float | Probability of the prediction (0.0 to 1.0). | 0.0 - 1.0 |
| `model_version` | String | Version of the TinyML model used. | e.g., "v1.0.0" |

## 4. Alert Data
| Field Name | Data Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `alert_id` | String (UUID) | Unique ID for the alert. | Primary Key |
| `patient_id` | String (UUID) | Foreign key linking to the patient. | Foreign Key |
| `alert_type` | String | Type of alert (e.g., Bradycardia). | "Tachycardia", "Bradycardia" |
| `severity` | String | Severity level of the alert. | "Low", "Medium", "Critical" |
| `is_acknowledged` | Boolean | Has the doctor seen this alert? | Default: False |

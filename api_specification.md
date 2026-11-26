# API Specification (RESTful)

This document defines the RESTful API endpoints used for communication between the BioSignal mobile app, the doctor's dashboard, and the backend server.

## 1. General Rules
- **Protocol:** HTTPS (TLS 1.3)
- **Authentication:** JWT (JSON Web Tokens) passed in the `Authorization: Bearer <token>` header.
- **Data Format:** JSON (application/json)

## 2. Endpoints

### 2.1. Authentication
**POST `/api/v1/auth/login`**
- **Description:** Authenticates a user (Patient or Doctor).
- **Request Body:** `{"email": "string", "password": "string"}`
- **Response (200 OK):** `{"token": "jwt_string", "role": "doctor|patient"}`

### 2.2. Device Data Upload
**POST `/api/v1/ecg/upload`**
- **Description:** The mobile app uploads compressed ECG data or AI alerts from the device.
- **Request Body:** 
  ```json
  {
    "patient_id": "uuid",
    "timestamp": "2026-11-26T10:00:00Z",
    "alert_triggered": true,
    "alert_type": "Tachycardia",
    "compressed_data": [0.1, 0.5, 0.3, ...] 
  }
· Response (201 Created): {"status": "success", "record_id": "uuid"}

2.3. Patient Data Retrieval (Doctor Dashboard)

GET /api/v1/patients/{patient_id}/ecg

· Description: Retrieves the ECG history for a specific patient.
· Query Parameters: ?limit=10&start_date=2026-11-01
· Response (200 OK):
{
  "data": [
    {
      "record_id": "uuid",
      "timestamp": "2026-11-26T10:00:00Z",
      "heart_rate": 72,
      "is_anomaly": false
    }
  ]
}
2.4. Alert Management

POST /api/v1/alerts/{alert_id}/acknowledge

· Description: The doctor acknowledges that they have seen an alert.
· Response (200 OK): {"status": "acknowledged", "time": "2026-11-26T10:05:00Z"}

3. Error Handling

· 400 Bad Request: Missing parameters or invalid data.
· 401 Unauthorized: Invalid or expired JWT token.
· 403 Forbidden: Patient trying to access another patient's data.
· 500 Internal Server Error: Server crash or database failure.

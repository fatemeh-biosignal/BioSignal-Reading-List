# Mobile App UI/UX Design

This document outlines the User Interface (UI) and User Experience (UX) design for the BioSignal mobile application.

## 1. Design Principles
- **Accessibility:** Large fonts and high-contrast colors for elderly patients.
- **Simplicity:** The patient app should require minimal interaction (plug and play).
- **Actionable Data:** The doctor app should highlight critical alerts, not just raw data.

## 2. Patient App Interface
### Screen 1: Home Dashboard
- **Visual:** A large, green heart icon in the center indicating the current heart rate (e.g., "72 BPM").
- **Status Bar:** "Device Connected" (Green) or "Patch Detached" (Red).
- **Action Button:** "View History" and "SOS/Emergency Call".

### Screen 2: Alerts & Notifications
- **Visual:** A full-screen red warning if an arrhythmia is detected.
- **Text:** "Irregular heartbeat detected. Please sit down and rest. Your doctor has been notified."
- **Action:** "Call Doctor" button.

## 3. Doctor Dashboard (Web/Tablet App)
### Screen 1: Patient List
- A list of patients with color-coded status indicators (Green = Stable, Yellow = Warning, Red = Critical).

### Screen 2: Patient Detail (ECG View)
- **Visual:** Real-time reconstructed ECG waveform (using the OMP algorithm).
- **Metrics:** Heart Rate trend chart over the last 24 hours.
- **Alert History:** A log of all arrhythmia events with timestamps.

## 4. Color Palette & Typography
- **Primary Color:** Medical Blue (#0056b3) - conveys trust and professionalism.
- **Alert Color:** Emergency Red (#dc3545).
- **Font:** Roboto or Vazirmatn (for Persian language support) with a minimum size of 16sp.

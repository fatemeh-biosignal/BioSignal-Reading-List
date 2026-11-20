# Demo Video Script (For Khwarizmi & ICEE)

This document outlines the script and visual cues for a 2-minute project demo video.

## Scene 1: Introduction (0:00 - 0:20)
- **Visual:** The presenter (Fatemeh Karimi) speaking to the camera, or a title slide with the BioSignal logo.
- **Audio/Script:** "Hello, I am Fatemeh Karimi. Cardiovascular diseases are the leading cause of death globally. Today, I will introduce BioSignal, a low-power wearable ECG monitoring system that integrates Compressive Sensing and TinyML to save lives through early arrhythmia detection."

## Scene 2: The Software Simulation (0:20 - 0:50)
- **Visual:** Screen recording of the `gui_dashboard.py` running.
- **Action:** Click the "Generate ECG Signal" button. A normal ECG wave appears.
- **Audio/Script:** "This is our Python-based simulation. We generate a synthetic ECG signal at 250 Hz. To save battery, we apply Compressive Sensing, reducing the data size by 70%, and then reconstruct it using the OMP algorithm."

## Scene 3: The AI Detection (0:50 - 1:20)
- **Visual:** Screen recording of the terminal running `tinyml_classifier.py`. Then, show the "Simulate Arrhythmia Alert" button on the GUI.
- **Action:** Click the alert button. A red warning box appears on the screen.
- **Audio/Script:** "But data reduction is not enough. Our TinyML Random Forest model runs directly on the device. When an irregular heartbeat is detected, the system immediately triggers an alert, notifying the patient to consult a doctor."

## Scene 4: Hardware Architecture (1:20 - 1:40)
- **Visual:** Display the Mermaid diagram from `architecture.md` or `hardware_wiring.md`.
- **Audio/Script:** "For the physical prototype, we will use an STM32 microcontroller, the AD8232 ECG sensor, and a BLE module. The total cost of the prototype is estimated at just $33, making it highly accessible for developing countries."

## Scene 5: Impact & Conclusion (1:40 - 2:00)
- **Visual:** The presenter looking at the camera, or a slide with the GitHub QR code.
- **Audio/Script:** "BioSignal is not just a device; it is a step toward accessible, private, and continuous healthcare. All our code and research are open-source on GitHub. Thank you for your attention."

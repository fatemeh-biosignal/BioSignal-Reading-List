# Risk Management Plan

This document identifies potential project risks and outlines mitigation strategies to ensure the successful development of BioSignal.

## 1. Technical Risks
- **Risk:** Hardware components (e.g., STM32) may face supply chain delays in Iran.
  - **Mitigation:** Sourcing alternative microcontrollers (e.g., RP2350 or ESP32) and maintaining a buffer stock of critical components.
- **Risk:** The TinyML model might not achieve the desired accuracy on real data.
  - **Mitigation:** Continuous retraining of the model using the MIT-BIH dataset and implementing human-in-the-loop validation.

## 2. Regulatory Risks
- **Risk:** Delays in obtaining medical device approval (IRC) from the Ministry of Health.
  - **Mitigation:** Hiring a regulatory consultant early in the process and starting clinical trials as soon as the prototype is ready.

## 3. Financial Risks
- **Risk:** Running out of funding before commercialization.
  - **Mitigation:** Applying for multiple grants simultaneously (Khwarizmi Award, University of Zanjan grants) and pitching to MedTech VCs.

## 4. Market Risks
- **Risk:** Doctors might be hesitant to trust an AI-based medical device.
  - **Mitigation:** Conducting workshops for doctors to demonstrate the device's accuracy and emphasizing that the final medical decision always remains with the physician.

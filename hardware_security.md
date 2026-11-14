# Hardware Security Architecture

This document outlines the security measures implemented at the hardware level to protect the BioSignal device from tampering and cyber-attacks.

## 1. Secure Boot
- **Mechanism:** The STM32 microcontroller uses a Secure Boot process. Before executing the firmware (C code), the hardware verifies the digital signature of the code.
- **Benefit:** Prevents attackers from flashing malicious firmware onto the device.

## 2. Hardware Cryptography
- **Mechanism:** The BLE module uses a hardware-based AES-128 encryption engine.
- **Benefit:** Ensures that the wireless transmission of alerts cannot be intercepted or decrypted by unauthorized devices.

## 3. Tamper Detection
- **Mechanism:** The device enclosure includes a physical tamper switch. If the case is opened without authorization, the device wipes the encryption keys and stops functioning.
- **Benefit:** Protects patient data if the device is stolen.

## 4. Debug Port Protection
- **Mechanism:** The JTAG/SWD debug ports on the STM32 are permanently disabled (locked) in the final production version.
- **Benefit:** Prevents attackers from reading the memory or injecting code via physical access to the board.

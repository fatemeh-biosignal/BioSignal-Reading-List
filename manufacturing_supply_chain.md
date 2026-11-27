# Manufacturing & Supply Chain Plan

This document outlines the strategy for sourcing components, manufacturing the device, and mitigating supply chain risks.

## 1. Sourcing Strategy (تأمین قطعات)
To avoid the "single point of failure," we will use a dual-sourcing strategy for critical components:
- **Microcontroller (MCU):** Primary choice is the STM32F4. The secondary/alternative is the RP2040 or ESP32 (in case of shortages).
- **Analog Front-End (AFE):** Primary choice is the AD8232. Alternative is the ADS1299 (higher cost, but more features).
- **Suppliers:** Sourcing directly from authorized distributors (Mouser, Digi-Key) for the prototype phase. For mass production, we will negotiate directly with manufacturers or local Iranian distributors to bypass sanctions.

## 2. Manufacturing Phases (مراحل تولید)
### Phase 1: In-House Prototyping (Current)
- PCB assembly done manually or via local quick-turn services.
- Enclosure manufactured using 3D printing (SLA/DLP).
- Batch size: 1 to 5 units.

### Phase 2: Small Batch Production (Pilot)
- **Contract Manufacturer (CM):** Partnering with a local PCBA (PCB Assembly) company in Iran (e.g., in Tehran or Isfahan).
- **Enclosure:** Soft tooling / CNC machining for a more professional look.
- **Batch size:** 50 to 100 units (for clinical trials).

### Phase 3: Mass Production
- **Injection Molding:** For the plastic enclosure.
- **Automated SMT Lines:** For high-speed, high-precision PCB assembly.
- **Batch size:** 1,000+ units.

## 3. Quality Control in Manufacturing
- **In-Circuit Testing (ICT):** Testing the bare PCB for short circuits before soldering components.
- **Functional Testing (FCT):** Every assembled device must be connected to a signal generator to verify ECG acquisition and BLE transmission before packaging.
- **Traceability:** Every batch will have a unique serial number linked to the manufacturing date and component lot numbers.

## 4. Supply Chain Risk Mitigation (مدیریت ریسک)
- **Component Shortages:** Maintaining a buffer stock of critical components (e.g., 3 months' worth of MCUs).
- **Sanctions & Customs:** Working with local medical device regulators to secure import licenses for specialized AFEs, while simultaneously designing a locally-sourced alternative for the future.

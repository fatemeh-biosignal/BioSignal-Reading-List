# Reading Log

A personal log of papers I read, with short summaries and key takeaways.

---

## Template

**Title:**  
**Authors:**  
**Year:**  
**Link:**  
**Status:** 📖 Reading / ✅ Read  
**Key idea:**  
**Why it matters for my project:**  
**Questions I have:**

---

## Entries

### October 16, 2026
**Title:** PhysioEdge: Multimodal Compressive Sensing Platform for Wearable Health

**Authors:**  Rens Baeyens, Dennis Laurijssen, Jan Steckel, Walter Daems

**Year:**  2025

**Link:** https://arxiv.org/abs/2507.07645

**Status:** 📖 Reading 

**Key idea:** A wearable platform that uses multimodal compressive sensing to acquire and process health signals efficiently.

**Why it matters:** It is directly related to my project on low-power ECG monitoring using compressive sensing.

**Questions:** How does it handle motion artifacts in wearable ECG?
---
**Summary:**  
This paper presents a custom wearable hardware platform based on the RP2350 microcontroller that uses multimodal compressive sensing to acquire cardiopulmonary sounds, ECG, EMG, PPG, and IMU data. It demonstrates reduced power consumption and efficient multi-node synchronization for wireless biomedical monitoring.

**Full Abstract:**  
The integration of compressive sensing with real-time embedded systems opens new possibilities for efficient, low-power biomedical signal acquisition. This paper presents a custom hardware platform based on the RP2350 microcontroller, tailored for synchronized multi-modal biomedical monitoring. The system is capable of capturing cardiopulmonary sounds, along with biopotential signals such as phonocardiography (PCG), electrocardiography (ECG) and electromyography (EMG), photoplethysmography (PPG), and inertial measurement unit (IMU) data for posture recognition. To ensure sample-accurate synchronization, a Sub-1GHz radio system is used across multiple nodes. Wi-Fi and Bluetooth connectivity enable centralized data aggregation. Experimental results demonstrate the achieved decrease in power consumption when using compressive sensing, efficient multi-node synchronization, and scalability for wireless biomedical monitoring applications. The compact form factor and low-cost design make it suitable for various medical applications, including remote healthcare and long-term monitoring.
**My Notes after reading:**
- **Problem:** Continuous health monitoring outside hospitals is limited by battery life, power consumption, and the need to transmit large amounts of data.
- **Hardware used:** RP2350 microcontroller with a Sub-1GHz radio system for synchronization.
- **Key Result:** Using multimodal compressive sensing significantly decreased power consumption and enabled efficient multi-node synchronization for wireless monitoring.
- **Relation to my project:** This proves that combining compressive sensing with a low-power microcontroller (like RP2350) is a practical approach for wearable ECG devices, which is exactly the core of my project idea.

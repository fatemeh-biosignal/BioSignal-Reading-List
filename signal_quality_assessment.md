# Signal Quality & Data Transparency Assessment

Inspired by recent findings in JMIR Biomedical Engineering (evaluating commercial wearables like Oura and Empatica), this document outlines BioSignal's approach to signal quality and data transparency.

## 1. The Problem with Commercial Wearables (The "Black Box")
Studies show that many commercial wearables use proprietary algorithms to process raw physiological data before exposing it to the user. 
- **Consequence:** Researchers cannot assess the true quality of the raw signal, nor can they apply their own preprocessing algorithms (e.g., for motion artifact removal).
- **Missing Data:** In controlled studies, commercial devices often miss a significant percentage of HRV data (e.g., up to 53% missing in some devices).

## 2. BioSignal's Open-Source Advantage
Unlike commercial devices, BioSignal is designed with **Data Transparency** as a core principle:
- **Raw Data Access:** The firmware will allow researchers to export raw, unfiltered ECG data for independent analysis.
- **Transparent Signal Processing:** Our pipeline (Butterworth filter, Compressive Sensing, OMP) is fully documented and open-source on GitHub. Any researcher can replicate or modify the algorithms.
- **Signal Quality Index (SQI):** We will implement an SQI algorithm that flags noisy segments (e.g., due to movement) instead of silently deleting them.

## 3. Comparison Matrix (BioSignal vs. Commercial Wearables)
| Feature | Commercial Wearables (e.g., Oura) | BioSignal (Open-Source) |
| :--- | :--- | :--- |
| **Raw Data Access** | ❌ No (Proprietary) | ✅ Yes (Open-Source) |
| **Algorithm Transparency** | ❌ Black Box | ✅ Fully Documented |
| **Motion Artifact Handling** | ❌ Hidden/Deleted | ✅ Flagged with SQI |
| **Custom Preprocessing** | ❌ Not Allowed | ✅ Allowed (Raw Data) |

## 4. Conclusion
While commercial wearables offer convenience, they lack the methodological control required for rigorous clinical research. BioSignal bridges this gap by providing a transparent, reproducible, and accessible platform for continuous cardiac monitoring.

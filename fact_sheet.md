# 📄 BioSignal Project Fact Sheet

**Project Name:** BioSignal
**Founder & Lead Researcher:** Fatemeh Karimi (Electrical Engineer)
**Goal:** Khwarizmi International Award 2027 & ICEE 2027 Conference

---

## 🎯 The Problem
Cardiovascular diseases are the leading cause of death globally. Continuous ECG monitoring is limited by **battery life** and **data privacy** concerns.

## 💡 The Solution
A low-power wearable ECG patch integrating:
1. **Compressive Sensing (CS):** Reduces data size by 70%, extending battery life.
2. **TinyML (On-Device AI):** A Random Forest classifier runs directly on the STM32 microcontroller for real-time arrhythmia detection without cloud dependency.

## 🚀 Key Metrics
- **Data Reduction:** 70% (Compression Ratio: 30%)
- **Estimated Hardware Cost:** ~$33 (Prototype)
- **AI Accuracy:** >90% (Expected on MIT-BIH)
- **Current TRL:** Level 4 (Lab Validation)

## 🛠️ Tech Stack
- **Software:** Python, NumPy, Scikit-Learn, PyWavelets.
- **Hardware:** STM32F4, AD8232 AFE, BLE Module.
- **Design Tools:** Altium Designer (PCB), Mermaid (Documentation).

## 📂 Repository Highlights
- Fully documented software pipeline (`methodology.md`).
- Complete hardware schematics and pinouts (`hardware_wiring.md`).
- Business and market analysis (`business_model_canvas.md`).
- Draft manuscript for ICEE 2027 (`full_paper_manuscript.md`).

**🌐 [English](README.md) | [فارسی](README.fa.md)**
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Focus](https://img.shields.io/badge/Focus-Biomedical_Signal_Processing-red)
![Goal](https://img.shields.io/badge/Goal-Khwarizmi_Award_2027-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Conference](https://img.shields.io/badge/Target-ICEE_2027-blueviolet)

# BioSignal Reading List

Welcome to my research repository! I am an Electrical Engineer exploring the intersection of electronics and biomedical signal processing.

## 🎯 My Project Focus
Designing a **low-power wearable ECG monitoring system** using **Compressive Sensing (CS)** and **TinyML** for on-device arrhythmia detection.
## 📑 Table of Contents
- [Project Focus](#-my-project-focus)
- [Repository Structure](#-repository-structure)
- [Current Status](#-current-status)
- [How to Run the Code](#-how-to-run-the-code)
- [License & Citation](#-license--citation)

---
## 📂 Repository Structure

Here is a categorized guide to what you can find in this repository:

### 🚀 Project Overview & Strategy
- 💡 **[Project Idea](project-idea.md)** — Overview of my proposed ECG system.
- 📝 **[Executive Summary](executive_summary.md)** — One-page overview of the problem and solution.
- ⚠️ **[Problem Statement](problem_statement.md)** — Global health challenge and our solution.
- 🔭 **[Vision](vision.md)** — Long-term roadmap (2027-2035).
- 🗺️ **[Project Roadmap](roadmap.md)** — Timeline and milestones.
- 🚀 **[Future Roadmap](future_roadmap.md)** — Path from simulation to a commercial device.
- 🏆 **[Khwarizmi Checklist](khwarizmi_checklist.md)** — Readiness checklist for the award.
- 💭 **[Brainstorming](ideas.md)** — Future ideas for the wearable ECG.
- 📈 **[TRL Assessment](technology_readiness_level.md)** — Technology readiness level (TRL 1-9).
- 📄 **[Fact Sheet](fact_sheet.md)** — One-page overview of the entire project.
- 👤 **[User Personas](user_personas.md)** — Target users and their clinical needs.
- 📋 **[To-Do List](todo_list.md)** — Immediate next steps for hardware and validation.
- 🧠 **[Project Mind Map](project_mindmap.md)** — Holistic view of hardware, software, AI, and business.
- 🌱 **[Environmental Impact](environmental_impact_plan.md)** — Sustainability and e-waste management.
- 🔬 **[Advanced Diagnostics](advanced_diagnostics_roadmap.md)** — Future roadmap for AI-assisted medical imaging.

### 💻 Software & Algorithms
- 🚀 **[Main Pipeline](main.py)** — The main script to run the entire project.
- 🐍 **[Python Basics](python-basics.md)** — My journey learning Python.
- 🗺️ **[Python Roadmap](python_roadmap.md)** — Step-by-step learning journey.
- 📥 **[ECG Simulation](ecg_simulation.py)** — First Python script for signal simulation.
- 📥 **[Load Real Data](load_real_data.py)** — Simulating MIT-BIH datasets.
- 🌊 **[Advanced Filtering](advanced_filtering.py)** — Butterworth bandpass filter.
- 〰️ **[Wavelet Analysis](wavelet_analysis.py)** — Applying Wavelet Transform.
- 📉 **[Compressed Sensing Demo](compressed_sensing_demo.py)** — Core algorithm for data compression.
- 🔄 **[Reconstruction Demo](reconstruction_demo.py)** — Recovering signals from compressed samples.
- 🧠 **[OMP Algorithm](omp_reconstruction.py)** — Advanced signal reconstruction.
- 📊 **[Performance Evaluation](performance_evaluation.py)** — Comparing OMP vs. Linear Interpolation.
- ❤️ **[R-Peak Detection](r_peak_detection.py)** — Heart rate calculation.
- 🚨 **[Heart Rate Alert](heart_rate_alert.py)** — Medical alert logic for Bradycardia/Tachycardia.
- 🫀 **[Real ECG Analysis](real_ecg_analysis.py)** — Signal filtering and noise removal.
- 🖥️ **[GUI Dashboard](gui_dashboard.py)** — Graphical user interface for demos.
- 🧪 **[Test Pipeline](test_pipeline.py)** — Unit tests for the code.
- ⚙️ **[Requirements](requirements.txt)** — Dependencies for running the code.
- ⚙️ **[Setup Guide](setup_guide.md)** — Instructions for setting up the environment.
- 🏗️ **[Software Design](software_design.md)** — Architecture of the Python modules.
- 📊 **[Data Dictionary](data_dictionary.md)** — Definitions of all data fields and types.
- 🔌 **[API Specification](api_specification.md)** — RESTful API endpoints for app-server communication.

### 🧠 AI & Machine Learning
- 🤖 **[TinyML Classifier](tinyml_classifier.py)** — Machine learning model for arrhythmia detection.
- 📊 **[TinyML Results](tinyml_results.md)** — Performance of the ML model.
- 🧮 **[Math Model](math_model.md)** — Mathematical foundations of CS.
- 🧠 **[Key Concepts](concepts.md)** — Theoretical foundations.
- 🃏 **[Model Card](model_card.md)** — Details and limitations of the ML model.
- ⚙️ **[TinyML Optimization](tinyml_optimization.md)** — Techniques for running AI on microcontrollers.

### 🔌 Hardware & Embedded Systems
- 💻 **[Embedded C Code](embedded_c_code.c)** — C implementation for microcontrollers.
- 🔌 **[Hardware Specs](hardware_specs.md)** — Bill of Materials for the prototype.
- ⚡ **[Circuit Schematic](circuit_schematic.md)** — Block-level electrical connections.
- 🔌 **[Hardware Wiring](hardware_wiring.md)** — Block diagram of hardware connections.
- 📌 **[Hardware Pinout](hardware_pinout.md)** — Pin mapping between STM32 and AD8232.
- 🛠️ **[PCB Design Plan](pcb_design_plan.md)** — Roadmap for Altium Designer.
- 🛠️ **[Board Test Plan](board_test_plan.md)** — Step-by-step hardware validation.
- 💰 **[BOM Estimate](bom_estimate.md)** — Bill of Materials and cost estimation.
- 🏗️ **[System Architecture](system_architecture.md)** — High-level overview of HW/SW layers.
- 🛡️ **[Hardware Security](hardware_security.md)** — Secure boot and tamper detection.
- 🛠️ **[Reliability & Maintenance](reliability_maintenance.md)** — Product lifecycle plan.
- ⚙️ **[Firmware Architecture](firmware_architecture.md)** — STM32 bare-metal software design.
- 🧬 **[Next-Gen Biosensors](next_gen_biosensors.md)** — Future roadmap for biomarker detection.
- 🛠️ **[Assembly Guide](assembly_guide.md)** — Step-by-step PCB soldering and testing.
- 📊 **[Hardware Validation](hardware_validation_metrics.md)** — Metrics for testing the physical prototype.
  - 📱 **[Mobile App UI/UX](mobile_app_ui_design.md)** — Design and user flow for the patient and doctor apps.
- 🔄 **[Data Flow Sequence](data_flow_sequence.md)** — Step-by-step interaction between hardware and software.
- 🐞 **[Hardware Debugging](hardware_debugging_guide.md)** — Troubleshooting guide for the physical prototype.
- 🛡️ **[Threat Model](cybersecurity_threat_model.md)** — STRIDE analysis and cybersecurity mitigations.
- 📐 **[Mechanical Design](mechanical_design.md)** — Enclosure materials and ergonomics.
- 🧬 **[Multi-Modal Sensing](multimodal_sensing_strategy.md)** — Future strategy for combining ECG, PPG, and ACC data.

### 🩺  Medical & Clinical
- 🩺 **[Clinical Roadmap](clinical_roadmap.md)** — Steps for clinical validation.
- 🏥 **[Clinical & Safety](clinical_safety.md)** — Medical standards (IEC 60601, ISO 10993).
- 🏥 **[Medical Data Standard](medical_data_standard.md)** — HL7 FHIR integration.
- 🧑‍⚕️ **[Patient Journey](patient_journey.md)** — UX map of the patient experience.
- ⚖️ **[Ethical Framework](ethical_framework.md)** — AI ethics and patient rights.
- ⚠️ **[Risk Analysis](risk_analysis.md)** — FMEA and safety mitigation strategies.
- 📋 **[Clinical Trial Protocol](clinical_trial_protocol.md)** — Design for the human pilot study.
- 🧠 **[EEG Integration](eeg_integration.md)** — Future roadmap for brain signal monitoring.
- 📋 **[QMS Plan](qms_plan.md)** — Quality Management System based on ISO 13485.
- 🔗 **[Traceability Matrix](traceability_matrix.md)** — Mapping requirements to test cases.
- 🌐 **[Cardiovascular Tech Landscape](cardiovascular_tech_landscape.md)** — Positioning BioSignal in the broader MedTech ecosystem.
- 📋 **[Patient Onboarding SOP](patient_onboarding_sop.md)** — Standard procedure for clinical trial enrollment.
- 🧑‍⚕️ **[Usability Engineering](usability_engineering_plan.md)** — IEC 62366 human factors plan.
- ✍️ **[Informed Consent Template](informed_consent_template.md)** — Ethical consent form for clinical trials.
- 🚨 **[Post-Market Surveillance](post_market_surveillance.md)** — Plan for monitoring device safety after release.
- ⌚ **[Wearable Tech Comparison](wearable_tech_comparison.md)** — Comparing ECG patches with smart rings and watches.
- 😴 **[Sleep & PPG Integration](sleep_and_ppg_integration.md)** — Roadmap for sleep staging and stress monitoring.
- 🧠 **[BCI & Neuroethics](bci_neuroethics_roadmap.md)** — Future roadmap for brain monitoring and mental privacy.
- 📊 **[Signal Quality](signal_quality_assessment.md)** — Why BioSignal's open-source data is better than commercial black boxes.
- 🧪 **[Biocompatibility Testing](biocompatibility_testing_plan.md)** — ISO 10993 plan for safe skin contact.
  
### 📊 Business & Commercialization
- 💼 **[Business Model](business_model.md)** — Value proposition and revenue streams.
- 📈 **[Business Model Canvas](business_model_canvas.md)** — Visual summary of the model.
- 📊 **[Market Analysis](market_analysis.md)** — Target market and value proposition.
- ⚖️ **[Competitive Analysis](competitive_analysis.md)** — Comparison with existing solutions.
- 💎 **[Value Proposition](value_proposition.md)** — Why choose BioSignal.
- 🎯 **[GTM Strategy](go_to_market_strategy.md)** — Marketing and sales roadmap.
- 💰 **[Revenue Model](revenue_model.md)** — Financial strategy and streams.
- 💵 **[Fundraising Strategy](fundraising_strategy.md)** — Investment phases.
- 📊 **[Cost-Benefit Analysis](cost_benefit_analysis.md)** — Economic justification.
- 📦 **[Packaging Design](packaging_design.md)** — Unboxing experience.
- 📜 **[Patent Strategy](patent_strategy.md)** — Plan for protecting novel aspects.
- 🛡️ **[Intellectual Property](intellectual_property.md)** — Patent and open-source licensing.
- 📈 **[Scalability Plan](scalability_plan.md)** — Strategy for mass production.
- 👥 **[Team Structure](team_structure.md)** — Roles and organizational chart.
- 📋 **[Execution Plan](project_execution_plan.md)** — Actionable steps and budget.
- 🚧 **[Risk Management](risk_management_plan.md)** — Risk mitigation.
- 🔄 **[User Feedback Plan](user_feedback_plan.md)** — Strategy for collecting feedback and iterating.
- 📊 **[SWOT Analysis](swot_analysis.md)** — Strategic analysis of strengths and threats.
- 🎓 **[Training & Support](training_support_plan.md)** — Strategy for training doctors and supporting patients.
- 🏭 **[Manufacturing Plan](manufacturing_supply_chain.md)** — Sourcing strategy and production phases.

### 📚 Research & Publications
- ✍️ **[Paper Abstract](paper_abstract.md)** — Draft for ICEE 2027.
- 📄 **[Paper Draft](paper_draft.md)** — Full structure for the paper.
- ✍️ **[Introduction Draft](paper_introduction_draft.md)** — Introduction section.
- 📖 **[Related Work Draft](paper_related_work.md)** — Literature review section.
- 🛠️ **[Methodology Draft](paper_methodology_draft.md)** — Methodology section.
- 📈 **[Results & Discussion](results_and_discussion.md)** — Results section.
- 🏁 **[Conclusion](conclusion.md)** — Summary of achievements.
- 📚 **[References](references.md)** — IEEE formatted bibliography.
- 📚 **[Literature Review](literature_review.md)** — Summary of related works.
- 📚 **[Reading Log](reading-log.md)** — Summaries of papers I read.
- 📄 **[Papers List](papers.md)** — Collection of relevant papers.
- 📝 **[Publication Guide](publication_guide.md)** — IEEE formatting rules.
- 🖼️ **[Scientific Poster](scientific_poster.md)** — Layout for the conference.
- 🎤 **[Presentation Outline](presentation_outline.md)** — Slide-by-slide pitch.
- 🖼️ **[Graphical Abstract](graphical_abstract.md)** — Visual summary.
- 🔬 **[Experimental Setup](experimental_setup.md)** — Hardware/Software environment.
- ⚠️ **[Threats to Validity](threats_to_validity.md)** — Scientific limitations.
- 🏆 **[Contributions](contributions.md)** — Key scientific achievements.
- ✍️ **[Authorship Guidelines](authorship_guidelines.md)** — ICMJE standards.
- 🏁 **[Conclusion Draft](paper_conclusion_draft.md)** — Final section of the ICEE paper.
- 📑 **[Full Manuscript](full_paper_manuscript.md)** — Master template linking all paper sections.
- 🎬 **[Demo Script](demo_script.md)** — 2-minute video presentation script.
- 🛡️ **[Reviewer Rebuttal Plan](reviewer_rebuttal_plan.md)** — Preparation for ICEE peer-review questions.

### 🌍 Community & Standards
- 🤝 **[Contributing](CONTRIBUTING.md)** — Guidelines for open-source contributions.
- 🤝 **[Contributors Guide](CONTRIBUTORS.md)** — Coding standards and Git workflow.
- 🤝 **[Code of Conduct](CODE_OF_CONDUCT.md)** — Ethical standards.
- 📜 **[Changelog](CHANGELOG.md)** — Version history.
- 📝 **[Citation](CITATION.cff)** — Academic citation format.
- 📑 **[Documentation](documentation.md)** — Technical overview of modules.
- 🗄️ **[Data Management Plan](data_management_plan.md)** — Data privacy guidelines.
- 📊 **[Data Availability](data_availability.md)** — Statement on data access.
- 🌐 **[Emerging Tech](emerging_tech_integration.md)** — 6G, GenAI, Digital Twins.
- 🌍 **[Social Impact](social_impact.md)** — Healthcare and economic impact.

### 📝 General & Notes
- 📖 **[Glossary](glossary.md)** — Medical and technical terms.
- 📝 **[Daily Notes](notes.md)** — My daily research thoughts.
- 📈 **[Results Summary](results_summary.md)** — Numerical results.
- 🏆 **[AI Competitions](ai_competitions.md)** — Future AI challenges.
- 🖼️ **[Project Visuals](visuals.md)** — Planned plots.
- ❓ **[FAQ](faq.md)** — Frequently asked questions.
- 🚀 **[Pitch Summary](pitch_summary.md)** — Quick overview.

## 🚀 How to Run the Code

If you want to run the Python scripts in this repository:
1. Make sure you have Python installed.
2. Install the required libraries by running:
   `pip install -r requirements.txt`
3. Run the ECG simulation script:
   `python ecg_simulation.py`
4. Run the Compressive Sensing demo:
   `python compressed_sensing_demo.py`

## 🌱 Current Status
- 🧪 Actively building my foundation in Biomedical Signal Processing and embedded systems.
- 📅 Preparing a research proposal for the Khwarizmi International Award (submission in Fall 2027).
- 🎤 Preparing a paper for the 33rd Iranian Conference on Electrical Engineering (ICEE 2027) in May 2027.

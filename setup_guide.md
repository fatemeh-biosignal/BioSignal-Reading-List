# Developer Setup Guide

This document provides step-by-step instructions on how to set up the development environment for the BioSignal project.

## 1. Software Requirements
- **Python:** Version 3.9 or higher.
- **C Compiler:** GCC (for embedded C code).
- **IDE:** VS Code (recommended for Python) or STM32CubeIDE (for C code).

## 2. Python Environment Setup
It is highly recommended to use a virtual environment to avoid dependency conflicts.
### Step 1: Clone the repository
```bash
git clone https://github.com/fatemeh-biosignal/BioSignal-Reading-List.git
cd BioSignal-Reading-List
```
### Step 2: Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run the main pipeline
```bash
python main.py
```

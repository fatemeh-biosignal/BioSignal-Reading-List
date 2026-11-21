# TinyML Optimization Techniques

This document outlines the techniques used to optimize the Machine Learning model for deployment on the resource-constrained STM32 microcontroller.

## 1. The Challenge
The STM32F4 microcontroller has limited Flash memory (1MB) and RAM (192KB). A standard Random Forest model or a Deep Neural Network trained in Python cannot be directly deployed on this hardware.

## 2. Optimization Strategies

### 2.1. Model Quantization (محدودسازی دقت)
- **Concept:** Converting the 32-bit floating-point numbers (weights and biases) into 8-bit integers (INT8).
- **Benefit:** Reduces the model size by 75% and speeds up inference, while maintaining high accuracy.
- **Tool:** TensorFlow Lite for Microcontrollers (TFLM) or Scikit-Learn's quantization tools.

### 2.2. Feature Reduction
- **Concept:** Instead of feeding the model all 250 time points of an ECG heartbeat, we extract the most important features (e.g., R-peak amplitude, RR interval).
- **Benefit:** Drastically reduces the input vector size, requiring less RAM and fewer computations.

### 2.3. Fixed-Point Arithmetic (محاسبات ممیز ثابت)
- **Concept:** Avoiding floating-point math (which is slow and power-hungry on some MCUs) and using integer math instead.
- **Benefit:** Significantly reduces power consumption and latency on the STM32.

### 2.4. Code Generation (تولید کد C)
- **Concept:** The trained Python model is converted into a C header file (`.h`) containing the model weights as an array.
- **Benefit:** The C code runs directly on the microcontroller without needing a Python interpreter.

## 3. Expected Outcomes
- **Model Size:** < 100 KB (fits easily in Flash memory).
- **RAM Usage:** < 20 KB.
- **Inference Time:** < 50 ms per heartbeat.

# Frequently Asked Questions (FAQ)

## 1. Why did you use Compressive Sensing (CS)?
Because traditional ECG devices send all raw data, which drains the battery quickly. CS allows us to keep only 30% of the data without losing the important information, significantly extending battery life.

## 2. Why TinyML and not Cloud AI?
Sending raw ECG data to the cloud requires a constant internet connection and raises privacy concerns. TinyML runs the AI model directly on the device (on-device inference), which is faster, more private, and uses less power.

## 3. What is the target price for this device?
Since it uses low-cost components (like the AD8232 and STM32), the estimated manufacturing cost is very low. This makes it affordable for widespread use in developing countries like Iran.

## 4. How accurate is the Arrhythmia detection?
Based on our synthetic tests, the Random Forest classifier is highly accurate. However, the next step is to validate it on the real MIT-BIH database to ensure clinical accuracy.

## 5. Is it comfortable to wear?
Yes, the device is designed as a small patch using biocompatible materials. The low-power design means it doesn't get hot, making it comfortable for 24/7 wear.

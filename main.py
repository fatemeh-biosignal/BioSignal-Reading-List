# main.py
# The main execution script for the BioSignal project.
# This script runs the entire pipeline from signal generation to AI classification.

import numpy as np
import matplotlib.pyplot as plt
from ecg_processor import ECGProcessor
from tinyml_classifier import generate_synthetic_ecg_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def run_full_pipeline():
    print("="*50)
    print("🚀 STARTING BIOSIGNAL PROJECT PIPELINE 🚀")
    print("="*50)

    # --- STEP 1: Signal Processing (Using OOP) ---
    print("\n[STEP 1] Processing ECG Signal...")
    processor = ECGProcessor(duration=5, sampling_rate=250)
    raw = processor.generate_signal()
    filtered = processor.apply_moving_average_filter()
    idx, compressed = processor.compress_signal(compression_ratio=0.3)
    
    print(f"✅ Signal Processed. Compressed to {len(compressed)} samples.")

    # --- STEP 2: AI Classification (TinyML) ---
    print("\n[STEP 2] Training AI Model for Arrhythmia Detection...")
    X, y = generate_synthetic_ecg_data(num_samples=500) # Smaller dataset for quick execution
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"✅ AI Model Trained. Accuracy: {accuracy * 100:.2f}%")

    # --- STEP 3: Final Visualization ---
    print("\n[STEP 3] Generating Final Dashboard...")
    plt.figure(figsize=(12, 8))
    
    # Plot Raw Signal
    plt.subplot(2, 2, 1)
    plt.plot(processor.time, raw, color='gray')
    plt.title("Raw Signal (With Noise)")
    plt.grid(True)
    
    # Plot Filtered Signal
    plt.subplot(2, 2, 2)
    plt.plot(processor.time, filtered, color='blue')
    plt.title("Filtered Signal")
    plt.grid(True)
    
    # Plot Compressed Samples
    plt.subplot(2, 2, 3)
    plt.plot(processor.time, filtered, color='lightblue', alpha=0.5)
    plt.scatter(processor.time[idx], compressed, color='red', s=10)
    plt.title("Compressed Sensing (30%)")
    plt.grid(True)
    
    # Plot Feature Importances
    plt.subplot(2, 2, 4)
    plt.plot(model.feature_importances_[:20], color='green')
    plt.title("AI Model: Feature Importance")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*50)
    print("🎉 PIPELINE EXECUTED SUCCESSFULLY! 🎉")
    print("="*50)

if __name__ == "__main__":
    run_full_pipeline()

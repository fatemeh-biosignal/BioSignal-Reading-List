# tinyml_classifier.py
# A simple demonstration of applying Machine Learning to ECG data.
# This is the first step towards implementing TinyML for arrhythmia detection.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def generate_synthetic_ecg_data(num_samples=1000):
    """
    Generates synthetic ECG data with two classes:
    0 = Normal Heartbeat
    1 = Arrhythmia (Simulated by a different frequency)
    """
    X = []
    y = []
    
    for _ in range(num_samples):
        t = np.linspace(0, 1, 100) # 1 second window
        noise = np.random.randn(100) * 0.1
        
        if np.random.rand() > 0.5:
            # Normal beat (base frequency)
            signal = np.sin(2 * np.pi * 1.2 * t) + noise
            y.append(0)
        else:
            # Arrhythmia (higher frequency)
            signal = np.sin(2 * np.pi * 2.5 * t) + noise
            y.append(1)
            
        X.append(signal)
        
    return np.array(X), np.array(y)

if __name__ == "__main__":
    print("--- TinyML Classifier Demo ---")
    
    # 1. Generate Data
    print("Generating synthetic ECG data...")
    X, y = generate_synthetic_ecg_data(1000)
    
    # 2. Split Data into Training and Testing sets (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training samples: {len(X_train)} | Testing samples: {len(X_test)}")
    
    # 3. Train a Random Forest Classifier (A lightweight ML model suitable for TinyML)
    print("Training the Random Forest model...")
    model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate the Model
    print("Evaluating the model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Normal", "Arrhythmia"]))
    # --- Visualizing Feature Importance ---
    print("\nPlotting feature importances...")

    # Get feature importances from the Random Forest model
    importances = model.feature_importances_

    # Plot the top 20 important features
    plt.figure(figsize=(10, 4))
    plt.plot(importances[:20], color='orange', marker='o', linestyle='dashed')
    plt.title("Feature Importances (Top 20 time points)")
    plt.xlabel("Time Index within the beat")
    plt.ylabel("Importance")
    plt.grid(True)
    plt.show()

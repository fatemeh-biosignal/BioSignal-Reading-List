# gui_dashboard.py
# A simple GUI dashboard to visualize the ECG signal processing.
# This is a prototype for the final demo to be presented to judges.

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_mock_ecg():
    t = np.linspace(0, 5, 1000)
    signal = np.sin(2 * np.pi * 1.2 * t) + 0.1 * np.random.randn(len(t))
    return t, signal

def plot_signal():
    t, signal = generate_mock_ecg()
    
    # Clear previous plots
    ax.clear()
    
    # Plot new signal
    ax.plot(t, signal, color='blue')
    ax.set_title("ECG Signal (Simulated)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    
    canvas.draw()

def show_alert():
    messagebox.showwarning("Medical Alert", "🚨 Arrhythmia Detected! Please consult a doctor.")

# --- GUI Setup ---
root = tk.Tk()
root.title("BioSignal Dashboard - Wearable ECG")
root.geometry("600x500")

# Title Label
title_label = tk.Label(root, text="BioSignal: Low-Power Wearable ECG", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Matplotlib Figure
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Buttons
btn_plot = tk.Button(root, text="Generate ECG Signal", command=plot_signal, bg="lightblue")
btn_plot.pack(pady=5)

btn_alert = tk.Button(root, text="Simulate Arrhythmia Alert", command=show_alert, bg="red", fg="white")
btn_alert.pack(pady=5)

# Run the GUI
root.mainloop()

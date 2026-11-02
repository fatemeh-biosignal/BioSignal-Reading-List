# heart_rate_alert.py
# A logic module to alert the patient if the heart rate is dangerously high or low.
# This simulates the real-time decision-making of the wearable device.

def check_heart_rate(bpm):
    """
    Analyzes the heart rate and returns an alert status.
    Normal resting heart rate: 60 - 100 BPM.
    """
    print(f"Analyzing Heart Rate: {bpm:.1f} BPM")
    
    if bpm < 60:
        return "⚠️ ALERT: Bradycardia (Heart rate is too low). Consult a doctor."
    elif bpm > 100:
        return "🚨 ALERT: Tachycardia (Heart rate is too high). Potential Arrhythmia detected!"
    else:
        return "✅ NORMAL: Heart rate is within the healthy range."

if __name__ == "__main__":
    print("--- Heart Rate Alert System ---")
    
    # Test scenarios (Simulating different patients)
    test_bpms = [72.5, 45.0, 130.2]
    
    for bpm in test_bpms:
        result = check_heart_rate(bpm)
        print(result)
        print("-" * 40)

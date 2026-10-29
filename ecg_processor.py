# ecg_processor.py
# An Object-Oriented approach to handling ECG signals.
# This module encapsulates signal generation, filtering, and compression.

import numpy as np

class ECGProcessor:
    def __init__(self, duration=5, sampling_rate=250):
        self.duration = duration
        self.fs = sampling_rate
        self.time = np.linspace(0, duration, duration * sampling_rate)
        self.raw_signal = None
        self.filtered_signal = None
        
    def generate_signal(self):
        """Generates a synthetic ECG signal with noise."""
        base_signal = np.sin(2 * np.pi * 1.2 * self.time)
        noise = 0.1 * np.random.randn(len(self.time))
        self.raw_signal = base_signal + noise
        return self.raw_signal

    def apply_moving_average_filter(self, window_size=5):
        """Applies a moving average filter to remove high-frequency noise."""
        if self.raw_signal is None:
            raise ValueError("Signal not generated yet. Run generate_signal() first.")
            
        self.filtered_signal = np.convolve(
            self.raw_signal, 
            np.ones(window_size)/window_size, 
            mode='same'
        )
        return self.filtered_signal

    def compress_signal(self, compression_ratio=0.3):
        """Simulates Compressive Sensing by keeping a percentage of samples."""
        if self.filtered_signal is None:
            raise ValueError("Signal not filtered yet. Run apply_moving_average_filter() first.")
            
        n_samples = len(self.filtered_signal)
        n_measurements = int(n_samples * compression_ratio)
        
        indices = np.random.choice(n_samples, n_measurements, replace=False)
        compressed_signal = self.filtered_signal[indices]
        
        return indices, compressed_signal

# Example usage (for testing)
if __name__ == "__main__":
    print("--- Testing ECGProcessor Class ---")
    
    # 1. Initialize the processor
    processor = ECGProcessor(duration=5, sampling_rate=250)
    
    # 2. Generate and filter
    raw = processor.generate_signal()
    filtered = processor.apply_moving_average_filter()
    
    # 3. Compress
    idx, compressed = processor.compress_signal()
    
    print(f"Original samples: {len(raw)}")
    print(f"Compressed samples: {len(compressed)}")
    print("Class executed successfully. Ready for integration.")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("outputs/plots", exist_ok=True)

np.random.seed(42)

time = np.arange(0, 100, 0.1)
signal = np.sin(time) + np.random.normal(0, 0.2, len(time))

# Create labels (0 = normal, 1 = fault)
label = np.zeros(len(signal))

# Spike fault
signal[300:310] += 3
label[300:310] = 1

# Drift fault
signal[700:] += np.linspace(0, 2, len(signal[700:]))
label[700:] = 1

df = pd.DataFrame({
    "time": time,
    "signal": signal,
    "fault": label
})

df.to_csv("data/sensor_data.csv", index=False)

# Plot with faults highlighted
plt.figure(figsize=(10,5))
plt.plot(time, signal, label="Signal")
plt.scatter(time[label==1], signal[label==1], color='red', label="Fault")
plt.legend()
plt.title("Sensor Signal with Fault Labels")
plt.savefig("outputs/plots/signal.png")
plt.show()
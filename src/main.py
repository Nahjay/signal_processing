import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create a time array from 0 to 1 with step size 0.01
t = np.arange(0, 1, 0.01)

# Generate a sine wave with frequency 1 Hz for the original signal
x_orig = np.sin(2 * np.pi * t)

# Generate a second sine wave with frequency 2 Hz for the filtered signal
x_filt = np.sin(4 * np.pi * t)

# Define the filter
b, a = signal.butter(4, 0.2, 'low')

# Apply the filter to the second sine wave
y_filt = signal.filtfilt(b, a, x_filt)

# Create a figure and axis objects for the original signal plot
fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=100)
ax1.plot(t, x_orig, label='Original')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.set_xlim([0, 1])
ax1.set_ylim([-1.2, 1.2])
ax1.legend()

# Create a figure and axis objects for the filtered signal plot
fig2, ax2 = plt.subplots(figsize=(8, 4), dpi=100)
ax2.plot(t, y_filt, label='Filtered')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
ax2.set_xlim([0, 1])
ax2.set_ylim([-1.2, 1.2])
ax2.legend()

# Display both plots
plt.show()
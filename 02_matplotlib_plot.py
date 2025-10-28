# plotting in python
# subplots
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.cos(2 * np.pi * 5 * t)

# Create the first subplot
plt.subplot(2, 1, 1) # (2 rows, 1 column, 1st plot)
plt.plot(t, x1)
plt.title("Sine Wave")
plt.ylabel("Amplitude")

# Create the second subplot
plt.subplot(2, 1, 2) # (2 rows, 1 column, 2nd plot)
plt.plot(t, x2)
plt.title("Cosine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout() # Adjusts plots to prevent titles/labels from overlapping
plt.show()

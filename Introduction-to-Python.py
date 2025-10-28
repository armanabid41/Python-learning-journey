#variable type
List (list): Ordered, mutable (changeable)
marks = [85, 90.1, 78, 'A']
marks[0] = 95 # list can be modified
print(type(marks)) # <class 'list'>
print(marks)

#plotting in python
#subplots
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.cos(2 * np.pi * 5 * t)
plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.title("Sine Wave")
plt.subplot(2, 1, 2)
plt.plot(t, x2)
plt.title("Cosine Wave")
plt.tight_layout()
plt.show()

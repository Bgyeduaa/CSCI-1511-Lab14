"""
Program Name: Lab14_Bgyeduaa.py
Author: Belinda Gyeduaa
Purpose: To plot a sine wave using matplotlib with style customizations.
Date: August 5, 2025
"""

import math
import matplotlib.pyplot as plt

# Create lists for x (in degrees) and y (sine values)
x_values = list(range(0, 361))  # 0 to 360 degrees
y_values = [math.sin(math.radians(x)) for x in x_values]

# Plotting the sine wave
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, linestyle='--', linewidth=2.5, color='purple', marker='o', markersize=3)

# Label the graph
plt.title("Sine Wave: y = sin(x)")
plt.xlabel("Degrees")
plt.ylabel("sin(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.show()

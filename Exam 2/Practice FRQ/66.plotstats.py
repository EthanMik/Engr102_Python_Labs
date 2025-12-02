import matplotlib.pyplot as plt
import numpy as np
from math import *

def compute(x_values: list[float], sigma: float, mew: float):
    computed_nums = []

    for x in x_values:
        output = (1 / (sqrt(2 * pi * sigma**2))) * e**((-(x - mew)**2) / (2 * sigma**2))
        computed_nums.append(output)
    return computed_nums

x = np.arange(50)
y_values = compute(x, 1, 1)
plt.plot(x, y_values)
plt.title("Probability Plot")
plt.ylabel("Probabilty")
plt.xlabel("x")
plt.show()
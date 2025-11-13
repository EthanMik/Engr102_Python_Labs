# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import numpy as np
import matplotlib.pyplot as plt

point = np.array([0, 1])
matrix = np.array([[1.02, 0.095],
                   [-0.095, 1.02]])

x = np.zeros(250)
y = np.zeros(250)

vector = matrix @ point
for i in range(len(x)):
    x[i] = vector[0]
    y[i] = vector[1]
    vector = matrix @ vector


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spiral Graph')
plt.show()
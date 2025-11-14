    # By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import matplotlib.pyplot as plt
import numpy as np
import math

def plot1():
    domain = (-2.0, 2.0)
    x = np.linspace(domain[0], domain[1])

    f = 2
    plt.plot(x, ((4 * f)**-1) * x**2, "r", linewidth=2, label='f=2')
    f = 6
    plt.plot(x, ((4 * f)**-1) * x**2, "b", linewidth=6, label='f=6')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Parabola plots with varying focal length')
    plt.legend()
    plt.figure()

def plot2():
    domain = (-4.0, 4.0)

    x = np.linspace(domain[0], domain[1], 25)

    plt.plot(x, 2*x**3 + 3*x**2 - 11*x - 6, 
            'y*',
            markersize=10,
            markeredgecolor="black", 
            markeredgewidth=.8)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Plot of cubic polynomial')
    plt.figure()

def plot3():

    domain = (-2 * math.pi, 2 * math.pi)

    x = np.linspace(domain[0], domain[1])

    plt.subplot(211)
    plt.plot(x, np.cos(x), 'maroon', label="cos(x)")
    plt.yticks([-1, 0, 1])
    plt.grid(True)
    plt.legend(loc='lower right')
    plt.ylabel('y=cos(x)')

    plt.subplot(212)
    plt.plot(x, np.sin(x), 'gray', label='sin(x)')
    plt.ylabel('y=sin(x)')
    plt.legend(loc='upper right')
    plt.suptitle('Plot of cos(x) and sin(x)')
    plt.yticks([-1, 0, 1])
    plt.xlabel('x')
    plt.grid(True)

plot1()
plot2()
plot3()
plt.show()


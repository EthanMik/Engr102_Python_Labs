# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from math import *

# Demonstrate roundoff error

a = 1.0 / 7.0
print(f"a = {a}")

b = a * 7
print(f"b = a * 7 = {b}")

f = 2 * a + 5 * a
print(f"f = 2 * a + 5 * a = {f}")

x = f / sqrt(3)
print(f"x = {x}")

y = x * x * 3
print(f"y = x * x * 3 = {y:.1f}")

z = x * 3 * x
print(f"z = x * 3 * x = {z}")

bf = abs(b - f) < 1e-10 
print(f"b and f are equal within tolerance of 1e-10")

yz = abs(y - z) < 1e-10 
print(f"y and z are equal within tolerance of 1e-10")

m = 0.1
print(f"m = {m}")

n = 3 * m
print(f"n = 3 * m = {n:.1f} {n == 0.3}")

p = 7 * m
print(f"p = 7 * m = {p:.1f} {p == 0.7}")

q = n + p
print(f"q = n + p = {q:.0f} {q == 1}")
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import numpy as np

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

print(f"A = {A}\n")
print(f"B = {B}\n")
print(f"C = {C}\n")

D = A @ B @ C

print(f"D = {D}\n")

print(f"D^T = {D.T}\n")

E = (np.sqrt(D) * 1/2)

print(f"E = {E}\n")
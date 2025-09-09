# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# Calculate roots

import math
import sys

# a = 0
# b = 2
# c = 3

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

if a == 0 and b == 0:
    print(f"You entered an invalid combination of coefficients!")
    sys.exit(0)

if (a == 0):
    print(f"The root is x = {(-c / b):.1f}")
    sys.exit(0)

x1 = 0
x2 = 0

i = 0
j = 0

j = (-b) / (2*a)

if (b**2 - 4*a*c < 0):
    i = "i"
    x1 = str(round(j, 1)) + " + 1.0i"
    x2 = str(round(j, 1)) + " - 1.0i"
else:
    i = math.sqrt(b**2 - 4*a*c) / (2*a)
    x1 = str(round(j + i, 1))
    x2 = str(round(j - i, 1))

if (i == 0):
    print(f"The root is x = {x1}")
else:
    print(f"The roots are x = {x1} and x = {x2}")



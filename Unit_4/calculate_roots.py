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
import cmath
import sys

a = 1
b = 4
c = 5

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

if a == 0 and b == 0:
    print(f"You entered an invalid combination of coefficients!")
    sys.exit(0)

x1 = 0
x2 = 0

i = 0
j = 0

append = ""

try:
    if (b**2 - 4*a*c < 0) {
        
    }
    i = math.sqrt(b**2 - 4*a*c) / (2*a)
except Exception as e:
    i = cmath.sqrt(b**2 - 4*a*c) / (2*a)

j = (-b) / (2*a)
x1 = j + i
x2 = j - i

if (i == 0):
    print(f"The root is x = {x1:.1f}")
else:
    print(f"The roots are x = {x1:.1f} and x = {x2:.1f}")



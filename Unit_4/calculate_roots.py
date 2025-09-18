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

def get_quadratic_roots(a: float, b: float, c: float) -> str:
    if a == 0 and b == 0:
        return f"You entered an invalid combination of coefficients!"
    elif a == 0:
        return f"The root is x = {(-c / b):.1f}"

    discriminant = b**2 - 4 * a * c
    axis_symmetry = -b / (2 * a)

    if (discriminant < 0):
        return f"The roots are x = {axis_symmetry:.1f} + 1.0i and x = {axis_symmetry:.1f} - 1.0i"
    
    quadratic_eq = math.sqrt(discriminant) / (2 * a)
    x1 = axis_symmetry + quadratic_eq
    x2 = axis_symmetry - quadratic_eq

    if (quadratic_eq == 0):
        return f"The root is x = {x1}"
    
    return f"The roots are x = {x1} and x = {x2}"
    
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

print(get_quadratic_roots(a, b, c))

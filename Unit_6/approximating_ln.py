# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

import math

# Compute natural log
def approx_natural_log(x: float, tolerance: float) -> float:
    natural_log = 0.0
    term = 1
    n = 1

    while abs(term) > tolerance:
        term = ((-1.0)**(n - 1.0) * (x - 1.0)**n) / n
        if abs(term) >= tolerance:
            natural_log += term
        n += 1
    return float(natural_log)

x_value = float(input("Enter a value for x: "))
while x_value <= 0 or x_value > 2:
    x_value = float(input("Out of range! Try again: "))

tolerance = float(input("Enter the tolerance: "))

approximated_ln = approx_natural_log(x_value, tolerance)
exact_ln = math.log(x_value)

print(f"ln({x_value}) is approximately {approximated_ln}")
print(f"ln({x_value}) is exactly {exact_ln}")
print(f"The difference is {abs(approximated_ln - exact_ln)}")
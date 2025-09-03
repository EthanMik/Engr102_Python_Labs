# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025


import math

tau = 2 * math.pi

precision = int(input("Please enter the number of digits of precision for tau: "))
p = 10 ** precision

# Rounding
tau = int(tau * p * 10)
if tau % 10 >= 5:
    tau = (tau // 10) + 1
else:
    tau = tau // 10

tau = tau / p
if (precision == 0):
    tau = int(tau)

print(f"The value of tau to {precision} digits is: {tau:.{precision}f}")

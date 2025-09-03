# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Follow direction
# Date:       8/27/2025
# 

import math as m

def calculate(x):
    return (1 - m.cos(x)) / (x**2)

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")

guessed_num = 0
print(f"My guess is {guessed_num}")

print(calculate(1))
print(calculate(.1))
print(calculate(.01))
print(calculate(.001))
print(calculate(.0001))
print(calculate(.00001))
print(calculate(.000001))
print(calculate(.0000001))

# How much I was off by
print(f"My guess was {abs(calculate(.0000001) - guessed_num)} off")
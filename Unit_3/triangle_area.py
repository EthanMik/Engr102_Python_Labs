# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import math

# Distance formula
def dist(a: list, b: list) -> float:
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

p1 = [0, x]
p2 = [x + y, 0]
p3 = [x, y]

a = dist(p1, p2)
b = dist(p2, p3)
c = dist(p3, p1)

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is {area:.3f}")
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from math import *

print("Part 1")
h = float(input("Enter the height of the door: "))
w = float(input("Enter the width of the door: "))

# This is wrong please someone help!!!
r = (w / 2)
rectange_area = w * (3/4) * h
circle_area = (1/4) * pi * r**2
door_area = rectange_area + circle_area
print(f"The area of the door is {door_area:.3f}\n")

print("Part 2")
h = float(input("Enter the height of the pyramid: "))

s = h * sqrt(2)
base_area = s**2
triangle_area = (sqrt(3)/4) * s**2
surface_area = base_area + 4 * triangle_area

print(f"The surface area of the pyramid is {surface_area:.2f}\n")

print("Part 3")
a = float(input("Enter the area of a triangle: "))

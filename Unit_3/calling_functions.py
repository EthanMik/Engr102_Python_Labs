# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

from math import *

def triangle_area(sides):
    return (sqrt(3)/4)*sides**2

def rectangle_area(sides):
    return sides**2

def reg_pentagon_area(sides):
    return (1/4)*sqrt(5*(5+2*sqrt(5)))*sides**2

def reg_hexagon_area(sides):
    return (3*sqrt(3)/2)*sides**2

def reg_dodecagon_area(sides):
    return 3 * (2 + sqrt(3)) * sides**2

# Compute areas
side_length = float(input("Please enter the side length: \n"))
print(f"A triangle with side {side_length:.2f} has area {triangle_area(side_length):.3f}")
print(f"A square with side {side_length:.2f} has area {rectangle_area(side_length):.3f}")
print(f"A pentagon with side {side_length:.2f} has area {reg_pentagon_area(side_length):.3f}")
print(f"A hexagon with side {side_length:.2f} has area {reg_hexagon_area(side_length):.3f}")
print(f"A dodecagon with side {side_length:.2f} has area {reg_dodecagon_area(side_length):.3f}")
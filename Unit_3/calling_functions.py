# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

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
printresult("triangle", side_length, triangle_area(side_length))
printresult("square", side_length, rectangle_area(side_length))
printresult("pentagon", side_length, reg_pentagon_area(side_length))
printresult("hexagon", side_length, reg_hexagon_area(side_length))
printresult("dodecagon", side_length, reg_dodecagon_area(side_length))
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

import math

# Return a range of vectors in between x value specified
def find_range(points: list[list[float]], x: int) -> list[list[float]]:
    for i in range(len(points) - 1):
        current_x = points[i][0]
        next_x = points[i + 1][0] 
        # If points are in range then return that range
        if x > current_x and x < next_x:
            return [points[i], points[i+1]]
        
    return None

# Interpolate using log base 10 as a scale for the y values
def interpolate_base10(points: list[list[float]], x: int):
    x0 = points[0][0]
    x1 = points[1][0]

    y0 = points[0][1]
    y1 = points[1][1]

    m = math.log10(y1 / y0) / math.log10(x1 / x0)
    value = y0 * (x / x0)**m

    return value 

# Points given to interpolate between
POINTS = [
    [1.3, 1000],
    [5, 7000],
    [30, 1.5 * 10**6],
    [120, 2.5 * 10**4],
    [1200, 1.5 * 10**6]
]

temp = float(input("Enter the excess temperature: ")) # Get user input
temp_range = find_range(POINTS, temp) # Find a range to interpolate between
if temp_range == None: print("Surface heat flux is not available") # if no range is found then dont execute code
else: print(f"The surface heat flux is approximately {interpolate_base10(temp_range, temp):.0f} W/m^2") # interpolate and find value
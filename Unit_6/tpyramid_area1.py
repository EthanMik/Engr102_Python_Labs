# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

import math

# Calcute pyramid surface area
def pyramid_surface_area(side_length: float, layers: int) -> float:
    pyramid_face_area = side_length**2 * 3 + 2 * (math.sqrt(3) / 4 * side_length**2)
    suraface_area = 0
    for i in range(1, layers + 1):
        if (i == layers):
            pyramid_face_area -= (math.sqrt(3) / 4 * side_length**2)
        suraface_area += i * pyramid_face_area
    return float(suraface_area)

side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
print(f"You need {pyramid_surface_area(side_length, layers):.2f} m^2 of gold foil to cover the pyramid") 
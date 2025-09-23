# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

def sum(a, n):
    return a * n * (n + 1) / 2

# Calcute pyramid surface area
def pyramid_surface_area(cube_length: float, layers: int) -> float:
    cube_face_area = cube_length * cube_length
    exposed_sides = 6
    surface_area = sum(exposed_sides * cube_face_area, layers - 1)
    surface_area += 5 * cube_face_area * layers
    return surface_area


side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
print(f"You need {pyramid_surface_area(side_length, layers):.2f} m^2 of gold foil to cover the pyramid") 
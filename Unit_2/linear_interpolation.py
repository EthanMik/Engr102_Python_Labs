# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Brendon Chan
# Ethan Mikolaycik
# Ruben Martinez
# Roy Liu


# Section: ENGR 353
# Assignment: THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date: 9/2/2025
#

import math

# Calculate slope
def slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)

# Interpolate between two vectors at a given time
def interpolate(time, x1, x2, y1, y2):
    return slope(y2, y1, x2, x1) * (time - x1) + y1

# Orbit radius in kilometers
orbit_radius = 6745
# Circumference of the orbit
circumference = orbit_radius * math.pi * 2

# Given points
x1 = 10
x2 = 55
y1 = 2029
y2 = 23029

# Times to interpolate
t1 = 25
t2 = 300

# Calculate positions at t = 25 and t = 300
position1 = interpolate(t1, x1, x2, y1, y2) % circumference
position2 = interpolate(t2, x1, x2, y1, y2) % circumference

# Print results
print("Part 1:")
print(f"For t = 25 minutes, the position p = {position1} kilometers")
print("Part 2:")
print(f"For t = 300 minutes, the position p = {position2} kilometers")


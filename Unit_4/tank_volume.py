# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import math

# calculate volume
def volume(H, h, r):
    v = 0

    if h <= r:
        v = (math.pi * h**2 * (3 * r - h)) / 3
    elif h > r and h < H - r:
        v = ((2 * math.pi * r**3) / 3) + (math.pi * r**2 * (h - r))
    elif h > H - r:
        v = ((4 * math.pi * r**3) / 3) + (math.pi * r**2 * (H - (2 * r))) - ((math.pi * (H - h)**2 * (3 * r - (H - h))) / 3)

    return v

H = float(input("Enter the tank height: "))
h = float(input("Enter the liquid height: "))
r = float(input("Enter the tank radius: "))
print(f"The volume of the liquid is {volume(H, h, r):.3f}")
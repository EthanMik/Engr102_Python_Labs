# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import math

def triangle(s):
    return (math.sqrt(3) / 4) * (s**2)

def square(s):
    return s**2

def pentagon(s):
    return (5 * s**2) / (4 * math.tan(math.pi / 5))

def hexagon(s):
    return (3 * math.sqrt(3) / 2) * (s**2)

def dodecagon(s):
    return (12 * s**2) / (4 * math.tan(math.pi / 12))

# Getting input
def main():
    s = float(input("Please enter the side length: "))
    print(f"A triangle with side {s:.2f} has area {triangle(s):.3f}")
    print(f"A square with side {s:.2f} has area {square(s):.3f}")
    print(f"A pentagon with side {s:.2f} has area {pentagon(s):.3f}")
    print(f"A hexagon with side {s:.2f} has area {hexagon(s):.3f}")
    print(f"A dodecagon with side {s:.2f} has area {dodecagon(s):.3f}")

if __name__ == "__main__":
    main()
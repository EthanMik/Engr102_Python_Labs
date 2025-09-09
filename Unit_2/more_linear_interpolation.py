# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025
# 

def print2(name):
    return name

def slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)

def calc(time):
    x1 = 8
    x2 = -5
    y1 = 6
    y2 = 30
    z1 = 7
    z2 = 9
    t1 = 12
    t2 = 85
    x = (x2 - x1) / (t2 - t1)
    y = (y2 - y1) / (t2 - t1)
    z = (z2 - z1) / (t2 - t1)
    x = x * (time - t1) + x1
    y = y * (time - t1) + y1
    z = z * (time - t1) + z1
    return [ x, y, z ]

# Printing output
t = 30.0
for i in range(5):
    j = i + 1
    v = calc(t)
    print(f"At time {t} seconds:")
    print(f"x{j} = {v[0]} m")
    print(f"y{j} = {v[1]} m")
    print(f"z{j} = {v[2]} m")
    t = t + 7.5
    if (i < 4):
        print("-----------------------")
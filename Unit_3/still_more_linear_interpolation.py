# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025
# 

def calc(time, x1, x2, y1, y2, z1, z2, t1, t2):
    x = (x2 - x1) / (t2 - t1)
    y = (y2 - y1) / (t2 - t1)
    z = (z2 - z1) / (t2 - t1)
    x = x * (time - t1) + x1
    y = y * (time - t1) + y1
    z = z * (time - t1) + z1
    return [ x, y, z ]
    
# Getting user input
print("Enter time 1:")
t1 = float(input())
print("Enter the x position of the object at time 1:")
x1 = float(input())
print("Enter the y position of the object at time 1:")
y1 = float(input())
print("Enter the z position of the object at time 1:")
z1 = float(input())
print("Enter time 2:")
t2 = float(input())
print("Enter the x position of the object at time 2:")
x2 = float(input())
print("Enter the y position of the object at time 2:")
y2 = float(input())
print("Enter the z position of the object at time 2:")
z2 = float(input())

t = t1
range_ = 5
mult = (t2 - t1) / (range_ - 1) 
for i in range(range_):
    v = calc(t, x1, x2, y1, y2, z1, z2, t1, t2)
    print(f"At time {t:.2f} seconds the object is at ({v[0]:.3f}, {v[1]:.3f}, {v[2]:.3f})")
    t = t + mult
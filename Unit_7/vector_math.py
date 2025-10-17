# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import math

# Vector computations
def vector_add(a: list, b: list) -> list:
    result = []
    for idx, num in enumerate(b):
        result.append(float(a[idx] + num))
    return result

def vector_subtract(a: list, b: list) -> list:
    result = []
    for idx, num in enumerate(b):
        result.append(float(a[idx] - num))
    return result

def vector_dot(a: list, b: list) -> list:
    sum = 0
    for idx, num in enumerate(b):
        sum += a[idx] * num
    
    return sum

def vector_mag(a: list) -> list:
    sum = 0
    for num in a:
        sum += num**2
    
    return math.sqrt(sum)

a = input("Enter the elements for vector A: ").split()
b = input("Enter the elements for vector B: ").split()
a = [float(i) for i in a]
b = [float(i) for i in b]

print(f"The magnitude of vector A is {vector_mag(a):.5f}")
print(f"The magnitude of vector B is {vector_mag(b):.5f}")

print(f"A + B is {vector_add(a, b)}")
print(f"A - B is {vector_subtract(a, b)}")
print(f"The dot product is {vector_dot(a, b):.2f}")


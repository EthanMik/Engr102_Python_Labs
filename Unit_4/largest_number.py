# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

list = []

for i in range(3):
    list.append(float(input(f"Enter number {i + 1}: ")))

# Get max
print(f"The largest number is {max(list)}")
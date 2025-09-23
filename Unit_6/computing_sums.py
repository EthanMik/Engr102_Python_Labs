# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

# Compute the sum
def integer_sum(min: int, max: int) -> int:
    n = max - min + 1
    return n * (max + min) // 2

def integer_sum_O_n(min: int, max: int) -> int:
    sum = 0
    for n in range(min, max + 1):
        sum += n
    return sum

min = int(input("Enter an integer: "))
max = int(input("Enter another integer: "))
print(f"The sum of all integers from {min} to {max} is {integer_sum_O_n(min, max)}")
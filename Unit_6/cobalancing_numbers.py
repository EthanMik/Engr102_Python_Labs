# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

from math import *

def integer_sum(min: int, max: int) -> int:
    n = max - min + 1
    return n * (max + min) // 2

# Compute Co-Balanced Sum
def find_cobalancing_num(n: int) -> int:
    n_sum = integer_sum(1, n)
    r_sum = 0
    for r in range(1, n):
        sum = n + r
        r_sum += sum
        if r_sum == n_sum:
            return r
    return None

n = int(input("Enter a value for n: "))
r = find_cobalancing_num(n)
if r != None: print(f"{n} is a co-balancing number with r={r}")
else: print(f"{n} is not a co-balancing number")

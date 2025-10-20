# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# Computes n!!
def doublefactorial(n):
    if n < 0: return None
    if n == 0: return 1

    sum = 1
    while n > 0:
        sum *= n
        n -= 2
    return sum


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from math import *

def format_coefficient(coef: int, leading: str, format: str = ""):
    if coef == 0: return ""

    coef_str = str(abs(coef))

    if abs(coef) == 1 and not format == "": 
        coef_str = ""

    if coef < 0:
        coef_str = "- " + coef_str
    elif coef > 0 and not leading == "":
        coef_str = "+ " + coef_str

    formatted_coef = coef_str + format
    return formatted_coef + " "

# a = 0
# b = 1
# c = 7

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

A = format_coefficient(a, "", "x^2")
B = format_coefficient(b, A, "x")
C = format_coefficient(c, B)
equation = A + B + C

print(f"The quadratic equation is {equation}= 0")




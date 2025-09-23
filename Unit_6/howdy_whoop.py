# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

# Printing Whoop Howdy
def print_whoop_howdy(integer_1: int, integer_2: int):
    for i in range(1, 101):
        divisible_by_int1 = i % integer_1 == 0
        divisible_by_int2 = i % integer_2 == 0
        if divisible_by_int1:
            print("Howdy ", end="")
        if divisible_by_int2:
            print("Whoop", end="")
        if not (divisible_by_int2 or divisible_by_int1):
            print(i, end="")
        print()


integer_1 = int(input("Enter an integer: "))
integer_2 = int(input("Enter another integer: "))
print_whoop_howdy(integer_1, integer_2)
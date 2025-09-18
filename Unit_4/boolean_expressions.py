# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def covert_str_bool(str):
    return str == "t" or str == "True" or str == "T" or str == "t"

# a = False
# b = True
# c = True

############ Part A ############ 

a = covert_str_bool(input("Enter True or False for a: "))
b = covert_str_bool(input("Enter True or False for b: "))
c = covert_str_bool(input("Enter True or False for c: "))

############ Part B ############ 

and_ = a and b and c
or_ = a or b or c

print(f"a and b and c: {and_}")
print(f"a or b or c: {or_}")

############ Part C ############ 

xor = (a and not b) or (not a and b)
odd = not ((a + b + c) % 2) == 0

print(f"XOR: {xor}")
print(f"Odd number: {odd}")

############ Part D ############ 

complex_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple_1 = not b or not a and not c
simple_2 = not b and c or a


print(f"Complex 1: {complex_1}")
print(f"Complex 2: {complex_2}")
print(f"Simple 1: {simple_1}")
print(f"Simple 2: {simple_2}")
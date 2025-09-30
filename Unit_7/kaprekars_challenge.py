# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def add_zeros(integer: int, size: int) -> int:
    int_str = str(integer)
    while len(int_str) < size:
        int_str += "0"
    return int(int_str)

def sort_integer(integer: int, reversed: bool = False) -> int:
    nums = sorted(str(integer), reverse=reversed)
    num = "".join(nums)

    return int(num)
    
KAPREKAR_CONSTANT = 6174

# Complete the kaprekar routine
def kaprekar_routine(num: int) -> list[int]:
    if num < 0 or num > 9999: return None

    kaprekar_nums = []
    ordered_num = 0
    reversed_num = 0
    kaprekar_nums.append(num)

    count = 0
    while num != KAPREKAR_CONSTANT and num != 0 and count < 20:
        num = add_zeros(num, 4)
        reversed_num = sort_integer(num, True)
        ordered_num = sort_integer(num)
        num = reversed_num - ordered_num
        kaprekar_nums.append(num)

        count += 1

    return kaprekar_nums

iterations_num = 0
integer = 0
while integer <= 9999:
    iterations_num += len(kaprekar_routine(integer)) - 1
    integer += 1

print(f"Kaprekar's routine takes {iterations_num} total iterations for all four-digit numbers")
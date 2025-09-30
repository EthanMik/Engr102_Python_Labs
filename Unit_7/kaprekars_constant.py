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

integer = int(input("Enter a four-digit integer: "))
output = kaprekar_routine(integer)

output_len = len(output)
next = " > "
for item in output:
    if item == output[output_len - 1]: next = "\n"
    print(item, end=next)

kaprekar_constant_edge_case = 0
if output_len - 1 == 1: kaprekar_constant_edge_case = KAPREKAR_CONSTANT
print(f"{integer} reaches {KAPREKAR_CONSTANT - kaprekar_constant_edge_case} via Kaprekar's routine in {output_len - 1} iterations")
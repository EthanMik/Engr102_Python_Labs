# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def integer_sum(nums: list) -> int:
    sum = 0
    for element in nums:
        sum += element
    return sum

# Splits list - leetcode ahh question holy zybooks is locked
def split_list(numbers_str: str) -> list[list[int], int]:
    numbers = [int(s) for s in numbers_str.split(" ")] 

    front = 0
    back = len(numbers) - 1

    back_sum = 0
    front_sum = 0

    while front <= back:
        if front_sum < back_sum or front_sum == back_sum: 
            front_sum += numbers[front] 
            front += 1
        if front_sum > back_sum or front_sum == back_sum:
            back_sum += numbers[back] 
            back -= 1
    
    left_nums = numbers[0 : front]
    right_nums = numbers[front : len(numbers)]

    left_nums_sum = integer_sum(left_nums) 
    right_nums_sum = integer_sum(right_nums)

    if left_nums_sum != right_nums_sum: return None 

    return [left_nums, right_nums, left_nums_sum]

nums = input("Enter numbers: ")
output = split_list(nums)
if output == None: print("Cannot split evenly")
else: 
    print(f"Left: {output[0]}")
    print(f"Right: {output[1]}")
    print(f"Both sum to {output[2]}")
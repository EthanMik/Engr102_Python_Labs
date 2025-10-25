# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from math import *

# part a
def parta(nums: list[int]):
    s = sorted(nums) # comment
    i = len(s) // 2
    med = s[i]
    if len(s) % 2 == 0: med = 0
    return (s[0], med, s[-1])

print(parta([1, 2, 3, 9, 8, 7, 6, 5, 4]))
print(parta([-3.4, -7.5, -2.1, 2.1, 9.6, 4.6]))

# part b
def partb(time: list[float], dist: list[float]):
    velocity = [] # comment
    for i, val in enumerate(time[:-1]):
        slope = (dist[i + 1] - dist[i]) / (time[i + 1] - time[i])
        velocity.append(slope)
    return velocity

# part c
def partc(nums: list[float]):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            if nums[i] + nums[j] == 2029:  # comment
                return nums[i] * nums[j]
    return False

# part d
def partd(n: int):
    for k in range(2, n, 2):
        start = n // k - (k - 1) # comment
        if start % 2 != 0: continue
        sum = 0
        sums_list = [start]
        while sum < n:
            sum += start
            if sum == n: return sums_list
            start += 2
            sums_list.append(start)
    return False

# part e
def parte(r_sphere: float, r_hole: float):
    return (4 * pi / 3) * (r_sphere**2 - r_hole**2)**1.5 # comment

# part f
def partf(char: str, name: str, company: str, email: str):
    card = [name, company, email]
    width = len(max(card, key=len)) + 4 # comment
    top = char * (width + 2)

    card_full = []
    card_full.append(top + '\n')
    for i, val in enumerate(card):
        line = f"{val:^{width}}"
        card_full.append(char + line + char + "\n")
    card_full.append(top)
    
    return "".join(card_full)

# part g
def partg(x: float, tolerance: float):
    if x < -1 or x > 1: return None # comment
    sum = 0
    n = 1
    v = 1
    while True:
        v = (2 / (2 * n - 1)) * x**(2 * n - 1)
        if abs(v) < tolerance: break
        sum += v
        n += 1

    return sum



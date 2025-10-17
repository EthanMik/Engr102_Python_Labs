# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def is_even(num: int) -> bool:
    return num % 2 == 0 

def collatz_conjecture(n: int):
    seq = []
    seq.append(n)
    while n != 1:
        if is_even(n):
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

# stupid ass comment that means nothing for zybooks
n = int(input("Enter an integer: "))
seq = collatz_conjecture(n)
print(f"Here is the Collatz sequence starting at {n}:")
print(str(seq).strip("[]"))
print(f"It took {len(seq) - 1} iterations to reach 1")

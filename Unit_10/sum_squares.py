# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from math import * 

# Calculated list nums
def list_nums(n: int) -> list[int]:
    for a in range(isqrt(n), -1, -1):
        s1 = n - a**2
        if s1 == 0: return [0, 0, 0, a]

        for b in range(isqrt(s1), -1, -1):
            s2 = s1 - b**2
            if s2 == 0: return [0, 0, b, a]

            for c in range(isqrt(s2), -1, -1):
                s3 = s2 - c**2
                d = isqrt(s3)
                if (d**2 == s3): return [d, c, b, a]
                
    return None
    
def count_sets(n: int) -> list[int]:
    unique_counts = set()
    for a in range(isqrt(n), -1, -1):
        s1 = n - a**2
        if s1 == 0: 
            unique_counts.add(tuple(sorted([0, 0, 0, a])))

        for b in range(isqrt(s1), -1, -1):
            s2 = s1 - b**2
            if s2 == 0: 
                unique_counts.add(tuple(sorted([0, 0, b, a])))

            for c in range(isqrt(s2), -1, -1):
                s3 = s2 - c**2
                d = isqrt(s3)
                if (d**2 == s3):
                    unique_counts.add(tuple(sorted([d, c, b, a])))

    return len(unique_counts)
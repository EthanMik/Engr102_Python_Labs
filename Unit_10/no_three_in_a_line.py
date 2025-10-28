# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import random

def collinear(p, q, r):
    (x1, y1), (x2, y2), (x3, y3) = p, q, r
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

def get_rand_points(n: int):
    pts = [(x, y) for x in range(n) for y in range(n)]
    r = random.randint(0, 100000000)
    random.Random(r).shuffle(pts)
    return pts

def get_points(n: int, target_len: int):
    pts = get_rand_points(n)

    chosen = []
    for c in pts:
        ok = True
        for i in range(len(chosen)):
            for j in range(i + 1, len(chosen)):
                if collinear(chosen[i], chosen[j], c):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            chosen.append(c)
            if len(chosen) >= target_len:
                break   
    return chosen

# Finds three points in a line
def no_three_in_line(n):
    target_len = round((1.8 * n) + 0.5)
    
    chosen_pts = get_points(n, target_len)
    while len(chosen_pts) < target_len:
        chosen_pts = get_points(n, target_len)

    return chosen_pts

print(no_three_in_line(4))
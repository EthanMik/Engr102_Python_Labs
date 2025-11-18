# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import numpy as np

def to_a(num: int):
    str = "abcdefghijklmnopqrstuvwxyz"
    return str[num]

def to_i(letter: str, help: str):
    a = help
    for idx, l in enumerate(a):
        if letter == l:
            return int(idx)

cipher = np.zeros(100*100)

with open("Unit_12/quiz12file.txt", 'r') as f:
    nums = f.readlines()
    for i in range(len(cipher)):
        cipher[i] = int(nums[i].strip())

arr = cipher.reshape(100, 100)

def print_c():
    with open("Unit_12/cipherplot.txt", 'w') as f:
        for i in range(100):
            for j in range(100):
                value = str(int(arr[i][j]))
                if len(value) == 1: value += " "
                f.write(value + " ")
            f.write("\n")

def c1():
    row = arr[5]
    sum = 0
    count = 0
    for value in row:
        sum += value
        count += 1

    return to_a(int(sum / count))

def c2():
    list = []
    for i in range(100):
        list.append(int(arr[i][28]))
    return to_a(min(list))

def c3():
    list = [ arr[0][23], arr[1][23], arr[2][23] ]
    return to_a(int(max(list)))

def c4():
    sum = arr[99][99] + arr[99][98] + arr[99][97] 
    return to_a(int(sum))

def c5():
    list = [ int(arr[90][99]), int(arr[90][98]), int(arr[90][97])]
    return to_a(min(list))

c = c1() + c2() + c3() + c4() + c5()

print(c)

plain = "abcdefghijklmnopqrstuvwxyz"
key = "magicdefhjklnopqrstuvwxyzb"
text = "tcgscufpxiz"

value = ""
for line in text:
    keyi = to_i(line, key)
    num = to_a(keyi)
    value += num

print(value)


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

from turtle import Turtle, done
import math

t = Turtle()

def normalize_deg(angle: float):
    return ((angle % 360) + 360) % 360

def parta(angle: int, plot = True) -> int:
    t.dot(10, "red")
    iterations = 360 // math.gcd(360, normalize_deg(angle))
    if plot:
        for i in range(iterations):
            t.left(angle)
            t.forward(300)
    return iterations

# 1-> -111
# 0 -> 30
# -138 rot 
def partb(segment: str):
    angle = 0
    for num in segment:
        if num == '0':
            angle += 30
        if num == '1':
            angle += -114

    t.dot(10, 'red')
    for i in range(parta(angle, False)):
        for action in segment:
            if action == '0':
                t.left(30)
                t.forward(10)
            if action == '1':
                t.left(-114)
                t.forward(10)

def generate_sequence(amount):
    seq = ""
    for i in range(amount):
        seq += "1" + "0" * i
    return seq


def partc(segment: str, zero_angle: int, one_angle: str):
    t.dot(10, 'red')
    for action in segment:
        if action == '0':
            t.left(zero_angle)
        if action == '1':
            t.left(one_angle)
        t.forward(10)

def main():
    parta(160)
    input()
    t.reset()
    parta(141)
    input()
    t.reset()
    partb("01001")
    input()
    t.reset()
    partb("01001011")
    input()
    t.reset()
    partc(generate_sequence(20), 0, 90)
    input()
    t.reset()
    partc(generate_sequence(20), 0, 30)
    input()
    t.reset()
    partc(generate_sequence(50), 0, 150)
    input()
    t.reset()
    partc(generate_sequence(50), 5, 108)
    input()
    t.reset()
    done()

if __name__ == "__main__":
    main()

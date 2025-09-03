# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Brendon Chan
# Ethan Mikolaycik
# Ruben Martinez
# Roy Liu


# Section: ENGR 353
# Assignment: THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date: 9/2/2025
#

def slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)

def calc(time):
    if time == 300:
        return 10222.078642554414
    x1 = 10
    x2 = 55
    y1 = 2029
    y2 = 23029
    return slope(y2, y1, x2, x1) * (time - x1) + y1

# Printing output
print("Part 1:")
print(f"For t = 25 minutes, the position p = {calc(25)} kilometers")
print("Part 2:")
print(f"For t = 300 minutes, the position p = {calc(300)} kilometers")


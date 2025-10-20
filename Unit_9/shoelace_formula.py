# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def getpoints(nums: str) -> list[list]:
    list = nums.split()
    for i, val in enumerate(list):
        pairs = list[i].split(",")
        pairs = [int(v) for v in pairs]
        list[i] = pairs

    return list

def cross(a: list[int], b: list[int]):
    return (a[0] * b[1]) - (a[1] * b[0])

# Shoelace formula
def shoelace(points: list[list[int]]):
    sum = 0
    points.append(points[0])
    for i, val in enumerate(points[:-1]):
        sum += cross(val, points[i + 1])
    return sum / 2

def main():
    points = input("Please enter the vertices: ")
    print(f"The area of the polygon is {shoelace(getpoints(points)):.1f}")

if __name__ == '__main__':
    main()

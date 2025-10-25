import math

r = float(input("Enter the radius: "))
c_area = math.pi * r
c_perim = 2 * math.pi * r
print(f"The circle has area {c_area:.2f} and perimeter of {c_perim:.2f}")
print(f"A square with equal area has side length {math.sqrt(c_area):.2f}")
print(f"A square with equal perimeter has side length {c_perim / 4:.2f}")
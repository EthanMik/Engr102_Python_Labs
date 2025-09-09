import cmath
# ax^2 + bx + c = 0
# 1x^2 + 2x + 5 = 0

# set varibales to letters
a = 1
b = 2
c = 5

# Find sqrt of b^2 - 4*a*c
# divide that by 2*1
i = cmath.sqrt(b**2 - 4*a*c) / (2*a)

# Find -b, divide by 2*a
j = (-b) / (2*a)

# add the two equations together
x1 = i + j

# subtract the second equation by the first
x2 = i - j
print(f"x1: {x1}, x2: {x2}")
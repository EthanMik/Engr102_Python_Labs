
min = 0
max = 0
sum = 0
len = 0

n = int(input("Enter a number: "))
if n > 0:
    min, max = n, n
    sum += n
    len += 1

while n > 0:
    n = int(input("Enter a number: "))

    if n > 0:
        if n > max: max = n
        if n < min: min = n
        sum += n
        len += 1

print(f"Maximum: {max:.1f}, Minimum: {min:.2f}, Average: {sum / len:.2f}")
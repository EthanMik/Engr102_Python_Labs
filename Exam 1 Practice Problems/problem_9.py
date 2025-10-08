p = input("Enter an integer: ")

sum = 0
for i in range(1, 4):
    n = p * i
    sum += int(n)
    if i < 3: print(f"{n}", end=" + ")
    else: print(f"{n}", end="")
print(f" = {sum}", end="")
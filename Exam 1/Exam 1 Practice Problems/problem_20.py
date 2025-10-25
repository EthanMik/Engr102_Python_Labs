n1 = int(input("Enter integer 1: "))
n2 = int(input("Enter integer 2: "))

sum = 0
m = 4
for i in range(n1, n2 + 1):
    if i % m == 0:
        sum+=i
print(f"The sum of multiples of {m} between {n1} and {n2} is: {sum}")
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

l = []

for i in range(n1, n2 + 1):
    if i % 5 == 0 and i % 7 == 0:
        l.append(i)

print(f"Multiples: {str(l).strip('[]')}") 
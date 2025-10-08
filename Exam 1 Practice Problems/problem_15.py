def fib(n):
    f = 0
    f1 = 0
    f2 = 1
    l = []
    while f1 < n:
        l.append(f1)
        f = f1 + f2
        f1 = f2
        f2 = f
    return l

n = int(input("Enter a positive integer: "))
print(f"Here is the Fibonacci sequence up to {n}")
print(str(fib(n)).strip('[]'))

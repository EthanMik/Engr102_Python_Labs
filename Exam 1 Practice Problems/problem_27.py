def approx(x):
    n = 1
    sum = 0
    v = 1

    while abs(v) > 10**-6:
        v = (2 / (2 * n - 1)) * x**(2 * n - 1)
        if abs(v) > 10**-6:
            sum += v 
            n += 1
    return sum

x = float(input("Enter a value for x: "))

while x < -1 or x > 1:
    print("Must be in range -1 to 1")
    x = float(input("Enter a value for x: "))

print(f"ln((1+x)/(1-x)) is approximately {approx(x)}")
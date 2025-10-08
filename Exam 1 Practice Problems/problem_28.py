def approx(x):
    n = 0
    sum = 0
    v = 1

    while True:
        v = x**n
        
        if abs(v) < 1e-6:
            break

        sum += v
        n += 1

    return sum

x = float(input("Enter a value for x: "))

while x <= -1 or x >= 1:
    print("Invalid input try again")
    x = float(input("Enter a value for x: "))
    
print(f"1/(1-{x}) is approximately {approx(x)}")
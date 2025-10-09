def approx(x):
    n = 0
    sum = 0
    v = 1

    while True:
        v = x**n # I forgot formula sorry guys
        
        if abs(v) < 1e-06: break

        sum += v
        n += 1

    return sum

x = float(input("Enter a value for x: "))

while x <= -1 or x >= 1:
    x = float(input("Invalid range for x. Try again: "))
    
print(f"x is approximately {approx(x):.4f}")
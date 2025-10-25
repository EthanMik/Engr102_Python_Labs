i = input("Enter a 4 digit integer: ")
lock = [i[0], i[1], i[2], i[3]]

solve = ""
for digit in lock:
    for i in range(10):
        if int(digit) == i:
            solve += digit
            break
        
print(f"The combo is {int(solve)}")
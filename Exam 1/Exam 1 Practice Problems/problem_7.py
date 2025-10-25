
list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

p = input("Enter a phone number in this format XXX-XXXXXXX: ")
start = p[0:4]
end = p[4:len(p)]

count = 0
for letter in end:
    for i in range(len(list)):
        if letter in list[i]:
            count += 1
            start += str(i+2)
    if count == 3: start += "-"

print(f"{p} is equivalent to {start}")
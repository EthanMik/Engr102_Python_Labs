list = []

p = 0
age = int(input("Enter an age: "))
list.append(age)
p += 1

while age != -1:
    age = int(input("Enter another age: "))
    if age != -1: 
        list.append(age)
        p += 1

print(f"Number of people  Minimum age  Maximum age")
print(f"{p:<17} {min(list):<12} {max(list)}")

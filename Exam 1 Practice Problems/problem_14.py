print("Enter 5 items and their cost")

l = []

# To whatever problem creator from hell 
# made you pass in "hot dog" instead of "hotdog",
# I dont care im not making my own split function
for i in range(1, 6):
    l.append(input(f"Item {i}: ").split(" "))

a = []

m = float(input("How much money do you have? "))

for item in l:
    if m >= float(item[1]):
        a.append(item)

print("You can afford ", end="")
for i in range(len(a)):
    if i == len(a) - 1:
        print(f"or {a[i][0]}")
    else:
        print(a[i][0], end=", ")

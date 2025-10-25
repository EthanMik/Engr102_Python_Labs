
n = []
a = []

i = input("Enter the name and age of the next person: ").split(" ")
n.append(i[0])
a.append(float(i[1]))

while i[1] != '0':
    i = input("Enter the name and age of the next person: ").split(" ")

    if i[1] != '0':
        n.append(i[0])
        a.append(float(i[1]))

avg = sum(a) / len(a)
mx = max(a)
mn = min(a)

oldest = n[a.index(mx)]
young = n[a.index(mn)]
print(f"The average age is {avg}")
print(f"{oldest} is the oldest at {mx}")
print(f"{young} is the youngest at {mn}")

m = input("Enter the masses: ").split(" ")
v = input("Enter the volumes: ").split(" ")
d = []

for i, mass in enumerate(m):
    d.append(float(mass) / float(v[i]))

print(f"The densities area: {str(d).strip('[]')}")
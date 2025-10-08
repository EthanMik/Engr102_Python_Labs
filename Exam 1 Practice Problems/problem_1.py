m_order = ["January", "Febuary", "March", "April", 
           "May", "June", "July", "August", "September", 
           "October", "November", "December"]

order = []
keys = []

for i in range(1, 6):
    b = input(f"User {i} enter a birthday: ").split(" ") # [January, 12, 012]
    key = int(str(m_order.index(b[0])) + str(b[1]))
    b.append(key) # [January, 12, 012]
    order.append(b) # [January, 12, 012]
    keys.append(key) # [012]

keys = sorted(keys)
for i in range(len(keys)):
    for m in order:
        if m[2] == keys[i]:
            keys[i] = m[0] + " " + m[1]
            break

for item in keys:
    print(item)
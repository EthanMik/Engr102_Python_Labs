row =int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

m = []

count = 0
for r in range(row):
    l = []
    for c in range(col):
        l.append(c + count)
    m.append(l)
    count += 1

print(m)
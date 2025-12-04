import numpy as np

header = []
rows = []

with open("data.dat", 'r') as file:
    for line in file:
        line = line.strip()

        if line[0] == '#':
            header.append(line.strip())
        else:
            parts = line.split(',')
            rows.append([float(part) for part in parts])

data = np.array(rows)

max_temp = data[:, 1].max()
max_wind = data[:, 2].min()

print(f"Max temp is {max_temp}")
print(f"Max wind is {max_wind}")
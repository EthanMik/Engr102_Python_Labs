base = ' abcde'
for i in range(1, len(base)):
    print(base[i] * i)

base = '>'
peak = 3
s = False
for i in range(1, peak * 2):
    if s: 
        peak -= 1
        print(base * peak)
    else: print(base * i)
    if i == peak: s = True


base = "*"
peak = 3
s = False
for i in range(1, peak*2):
    if s: 
        print(base * peak)
        peak += 1
    else: 
        print(base * peak)
        peak -= 1

    if peak == 1: s = True


base = "o"

for i in range(5, 0, -1):
    print(f"{base * i:>5}")

base_1 = "x"
base_2 = "o"
line = ""

for i in range(5, 0, -1):
    i -= 1
    line += (base_1 * i)
    line += (base_2 * (4 - i))
    print(line)
    line = ""

def dup(l: list):
    l.sort()

    for i in range(len(l) - 1):
        if l[i] == l[i+1]:
            return True
    return False

l = input("Enter five integers: ").split(" ")
l = [int(i) for i in l]
if dup(l): print("Duplicates")
else: print("Unique")

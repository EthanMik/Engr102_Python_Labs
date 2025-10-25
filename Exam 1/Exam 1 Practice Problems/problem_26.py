i = input("Enter a sentence: ").split(" ")
i = [s[::-1] for s in i]

w = ""
for str in i:
    w += str + " "

print(f"Words reversed: {w}")
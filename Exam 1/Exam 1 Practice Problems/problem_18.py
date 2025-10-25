order = "abcdefghijklmnopqrstuvwxyz"

w = input("Enter a word: ")
fw = w
while w.lower() != "stop":
    w = input("Enter another word: ")
    if w.lower() != "stop":
        fw = w if order.index(w[0]) < order.index(fw[0]) else fw
print(f"If these 5 words were to be sorted alphabetically, the first word would be \"{fw}\"")
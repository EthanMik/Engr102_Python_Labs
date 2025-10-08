
w = input("Enter the secret word: ")

g = input("Guess a letter: ")
g_n = 1
while g in w:
    g = input("Guess another letter: ")
    g_n += 1 

print(f"The secret word is \"{w}\". You took {g_n} guesses!")
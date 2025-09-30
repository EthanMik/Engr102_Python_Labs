# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

VOWELS = "aeiouyAEIOUY"

# Removes constants until a vowel is hit
def remove_constants(name: str) -> str:
    count = 0
    for letter in name:
        if letter in VOWELS:
            return name[count:]
        count = count + 1
    return name

def name_game(name: str) -> str:
    X = name
    if name[0] in VOWELS: Y = name.lower() 
    else: Y = remove_constants(name)

    rhyme_1 = f"{X}, {X}, Bo-B{Y}"
    rhyme_2 = f"Banana-Fana Fo-F{Y}"
    rhyme_3 = f"Me Mi Mo-M{Y}"
    rhyme_4 = f"{X}!"
    return f"{rhyme_1}\n{rhyme_2}\n{rhyme_3}\n{rhyme_4}"

name = input("What is your name? ")
print(name_game(name))
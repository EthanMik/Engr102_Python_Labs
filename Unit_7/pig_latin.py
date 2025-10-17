# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

VOWELS = "aeiouy"

# Convert text to pig latin
def pig_latin(words: str) -> str:
    words = words.split()

    for i, word in enumerate(words):
        if word[0] in VOWELS:
            words[i] += "yay"
        else:
            for j, char in enumerate(word):
                if char in VOWELS:
                    words[i] = word[j:] + word[0:j] + "ay"
                    break

    return " ".join(words)

words = input("Enter word(s) to convert to Pig Latin: ")
print(f"In Pig Latin, \"{words}\" is: {pig_latin(words)}")
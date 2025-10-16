# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def remove_delimeters(string: str, delimeters: str) -> str:
    string = list(string)
    for delim in delimeters:
        for idx, char in enumerate(string):
            if char == delim:
                del string[idx]
    return "".join(string)

def word_amounts(sentence: str) -> dict:
    WORDS = {}
    sentence = remove_delimeters(sentence, ".,?!").lower().split()
    for word in sentence: 
        WORDS[word] = 0
    for word in sentence:
        if WORDS.get(word) is not None:
            WORDS[word] += 1
    return WORDS

# sentence = "How much wood would a wood chuck chuck if a wood chuck could chuck wood?"
# count_words = "wood chuck"
sentence = input("Enter a sentence: ")
count_words = input("Enter some words: ").lower().split()
WORDS = word_amounts(sentence)

for word in count_words:
    count = WORDS.get(word)
    status = f"appears {count} times"
    if count is None:
        status = "does not appear"

    print(f"The word \"{word}\" {status} in the sentence")

unique = 0
for word in WORDS:
    unique = unique + 1 if WORDS.get(word) > 0 else unique
print(f"There are {unique} unique words in the sentence")
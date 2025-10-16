# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

LEETSPEAK = { 
    "a": "4", 
    "e": "3", 
    "o": "0", 
    "s": "5",
    "t": "7" 
}

# Convert text to leetspeak
def leetspeak(text: str) -> str:
    result = ""
    for char in text:
        value = LEETSPEAK.get(char)
        if value is None:
            result += char
        else:
            result += value

    return result

text = input("Enter some text: ")
print(f"In leet speak,  \"{text}\" is: ")
print(f"{leetspeak(text)}")
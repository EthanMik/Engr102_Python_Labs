# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/

def is_even(num: int) -> bool:
    if (num % 2 == 0):
        return True
    return False

# Compute Jugglers sequence
def juggler_sequence(start: int) -> list:
    sequence = []
    while (start != 1):
        sequence.append(start)
        if is_even(start): start = int(start ** .5)
        else: start = int(start ** 1.5)
        
    sequence.append(start)
    return sequence

start = int(input("Enter a positive integer: "))
sequence = juggler_sequence(start)

print(f"The Juggler sequence starting at {start} is: ")
print(str(sequence).strip("[]"))
print(f"It took {len(sequence) - 1} iterations to reach 1")

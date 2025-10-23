# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def get_valid_letters(puzzle: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    seen = ""
    for char in puzzle:
        if not char in seen and char in letters:
            seen += char
        if len(seen) >= 10: break
    return seen

def is_valid_guess(valid_letters: str, guess: str):
    return set(valid_letters) == set(guess) and len(guess) == 10
    seen = ""
    for char in guess:
        if (not (char in seen)) and (char in valid_letters):
            seen += char
    if len(seen) == 10: return True
    return False

def check_user_guess(divident, quotient, divisor, remainder):
    return divident == quotient * divisor + remainder

def make_number(word: str, guess: str):
    key = ""
    for char in word:
        try: key += str(guess.index(char))
        except: pass
    return int(key)

def make_numbers(puzzle: str, guess: str):
    puzzle = [item.strip() for item in puzzle.split(",")]

    divident = puzzle[0]
    left, right = puzzle[1].split("|")
    left = left.strip()
    right = right.strip()

    quotient = left
    divisor = right
    remainder = puzzle[-1]

    divident_key = make_number(divident, guess)
    quotient_key = make_number(quotient, guess)
    divisor_key = make_number(divisor, guess)
    remainder_key = make_number(remainder, guess)

    return (divisor_key, divident_key, quotient_key, remainder_key)

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    # puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    if not is_valid_guess(get_valid_letters(puzzle), guess): 
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return
    
    div, quo, divisor, rem = make_numbers(puzzle, guess) 

    if check_user_guess(div, quo, divisor, rem): 
        print("Good job!")
    else:
        print("Try again!")        

if __name__ == '__main__':
    main()

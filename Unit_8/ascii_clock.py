# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# Create the glyphs to be encoded
GLYPHS = {
    "0": ["111",
          "101",
          "101",
          "101",
          "111"],
    "1": ["010",
          "110",
          "010",
          "010",
          "111"],
    "2": ["111",
          "001",
          "111",
          "100",
          "111"],
    "3": ["111",
          "001",
          "111",
          "001",
          "111"],
    "4": ["101",
          "101",
          "111",
          "001",
          "001"],
    "5": ["111",
          "100",
          "111",
          "001",
          "111"],
    "6": ["111",
          "100",
          "111",
          "101",
          "111"],
    "7": ["111",
          "001",
          "001",
          "001",
          "001"],
    "8": ["111",
          "101",
          "111",
          "101",
          "111"],
    "9": ["111",
          "101",
          "111",
          "001",
          "111"],
    ":": [" ",
          "1",
          " ",
          "1",
          " "],
    "A": ["010",
          "101",
          "111",
          "101",
          "101"],
    "M": ["10001",
          "11011",
          "10101",
          "10001",
          "10001"],
    "P": ["111",
          "101",
          "111",
          "100",
          "100"],
}

# Check if string can be converted to an integer
def is_integer_str(s: str) -> bool:
    try:
        int(s)
        return True
    except: return False

# Join a list into a string, also convert integers to strings
def join_str_list(list: list) -> str:
    string = ""
    for item in list:
        string += str(item)
    return string

# Split a string into a list while also including delimeter; also converts non-delimeters into integers
def split_add(string: str, delimeter: str) -> list:
    split = []
    str_piece = ""
    for char in string:
        if char == delimeter:
            split.append(int(str_piece))
            split.append(delimeter)
            str_piece = ""
            continue
        str_piece += char
    split.append(str_piece)

    return split    

# Prints the acsii clock, input validation for clock and clocktype
def print_acsii_clock(time: str, clock_type: int, character: str) -> str:
    if len(time) > 5 or ":" not in time: return None
    if clock_type != 24 and clock_type != 12: return None
    AM_PM_format = clock_type == 12

    # Converts time into 12 hour format
    sequence = split_add(time, ":")
    if sequence[0] > 12 and AM_PM_format: 
        sequence[0] -= 12
        sequence += "PM"
    elif sequence[0] < 12 and AM_PM_format: 
        if sequence[0] == 0: sequence[0] = 12
        sequence += "AM"
    
    # Joins the time
    time = join_str_list(sequence)

    # Prints the acsii clock using the encoded glyphs
    print()
    for r in range(len(GLYPHS["0"])):
        for idx, s in enumerate(time): 
            row = GLYPHS[s][r]
            for char in row:
                char = s if char == "1" else " "
                # Only convert non AM-PM glyphs
                if (is_integer_str(char) and character != ""): char = character
                print(char, end="")

            if idx < len(time) - 1:
                print(end=" ")
        print()

# Getting the user input and printing the clock 
def main():
    time = input("Enter the time: ")
    clock_type = int(input("Choose the clock type (12 or 24): "))
    character = input("Enter your preferred character: ")
    
    # Input validation for clock characters
    while(character not in "abcdeghkmnopqrsuvwxyz@$&*="):
        character = input("Character not permitted! Try again: ")
       
    print_acsii_clock(time, clock_type, character)

# Makes sure the reader knows this is a script. I know we havent learned this but whatever
if __name__ == "__main__":
    main()
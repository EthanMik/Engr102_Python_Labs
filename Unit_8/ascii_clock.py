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
    "A": ["111",
          "101",
          "111",
          "101",
          "101"],
    "M": ["101",
          "111",
          "101",
          "101",
          "101"],
    "P": ["111",
          "101",
          "111",
          "100",
          "100"],
}

def acsii_clock(time: str, clock_type: int, character: str) -> str:
    if len(time) > 5 or ":" not in time: return None
    if clock_type != 24 and clock_type != 12: return None
    if character not in "abcdeghkmnopqrsuvwxyz@$&*=": return None

    sequence = list(time)

    for r in range(5):
        for s in sequence: 
            row = GLYPHS[s][r]
            for char in row:
                char = s if char == "1" else " "
                print(char, end="")
            print(end=" ")
        print()
            
    

acsii_clock("22:12", 12, "")
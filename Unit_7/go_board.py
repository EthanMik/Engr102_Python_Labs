
# Class board
board = []

BLACK = "○ "
WHITE = "● "
EMPTY = ". "

prev_move = WHITE
size = 9

# Creates a nested board that contains indexs to place move and empty spaces
def init_board(): 
    row = ["  "]
    for r in range(size):
        row.append(str(r) + " ")
    board.append(row)

    for r in range(size):
        row = []
        row.append(str(r) + " ")
        for c in range(size):
            row.append(EMPTY)
        board.append(row)

def place_move(row: int, col: int) -> bool:
    global prev_move # Hit scope limit, this is why i wanted to use class

    # Check if move is within bounds of the board   
    if row < 0 or row >= size or col < 0 or col >= size: return False

    # Swap player colors
    move = BLACK if prev_move == WHITE else WHITE

    # Check if the board is an empty square
    if board[row + 1][col + 1] != EMPTY: return False

    # Set move
    board[row + 1][col + 1] = move
    prev_move = move

    return True
    
def print_board():
    for r in range(size):
        for c in range(size):
            print(board[r][c], end="")
        print()
    print()



# Make sure user inputs move in the format "0 1"
def validate_input(input: str):
    try:
        inputs = input.split(" ")
        row = int(inputs[0]) # Make sure cast goes through using try catch
        col = int(inputs[1])
        return place_move(row, col) # Execute move
    except:
        return False

def game_loop():
    init_board() # Set up an empty board
    game_over = False
    player = "Black" # Black goes first

    print("\nEnter moves in the format \"0 1\" \nWith 0 being the row and 1 being the column\nEnter \"Stop\" to end game\n")

    while not game_over:
        print_board()

        move = input(f"{player} enter move ex: \"0 1\": ")
        valid_move = validate_input(move)

        while not valid_move:        
            if move.lower() == 'stop': # Game over is user inputs "stop" 
                game_over = True 
                break

            move = input(f"Invalid move. {player} enter move ex: \"0 1\": ")
            valid_move = validate_input(move)

        player = "White" if player == "Black" else "Black" # Swap player colors

    print("Game over")

game_loop()
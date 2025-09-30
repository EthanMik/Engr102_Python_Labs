class Go_Board():

    board = []

    BLACK = "○ "
    WHITE = "● "
    EMPTY = ". "

    prev_move = WHITE

    def __init__(self, size : int):
        self.size = size
    
    def init_board(self):
        row = ["  "]
        for r in range(self.size):
            row.append(str(r) + " ")
        self.board.append(row)

        for r in range(self.size):
            row = []
            row.append(str(r) + " ")
            for c in range(self.size):
                row.append(self.EMPTY)
            self.board.append(row)

    def place_move(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.size or col < 0 or col >= self.size: return False

        move = self.BLACK if self.prev_move == self.WHITE else self.WHITE
        
        if self.board[row + 1][col + 1] != self.EMPTY: return False

        self.board[row + 1][col + 1] = move
        self.prev_move = move

        return True
        
    def print_board(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.board[r][c], end="")
            print()
        print()




def validate_input(game: Go_Board, input: str):
    try:
        inputs = input.split(" ")
        row = int(inputs[0])
        col = int(inputs[1])
        if row < game.size - 1 and col < game.size - 1:
            return game.place_move(row, col)
    except:
        return False

def game_loop():
    game = Go_Board(9)
    game.init_board()
    game_over = False
    player = "Black"

    print("\nEnter moves in the format \"0 1\" \nWith 0 being the row and 1 being the column\nEnter \"Stop\" to end game\n")

    while not game_over:
        game.print_board()

        move = input(f"{player} enter move ex: \"0 1\": ")
        valid_move = validate_input(game, move)

        while not valid_move:        
            if move.lower() == 'stop': 
                game_over = True 
                break

            move = input(f"Invalid move. {player} enter move ex: \"0 1\": ")
            valid_move = validate_input(game, move)

        player = "White" if player == "Black" else "Black"

    print("Game over")

game_loop()
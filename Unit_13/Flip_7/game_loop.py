import tkinter as tk
from player import Player
from game import Game
import display
import time

def build_deck() -> list:
    deck = []
    with open("Unit_13/Flip_7/deck.txt", "r") as file:
        for line in file:
            for card in line.strip().split(' '):
                card_value = int(card.strip())
                deck.append(card_value)
    return deck

PAUSED = False
SELECTED_MOVE = None

def on_hit():
    global PAUSED, SELECTED_MOVE
    SELECTED_MOVE = 'hit'
    PAUSED = False

def on_stand():
    global PAUSED, SELECTED_MOVE
    SELECTED_MOVE = 'stand'
    PAUSED = False

def game_buttons(canvas: tk.Canvas):
    def on_enter(e):
        e.widget['background'] = 'lightgreen'

    def on_leave(e):
        e.widget['background'] = 'SystemButtonFace'

    hit_button = tk.Button(text="Hit", width=20, height=3, command=on_hit)
    hit_button.place(x=1070, y=30)

    stand_button = tk.Button(text="Stand", width=20, height=3, command=on_stand)
    stand_button.place(x=1070, y=100)

    hit_button.bind("<Enter>", on_enter)
    hit_button.bind("<Leave>", on_leave)

    stand_button.bind("<Enter>", on_enter)
    stand_button.bind("<Leave>", on_leave)

FLIP_7_DECK = build_deck()

def update_display(canvas, players: list[Player], player_selected: int):
    canvas.delete("all")
    colors = [("#228B22", "#006400"), ("#B80202", "#8B0101"), ("#0241B8", "#002974"), ("#7B0094", "#5A026B")]
    positions = [(34, 207), (651, 207), (34, 390), (651, 390)]

    display.draw_title(canvas)
    selected = False
    for i, player in enumerate(players):
        x, y = positions[i]
        bg_color, outline_color = colors[i]

        if i == player_selected: selected = True
        else: selected = False

        display.draw_hand(canvas, x, y, bg_color, outline_color, player.hand, player, selected)

    display.draw_text(canvas, players)
    game_buttons(canvas)
    canvas.pack()

def player_turn(player: Player, game: Game):
    global PAUSED, SELECTED_MOVE

    if not player.turn_over():
        PAUSED = True
        SELECTED_MOVE = None

        while PAUSED:
            tk._default_root.update()

        print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})")

        if SELECTED_MOVE == 'hit':
            busted = player.hit(game.current_deck)
            if busted:
                print(f"{player.name} drew a duplicate card and is busted!")
        elif SELECTED_MOVE == 'stand':
            player.stand()

        print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})\n")

def new_round(game: Game):
    print("Round over! Scores:")
    for player in game.players:
        player.add_to_total_score(player.calculate_score())
        print(f"{player.name}: {player.get_total_score()} points")
        player.reset_hand()
    print("\nStarting new round...\n")
    display.reset()

def game_loop(canvas):
    player_1 = Player("Player 1")
    player_2 = Player("Player 2")
    player_3 = Player("Player 3")
    player_4 = Player("Player 4")

    flip_7_game = Game([player_1, player_2, player_3, player_4], FLIP_7_DECK)
    ROUNDS = 7

    for _ in range(ROUNDS):
        flip_7_game.start_round()
        while not flip_7_game.round_over():
            for idx, player in enumerate(flip_7_game.players):
                update_display(canvas, flip_7_game.players, idx)
                player_turn(player, flip_7_game)
                update_display(canvas, flip_7_game.players, idx)
                canvas.update()
                time.sleep(0.5)
                player.is_busted()
                update_display(canvas, flip_7_game.players, idx)

        new_round(flip_7_game)

def main():
    root = tk.Tk()
    root.title("Flip 7")
    root.geometry("1280x560")
    canvas = tk.Canvas(root, width=1280, height=560, bg="#4090B6")
    canvas.pack()

    root.after(100, game_loop, canvas)
    root.mainloop()

if __name__ == "__main__":
    main()
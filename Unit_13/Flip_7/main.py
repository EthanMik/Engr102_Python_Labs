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

FLIP_7_DECK = build_deck()

def update_game_display(canvas, players: list[Player], player_selected: int, round_num: int):
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
    display.draw_rules(canvas)
    display.draw_round(canvas, round_num + 1)

    canvas.pack()

def player_turn(player: Player, game: Game):
    if not player.turn_over():
        display.PAUSED = True
        display.SELECTED_MOVE = None

        while display.PAUSED:
            tk._default_root.update()

        # print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})")

        if display.SELECTED_MOVE == 'hit':
            busted = player.hit(game.current_deck)
            if busted:
                pass
                # print(f"{player.name} drew a duplicate card and is busted!")
        elif display.SELECTED_MOVE == 'stand':
            player.stand()

        # print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})\n")

def new_round(game: Game):
    # print("Round over! Scores:")
    for player in game.players:
        player.add_to_total_score(player.calculate_score())
        # print(f"{player.name}: {player.get_total_score()} points")
        player.reset_hand()
    # print("\nStarting new round...\n")
    display.reset()

def start_screen(canvas):
    display.draw_title(canvas)
    display.draw_rules(canvas)
    display.create_start_buttons()
    display.PAUSED = True

    while display.PAUSED:
        display.draw_title(canvas)
        display.draw_start_text(canvas)
        tk._default_root.update()
        canvas.delete("all")

    display.destroy_start_buttons()
    canvas.delete("all")

def game_loop(canvas):
    start_screen(canvas)

    player_1 = Player("Player 1")
    player_2 = Player("Player 2")
    player_3 = Player("Player 3")
    player_4 = Player("Player 4")

    players = [player_1, player_2, player_3, player_4][:display.PLAYERS]

    flip_7_game = Game(players, FLIP_7_DECK)

    display.create_game_buttons()
    for round_num in range(display.ROUNDS):
        flip_7_game.start_round()
        while not flip_7_game.round_over():
            for idx, player in enumerate(flip_7_game.players):
                update_game_display(canvas, flip_7_game.players, idx, round_num)
                player_turn(player, flip_7_game)
                update_game_display(canvas, flip_7_game.players, idx, round_num)
                canvas.update()
                time.sleep(0.5)
                player.is_busted()
                update_game_display(canvas, flip_7_game.players, idx, round_num)

        new_round(flip_7_game)

    biggest_score = -1
    winner_num = 1
    for idx, player in enumerate(flip_7_game.players):
        if player.get_total_score() > biggest_score:
            biggest_score = player.get_total_score()
            winner_num = idx + 1

    display.destroy_game_buttons()
    display.draw_end_screen(canvas, winner_num, biggest_score)

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
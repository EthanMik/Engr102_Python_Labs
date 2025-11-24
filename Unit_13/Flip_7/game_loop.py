from tkinter import *
from player import Player
from game import Game

def build_deck() -> list:
    deck = []
    with open("Unit_13/Flip_7/deck.txt", "r") as file:
        for line in file:
            for card in line.strip().split(' '):
                card_value = int(card.strip())
                deck.append(card_value)
    return deck

FLIP_7_DECK = build_deck()

def game_loop(root):
    player_1 = Player("Player 1")
    player_2 = Player("Player 2")
    player_3 = Player("Player 3")
    player_4 = Player("Player 4")

    flip_7_game = Game([player_1, player_2, player_3, player_4], FLIP_7_DECK)
    ROUNDS = 7

    for _ in range(ROUNDS):
        flip_7_game.start_round()
        while not flip_7_game.round_over():
            for player in flip_7_game.players:
                if not player.turn_over():
                    print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})")
                    choice = input(f"{player.name}, Enter 'h' to hit or 's' to stand: ")
                    if choice == 'h':
                        busted = player.hit(flip_7_game.current_deck)
                        if busted:
                            print(f"{player.name} drew a duplicate card and is busted!")
                        
                    elif choice == 's':
                        player.stand()

                    print(f"{player.name}'s hand: {player.show_hand()} (Score: {player.calculate_score()})\n")

        print("Round over! Scores:")
        for player in flip_7_game.players:
            player.add_to_total_score(player.calculate_score())
            print(f"{player.name}: {player.get_total_score()} points")
            player.reset_hand()
        print("\nStarting new round...\n")


def main():
    # window = Tk()
    # window.title("Flip 7")
    # window.geometry("1280x720")
    # img = PhotoImage(file="Unit_13/Flip 7/assets/0_card.png")
    # label = Label(window, image=img)
    # label.pack()

    # window.mainloop()
    game_loop(None)

if __name__ == "__main__":
    main()
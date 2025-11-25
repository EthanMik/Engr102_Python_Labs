import tkinter as tk
from PIL import Image, ImageTk
from player import Player
from util import *

card_images = []

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

hit_button = None
stand_button = None

def create_game_buttons():
    global hit_button, stand_button

    hit_img = tk.PhotoImage(file=resource_path("assets/hit_button.png"))
    hit_hover_img = tk.PhotoImage(file=resource_path("assets/hit_button_hover.png"))

    stand_img = tk.PhotoImage(file=resource_path("assets/stand_button.png"))
    stand_hover_img = tk.PhotoImage(file=resource_path("assets/stand_button_hover.png"))

    def on_enter_hit(e):
        e.widget.config(image=hit_hover_img)

    def on_leave_hit(e):
        e.widget.config(image=hit_img)

    def on_enter_stand(e):
        e.widget.config(image=stand_hover_img)

    def on_leave_stand(e):
        e.widget.config(image=stand_img)

    card_images.append([hit_img, hit_hover_img, stand_img, stand_hover_img])
    hit_button = tk.Button(command=on_hit, image=hit_img, relief="flat", borderwidth=0, highlightthickness=0)
    hit_button.place(x=1030, y=27)

    stand_button = tk.Button(command=on_stand, image=stand_img, relief="flat", borderwidth=0, highlightthickness=0)
    stand_button.place(x=1030, y=102)

    hit_button.bind("<Enter>", on_enter_hit)
    hit_button.bind("<Leave>", on_leave_hit)

    stand_button.bind("<Enter>", on_enter_stand)
    stand_button.bind("<Leave>", on_leave_stand)

def destroy_game_buttons():
    global hit_button, stand_button
    if hit_button:
        hit_button.destroy()
        hit_button = None
    if stand_button:
        stand_button.destroy()
        stand_button = None

ROUNDS = 7
PLAYERS = 4

def start_game():
    global PAUSED
    PAUSED = False

def decrement_round():
    global ROUNDS
    if ROUNDS > 1:
        ROUNDS -= 1

def inrecment_round():
    global ROUNDS
    if ROUNDS >= 0:
        ROUNDS += 1

def decrement_players():
    global PLAYERS
    if PLAYERS > 1:
        PLAYERS -= 1

def increment_players():
    global PLAYERS
    if PLAYERS < 4:
        PLAYERS += 1

increase_round_button = None
decrease_round_button = None
increment_players_button = None
decrement_players_button = None
start_button = None

def create_start_buttons():
    global increase_round_button, decrease_round_button
    global increment_players_button, decrement_players_button
    global start_button

    decrement_img = tk.PhotoImage(file=resource_path("assets/decrement_button.png"))
    decrement_img_hover = tk.PhotoImage(file=resource_path("assets/decrement_button.png"))

    increment_img = tk.PhotoImage(file=resource_path("assets/increment_button.png"))
    increment_img_hover = tk.PhotoImage(file=resource_path("assets/increment_button.png"))

    start_img = tk.PhotoImage(file=resource_path("assets/start_button.png"))
    start_img_hover = tk.PhotoImage(file=resource_path("assets/start_button.png"))

    def on_enter_in(e):
        e.widget.config(image=increment_img_hover)

    def on_leave_in(e):
        e.widget.config(image=increment_img)

    def on_enter_dec(e):
        e.widget.config(image=decrement_img_hover)

    def on_leave_dec(e):
        e.widget.config(image=decrement_img)

    card_images.append([decrement_img, decrement_img_hover, increment_img, increment_img_hover, start_img, start_img_hover])

    increase_round_button = tk.Button(command=inrecment_round, image=increment_img, relief="flat", borderwidth=0, highlightthickness=0)
    increase_round_button.place(x=743, y=269)
    decrease_round_button = tk.Button(command=decrement_round, image=decrement_img, relief="flat", borderwidth=0, highlightthickness=0)
    decrease_round_button.place(x=486, y=269)

    increment_players_button = tk.Button(command=increment_players, image=increment_img, relief="flat", borderwidth=0, highlightthickness=0)
    increment_players_button.place(x=743, y=360)
    decrement_players_button = tk.Button(command=decrement_players, image=decrement_img, relief="flat", borderwidth=0, highlightthickness=0)
    decrement_players_button.place(x=486, y=360)

    start_button = tk.Button(command=start_game, image=start_img, relief="flat", borderwidth=0, highlightthickness=0)
    start_button.place(x=536, y=463)

    increase_round_button.bind("<Enter>", on_enter_in)
    increase_round_button.bind("<Leave>", on_leave_in)

    decrease_round_button.bind("<Enter>", on_enter_dec)
    decrease_round_button.bind("<Leave>", on_leave_dec)

    increment_players_button.bind("<Enter>", on_enter_in)
    increment_players_button.bind("<Leave>", on_leave_in)

    decrement_players_button.bind("<Enter>", on_enter_dec)
    decrement_players_button.bind("<Leave>", on_leave_dec)

def destroy_start_buttons():
    global increase_round_button, decrease_round_button
    global increment_players_button, decrement_players_button
    global start_button

    if increase_round_button:
        increase_round_button.destroy()
        increase_round_button = None
    if decrease_round_button:
        decrease_round_button.destroy()
        decrease_round_button = None
    if increment_players_button:
        increment_players_button.destroy()
        increment_players_button = None
    if decrement_players_button:
        decrement_players_button.destroy()
        decrement_players_button = None
    if start_button:
        start_button.destroy()
        start_button = None

def draw_start_text(canvas: tk.Canvas):
    canvas.create_text(650, 275+20, text=f"Rounds: {ROUNDS}  ", font=("Helvetica", 20), fill="white")
    canvas.create_text(645, 365+20, text=f"Players: {PLAYERS}", font=("Helvetica", 20), fill="white")

def load_card_image(card_value: int) -> tk.PhotoImage:
    img_path = resource_path(f"assets/{card_value}_card.png")
    card_image = tk.PhotoImage(file=img_path)
    card_images.append(card_image)
    return card_image

def reset():
    card_images.clear()

def draw_round(canvas: tk.Canvas, round_num: int):
    global ROUNDS
    round_label = tk.Label(canvas, text=f"Round {round_num}/{ROUNDS}", font=("Helvetica", 30), bg="#4090B6", fg="white")
    round_label.place(x=800, y=35)

def draw_title(canvas: tk.Canvas):
    logo = tk.PhotoImage(file=resource_path("assets/flip_7_logo.png"))
    card_images.append(logo)
    canvas.create_image(480, 12, anchor="nw", image=logo)

def draw_rules(canvas: tk.Canvas):
    rules_text = (
    "How to play:\n"
    "• Flip cards to build a total as close to 7 as you dare.\n"
    "• Click Hit to flip a new card.\n"
    "• Click Stand to stop; your score is the sum of your cards.\n"
    "• If you flip a duplicate number, you bust and score 0 for the round.\n"
    "• The higher the card number the more common that card is.\n"
    "• After everyone stands or busts, highest score (up to 7) wins."
    )

    rules_label = tk.Label(canvas, text=rules_text, font=("Helvetica", 12), bg="#4090B6", fg="white", justify="left", anchor="nw")
    rules_label.place(x=20, y=15)

def draw_text(canvas: tk.Canvas, players: list[Player]):
    positions = [(30, 170), (651, 170), (30, 353), (651, 353)]
    for idx, player in enumerate(players):
        player_info = tk.Label(canvas, text=f"Player {idx + 1}, Score: {player.get_total_score()}", font=("Helvetica", 16), bg="#4090B6", fg="white")
        x, y = positions[idx]
        player_info.place(x=x, y=y)

def draw_hand(canvas: tk.Canvas, x: int, y: int, bg_color, outline_color, hand: list[int], player: Player, selected: bool = False):
    w = 560
    h = 140
    x2 = x + w
    y2 = y + h

    if selected: outline_color = "yellow"
    canvas.create_rectangle(x, y, x2, y2, fill=bg_color, outline=outline_color, width=4)

    if len(hand) == 0:
        for i in range(player.card_num):
            card_back = tk.PhotoImage(file=resource_path("assets/card_back.png"))
            card_images.append(card_back)
            canvas.create_image(x + 32 + i * (7 + card_back.width()), y + 28, anchor="nw", image=card_back)

    for i, card_value in enumerate(hand):
        card_image = load_card_image(card_value)
        canvas.create_image(x + 32 + i * (7 + card_image.width()), y + 28, anchor="nw", image=card_image)

def draw_end_screen(canvas: tk.Canvas, winner_num: int, score: int):
    for child in canvas.winfo_children(): # clearing my tech debt 💀
        child.destroy()

    img = tk.PhotoImage(file=resource_path("assets/end_screen.png"))
    card_images.append(img)
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.create_text(200, 200, text=f"Player {winner_num} with a score of {score} has won!", font=("Helvetica", 40), fill="white", anchor="nw")
    canvas.pack()
    canvas.update()

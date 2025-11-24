import tkinter as tk
from PIL import Image, ImageTk
from player import Player

card_images = []

def load_card_image(card_value: int) -> tk.PhotoImage:
    img_path = f"Unit_13/Flip_7/assets/{card_value}_card.png"
    card_image = tk.PhotoImage(file=img_path)
    card_images.append(card_image)
    return card_image

def reset():
    card_images.clear()

def draw_title(canvas: tk.Canvas):
    logo = tk.PhotoImage(file="Unit_13/Flip_7/assets/flip_7_logo.png")
    card_images.append(logo)
    canvas.create_image(480, 12, anchor="nw", image=logo)

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
            card_back = tk.PhotoImage(file="Unit_13/Flip_7/assets/card_back.png")
            card_images.append(card_back)
            canvas.create_image(x + 32 + i * (7 + card_back.width()), y + 28, anchor="nw", image=card_back)

    for i, card_value in enumerate(hand):
        card_image = load_card_image(card_value)
        canvas.create_image(x + 32 + i * (7 + card_image.width()), y + 28, anchor="nw", image=card_image)
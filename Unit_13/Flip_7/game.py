from player import Player

class Game:
    def __init__(self, players: list[Player], deck: list):
        self.players = players
        self.deck = deck
        self.current_deck = deck.copy()
    
    def shuffle_deck(self):
        import random
        random.shuffle(self.current_deck)
    
    def deal_initial_hands(self):
        for _ in range(1):
            for player in self.players:
                player.hit(self.current_deck)

    def start_round(self):
        self.current_deck = self.deck.copy()
        self.shuffle_deck()
        self.deal_initial_hands()
    
    def round_over(self) -> bool:
        count = 0
        for player in self.players:
            if not player.turn_over():
                count += 1
        if count <= 0:
            return True
        return False    
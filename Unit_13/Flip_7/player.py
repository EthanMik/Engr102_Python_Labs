class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.card_num = 0
        self.standing = False
        self.busted = False
        self.total_score = 0
    
    def hit(self, deck: list) -> bool:
        card = deck.pop()
        self.card_num += 1
        if self.hand.count(card) >= 1:
            self.busted = True
        self.hand.append(card)
        
    def is_busted(self) -> bool:
        if self.busted:
            self.hand.clear()
        return self.busted

    def stand(self):
        self.standing = True

    def show_hand(self):
        return self.hand
    
    def calculate_score(self):
        return sum(self.hand)
    
    def add_to_total_score(self, score):
        self.total_score += score

    def get_total_score(self):
        return self.total_score
    
    def reset_hand(self):
        self.hand = []
        self.card_num = 0
        self.standing = False
        self.busted = False

    def turn_over(self) -> bool:
        if len(self.hand) >= 7 or self.busted or self.standing:
            return True
        return False
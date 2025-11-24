class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.standing = False
        self.busted = False
        self.total_score = 0
    
    def hit(self, deck: list) -> bool:
        card = deck.pop()
        if not self.hand.count(card) >= 1:
            self.hand.append(card)
            return False
        
        self.busted = True
        self.hand.clear()
        return True

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
        self.standing = False
        self.busted = False

    def turn_over(self) -> bool:
        if len(self.hand) >= 7 or self.busted or self.standing:
            return True
        return False
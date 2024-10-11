import random

class Deck():
    def __init__(self):
        self.deck = list(range(52))
        self.top = 51
    
    def draw(self):
        select = random.randint(0, self.top)
        self.deck[select], self.deck[self.top] = self.deck[self.top], self.deck[select] 
        if self.top > 0:
            self.top -= 1 
            card_id = self.deck[self.top + 1]
            return (card_id % 13, card_id // 13) 
        return None
    
    def shuffle(self):
        self.top = 51

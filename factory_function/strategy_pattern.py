class Hand:
    def __init__(self, cards):
        self.cards = cards

    def value(self):
        return sum(card.value for card in self.cards)

    def is_blackjack(self):
        return self.value() == 21

    def is_bust(self):
        return self.value() > 21
    
class GameStrategy:
    def insurance(self, hand: Hand) -> bool:
        return False
    def split(self, hand: Hand) -> bool:
        return False
    def double(self, hand: Hand) -> bool:
        return False
    def hit(self, hand: Hand) -> bool:
        return sum(c.value for c in hand.cards) <= 17


 
def main():
    dumb = GameStrategy()
    pass

if __name__=="__main__":
    main()



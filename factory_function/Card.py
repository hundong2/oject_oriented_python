class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()
    def _points(self) -> tuple[int, int]:
        """Return the hard and soft points of the card."""
        if self.rank in ['J', 'Q', 'K']:
            return 10, 10
        elif self.rank == 'A':
            return 1, 11
        else:
            return int(self.rank), int(self.rank)
class AceCard(Card):
    def _points(self) -> tuple[int, int]:
        """Return the hard and soft points of the Ace card."""
        return 1, 11
class FaceCard(Card):
    def _points(self) -> tuple[int, int]:
        """Return the hard and soft points of the face card."""
        return 10, 10
class NumberCard(Card):
    def _points(self) -> tuple[int, int]:
        """Return the hard and soft points of the number card."""
        return int(self.rank), int(self.rank)
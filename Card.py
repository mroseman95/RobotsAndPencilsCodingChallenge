from Rank import Rank
from Suit import Suit


class Card:
    """
    Card represents a standard playing card that contains a rank and a suit
    """

    def __init__(self, rank, suit):
        """
        @param rank: a Rank enum representing the rank of this card
        @param suit: a Suit enum representing the suit of this card
        """
        if not isinstance(rank, Rank):
            raise TypeError("Card rank must be of type Rank")

        self.rank = rank

        if not isinstance(suit, Suit):
            raise TypeError("Card suit must be of type Suit")

        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{} of {}".format(self.rank.name, self.suit.name)

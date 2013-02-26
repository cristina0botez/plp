import random

SUITES = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card(object):

    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, value):
        self._suite = suite

    def __eq__(self, another):
        return self._rank == another._rank and self._suite == another._suite

    def __repr__(self):
        return 'Card=(rank=%s,suite=%s)' % (self._rank, self._suite)

class Deck(object):

    def __init__(self):
        self._cards = []
        for suite in SUITES:
            for rank in RANKS:
                self._cards.append(Card(rank, suite))

    def popCard(self):
        return self._cards.pop()

    def shuffle(self):
        return random.shuffle(self._cards)

    def __repr__(self):
        return repr(self._cards)

    def __eq__(self, another):
        return self._cards == another._cards

    def __ne__(self, another):
        return self._cards != another._cards

class Dealer(object):

    def __init__(self):
        self._deck = Deck()

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, value):
        self._deck = value

    def dealPlayerHand(self):
        return (self.dealOneCard(), self.dealOneCard())

    def dealTableHand(self):
        return tuple([self.dealOneCard() for i in range(5)])

    def dealOneCard(self):
        return self._deck.popCard()

    def shuffleCards(self):
        return self._deck.shuffle()


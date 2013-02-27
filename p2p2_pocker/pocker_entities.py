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

    def __str__(self):
        return '%s of %s' % (self._rank, self._suite)

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
        cards = (self.dealOneCard(), self.dealOneCard())
        return Hand(cards)

    def dealTableHand(self):
        cards = tuple([self.dealOneCard() for i in range(5)])
        return Hand(cards)

    def dealOneCard(self):
        return self._deck.popCard()

    def shuffleCards(self):
        return self._deck.shuffle()

class Player(object):

    def __init__(self, name):
        self._name = name
        self._hand = None

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value

    def __repr__(self):
        return 'Player=(name=%s,%r)' % (self._name, self._hand)

    def __str__(self):
        return '%s has the following hand:\n%s' % (self._name, self._hand)

class Hand(object):

    def __init__(self, cards):
        self._cards = cards

    def __iter__(self):
        return iter(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return 'Hand=%s' % self._cards

    def __str__(self):
        cardsAsStrings = [str(card) for card in self._cards]
        return '\n'.join(cardsAsStrings)


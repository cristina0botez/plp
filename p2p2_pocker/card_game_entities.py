"""Module containing the entities involved in a generic card game."""

import random
from collections import namedtuple


BaseCard = namedtuple('BaseCard', ['suit', 'rank'])


class Card(BaseCard):
    """A card type based on suit/colour and rank."""

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)


class Deck(object):
    """A collection of Cards of different suits and ranks."""

    def __init__(self, suits, ranks):
        """Create a deck of cards from a given set of suits and ranks."""
        self._cards = [Card(suit, rank) for suit in suits
                for rank in ranks]

    def pop_card(self):
        """Remove and return the last card from the deck."""
        return self._cards.pop()

    def shuffle(self):
        return random.shuffle(self._cards)

    def __eq__(self, other):
        """
        Two decks are equal if they have the same cards in the same order.

        """
        return self._cards == other._cards

    def __ne__(self, other):
        """
        Two decks are not equal if the set of cards are different or if the
        cards are not in the same order.

        """
        return self._cards != other._cards

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return '%s(ranks=%r, suits=%r)' % (self.__class__.name,
                                            suits, ranks)

    def __str__(self):
        return str(self._cards)


class Player(object):
    """Card game player."""

    def __init__(self, name, hand=None):
        """
        Create a card game player with a mandatory name and an optional set of
        cards.

        """
        self._name = name
        self.hand = hand

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return '%s(name=%r, hand=%r)' % (self.__class__.__name__,
                                         self._name, self.hand)

    def __str__(self):
        return '%s has the following hand:\n%s' % (self._name, self.hand)


class Hand(object):
    """The set of cards owned by a player."""

    def __init__(self, cards):
        """
        Create the hand from a set of cards.
        The cards input must be a sized, iterable sequence.

        """
        self._cards = cards

    def __iter__(self):
        return iter(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return '%s(cards=%r)' % (self.__class__.__name__, self._cards)

    def __str__(self):
        cardsAsStrings = [str(card) for card in self._cards]
        return '\n'.join(cardsAsStrings)


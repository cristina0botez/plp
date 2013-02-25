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

class Dealer(object):
    
    def deal_player_hand(self):
        return (Card('A', 'Diamonds'), Card('2', 'Spades'))


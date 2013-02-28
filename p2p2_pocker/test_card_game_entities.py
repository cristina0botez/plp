import unittest

class TestCardGameEntities(unittest.TestCase):

    def testShuffledDecksAreDifferent(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        deck2.shuffle()
        self.assertNotEqual(deck1, deck2)

import unittest

from pocker_entities import Dealer, Card

class TestTexasHoldemRules(unittest.TestCase):
    
    def setUp(self):
        self._dealer = Dealer()
        self._hand = self._dealer.deal_player_hand()
    
    def tearDown(self):
        del self._dealer
        del self._hand
    
    def testPlayerReceives2Cards(self):
        self.assertEqual(2, len(self._hand))

    def testPlayerReceivesValidCards(self):
        self._assertValidCard(self._hand[0])
        self._assertValidCard(self._hand[1])
    
    def testPlayerReceivesUniqueCards(self):
        self.assertNotEqual(self._hand[0], self._hand[1])
    
    def _assertValidCard(self, card):
        self.assertIn(card.rank, ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
        self.assertIn(card.suite, ['Spades', 'Hearts', 'Diamonds', 'Clubs'])


if __name__ == '__main__':
    unittest.main()


import unittest

from pocker_entities import Dealer, Card

class TestTexasHoldemRules(unittest.TestCase):

    def setUp(self):
        self._dealer = Dealer()

    def tearDown(self):
        del self._dealer

    def testTableHandReceives5Cards(self):
        hand = self._dealer.dealTableHand()
        self.assertEqual(5, len(hand))

    def testTableHandReceivesValidCards(self):
        hand = self._dealer.dealTableHand()
        self._assertValidHand(5, hand)

    def testPlayerHandReceives2Cards(self):
        hand = self._dealer.dealPlayerHand()
        self.assertEqual(2, len(hand))

    def testPlayerReceivesValidCards(self):
        hand = self._dealer.dealPlayerHand()
        self._assertValidHand(2, hand)

    def testPlayerReceivesUniqueCards(self):
        hand = self._dealer.dealPlayerHand()
        self.assertNotEqual(hand[0], hand[1])

    def testUniqueCardsAreDealtFromOneDeck(self):
        dealtCards = []
        for i in range(52):
            dealtCards.append(self._dealer.dealOneCard())
        self._assertUniqueCards(dealtCards)

    def _assertUniqueCards(self, deck):
        for i, card in zip(range(52), deck):
            self.assertNotIn(card, deck[:i])

    def _assertValidHand(self, handSize, hand):
        for i in range(handSize):
            self._assertValidCard(hand[i])

    def _assertValidCard(self, card):
        self.assertIn(card.rank, ['2', '3', '4', '5', '6', '7', '8',
                                  '9', '10', 'J', 'Q', 'K', 'A'])
        self.assertIn(card.suite, ['Spades', 'Hearts', 'Diamonds', 'Clubs'])


if __name__ == '__main__':
    unittest.main()


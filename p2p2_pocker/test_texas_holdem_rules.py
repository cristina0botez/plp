import unittest

from pocker_entities import Dealer, Deck, Card

class TestTexasHoldemRules(unittest.TestCase):

    def setUp(self):
        self._dealer = Dealer()

    def tearDown(self):
        del self._dealer

    def testTableHandReceives5Cards(self):
        hand = self._dealer.dealTableHand()
        self.assertEqual(len(hand), 5)

    def testTableHandReceivesValidCards(self):
        hand = self._dealer.dealTableHand()
        self._assertValidHand(hand)

    def testPlayerHandReceives2Cards(self):
        hand = self._dealer.dealPlayerHand()
        self.assertEqual(len(hand), 2)

    def testPlayerReceivesValidCards(self):
        hand = self._dealer.dealPlayerHand()
        self._assertValidHand(hand)

    def testPlayerReceivesUniqueCards(self):
        hand = self._dealer.dealPlayerHand()
        self.assertNotEqual(hand[0], hand[1])

    def testUniqueCardsAreDealtFromOneDeck(self):
        dealtCards = [self._dealer.dealOneCard() for i in range(52)]
        self._assertUniqueCards(dealtCards)

    def testCardsAreShuffled(self):
        initialDeck = Deck()
        self._dealer.shuffleCards()
        shuffledDeck = self._dealer.deck
        self.assertNotEqual(shuffledDeck, initialDeck)

    def testShuffledDecksAreDifferent(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        deck2.shuffle()
        self.assertNotEqual(deck1, deck2)

    def testDeckHasExactly52Cards(self):
        deck = Deck()
        for i in range(52):
            deck.popCard()
        with self.assertRaises(IndexError) as outcome:
            deck.popCard()
        ie = outcome.exception
        self.assertEqual(ie.message, 'pop from empty list')

    def testDealerMayGiveOutUpTo52Cards(self):
        for i in range(52):
            self._dealer.dealOneCard()
        with self.assertRaises(IndexError) as outcome:
            self._dealer.dealOneCard()
        ie = outcome.exception
        self.assertEqual(ie.message, 'pop from empty list')

    def _assertUniqueCards(self, deck):
        for i, card in zip(range(52), deck):
            self.assertNotIn(card, deck[:i])

    def _assertValidHand(self, hand):
        for card in hand:
            self._assertValidCard(card)

    def _assertValidCard(self, card):
        self.assertIn(card.rank, ['2', '3', '4', '5', '6', '7', '8',
                                  '9', '10', 'J', 'Q', 'K', 'A'])
        self.assertIn(card.suite, ['Spades', 'Hearts', 'Diamonds', 'Clubs'])


if __name__ == '__main__':
    unittest.main()


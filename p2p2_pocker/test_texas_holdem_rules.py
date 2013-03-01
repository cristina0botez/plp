import unittest

from card_game_entities import Deck
from texas_holdem import TexasHoldemDealer
import texas_holdem


SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class TestTexasHoldemRules(unittest.TestCase):

    def setUp(self):
        self.dealer = TexasHoldemDealer()

    def tearDown(self):
        del self.dealer

    def test_table_hand_receives_5_cards(self):
        hand = self.dealer.deal_table_hand()
        self.assertEqual(len(hand), 5)

    def test_table_hand_receives_valid_cards(self):
        hand = self.dealer.deal_table_hand()
        self.assertValidHand(hand)

    def test_player_hand_receives_2_cards(self):
        hand = self.dealer.deal_player_hand()
        self.assertEqual(len(hand), 2)

    def test_player_receives_valid_cards(self):
        hand = self.dealer.deal_player_hand()
        self.assertValidHand(hand)

    def test_unique_cards_are_dealt(self):
        dealt_cards = [self.dealer.deal_one_card() for i in range(52)]
        self.assertUniqueCards(dealt_cards)

    def test_cards_are_shuffled_correctly(self):
        initial_deck = Deck(SUITS, RANKS)
        self.dealer.shuffle_cards()
        shuffled_deck = self.dealer.deck
        self.assertNotEqual(shuffled_deck, initial_deck)

    def test_dealer_may_give_up_to_52_cards(self):
        for i in range(52):
            self.dealer.deal_one_card()
        with self.assertRaises(IndexError) as outcome:
            self.dealer.deal_one_card()
        ie = outcome.exception
        self.assertEqual(ie.message, 'pop from empty list')

    def assertUniqueCards(self, deck):
        for i, card in zip(range(52), deck):
            self.assertNotIn(card, deck[:i])

    def assertValidHand(self, hand):
        for card in hand:
            self.assertValidPockerCard(card)

    def assertValidPockerCard(self, card):
        self.assertIn(card.rank, RANKS)
        self.assertIn(card.suit, SUITS)


class TestPlayerRegistration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name_registration_returns_the_players(self):
        playerNames = ['Albert', 'Bob', 'Jim']
        players = texas_holdem.register_players(playerNames)
        self.assertEqual([player.name for player in players], playerNames)

    def test_register_one_player_raises_error(self):
        with self.assertRaises(ValueError) as outcome:
            texas_holdem.register_players(['Bob'])
        ve = outcome.exception
        self.assertEqual(ve.message,
                         'Not enough players. A minimum of 2 is required.')

    def test_register_10_players_raises_error(self):
        with self.assertRaises(ValueError) as outcome:
            texas_holdem.register_players(['Bob'] * 10)
        ve = outcome.exception
        self.assertEqual(ve.message, 'Too many players. At most 9 players can'
                ' join the game.')


if __name__ == '__main__':
    unittest.main()


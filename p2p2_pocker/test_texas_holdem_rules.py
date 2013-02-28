import unittest

from card_game_entities import Deck, Card
from texas_holdem import TexasHoldemDealer


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


class TestAutomatedDealer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reading_empty_string_for_name_raises_error(self):
        stdin_mock = open(STDIN_MOCK_FILENAME, 'w')
        stdin_mock.write('\n')
        stdin_mock.close()
        sys.stdin = open(STDIN_MOCK_FILENAME, 'r')
        sys.stdout = open(STDOUT_MOCK_FILENAME, 'w')
        with self.assertRaises(ValueError) as outcome:
            texas_holdem.read_player_name(1)
        ve = outcome.exception
        self.assertEqual(ve.message, 'No name given')
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        sys.stdin.close()
        sys.stdin = sys.__stdin__

    def test_return_players_read_from_input(self):
        PLAYER_NAMES = ('Bob', 'Nick', 'Jenny')
        self._set_up_io_for_registration(PLAYER_NAMES)
        players = texas_holdem.registerPlayers()
        self._assertCorrectPlayers(players, PLAYER_NAMES)
        self._tearDownIOForRegistration()

    def testInputOnlyOnePlayerThrowsError(self):
        PLAYER_NAMES = ('Bob',)
        self._setUpIOForRegistration(PLAYER_NAMES)
        with self.assertRaises(texas_holdem.RegistrationError) as outcome:
            texas_holdem.registerPlayers()
        re = outcome.exception
        self.assertEqual(re.message,
                'Not enough players. A minimum of 2 is required.')
        self._tearDownIOForRegistration()

    def testEachPlayerReceives2Cards(self):
        players = (Player('Bob'), Player('Nick'), Player('Jenny'))
        texas_holdem.distributeCardsToPlayers(Dealer(), players)
        self._assertCorrectCardToPlayerDistribution(players)

    def testTableReceives5Cards(self):
        tableHand = texas_holdem.setCardsOnTable(Dealer())
        self.assertEqual(len(tableHand), 5)

    def _assertCorrectPlayers(self, actualPlayers, expectedNames):
        self.assertEqual(len(expectedNames), len(actualPlayers))
        for player in actualPlayers:
            self.assertIn(player.name, expectedNames)

    def _assertCorrectCardToPlayerDistribution(self, players):
        for player in players:
            self.assertEqual(len(player.hand), 2)

    def _setUpIOForRegistration(self, namesList):
        playerNamesFile = open(PLAYER_NAMES_FILENAME, 'w')
        playerNamesFile.writelines(['%s\n' % name for name in namesList])
        playerNamesFile.write('\n')
        playerNamesFile.close()
        sys.stdin = open(PLAYER_NAMES_FILENAME, 'r')
        sys.stdout = open(REGISTRATION_OUTPUT_FILENAME, 'w')

    def _tearDownIOForRegistration(self):
        sys.stdin.close()
        sys.stdout.close()
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        os.remove(PLAYER_NAMES_FILENAME)
        os.remove(REGISTRATION_OUTPUT_FILENAME)


if __name__ == '__main__':
    unittest.main()


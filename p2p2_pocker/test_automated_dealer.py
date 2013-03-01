"""This module tests the functionality used in the 
"""
import unittest
import sys
import os

from card_game_entities import Player, Hand, Card
from texas_holdem import TexasHoldemDealer
import texas_holdem


STDIN_MOCK_FILENAME = 'stdin_mock.tmp'
STDOUT_MOCK_FILENAME = 'stdout_mock.tmp'


class TestInputReader(unittest.TestCase):

    def tearDown(self):
        self._reset_io_environment()
        os.remove(STDIN_MOCK_FILENAME)
        os.remove(STDOUT_MOCK_FILENAME)

    def test_trailing_spaces_removed_from_name(self):
        self._prepare_io_environment('  Albert   \n')
        name = texas_holdem.read_player_name(1)
        self.assertEqual(name, 'Albert')

    def test_reading_empty_string_for_name_raises_error(self):
        self._prepare_io_environment('\n')
        with self.assertRaises(ValueError) as outcome:
            texas_holdem.read_player_name(1)
        ve = outcome.exception
        self.assertEqual(ve.message, 'No name given')

    def test_read_names_are_unique(self):
        self._prepare_io_environment('Bob\nLucy\nBob\n\n')
        names = texas_holdem.read_all_player_names()
        self.assertEquals(names, set(['Bob', 'Lucy']))

    def _provision_input(self, input_text):
        stdin_mock = open(STDIN_MOCK_FILENAME, 'w')
        stdin_mock.write(input_text)
        stdin_mock.close()

    def _prepare_io_environment(self, input_text):
        self._provision_input(input_text)
        sys.stdin = open(STDIN_MOCK_FILENAME, 'r')
        sys.stdout = open(STDOUT_MOCK_FILENAME, 'w')

    def _reset_io_environment(self):
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        sys.stdin.close()
        sys.stdin = sys.__stdin__


class TestAutomatedDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = TexasHoldemDealer()

    def test_each_player_receives_cards(self):
        players = [Player('Ane'), Player('Bill')]
        players = texas_holdem.distribute_cards_to_players(self.dealer,
                                                           players)
        self.assertEveryPlayerHasCards(players)

    def test_player_list_remains_unchanged(self):
        players = (Player('Ane'), Player('Bill'))
        result = texas_holdem.distribute_cards_to_players(self.dealer,
                                                          players)
        self.assertEqual(len(result), len(players))

    def assertEveryPlayerHasCards(self, players):
        for player in players:
            self.assertIsNotNone(player.hand)


class TestCardDisplay(unittest.TestCase):

    def setUp(self):
        self.table_hand = Hand([Card('Diamonds', '3'),
                                Card('Clubs', 'A'),
                                Card('Clubs', '5'),
                                Card('Spades', 'Q'),
                                Card('Diamonds', '8')])
        bob = Player(name='Bob', hand=Hand([Card('Hearts', 'A'),
                                            Card('Diamonds', '9')]))
        jim = Player(name='Jim', hand=Hand([Card('Spades', 'K'),
                                            Card('Spades', 'J')]))
        self.players = [bob, jim]

    def test_all_cards_are_displayed(self):
        result = texas_holdem.serialize_cards(self.table_hand, self.players)
        self.assertEqual(result, '''
Cards on table:
3 of Diamonds
A of Clubs
5 of Clubs
Q of Spades
8 of Diamonds

Bob has the following hand:
A of Hearts
9 of Diamonds

Jim has the following hand:
K of Spades
J of Spades
''')


if __name__ == '__main__':
    unittest.main()


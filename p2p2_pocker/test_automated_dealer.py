import unittest
import sys
import os

import texas_holdem
from pocker_entities import Player, Dealer

PLAYER_NAMES_FILENAME = 'player_names.tmp'
REGISTRATION_OUTPUT_FILENAME = 'registration_output.tmp'

class TestAutomatedDealer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReturnPlayersReadFromInput(self):
        PLAYER_NAMES = ('Bob', 'Nick', 'Jenny')
        self._setUpIOForRegistration(PLAYER_NAMES)
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


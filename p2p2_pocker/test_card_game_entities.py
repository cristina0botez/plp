import unittest

from card_game_entities import Deck

class TestCardGameEntities(unittest.TestCase):

    def setUp(self):
        suits = ['A', 'B']
        ranks = ['1', '2', '3', '4']
        self.deck1 = Deck(suits, ranks)
        self.deck2 = Deck(suits, ranks)

    def test_shuffled_decks_of_same_type_are_not_equal(self):
        self.deck1.shuffle()
        self.deck2.shuffle()
        self.assertNotEqual(self.deck1, self.deck2)

    def test_initial_decks_with_same_cards_are_equal(self):
        self.assertEqual(self.deck1, self.deck2)

    def test_popping_a_card_removes_it_from_the_deck(self):
        initial_size = len(self.deck1)
        self.deck1.pop_card()
        self.assertEqual(len(self.deck1), initial_size - 1)


if __name__ == '__main__':
    unittest.main()


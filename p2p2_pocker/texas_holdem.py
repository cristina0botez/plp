"""
Problem statement:

Create an automated card dealer for a Texas Hold'em application. It should be
able to handle Deck objects, consisting of Cards. Cards can be added or
removed from Decks, and Decks can be shuffled and sorted. When dealing cards,
each Player receives a Hand consisting of 2 Cards. After all cards are dealt,
the Dealer should draw the table Hand of 5 Cards.

"""


import sys
from card_game_entities import Card, Deck, Player, Hand


SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class TexasHoldemDealer(object):
    """Entity that coordinates a Texas Hold'em Pocker game."""
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)

    def deal_player_hand(self):
        """Gives out 2 cards (1 player hand) from the deck."""
        cards = (self.deal_one_card(), self.deal_one_card())
        return Hand(cards)

    def deal_table_hand(self):
        """Gives out 5 cards (the table hand) from the deck."""
        cards = [self.deal_one_card() for i in range(5)]
        return Hand(cards)

    def deal_one_card(self):
        return self.deck.pop_card()

    def shuffle_cards(self):
        return self.deck.shuffle()


def register_players(player_names):
    """
    Validates the number of players and registers them as Player entities.

    """
    if len(player_names) < 2:
        raise ValueError('Not enough players. A minimum of 2 is required.')
    elif len(player_names) > 9:
        raise ValueError(
                'Too many players. At most 9 players can join the game.')
    players = [Player(name) for name in player_names]
    print '%d players are in the game: %s' % (len(players), players)
    return tuple(players)


def read_all_player_names():
    """
    Reads the names of the players from the standard input.
    When an empty name is provided, the reading process will stop.
    Unique names must be provided.

    """
    names = set()
    print 'Input the names of each player. When done, input an empty name.'
    while True:
        try:
            name = read_player_name(len(names) + 1)
        except ValueError:
            break
        names.add(name)
    return names


def read_player_name(index):
    """
    Reads the name of a pocker player from the standard input.
    If an empty name is provided, a ValueError will be thrown.

    """
    user_input = raw_input('Player #%d: ' % index)
    user_input = user_input.strip()
    if user_input != '':
        return user_input
    else:
        raise ValueError('No name given')


def distribute_cards_to_players(dealer, players):
    """
    Provisions each player with a suitable hand of cards.
    The dealer must implement a deal_player_hand() method that provides a hand
    of cards appropriate for the game.
    The player must have a hand property used to store the set of cards.

    """
    for player in players:
        player.hand = dealer.deal_player_hand()
    return players


def serialize_cards(table_hand, players):
    """Serialize the dealt cards in a string."""
    table_cards = '\nCards on table:\n%s\n' % str(table_hand)
    player_cards = ['\n%s\n' % player for player in players]
    result = table_cards + ''.join(player_cards)
    return result


def runner():
    """Runs the automated Texas Hold'em dealer."""
    player_names = read_all_player_names()
    try:
        players = register_players(player_names)
    except ValueError, re:
        print re.message
        sys.exit(0)
    dealer = TexasHoldemDealer()
    dealer.shuffle_cards()
    players = distribute_cards_to_players(dealer, players)
    table_hand = dealer.deal_table_hand()
    print serialize_cards(table_hand, players)


if __name__ == '__main__':
    runner()


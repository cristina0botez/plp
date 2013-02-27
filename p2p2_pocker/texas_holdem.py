from pocker_entities import Card, Deck, Dealer, Player

class RegistrationError(Exception):
    pass

def registerPlayers():
    print 'Input the names of each player. When done, input an empty name.'
    playerNames = readAllPlayerNames()
    if len(playerNames) < 2:
        raise RegistrationError(
                'Not enough players. A minimum of 2 is required.')
    elif len(playerNames) > 9:
        raise RegistrationError(
                'Too many players. At most 9 players can join the game')
    players = [Player(name) for name in playerNames]
    print '%d players are in the game: %s' % (len(players), players)
    return tuple(players)

def readAllPlayerNames():
    names = set()
    try:
        while True:
            name = readPlayerName(len(names) + 1)
            names.add(name)
    except RegistrationError, re:
        pass
    return names

def readPlayerName(index):
    userInput = raw_input('Player #%d: ' % index)
    userInput = userInput.strip()
    if userInput != '':
        return userInput
    else:
        raise RegistrationError('No name given')

def distributeCardsToPlayers(dealer, players):
    for player in players:
        player.hand = dealer.dealPlayerHand()
    return players

def setCardsOnTable(dealer):
    return dealer.dealTableHand()

def displayCards(tableHand, players):
    print '\nCards on table:\n%s\n' % str(tableHand)
    for player in players:
        print '%s\n' % player

def runner():
    players = None
    try:
        players = registerPlayers()
    except RegistrationError, re:
        print re.message
    else:
        dealer = Dealer()
        dealer.shuffleCards()
        distributeCardsToPlayers(dealer, players)
        tableHand = setCardsOnTable(dealer)
        displayCards(tableHand, players)


if __name__ == '__main__':
    runner()


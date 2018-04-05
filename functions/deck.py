from random import shuffle
from functions.subfunctions.split_file import split_file


NEW_DECK = split_file('standarddeck')
DECK_OF_MANY_THINGS = split_file('domt')
HARROW_DECK = split_file('harrowdeck')


def parse_deck_request(msg, thisdeck):
    subcommand = ''
    try:
        trash, command, subcommand = str(msg.content).split(' ')
    except ValueError:
        trash, command = str(msg.content).split(' ')
    if command.startswith('new'):
        thisdeck = NEW_DECK.copy()
        shuffle(thisdeck)
        return thisdeck, 'Deck remade!'
    elif command.startswith('shuffle'):
        shuffle(thisdeck)
        return thisdeck, 'Shuffle complete!'
    elif command.startswith('change'):
        newstate = ''
        if subcommand.startswith('domt'):
            newstate = 'the Deck of Many Things!'
            thisdeck = DECK_OF_MANY_THINGS.copy()
            shuffle(thisdeck)
        elif subcommand.startswith('normal'):
            newstate = 'a regular deck of playing cards.'
            thisdeck = NEW_DECK.copy()
            shuffle(thisdeck)
        elif subcommand.startswith('harrow'):
            newstate = 'the harrow deck!'
            thisdeck = HARROW_DECK.copy()
            shuffle(thisdeck)
        return thisdeck, 'Deck changed to ' + newstate
    elif command.startswith('draw'):
        if len(thisdeck) < 1:
            return None, 'Deck is empty!'
        hand = []
        if subcommand is not '':
            num = int(subcommand)
        else:
            num = 1
        for i in range(num):
            try:
                card = thisdeck.pop()
            except IndexError:
                return thisdeck, str(hand) + '... Ran out of cards!'
            hand.append(card)
        return thisdeck, str(hand)
    elif command.startswith('left'):
        return None, 'This deck has ' + str(len(thisdeck)) + " cards left."
    elif command.startswith(''):
        return None, 'Available commands: new, shuffle, draw num, left'

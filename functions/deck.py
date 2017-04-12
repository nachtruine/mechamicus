from random import shuffle
NEW_DECK = ['Joker (Colored)', 'Joker (Uncolored)',
            '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds',
            '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
            'King of Diamonds', 'Ace of Diamonds',
            '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs',
            '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs',
            'King of Clubs', 'Ace of Clubs',
            '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts',
            '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
            'King of Hearts', 'Ace of Hearts',
            '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades',
            '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades',
            'King of Spades', 'Ace of Spades'
            ]
deck_of_many_things = ['Balance - Change alignment instantly. If you fail to act accordingly, gain a negative level.',
                       'Comet - Defeat the next monster single-handedly you meet to gain one level.',
                       'Donjon - Become imprisoned. All gear and spells are stripped. Draw no more cards.',
                       'Eurayle - –1 penalty on all saving throws permanently.',
                       'The Fates - You, and only you, may avoid any situation you choose, once.',
                       'Flames - Gain the enmity of an outsider.',
                       'Fool - Lose 10,000 experience points and you must draw again. Discard this card from the deck.',
                       'Gem - Gain your choice of 25 pieces of jewelry or 50 gems, for a total of 50,000 gp.',
                       'Idiot - Lose 1d4+1 Intelligence. You may draw again.',
                       'Jester - Gain 10,000 XP or two more draws from the deck. Discard this card from the deck.',
                       'Key - Gain a major magic weapon.',
                       'Knight - Gain the service of a loyal 4th-level fighter.',
                       'Moon - You are granted 1d4 wishes.',
                       'Rogue - One of your friends turns against you.',
                       'Ruin - Immediately lose all non-magical wealth and property.',
                       'Skull - Defeat a dread wraith in single combat or be forever destroyed.',
                       'Star - Immediately gain a +2 inherent bonus to one ability score.',
                       'Sun - Gain beneficial medium wondrous item and 50,000 XP.',
                       'Talons - All magic items you possess disappear permanently.',
                       'Throne - Gain a +6 bonus on Diplomacy checks plus a small castle.',
                       'Vizier - Know the answer to your next dilemma.',
                       'The Void - Your soul is sucked from your body and placed in another plane. Draw no more cards.']


def parseDeckRequest(msg, thisdeck):
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
            thisdeck = deck_of_many_things.copy()
            shuffle(thisdeck)
        elif subcommand.startswith('normal'):
            newstate = 'a regular deck of playing cards.'
            thisdeck = NEW_DECK.copy()
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

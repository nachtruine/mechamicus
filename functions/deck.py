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
deck_of_many_things = ['Balance - Change alignment instantly. The character must change to a radically different alignment. If the character fails to act according to the new alignment, she gains a negative level.',
                       'Comet - Defeat the next monster you meet to gain one level. The character must single-handedly defeat the next hostile monster or monsters encountered, or the benefit is lost. If successful, the character gains enough XP to attain the next experience level.',
                       'Donjon - You are imprisoned. This card signifies imprisonment—either by the imprisonment spell or by some powerful being. All gear and spells are stripped from the victim in any case. Draw no more cards.',
                       'Eurayle - –1 penalty on all saving throws henceforth. The medusa-like visage of this card brings a curse that only the Fates card or a deity can remove. The —1 penalty on all saving throws is otherwise permanent.',
                       'The Fates - Avoid any situation you choose, once. This card enables the character to avoid even an instantaneous occurrence if so desired, for the fabric of reality is unraveled and respun. Note that it does not enable something to happen. It can only stop something from happening or reverse a past occurrence. The reversal is only for the character who drew the card; other party members may have to endure the situation.',
                       'Flames - Enmity between you and an outsider. Hot anger, jealousy, and envy are but a few of the possible motivational forces for the enmity. The enmity of the outsider can’t be ended until one of the parties has been slain. Determine the outsider randomly, and assume that it attacks the character (or plagues her life in some way) within 1d20 days.',
                       'Fool - Lose 10,000 experience points and you must draw again. The payment of XP and the redraw are mandatory. This card is always discarded when drawn, unlike all others except the Jester.',
                       'Gem - Gain your choice of 25 pieces of jewelry or 50 gems. This card indicates wealth. The jewelry is all gold set with gems, each piece worth 2,000 gp, and the gems are worth 1,000 gp each.',
                       'Idiot - Lose 1d4+1 Intelligence. You may draw again. This card causes the drain of 1d4+1 points of Intelligence immediately. The additional draw is optional.',
                       'Jester - Gain 10,000 XP or two more draws from the deck. This card is always discarded when drawn, unlike all others except the Fool. The redraws are optional.',
                       'Key - Gain a major magic weapon. The magic weapon granted must be one usable by the character. It suddenly appears out of nowhere in the character’s hand.',
                       'Knight - Gain the service of a 4th-level fighter. The fighter appears out of nowhere and serves loyally until death. He or she is of the same race (or kind) and gender as the character. This fighter can be taken as a cohort by a character with the Leadership feat.',
                       'Moon - You are granted 1d4 wishes. These wishes are the same as those granted by the 9th-level wizard spell and must be used within a number of minutes equal to the number received.',
                       'Rogue - One of your friends turns against you. When this card is drawn, one of the character’s NPC friends (preferably a cohort) is totally alienated and made forever hostile. If the character has no cohorts, the enmity of some powerful personage (or community, or religious order) can be substituted. The hatred is secret until the time is ripe for it to be revealed with devastating effect.',
                       'Ruin - Immediately lose all wealth and property. As implied by its name, when this card is drawn, all nonmagical possessions of the drawer are lost.',
                       'Skull - Defeat dread wraith or be forever destroyed. A dread wraith appears. Treat this creature as an unturnable undead. The character must fight it alone-if others help, they get dread wraiths to fight as well. If the character is slain, she is slain forever and cannot be revived, even with a wish or a miracle.',
                       'Star - Immediately gain a +2 inherent bonus to one ability score. The 2 points are added to any ability the character chooses. They cannot be divided among two abilities.',
                       'Sun - Gain beneficial medium wondrous item and 50,000 XP. Roll for a medium wondrous item until a useful item is indicated.',
                       'Talons - All magic items you possess disappear permanently. When this card is drawn, every magic item owned or possessed by the character is instantly and irrevocably gone.',
                       'Throne - Gain a +6 bonus on Diplomacy checks plus a small castle. The character becomes a true leader in people\'s eyes. The castle gained appears in any open area she wishes (but the decision where to place it must be made within 1 hour).',
                       'Vizier - Know the answer to your next dilemma. This card empowers the character drawing it with the one-time ability to call upon a source of wisdom to solve any single problem or answer fully any question upon her request. The query or request must be made within one year. Whether the information gained can be successfully acted upon is another question entirely.',
                       'The Void - Body functions, but soul is trapped elsewhere. This black card spells instant disaster. The character\'s body continues to function, as though comatose, but her psyche is trapped in a prison somewhere-in an object on a far plane or planet, possibly in the possession of an outsider. A wish or a miracle does not bring the character back, instead merely revealing the plane of entrapment. Draw no more cards. Strong (all schools); CL 20th.']


def shuffleDeck(deck):
    shuffle(deck)


def parseDeckRequest(msg, deck):
    subcommand = ''
    try:
        trash, command, subcommand = str(msg.content).split(' ')
    except ValueError:
        trash, command = str(msg.content).split(' ')
    if command.startswith('new'):
        deck = deck_of_many_things
        shuffleDeck(deck)
        return 'Deck remade!'
    elif command.startswith('shuffle'):
        shuffleDeck(deck)
        return 'Shuffle complete!'
    elif command.startswith('draw'):
        if len(deck) < 1:
            return 'Deck is empty!'
        hand = []
        if subcommand is not '':
            num = int(subcommand)
        else:
            num = 1
        for i in range(num):
            try:
                card = deck.pop()
            except IndexError:
                return str(hand) + '... Ran out of cards!'
            hand.append(card)
        return str(hand)
    elif command.startswith('left'):
        return 'This deck has ' + str(len(deck)) + " cards left."
    elif command.startswith(''):
        return 'Available commands: new, shuffle, draw num, left'

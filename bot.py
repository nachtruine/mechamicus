import random
import re
import discord
import sys

from datetime import datetime
from functions import db, deck, dice, gcs, quote
from functions.dice import total_dice_regex

token = sys.argv[1]

prefix = '/'
credo = ('There is no truth in flesh, only betrayal. ' +
         'There is no strength in flesh, only weakness. ' +
         'There is no constancy in flesh, only decay. ' +
         'There is no certainty in flesh but death.')
eight_ball = ['It is the will of the Omnissiah.',
              'The Omnissiah has decreed it so.',
              'There can be no doubt to it.',
              'The Imperium marches in its favor.',
              'Rely on it, and the Machine God.',
              'The Astronomican agrees.',
              'It is as the Astronomican expects.',
              'The Omnissiah looks favorably upon it.',
              'It must be so.',
              'It is the will of Terra.',
              'The Astronomican provides no answer.',
              'The Omnissiah is silent.',
              'The Imperium is unsure.',
              'The Warp shrouds our answers now.',
              'Strengthen your will and try again.',
              'To ask that would be heresy.',
              'The Omnissiah frowns upon it.',
              'The Astronomican expects otherwise.',
              'To allow this would invoke Chaos. So no.',
              'This is against the Emperor\'s will.'
              ]

decks = {}
bot = discord.Client()

try:
    conn = db.connect()
except:
    conn = None


@bot.event
async def on_ready():
    print('Logging in...')
    for server in bot.servers:
        decks[server.name] = deck.NEW_DECK.copy()
        random.shuffle(decks[server.name])
    print("I am ready to serve.")


@bot.event
async def on_member_join(member):
    await bot.send_message(member.server.default_channel,
                           "Welcome, " + member.display_name + ", to " + member.server.name + "!")


@bot.event
async def on_server_join(server):
    await bot.send_message(server.default_channel,
                           "Hello, people of " + server.name + "! I am " + bot.user.display_name + "!")


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    clean_message = str(msg.clean_content)
    if re.search(total_dice_regex, clean_message):  # message matches dice regex pattern
        try:
            await sendResponse(msg, dice.parseDiceRequest(msg))
        except TypeError:
            return
        return

    elif str(msg.content).startswith(prefix):
        content = parseCommand(msg)
        await sendResponse(msg, content)


def parseCommand(msg):
    str_content = str(msg.content[1:])
    command = str_content.split(' ', 1)[0]

    if command == 'echo':
        return 'Echo!'
    elif command == 'repeat':
        return str_content[7:]
    elif command == 'credo':
        return credo
    elif command == '8ball' or command == 'eightball':
        return random.choice(eight_ball)
    elif command == 'choose' or command == 'ch':
        return random.choice(str_content[len(command)+1:].split(','))
    elif command == 'deck':
        response = deck.parseDeckRequest(msg, decks[msg.server.name])
        if response[0] is not None:
            decks[msg.server.name] = response[0]
        return response[1]
    elif command == 'roll':
        return dice.parseDiceRequest(msg)
    elif command == 'pfsrd':
        return gcs.pfsrd(msg)
    elif command == 'nethys':
        return gcs.nethys(msg)
    elif command == 'quote':
        if conn is not None:
            return quote.parseQuoteRequest(msg, conn)
        else:
            return 'I cannot access the database right now.'


async def sendResponse(msg, content):
    await bot.send_message(msg.channel, msg.author.mention + ': ' + content)

start_time = datetime.now()
bot.run(token)

import random
import re
from random import shuffle
import discord

from functions import dice, deck, gcs, log
from functions.deck import NEW_DECK
from functions.dice import total_dice_regex


tokenFile = 'token.txt'
with open(tokenFile, 'r') as f:
    token = f.readline()

prefix = '/'
credo = ('There is no truth in flesh, only betrayal. ' +
         'There is no strength in flesh, only weakness. ' +
         'There is no constancy in flesh, only decay. ' +
         'There is no certainty in flesh but death.')
decks = {}
bot = discord.Client()
pfsrd_cx = '010353485282640597323:i406fguqdfe'
nethys_cx = '012046020158994114137:raqss6g6jvy'


def not_ready(name):
    return str(name) + ' is not yet ready!'


@bot.event
async def on_ready():
    print('Logging in...')
    for _ in bot.servers:
        print('Checking into ' + _.name)
        decks[_.name] = shuffle(NEW_DECK.copy())
    print("I am ready to serve.")


@bot.event
async def on_member_join(member):
    await bot.send_message(member.server.default_channel,
                           "Welcome, " + member.display_name + ", to " + member.server + "!")


@bot.event
async def on_server_join(server):
    await bot.send_message(server.default_channel,
                           "Hello, people of " + server.name + "! I am " + bot.user.display_name + "!")


@bot.event
async def on_message(msg):
    log.logMessage(msg)
    clean_message = str(msg.clean_content)
    str_content = str(msg.content[1:])

    commands = dict(echo='msg.author.mention + \': Echo!\'',
                    repeat='msg.author.mention + \': \' + str_content[7:]',
                    credo='credo',
                    deck='deck.parseDeckRequest(msg, decks.get(msg.server.name))',
                    quote='not_ready(\'Quote\')',
                    choose='random.choice(str_content[7:].split(\',\'))',
                    pfsrd='gcs.makeCustomSearch(\'d20pfsrd.com\', pfsrd_cx, msg, len(\'/pfsrd \'))',
                    nethys='gcs.makeCustomSearch(\'archivesofnethys.com\', nethys_cx, msg, len(\'/nethys \'))'
                    )

    if msg.author.bot:
        return

    if re.search(total_dice_regex, clean_message):  # message matches dice regex
        result = dice.parseDiceRequest(msg)
        sent_message = str(msg.author.mention + ': ' + result)
        await bot.send_message(msg.channel, sent_message)
        return

    elif str(msg.content).startswith(prefix):
        for command in commands:
            if str_content.startswith(command):
                await bot.send_message(msg.channel, eval(commands[command]))
                return

bot.run(token)

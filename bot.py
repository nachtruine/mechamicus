import random
import re
import discord
import sys

from datetime import datetime
from functions import dice, deck, gcs, quote, db
from functions.dice import total_dice_regex

token = sys.argv[1]

pfsrd_cx = '010353485282640597323:i406fguqdfe'
nethys_cx = '012046020158994114137:raqss6g6jvy'
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
conn = db.connect()
bot = discord.Client()


@bot.event
async def on_ready():
    print('Logging in...')
    for server in bot.servers:
        decks[server.name] = deck.NEW_DECK.copy()
        deck.shuffleDeck(decks[server.name])
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
    clean_message = str(msg.clean_content)
    str_content = str(msg.content[1:])

    if msg.author.bot:
        return

    commands = dict(echo='\'Echo!\'',
                    roll='str(dice.parseDiceRequest(msg))',
                    repeat='str_content[7:]',
                    credo='credo',
                    deck='deck.parseDeckRequest(msg, decks.get(msg.server.name))',
                    quote='quote.parseQuoteRequest(msg, conn)',
                    choose='random.choice(str_content[7:].split(\',\'))',
                    pfsrd='gcs.makeCustomSearch(\'d20pfsrd.com\', pfsrd_cx, msg, len(\'/pfsrd \'), gcsKey)',
                    nethys='gcs.makeCustomSearch(\'archivesofnethys.com\', nethys_cx, msg, len(\'/nethys \'), gcsKey)',
                    uptime='\'I have been up for: \' + str(datetime.now() - start_time)',
                    eightball='random.choice(eight_ball)'
                    )

    if re.search(total_dice_regex, clean_message):  # message matches dice regex
        try:
            await bot.send_message(msg.channel, str(msg.author.mention + ': ' + dice.parseDiceRequest(msg)))
        except TypeError:
            return
        return

    elif str(msg.content).startswith(prefix):
        if str(msg.content)[1:] == '8ball':
            sendthis = random.choice(eight_ball)
            await bot.send_message(msg.channel, msg.author.mention + ': ' + sendthis)
        else:
            for command in commands:
                if str_content.startswith(command):
                    try:
                        sendthis = str(eval(commands[command]))
                        await bot.send_message(msg.channel, msg.author.mention + ': ' + sendthis)
                    except SyntaxError:
                        await bot.send_message(msg.channel, commands[command])
                    except ValueError:
                        return
                    return

start_time = datetime.now()
bot.run(token)

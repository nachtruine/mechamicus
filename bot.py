import random
import re
import discord
import ast

from functions import dice, deck, gcs, log, quote
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


@bot.event
async def on_ready():
    print('Logging in...')
    for server in bot.servers:
        print('Checking into ' + server.name)
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
    log.logMessage(msg)

    clean_message = str(msg.clean_content)
    str_content = str(msg.content[1:])

    if msg.author.bot:
        if clean_message == 'Logging out...':
            await bot.logout()
        else:
            return

    commands = dict(echo='\'Echo!\'',
                    roll='str(dice.parseDiceRequest(msg))',
                    repeat='str_content[7:]',
                    credo='credo',
                    deck='deck.parseDeckRequest(msg, decks.get(msg.server.name))',
                    quote='quote.parseQuoteRequest(msg)',
                    choose='random.choice(str_content[7:].split(\',\'))',
                    pfsrd='gcs.makeCustomSearch(\'d20pfsrd.com\', pfsrd_cx, msg, len(\'/pfsrd \'))',
                    nethys='gcs.makeCustomSearch(\'archivesofnethys.com\', nethys_cx, msg, len(\'/nethys \'))',
                    shutdown='Logging out...',
                    calc='str(ast.literal_eval(str_content[5:]))'
                    )

    if re.search(total_dice_regex, clean_message):  # message matches dice regex
        await bot.send_message(msg.channel, str(msg.author.mention + ': ' + dice.parseDiceRequest(msg)))
        return

    elif str(msg.content).startswith(prefix):
        for command in commands:
            if str_content.startswith(command):
                try:
                    await bot.send_message(msg.channel, msg.author.mention + ': ' + str(eval(commands[command])))
                except SyntaxError:
                    await bot.send_message(msg.channel, commands[command])
                return

bot.run(token)

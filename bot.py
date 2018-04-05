import random
import re
import discord
import sys

from datetime import datetime
from functions import db, deck, dice, gcs, quote
from functions.dice import total_dice_regex
from functions.subfunctions import split_file

token = sys.argv[1]

prefix = '/'
eight_ball = split_file.eight_ball()

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
            await send_response(msg, dice.parse_dice_request(msg))
        except TypeError:
            return
        return

    elif str(msg.content).startswith(prefix):
        content = parse_command(msg)
        await send_response(msg, content)


def parse_command(msg):
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
        result = ""
        if len(str_content[len(command)+1:]) > 0:
            while result == "":
                result = random.choice(str_content[len(command)+1:].split(','))
            return random.choice(str_content[len(command)+1:].split(','))
    elif command == 'deck':
        response = deck.parse_deck_request(msg, decks[msg.server.name])
        if response[0] is not None:
            decks[msg.server.name] = response[0]
        return response[1]
    elif command == 'roll':
        return dice.parse_dice_request(msg)
    elif command == 'pfsrd':
        return gcs.pfsrd(msg)
    elif command == 'nethys':
        return gcs.nethys(msg)
    elif command == 'google':
        return gcs.google(msg)
    elif command == 'g':
        return gcs.g(msg)
    elif command == 'youtube':
        return gcs.youtube(msg)
    elif command == 'yt':
        return gcs.yt(msg)
    elif command == 'quote':
        if conn is not None:
            return quote.parse_quote_request(msg, conn)
        else:
            return 'I cannot access the database right now.'


async def send_response(msg, content):
    await bot.send_message(msg.channel, msg.author.mention + ': ' + content)

start_time = datetime.now()
bot.run(token)

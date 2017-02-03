import os
import random


def parseQuoteRequest(msg):
    command = str(msg.clean_content)[len('/quote '):]
    server = str(msg.server).replace(':', '')
    str_channel = str(msg.channel)

    log_file = ("quotes/" + server + "/" + str_channel + ".txt")

    if command.startswith('add'):
        trash, user, quote = command.split(' ', 2)
        str_timestamp = str(msg.timestamp.strftime('%b %d, %Y'))
        try:
            with open(log_file, 'a+', encoding='utf-8') as f:
                f.write('**' + user + '**: ' + quote + ' - ' + str_timestamp + '\n')
        except IOError or FileNotFoundError:
            os.makedirs("quotes/" + server)
            with open(log_file, 'a+', encoding='utf-8') as f:
                f.write('**' + user + '**: ' + quote + ' - ' + str_timestamp + '\n')
        return 'Quote saved!'
    elif command.startswith('random'):
        lines = open(log_file).read().splitlines()
        return random.choice(lines)
    elif command == '':
        return 'Available commands: add <name> <quote>, random, <name>'
    else:
        lines = open(log_file).read().splitlines()
        quotes_from_user = []
        for quote in lines:
            name, speech = quote.split(' ', 1)
            name = str(name).replace('*', '')
            if command == name[:-1]:
                quotes_from_user.append(quote)
        if len(quotes_from_user) > 0:
            return random.choice(quotes_from_user)
        else:
            return "No quotes found for " + command

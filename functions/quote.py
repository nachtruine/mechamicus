import random
from datetime import datetime


def formatQuote(list_quotes, number):
    if number <= 0:
        index = random.randint(0, len(list_quotes)-1)
    else:
        index = number-1
    selected_quote = list_quotes[index]
    return '{}: <{}/{}> {}'.format(selected_quote[0], index+1, len(list_quotes), selected_quote[1])


def parseQuoteRequest(msg, conn):
    command = str(msg.clean_content)[len('/quote '):]
    serv_id = str(msg.server.id)
    chan_id = str(msg.channel.id)
    cursor = conn.cursor()
    if len(command) < 1:
        cursor.execute('''
        SELECT author, text FROM Quotes
        WHERE chan_id = %s''', (chan_id,))
        list_quotes = []
        for i in cursor:
            list_quotes.append(i)
        if len(list_quotes) < 1:
            return 'No quotes found for this server.'
        return formatQuote(list_quotes)
    elif command.startswith('add'):
        trash, author, content = command.split(' ', 2)
        cursor.execute('''
        INSERT INTO Quotes(id, serv_id, chan_id, author, text, date)
        VALUES(DEFAULT, %s, %s, %s, %s, %s)
        ''', (serv_id, chan_id, author, content, str(datetime.today().date())))
        conn.commit()
        return 'Quote added!'
    else:
        try:
            author, number = command.rsplit(' ', 1)
        except:
            author = command
            number = 0
        cursor.execute('''
        SELECT author, text FROM Quotes
        WHERE chan_id = %s
        AND author = %s''', (chan_id, author))
        list_quotes = []
        for i in cursor:
            list_quotes.append(i)
        if len(list_quotes) < 1:
            return 'No quotes found for ' + author
        return formatQuote(list_quotes, int(number))

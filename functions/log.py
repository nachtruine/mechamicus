from datetime import date
import os


def logMessage(msg):
    clean_message = str(msg.clean_content)
    server = str(msg.server).replace(':', '')
    str_channel = str(msg.channel)
    str_timestamp = str(msg.timestamp.strftime('%H:%M:%S'))

    if server == 'None':
        server = 'DM'
    logFile = ("logs/" + server + "/" + str_channel + "/" + str(date.today()) + ".txt")

    if os.path.exists("logs/" + server + "/" + str_channel):
        with open(logFile, 'a', encoding='utf-8') as f:
            f.write('<' + str_timestamp + '> ' + msg.author.display_name + ': ' + str(clean_message) + '\n')
    else:
        os.makedirs('logs/' + server + '/' + str_channel)
        with open(logFile, 'a', encoding='utf-8') as f:
            f.write('<' + str_timestamp + '> ' + msg.author.display_name + ': ' + str(clean_message) + '\n')

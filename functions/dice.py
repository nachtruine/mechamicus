import random
import re
dice_regex = r'(?:([+-]?)(\d+)d(\d+))|(?:([+-]\d+))| (.+$)'
listResults = []
maxRolls = []

def __roll_dice(mod, num, sides):
    result = 0
    num = int(num)
    sides = int(sides)
    
    if mod.casefold() == '' or mod.casefold() == '+':
        for i in range(num):
            roll = random.randint(1, sides)
            listResults.append(roll)
            if roll == sides:
                maxRolls.append(1)
            else:
                maxRolls.append(0)
            result += roll
    elif mod.casefold() == '-':
        for i in range(num):
            roll = random.randint(1, sides)
            listResults.append(roll)
            result -= roll
    return result


def parse_dice_request(msg):
    content = str(msg.content)
    comment = ''
    if str(msg.content).startswith('/roll '):
        content = content[len('/roll '):]
    rolls_to_process = re.findall(dice_regex, content)
    roll_result = 0
    for x in rolls_to_process:
        if x[3] == '' and x[4] == '':
            roll_result += __roll_dice(x[0], x[1], x[2])
        elif x[3] != '' and x[4] == '':
            roll_result += int(x[3])
        else:
            comment = x[4]
    for i in range(len(listResults)):
        if maxRolls[i] == 1:
            listResults[i] = str(listResults[i])
    if len(comment) > 0:
        end_result = '\"' + comment + '\": ' + str(listResults) + ' -> **' + str(roll_result) + '**'
    else:
        end_result = str(listResults) + ' -> **' + str(roll_result) + '**'
    listResults.clear()
    return end_result

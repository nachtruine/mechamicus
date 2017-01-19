import random
import re
__single_dice_regex = r'^([+-]?)(\d+)d(\d+)|([+-])(\d+)$'
total_dice_regex = r'^([+-]?(?:\d+|\d*d(?:\d+))(?:[+-](?:\d+|\d*d(?:\d+)))*)( .+)?$'
__bad_regex = r'^([+-])(\d+)$'
listResults = []


def __rollDice(mod, num, sides):
    result = 0
    num = int(num)

    if sides == -1:
        if mod.casefold() == '+':
            result = num
        elif mod.casefold() == '-':
            result = num * -1
        return result

    else:
        sides = int(sides)
        if mod.casefold() == '' or mod.casefold() == '+':
            for i in range(num):
                roll = random.randint(1, sides)
                listResults.append(roll)
                result += roll
        elif mod.casefold() == '-':
            for i in range(num):
                roll = random.randint(1, sides)
                listResults.append(roll)
                result -= roll
        else:
            print('uh oh')
        return result


def __parseSingleRequest(cmd):
    single_search = re.match(__single_dice_regex, cmd)
    mod = single_search.group(1)
    num = single_search.group(2)
    sides = single_search.group(3)
    flatmod = single_search.group(4)
    flatnum = single_search.group(5)
    if flatmod is None and flatnum is None:
        result = __rollDice(mod, num, sides)
        return result
    elif mod is None and num is None and sides is None:
        result = __rollDice(flatmod, flatnum, -1)
        return result


def __removeUsedRequest(cmd):
    length = 1

    single_search = re.match(__single_dice_regex, cmd)

    mod = single_search.group(1)
    num = single_search.group(2)
    sides = single_search.group(3)
    flatmod = single_search.group(4)
    flatnum = single_search.group(5)

    if mod is not None:
        length += len(mod)
    if num is not None:
        length += len(num)
    if sides is not None:
        length += len(sides)
    if flatmod is not None:
        length += len(flatmod)
    if flatnum is not None:
        length += len(flatnum)
    cmd = cmd[length:]
    return cmd


def parseDiceRequest(msg):
    print('Rolling dice...')

    content = msg.content
    total_search = re.search(total_dice_regex, content)
    cmd = total_search.group(1)

    if re.search(__bad_regex, cmd) is not None:
        return

    comment = total_search.group(2)

    if type(comment) is str:
        comment = comment[1:]
    else:
        comment = ''

    roll_result = 0

    while cmd is not "":
        add_result = __parseSingleRequest(cmd)
        roll_result += add_result
        cmd = __removeUsedRequest(cmd)
    if len(comment) > 0:
        end_result = '\"' + comment + '\": ' + str(listResults) + ' -> **' + str(roll_result) + '**'
    else:
        end_result = str(listResults) + ' -> **' + str(roll_result) + '**'

    listResults.clear()
    return end_result

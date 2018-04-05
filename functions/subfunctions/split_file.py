import os

cur_path = os.path.dirname(__file__)


def deck_of_many_things():
    file = open(cur_path + "../../textdbs/domt.txt")
    split_deck = file.readlines()
    return split_deck


def eight_ball():
    file = open(cur_path + "../../textdbs/eightball.txt")
    split_deck = file.readlines()
    return split_deck


def harrow_deck():
    file = open(cur_path + "../../textdbs/harrowdeck.txt")
    split_deck = file.readlines()
    return split_deck


def standard_deck():
    file = open(cur_path + "../../textdbs/standarddeck.txt")
    split_deck = file.readlines()
    return split_deck

import os

cur_path = os.path.dirname(__file__)


def split_file(filename):
    file = open(cur_path + '\..\..\\textdbs\\' + filename + '.txt', 'r')
    this_list = file.readline().split('|||')
    return this_list

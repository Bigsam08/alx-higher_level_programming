#!/usr/bin/python3
""" A function that reads from a file """


def read_file(filename=""):
    """ Opens and read a file to stdout  """
    with open(filename, "r", encoding="utf-8") as new_file:
        print(new_file.read(), end='')

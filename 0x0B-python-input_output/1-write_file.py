#!/usr/bin/python3
""" A function that writes into a file """


def write_file(filename="", text=""):
    """
        text: what to write into the file
        Return: the no of character of text
    """

    with open(filename, "w", encoding="utf-8") as new_file:
        return new_file.write(text)

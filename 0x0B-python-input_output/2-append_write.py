#!/usr/bin/python3
""" A function to append text at the end of existing text """


def append_write(filename="", text=""):
    """
                text: what to writ into the file
                Return: the number of files written
    """

    with open(filename, "a", encoding="utf-8") as new_file:
        return new_file.write(text)

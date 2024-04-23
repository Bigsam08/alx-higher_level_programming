#!/usr/bin/python3
"""text file insert."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    """
    words = ""
    with open(filename) as read:
        for i in read:
            words += i
            if search_string in i:
                words += new_string
    with open(filename, "w") as app:
        app.write(words)

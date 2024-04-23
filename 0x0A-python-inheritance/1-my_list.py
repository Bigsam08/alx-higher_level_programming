#!/usr/bin/python3
""" inheritance class list"""


class MyList(list):
    """ a sub-class list """

    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))

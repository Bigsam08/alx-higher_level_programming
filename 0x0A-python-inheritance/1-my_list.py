#!/usr/bin/python3
""" MyList class objects """


class MyList(list):
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints out sorted list"""
        print(sorted(self))

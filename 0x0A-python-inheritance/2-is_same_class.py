#!/usr/bin/python3
""" checks if an object is
    instance of  class
"""


def is_same_class(obj, a_class):
    """

        Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to

        Returns True if the object and class are of the same instance
        Returns False if not
    """
    if type(obj) == a_class:
        return True
    return False

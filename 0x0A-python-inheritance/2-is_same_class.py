#!/usr/bin/python3
""" checks if an object is
    instance of  class
"""


def is_same_class(obj, a_class):
    """ Returns True if the object and class are of the same instance
        Returns False if not
    """
    if type(obj) == a_class:
        return True
    return False

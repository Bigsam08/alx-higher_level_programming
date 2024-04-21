#!/usr/bin/python3
"""A dic function """


def class_to_json(obj):
    """ returns dictionary of data. """
    return obj.__dict__

#!/usr/bin/python3
""" A module that that retuens a JSON rep of an obj """
import json


def to_json_string(my_obj):
    """ my_obj is a python string. """
    return json.dumps(my_obj)

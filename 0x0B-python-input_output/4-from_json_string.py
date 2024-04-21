#!/usr/bin/python3
""" A module that convert json to python """
import json


def from_json_string(my_str):
    """ python representing json """
    return json.loads(my_str)

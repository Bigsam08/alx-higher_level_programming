#!/usr/bin/python3
""" converting json to python from a file """
import json


def load_from_json_file(filename):
    """ returns  The python form of json """
    with open(filename, "r", encoding="utf-8") as new_file:
        return json.loads(new_file.read())

#!/usr/bin/python3
""" writes an Obj to a txt, using a JSON  """
import json


def save_to_json_file(my_obj, filename):
    """ My json function"""
    with open(filename, "w", encoding="utf-8") as new_file:
        json.dump(my_obj, new_file)

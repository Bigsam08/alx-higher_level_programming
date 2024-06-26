#!/usr/bin/python3
"""Add  args to a  list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        lst = load_from_json_file("add_item.json")
    except FileNotFoundError:
        lst = []
    items.extend(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")

#!/usr/bin/python3
"""
    Adding all arguments to a list
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    store = load_from_json_file("add_item.json")
except FileNotFoundError:
    store = []

for ipp in sys.argv[1:]:
    store.append(ipp)
save_to_json_file(store, "add_item.json")

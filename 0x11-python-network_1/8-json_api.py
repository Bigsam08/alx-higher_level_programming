#!/usr/bin/python3
""" a python script that takes in a letted and semd to POST """

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})
    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            for detail in data:
                print(F"[{detail['id']}] {detail['name']}")
    except ValueError:
        print("Not a valid JSON")

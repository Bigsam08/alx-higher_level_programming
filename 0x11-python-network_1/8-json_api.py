#!/usr/bin/python3
""" a python script that takes in a letted and semd to POST """

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        q = {}

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data)
    try:
        dic = response.json()
        if len(dic) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dic['id'], dic['name']))
    except ValueError:
        print("Not a valid JSON")

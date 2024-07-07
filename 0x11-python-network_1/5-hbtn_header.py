#!/usr/bin/python3
""" using requests package get the value id of a URL header """

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    response_H = response.headers.get("X-Request-Id")
    print(response_H)

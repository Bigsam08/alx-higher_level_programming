#!/usr/bin/python3
""" handling request errors in urllib """
import urllib
from urllib import request, error
import sys


if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            msg = response.read().decode('utf-8')
            print(msg)
    except error.HTTPError as e:
        print(F"Error code: {e.code}")

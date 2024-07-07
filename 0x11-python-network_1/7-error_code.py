#!/usr/bin/python3
""" a python script that uses a GET requests to send to a url
    and printing back in display
    if status is greater or equal to 400 display error
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    print(response.text)
#!/usr/bin/python3
""" using the requests library to POST an email """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data=data)
    print(response.text)

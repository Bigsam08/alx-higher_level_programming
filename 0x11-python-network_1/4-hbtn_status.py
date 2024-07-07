#!/usr/bin/python3
""" python script that fetches the URL using the requests package """
import requests


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(F"\t- type: {type(response.text)}")
    print(F"\t- content: {type(response.txt)}")

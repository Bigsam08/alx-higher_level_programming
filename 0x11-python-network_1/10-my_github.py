#!/usr/bin/python3
# a python script that takes a github USERNAME 
# and  PASSWORD displaying the result using GITHUBAPI

import requests
import sys


if __name__ = '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    dic = response.json()
    try:
        print(dic['id'])
    except:
        print('None')

#!/usr/bin/python3
""" a script that gets the email using the command line args
    args[1] as the url abd args[2] as the email to be posted
    using the POST verb and display back the body of response
    in utf-8 mode
"""
import sys
import urllib
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        msg = response.read().decode('utf-8')
        print(msg)

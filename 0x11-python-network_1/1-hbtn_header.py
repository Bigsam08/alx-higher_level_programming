#!/usr/bin/python3
""" Scriot that takes url from command line
    sends request and displays the -X requested-id header
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    requested_id = response.info().get('X-Request-Id')
    print(requested_id)

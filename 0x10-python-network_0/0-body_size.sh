#!/bin/bash
# display size of a url response
url = "$1"
curl -s url | wc -c

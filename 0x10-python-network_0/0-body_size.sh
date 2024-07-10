#!/bin/bash
# display size of a url response
curl -s "$1" | wc -c

#!/bin/bash
# send a post msg to a url and display response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

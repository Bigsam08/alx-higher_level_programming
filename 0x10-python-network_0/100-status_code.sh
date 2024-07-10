#!/bin/bash
# Bash script tsends a URLrequest
curl -sI -w '%{response_code}' "$1" -o /dev/null

#!/bin/bash
# display all url HTTP response server accepts
curl -Is "$1" | grep Allow | cut -c 8-

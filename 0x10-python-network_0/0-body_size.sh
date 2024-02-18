#!/bin/bash
# Bash script that akes in a URL that sends a request and displays size of response body
curl -s "$1" | wc -c

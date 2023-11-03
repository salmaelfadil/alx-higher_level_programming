#!/usr/bin/python3
"""takes a url, sends a request and displays the value of X-Request-Id"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])

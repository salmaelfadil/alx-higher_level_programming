#!/usr/bin/python3
"""takes a url, sends a post request and displays the response"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

#!/usr/bin/python3
"""fetches a url and sends a request, display response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    html = requests.get(url)
    if html.status_code >= 400:
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)

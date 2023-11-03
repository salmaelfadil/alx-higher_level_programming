#!/usr/bin/python3
"""fetches a url using requests displays variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    html = requests.get(url)
    print(html.headers.get("X-Request-Id"))

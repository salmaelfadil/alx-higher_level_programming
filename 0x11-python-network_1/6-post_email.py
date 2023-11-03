#!/usr/bin/python3
"""fetches a url and sends a post request, display response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    html = requests.post(url, data=email)
    print(html.text)

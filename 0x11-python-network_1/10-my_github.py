#!/usr/bin/python3
"""takes your GitHub credentials and uses GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, access_token)
    request = requests.get(url, auth=auth)
    print(request.json().get("id"))

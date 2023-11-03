#!/usr/bin/python3
"""takes your GitHub credentials and uses GitHub API to commits"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
    owner, repo)


    request = requests.get(url)
    comm = request.json()

    try:
        for i in range(10):
            print("{}: {}".format(comm[i].get("sha"),
                comm[i].get("author").get("name")))
    except IndexError:
        pass

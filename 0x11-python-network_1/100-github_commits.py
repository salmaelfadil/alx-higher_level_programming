#!/usr/bin/python3
"""takes your GitHub credentials and uses GitHub API to commits"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    request = requests.get(url)
    comm = request.json()

    try:
        for i in comm[:10]:
            sha = i['sha']
            n = i['commit']['author']['name']
            print("{}: {}".format(sha, n))
    except IndexError:
        pass

#!/usr/bin/python3
"""takes in a letter and sends a post request, display response"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {"q": letter}

    html = requests.post(url, data=data)
    try:
        res = html.json()
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

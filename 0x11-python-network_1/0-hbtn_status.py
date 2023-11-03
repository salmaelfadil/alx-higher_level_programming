#!/usr/bin/python3
"""Python script that fetches a url"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf content: {}".format(html.decode("utf-8")))

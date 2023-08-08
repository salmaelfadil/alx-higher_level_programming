#!/usr/bin/python3
"""text_indentation function prints two lines after '.' '?' and ':'"""


def text_indentation(text):
    """
    Args:
    string of text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    newline_chars = ['.', '?', ':']
    current_line = ""

    for i in text:
        current_line += i
        if i in newline_chars:
            print(current_line.strip())
            print()
            current_line = ""
    if current_line:
        print(current_line.strip())

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary = {} or a_dictionary is None:
        return None
    largest = max(a_dictionary.items())
    for key, value in a_dictionary.items():
        if value is largest:
            return key

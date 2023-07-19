#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary = {} and len(a_dictionary) == 0:
        return None
    largest = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if key is largest:
            return key

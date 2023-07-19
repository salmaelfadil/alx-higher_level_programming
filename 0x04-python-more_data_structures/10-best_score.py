#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary = {} or a_dictionary is None:
        return None
    else:
        new_list = list(a_dictionary.key())
        largest = 0
        l_key = ""
        for i in new_list:
            if a_dictionary[i] > largest:
                largest = a_dictionary[i]
                l_key = i
        return l_key

#!/usr/bin/python3
def no_c(my_string):
    str = my_string.translate({ord('c'): None})
    str = my_string.translate({ord('C'): None})
    return str

#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    s2 =""
    for i in range(len(str)):
        if i == n:
            break
        s2 += str[i]
    return (s2)

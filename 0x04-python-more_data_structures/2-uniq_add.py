#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_list = []
    res = 0
    for i in my_list:
        if i not in add_list:
            add_list.append(i)

    for i in add_list:
        res += i

    return res

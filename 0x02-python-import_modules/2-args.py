#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argc = len(sys.argv)
    i = 1

    if argc ==  1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    while i < argc:
        print("{} : {}".format(i, sys.argv[i]))
        i += 1

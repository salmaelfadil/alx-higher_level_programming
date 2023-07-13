#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)

    if argc ==  1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1 : {}".format(argv[1]))
    else:
        print("{} arguments:".format(argv))
        i = 1
        while i <= argc:
            print("{} : {}".format(i, argv[i]))
            i++

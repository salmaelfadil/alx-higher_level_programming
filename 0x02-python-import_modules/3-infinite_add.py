#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(argv) - 1
    res = 0

    if argc == 0:
        print("0")

    else:
        i = 1
    
        while i <= argc:
            res += int(sys.argv[i])
            i += 1 

        print("{}".format(res))

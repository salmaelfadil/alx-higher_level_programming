#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(argv) - 1
    res = 0

    for i in range(argc):
        res += int(sys.argv[i + 1])

    print("{}".format(res))

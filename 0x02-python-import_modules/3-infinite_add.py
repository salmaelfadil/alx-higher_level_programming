#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(argv) - 1
    res = 0

    for i in range(args):
        res += int(sys.argv[i + 1])

    print("{}".format(res))

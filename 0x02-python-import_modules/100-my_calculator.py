#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("{} {} = {}".format(int(sys.argv[1]), sys.argv[2], int(argv[3]), operators[sys.argv[2]](a,b))) 


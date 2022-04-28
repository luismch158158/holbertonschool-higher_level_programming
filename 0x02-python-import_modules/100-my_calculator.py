#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    longitud = len(sys.argv)

    if (longitud != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    item_1 = int(sys.argv[1])
    item_2 = int(sys.argv[3])
    operator = sys.argv[2]

    struct = {"+": add, "-": sub, "*": mul, "/": div}

    if ((operator != "+") and (operator != "-")
            and (operator != "*") and (operator != "/")):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f'{item_1} {operator} {item_2} = {struct[operator](item_1, item_2)}')

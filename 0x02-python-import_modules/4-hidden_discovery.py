#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    for j in dir(hidden_4):
        if (j[0] != '_'):
            print(f'{j}')

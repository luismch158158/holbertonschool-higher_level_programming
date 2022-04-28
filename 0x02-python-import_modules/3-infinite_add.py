#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = len(sys.argv)
    acum = 0
    items = 0

    if (total == 1):
        print("0")
    else:
        for i in sys.argv:
            if items != 0:
                acum = acum + int(i)
            items += 1
        print(f'{acum}')

#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    lengthen = len(sys.argv)
    items = 0
    if lengthen == 1:
        print("0 arguments.")

    elif lengthen == 2:
        print("{:d} argument:".format(lengthen - 1))
        print(f'{lengthen - 1}: {sys.argv[1]}')

    else:
        print("{:d} arguments:".format(lengthen - 1))
        for i in sys.argv:
            if items != 0:
                print(f'{items}: {i}')
            items += 1

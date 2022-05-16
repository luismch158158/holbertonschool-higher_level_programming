#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        try:
            if x > j:
                print(f'{i}', end="")
            j = j + 1
        except (IndexError):
            continue
    print()
    return (j)

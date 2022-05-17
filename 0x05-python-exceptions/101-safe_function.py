#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(args[0], args[1])
        return (a)
    except ZeroDivisionError as ne:
        return None
        print("Exception: {}".format(ne))
    except IndexError as ni:
        return None
        print("Excepction: {}".format(ni))

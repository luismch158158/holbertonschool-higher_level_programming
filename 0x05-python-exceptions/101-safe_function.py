#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(args[0], args[1])
        return (a)
    except ZeroDivisionError as ne:
        return None
        sys.stderr.write("Exception: {}\n".format(ne))
    except IndexError as ni:
        return None
        sys.stderr.write("Exception: {}\n".format(ni))

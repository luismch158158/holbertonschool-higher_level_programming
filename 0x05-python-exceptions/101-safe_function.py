#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(args[0], args[1]))
    except ZeroDivisionError as ne:
        sys.stderr.write("Exception: {}\n".format(ne))
        return None
    except IndexError as ni:
        sys.stderr.write("Exception: {}\n".format(ni))
        return None

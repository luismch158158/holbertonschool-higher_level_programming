#!/usr/bin/python3
"""Class definition"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """prints list ordered"""
        print(sorted(self))

#!/usr/bin/python3
"""Class definition"""


class MyInt(int):
    """Class MyInt that is inherited from int"""

    def __eq__(self, other):
        """Operators inverted not equals"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Operators inverted equals"""
        return super().__eq__(other)

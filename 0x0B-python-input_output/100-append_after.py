#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file,
    after each line containing a specific string"""

    with open(filename, mode="r+", encoding="utf-8") as f:
        all_text = f.readlines()
        new_text = ""
        for line in all_text:
            new_text += line
            if search_string in line:
                new_text += new_string

        f.seek(0)
        f.write(new_text)

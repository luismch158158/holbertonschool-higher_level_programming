#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = []
    second_text = []

    new_text = text.replace(".", ".\n").replace(":", ":\n").replace("?", "?\n")
    new_text = new_text.split("\n")

    for jumps in new_text:
        second_text.append(jumps.strip(" "))

    ultimate_text = "\n\n".join(second_text)
    print(ultimate_text, end="")

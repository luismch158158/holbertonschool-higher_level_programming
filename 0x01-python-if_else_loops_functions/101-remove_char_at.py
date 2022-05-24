#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if (n > len(str)) or (n < 0):
        return str
    for i in str:
        if i != str[n]:
            new_str = new_str + i
    return new_str

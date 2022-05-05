#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return (0)

    dig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count_sum = 0

    for i in range(len(roman_string)):
        if (i > 0) and (dig[roman_string[i]] > dig[roman_string[i - 1]]):
            count_sum += dig[roman_string[i]] - (2 * dig[roman_string[i - 1]])
        else:
            count_sum += dig[roman_string[i]]

    return count_sum

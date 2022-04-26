#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = str(number)
if (number >= 0):
    last_digit = int(string[-1])
else:
    last_digit = int(string[-1])
    last_digit = -last_digit

if (last_digit == 0):
    print("Last digit of {:d} is 0 and is 0".format(number))
elif (last_digit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_digit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_digit))

#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            result += "{:c}".format(ord(char) - ord('a') + ord('A'))
        else:
            result += "{:c}".format(ord(char))
    print(result)

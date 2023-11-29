#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - ord('a') + ord('A')), end="")
        else:
            print("{:c}".format(ord(char)), end="")

    print()

#!/usr/bin/python3
def safe_print_division(a, b):
    output = 0

    try:
        output = a / b
    except ZeroDivisionError:
        output = None
    finally:
        print('Inside output: {:d}'.format(output))
        return output

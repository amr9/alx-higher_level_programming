#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    value = 0
    key = None
    for ke, val in a_dictionary.items():
        if val > value:
            value = val
            key = ke
    return key

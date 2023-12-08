#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda z: replace if z == search else z, my_list))

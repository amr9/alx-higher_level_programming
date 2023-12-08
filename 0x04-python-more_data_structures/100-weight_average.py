#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(n1 * m2 for n1, m2 in my_list) /
                sum(n2 for n1, n2 in my_list))

#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = set(my_list)
    result = 0

    for value in unique_values:
        result += value

    return result

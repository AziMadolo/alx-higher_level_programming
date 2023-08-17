#!/usr/bin/python3

def compute_weighted_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for entry in my_list:
        numerator += entry[0] * entry[1]
        denominator += entry[1]

    return (numerator / denominator)

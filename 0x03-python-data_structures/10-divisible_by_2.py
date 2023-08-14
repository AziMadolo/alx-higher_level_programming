#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    Checks if elements in the list are divisible by 2.

    Args:
        my_list (list): The list to be checked.

    Returns:
        list: A list of Boolean values indicating divisibility by 2.
    """
    results = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    return results

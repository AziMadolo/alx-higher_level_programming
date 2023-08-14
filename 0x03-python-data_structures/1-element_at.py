#!/usr/bin/python3
#1_element_at.py

def retrieve_element(lst, index):
    """Retrieve an element from a list."""
    if index < 0 or index > (len(lst) - 1):
        return None
    return lst[index]

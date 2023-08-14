#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.
    
    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace the element.
        element: The new element to place in the list.
    
    Returns:
        list: The modified list.
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list

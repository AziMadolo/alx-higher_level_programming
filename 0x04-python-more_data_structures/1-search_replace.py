#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace occurrences of a specific value in a list with another value.
    
    Args:
        my_list (list): The original list.
        search: The value to be replaced.
        replace: The value to replace `search` with.
    
    Returns:
        list: A new list with replaced values.
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list

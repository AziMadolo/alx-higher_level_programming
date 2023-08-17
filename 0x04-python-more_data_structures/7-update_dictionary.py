#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update a dictionary by adding or replacing key/value pairs.

    Args:
        a_dictionary (dict): The dictionary to be updated.
        key: The key to be added or replaced.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

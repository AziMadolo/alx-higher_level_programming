#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all instances of characters 'c' and 'C' from a given string."""
    copy = [char for char in my_string if char.lower() != 'c']
    return ''.join(copy)

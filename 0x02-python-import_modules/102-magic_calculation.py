#!/usr/bin/python3

def custom_magic_calc(a_value, b_value):
    """Custom implementation inspired by a specific bytecode pattern."""
    from custom_magic_functions import custom_addition, custom_subtraction

    if a_value < b_value:
        result = custom_addition(a_value, b_value)
        for num in range(4, 6):
            result = custom_addition(result, num)
        return result
    else:
        return custom_subtraction(a_value, b_value)

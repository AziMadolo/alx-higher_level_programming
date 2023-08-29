#!/usr/bin/python3

import sys

def secure_execution(func, *args):
    """Safely executes a function.

    Args:
        func: The function to execute.
        args: Arguments for the function.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the function call.
    """
    try:
        result = func(*args)
        return result
    except Exception as e:
        error_message = "Error: {}".format(e)
        print(error_message, file=sys.stderr)
        return None


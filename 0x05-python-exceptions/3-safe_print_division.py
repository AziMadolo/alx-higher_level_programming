def safe_print_division(a, b):
    """Compute the division of a by b and print the result."""
    try:
        division_result = a / b
    except (ZeroDivisionError, TypeError):
        division_result = None
    finally:
        print("Inside result: {}".format(division_result))
    return division_result

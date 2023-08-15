#!/usr/bin/python3

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

def perform_calculations(a, b):
    """Perform addition, subtraction, multiplication, and division on two numbers."""
    results = {
        "sum": add(a, b),
        "difference": sub(a, b),
        "product": mul(a, b),
        "quotient": div(a, b)
    }
    return results

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    calculations = perform_calculations(num1, num2)

    print("{} + {} = {}".format(num1, num2, calculations["sum"]))
    print("{} - {} = {}".format(num1, num2, calculations["difference"]))
    print("{} * {} = {}".format(num1, num2, calculations["product"]))
    print("{} / {} = {}".format(num1, num2, calculations["quotient"]))

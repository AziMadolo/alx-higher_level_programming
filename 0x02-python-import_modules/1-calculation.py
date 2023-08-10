#!/usr/bin/python3

def perform_calculations(a, b):
    """Perform addition, subtraction, multiplication, and division on two numbers."""
    from calculator_1 import add, sub, mul, div
    
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

#!/usr/bin/python3

def add(a, b):
    """Perform addition: a + b"""
    return a + b

def sub(a, b):
    """Perform subtraction: a - b"""
    return a - b

def mul(a, b):
    """Perform multiplication: a * b"""
    return a * b

def div(a, b):
    """Perform division: a / b"""
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

    print(f"{num1} + {num2} = {calculations['sum']}")
    print(f"{num1} - {num2} = {calculations['difference']}")
    print(f"{num1} * {num2} = {calculations['product']}")
    print(f"{num1} / {num2} = {calculations['quotient']}")

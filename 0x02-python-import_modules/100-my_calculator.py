#!/usr/bin/python3

if __name__ == "__main__":
    """Perform basic arithmetic calculations."""
    from custom_calculator import add, subtract, multiply, divide 
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./custom_calculator.py <operand1> <operation> <operand2>")
        sys.exit(1)

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if sys.argv[2] not in list(operations.keys()):
        print("Unrecognized operation. Available operations: +, -, * and /")
        sys.exit(1)

    operand1 = int(sys.argv[1])
    operand2 = int(sys.argv[3])
    print("{} {} {} = {}".format(operand1, sys.argv[2], operand2, operations[sys.argv[2]](operand1, operand2)))

#!/usr/bin/python3

def calculate_total(arguments):
    """Calculate the sum of all arguments."""
    total = 0
    for argument in arguments:
        total += int(argument)
    return total

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    total = calculate_total(arguments)
    print("Total: {}".format(total))

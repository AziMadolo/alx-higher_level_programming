#!/usr/bin/python3

if __name__ == "__main__":
    """Calculate and display the addition, subtraction, multiplication, and division of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    num1 = 10
    num2 = 5

    print("{} plus {} equals {}".format(num1, num2, add(num1, num2)))
    print("{} minus {} equals {}".format(num1, num2, sub(num1, num2)))
    print("{} times {} equals {}".format(num1, num2, mul(num1, num2)))
    print("{} divided by {} equals {}".format(num1, num2, div(num1, num2)))


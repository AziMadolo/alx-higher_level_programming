#!/usr/bin/python3

def main():
    """Display the count and list of arguments."""
    import sys

    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("No arguments.")
    elif arg_count == 1:
        print("One argument:")
    else:
        print("{} arguments:".format(arg_count))

    for index in range(arg_count):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

if __name__ == "__main__":
    main()

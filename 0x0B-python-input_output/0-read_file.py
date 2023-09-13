#!/usr/bin/python3
"""
Defines a text file-reading function.
"""

def read_file(filename=""):
    """
    Reads and prints the contents of a UTF-8 encoded text file.

    Args:
        filename (str): The name of the text file to read.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    read_file("my_file_0.txt")


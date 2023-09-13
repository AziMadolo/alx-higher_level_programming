#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            return file.write(text)
    except FileNotFoundError:
        return 0
    except Exception:
        return 0

if __name__ == "__main__":
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    nb_characters_added = append_write(filename, text)
    print(nb_characters_added)


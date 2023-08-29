#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        :param size: An integer representing the size of the square.
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is a negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        elif size < 0:
            raise ValueError("Size must be greater than or equal to 0.")
        self.__size = size

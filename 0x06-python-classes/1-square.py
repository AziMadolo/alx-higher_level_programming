#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, side_length):
        """Initialize a new Square.

        Args:
            side_length (int): The length of a side of the new square.
        """
        self.__side_length = side_length

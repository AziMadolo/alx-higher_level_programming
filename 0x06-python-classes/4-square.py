#!/usr/bin/python3
"""Definition of the Square class."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The side length of the new square.
        """
        self._size = size

    @property
    def size(self):
        """Get or set the current side length of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the side length of the square.

        Args:
            value (int): The new side length value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be non-negative")
        self._size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

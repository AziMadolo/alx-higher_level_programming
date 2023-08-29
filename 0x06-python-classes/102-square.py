#!/usr/bin/python3
"""Implementation of the Square class."""


class Square:
    """Represents a geometric square."""

    def __init__(self, side_length=0):
        """Initialize a new square instance.

        Args:
            side_length (int): The length of a side of the square.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """Retrieve or modify the side length of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side length must be an integer")
        elif value < 0:
            raise ValueError("side length must be non-negative")
        self.__side_length = value

    def compute_area(self):
        """Calculate and return the area of the square."""
        return self.__side_length * self.__side_length

    def __eq__(self, other_square):
        """Custom equality comparison for squares."""
        return self.compute_area() == other_square.compute_area()

    def __ne__(self, other_square):
        """Custom inequality comparison for squares."""
        return self.compute_area() != other_square.compute_area()

    def __lt__(self, other_square):
        """Custom less-than comparison for squares."""
        return self.compute_area() < other_square.compute_area()

    def __le__(self, other_square):
        """Custom less-than-or-equal comparison for squares."""
        return self.compute_area() <= other_square.compute_area()

    def __gt__(self, other_square):
        """Custom greater-than comparison for squares."""
        return self.compute_area() > other_square.compute_area()

    def __ge__(self, other_square):
        """Custom greater-than-or-equal comparison for squares."""
        return self.compute_area() >= other_square.compute_area()

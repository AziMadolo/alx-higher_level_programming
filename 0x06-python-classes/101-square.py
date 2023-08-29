#!/usr/bin/python3
"""Implement a Square class with size and position attributes."""


class Square:
    """Representation of a square."""

    def __init__(self, dimensions=0, coordinates=(0, 0)):
        """Initialize a new square.

        Args:
            dimensions (int): The size of the square's sides.
            coordinates (tuple): The position of the square.
        """
        self.dimensions = dimensions
        self.coordinates = coordinates

    @property
    def dimensions(self):
        """Get or set the dimensions of the square."""
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, value):
        if not isinstance(value, int):
            raise TypeError("Dimensions must be an integer")
        elif value < 0:
            raise ValueError("Dimensions must be non-negative")
        self.__dimensions = value

    @property
    def coordinates(self):
        """Get or set the coordinates of the square."""
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(coord, int) for coord in value)
            or not all(coord >= 0 for coord in value)
        ):
            raise TypeError("Coordinates must be a tuple of two non-negative integers")
        self.__coordinates = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__dimensions * self.__dimensions

    def print_square(self):
        """Print the square pattern using '#'."""
        if self.__dimensions == 0:
            print("")
            return [print("") for _ in range(0, self.__coordinates[1])]
        for _ in range(0, self.__dimensions):
            [print(" ", end="") for _ in range(0, self.__coordinates[0])]
            [print("#", end="") for _ in range(0, self.__dimensions)]
            print("")

    def __str__(self):
        """Return a string representation of the square."""
        if self.__dimensions != 0:
            [print("") for _ in range(0, self.__coordinates[1])]
        for _ in range(0, self.__dimensions):
            [print(" ", end="") for _ in range(0, self.__coordinates[0])]
            [print("#", end="") for _ in range(0, self.__dimensions)]
            if _ != self.__dimensions - 1:
                print("")
        return ""


#!/usr/bin/python3
"""Define a custom Square class."""


class Square:
    """Represents a square."""

    def __init__(self, side_length=0, placement=(0, 0)):
        """Initialize a new square.

        Args:
            side_length (int): The length of the sides of the square.
            placement (int, int): The placement of the square.
        """
        self.side_length = side_length
        self.placement = placement

    @property
    def side_length(self):
        """Get or set the current side length of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side length must be an integer")
        elif value < 0:
            raise ValueError("side length must be non-negative")
        self.__side_length = value

    @property
    def placement(self):
        """Get or set the current placement of the square."""
        return self.__placement

    @placement.setter
    def placement(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("placement must be a tuple of 2 non-negative integers")
        self.__placement = value

    def area(self):
        """Return the current area of the square."""
        return self.__side_length * self.__side_length

    def my_print(self):
        """Print the square using the # character."""
        if self.__side_length == 0:
            print("")
            return

        [print("") for _ in range(0, self.__placement[1])]
        for _ in range(0, self.__side_length):
            [print(" ", end="") for _ in range(0, self.__placement[0])]
            [print("#", end="") for _ in range(0, self.__side_length)]
            print("")

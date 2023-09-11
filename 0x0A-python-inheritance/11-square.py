#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

from 9-rectangle import Rectangle as BaseRectangle

class Rectangle(BaseRectangle):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        super().__init__(width, height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())

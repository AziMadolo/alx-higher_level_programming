#!/usr/bin/python3
"""Square class definition."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.set_size(size)

    def get_size(self):
        """Get the size of the square."""
        return self.__size

    def set_size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def calculate_area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def display(self):
        """Display the square using # characters."""
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")


# Example usage
if __name__ == "__main__":
    try:
        size_input = int(input("Enter the size of the square: "))
        square = Square(size_input)
        print(f"Area of the square: {square.calculate_area()}")
        print("Square:")
        square.display()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


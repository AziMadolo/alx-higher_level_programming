#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# The following part of the code is used for testing the BaseGeometry class.
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        bg.integer_validator("my_int", 12)
        bg.integer_validator("width", 89)

        bg.integer_validator("name", "John")  # Raises TypeError
        bg.integer_validator("age", 0)        # Raises ValueError
        bg.integer_validator("distance", -4)  # Raises ValueError
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

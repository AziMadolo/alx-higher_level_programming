#!/usr/bin/python3
"""Implements a CustomCircle class with similar functionality."""

import math

class CustomCircle:
    """A class representing a circle with custom methods."""

    def __init__(self, radius=0):
        """Initialize a CustomCircle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number")
        self.__radius = radius

    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.__radius ** 2

    def calculate_circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius


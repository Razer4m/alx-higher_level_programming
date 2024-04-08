#!/usr/bin/python3
"""
Defines a Rectangle class with private attributes width and height,
and public methods area, perimeter, __str__, and __repr__.
"""


class Rectangle:
    """
    Defines a rectangle with width and height attributes,
    and methods to calculate its area and perimeter.
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height) if self.width and self.height else 0

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction."""
        return f"Rectangle({self.width}, {self.height})"

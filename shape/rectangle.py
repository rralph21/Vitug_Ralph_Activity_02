"""This module defines the Rectangle class."""

__author__ = "Ralph Vitug"
__version__ = "2.0.0"

from shape.shape import Shape
from shape.triangle import Triangle

class Rectangle(Shape):
    """
    Initializes Rectangle object upon received argument
    (if valid).

    args:
        length (int): Represents the length of two opposing
        sides of the Rectangle in centimeters.
        width (int): Represents the width of two opposing sides
        of the Rectangle in centimeters.
    """

    def __init__(self, length: int, width: int):

        super().__init__(color=str)

        if isinstance(length, int):
            self.__length = length

        else:
            raise ValueError("Length must be numeric")
        
        if isinstance(width, int):
            self.__width = width

        else:
            raise ValueError("Width must be numeric")
        
        
    

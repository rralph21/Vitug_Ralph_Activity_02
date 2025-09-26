"""This module defines the Rectangle class."""

__author__ = "Ralph Vitug"
__version__ = "3.0.0"

from shape import Shape


class Rectangle(Shape):
    """
    Initializes Rectangle object upon received argument
    (if valid).

    args:
        length (int): Represents the length of two opposing
        sides of the Rectangle in centimeters.
        width (int): Represents the width of two opposing sides
        of the Rectangle in centimeters.

    raises:
        length: ValueError is raised if non numeric
        width: ValueError is raised if non numeric
    """

    def __init__(self, color: str, length: int, width: int):

        super().__init__(color)

        if isinstance(length, int):
            self.__length = length

        else:
            raise ValueError("Length must be numeric")
        
        if isinstance(width, int):
            self.__width = width

        else:
            raise ValueError("Width must be numeric")
        
    def calculate_area(self):
        return self.__length * self.__width
    
    def calculate_perimeter(self):
        return (self.__length * 2) + (self.__width * 2)
        
    def __str__(self) -> str:

        return (
                super().__str__() 
                + "\nThis rectangle has four sides with " 
                + f"the lengths of {self.__length}, {self.__width}, {self.__length}"
                + f" and {self.__width} centimeters")
        



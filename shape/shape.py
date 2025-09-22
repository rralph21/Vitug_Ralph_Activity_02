"""This module defines the Shape class."""

__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):

    """
    Initializes a shape object upon received arguments
    (if valid).

    args:
    color (str): Represents color of the shape

    raises:
    raises ValueError if color is blank.
    """

    def __init__(self, color: str):
        
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")

        else:
            self._color = color
        

    @property
    def color(self) -> str:
        return self._color
    
    
    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculates the area of the shape.
        Args:
            calculate_area (float): Calculates the area of the shape.
        returns: float: indicates the area of the shape.

        """

        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the shape.
        Args:
            calculate_perimeter (float): Calculates the area of the shape
        returns: float: indicates the perimeter of the shape.
        """

        pass

    def __str__(self) -> str:

        return (f"The shape color is {self._color}.")
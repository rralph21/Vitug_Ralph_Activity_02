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

    """

    def __init__(self, color: str)
        
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")

        else:
            self._color = color
        

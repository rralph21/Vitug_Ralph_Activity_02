"""This module defines the Triangle class."""

__author__ = "Ralph Vitug"
__version__ = "2.0.0"

from shape.shape import Shape

class Triangle(Shape):

    """
    Initializes a triangle object upon received argument
    (if valid)

    args:
        side_1 (int):Represents the length of the first
        side of the Triangle in centimeters.
        side_2 (int): Represents the length of the second side
        of the Triangle in centimeters.
        side_3 (int): Represents the length o the third
        side of the Triangle in centimeters.

    raises:
        side_1: ValueError is raised if non numeric
        side_2: ValueError is raised if non numeric
        side_3: ValueError is raised if non numeric

    """

    def __init__(self, side_1: int, side_2: int, side_3: int):

        super().__init__(color=str)

        if isinstance(side_1, int):
            self.__side_1 = side_1

        else:
            raise ValueError("Side 1 must be a numeric type")
        
        if isinstance(side_2, int):
            self.__side_2 = side_2

        else:
            raise ValueError("Side 2 must be a numeric type")
        
        if isinstance(side_3, int):
            self.__side_3 = side_3
        
        else:
            raise ValueError("Side 3 must be a numeric type")
        
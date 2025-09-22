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
        calculate_area: ValueError is raised if TIT 
        is not satisfied.
        calculate_perimeter: ValueError is raised if TIT
        is not satisfied.

    """

    def __init__(self, side_1: int, side_2: int, side_3: int,
                 calculate_area: float, calculate_perimeter: float):

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
        
        if isinstance(calculate_area, float):
            self.__calculate_area = calculate_area

        else:
            raise ValueError("The sides did not satisfy the Triangular" +
            "Inequality Theorem")
        
        if isinstance(calculate_perimeter, float):
            self.__calculate_perimeter = calculate_perimeter
        
        else:
            raise ValueError("The sides did not satisfy the Triangular" +
                             " Inequality Theorem")
        

    def calculate_area(self) -> float:

        sp = ((self.__side_1 + self.__side_2 + self.__side_3) /2)
        area = ((sp * (sp - self.__side_1), sp * (sp - self.__side_2), sp * (sp - self.__side_3)) / sp)

        self.calculate_area = area
        

    def __str__(self) -> str:
        return (
                super().__str__() + f"The shape color is {self._color}."
                + f"\nThis triangle has three sides with" 
                + f"the lengths of {self.__side_1}, {self.__side_2} and {self.__side_3}"
                + f"centimeters")
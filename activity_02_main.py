""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from shape import *

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    triangle_1 = Triangle("red", 3,4,5)
    shapes.append(triangle_1)

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    rectangle_1 = Rectangle("blue", 10, 5)
    shapes.append(rectangle_1)


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    triangle_2 = Triangle("white", 6, 8, 10)   
    rectangle_2 = Rectangle("yellow", 4, 4)     
    rectangle_3 = Rectangle("black", 12, 7)    

    shapes.append(triangle_2)
    shapes.append(rectangle_2)
    shapes.append(rectangle_3)

    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")

    # *** END PART 1 ***


if __name__ == "__main__":
    main()
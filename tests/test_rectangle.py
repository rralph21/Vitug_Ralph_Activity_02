"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Ralph Vitug"
__version__ = "5.0.0"

import unittest
from shape import *

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle("blue", 10, 5)
        # setUp is arrange.
        # it will be used in each test to reduce
        # redundancy

    def test_init_valid(self):
        # Act and Assert
        self.assertEqual("blue", self.rectangle.color)
        self.assertEqual(10, self.rectangle._Rectangle__length)
        self.assertEqual(5, self.rectangle._Rectangle__width)

    def test_init_blank_color_raises_exception(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            Rectangle("", 10, 5)

    def test_init_length_invalid_raises_exception(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            Rectangle("red", "a", 5)

    def test_init_width_invalid_raises_exception(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            Rectangle("red", 10, "b")

    def test_str_method(self):
        expected = (
            "The shape color is blue.\n"
            "This rectangle has four sides with the lengths "
            "of 10, 5, 10 and 5 centimeters"
        )
        self.assertEqual(str(self.rectangle), expected)

    def test_area_valid(self):
        self.assertEqual(50, self.rectangle.calculate_area())

    def test_perimeter_valid(self):
        self.assertEqual(30, self.rectangle.calculate_perimeter())


if __name__ == "__main__":
    unittest.main()



"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Ralph Vitug"
__version__ = "4.0.0"

import unittest
from shape import *


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle("red", 3, 4, 5)

    def test_init_valid(self):
        # Assert and Act
        self.assertEqual("red", self.triangle.color)
        self.assertEqual(3, self.triangle._Triangle__side_1)
        self.assertEqual(4, self.triangle._Triangle__side_2)
        self.assertEqual(5, self.triangle._Triangle__side_3)

    def test_init_blank_color_raises_exception(self):
        with self.assertRaises(ValueError):
            Triangle(" ", 3, 4, 5)

    def test_init_side1_invalid_raises_exception(self):
        with self.assertRaises(ValueError):
            Triangle("red", "a", 4, 5)

    def test_init_side2_invalid_raises_exception(self):
        with self.assertRaises(ValueError):
            Triangle("red", 3, "b", 5)

    def test_init_side3_invalid_raises_exception(self):
        with self.assertRaises(ValueError):
            Triangle("red", 3, 4, "c")

    def test_init_invalid_triangle_fails_TIT(self):
       
        with self.assertRaises(ValueError):
            Triangle("red", 1, 2, 3)

    def test_area_valid(self):
        # (3 + 4 + 5) / 2 = 6
        self.assertEqual(6, self.triangle.calculate_area())

    def test_perimeter_valid(self):
        # 3 + 4 + 5 = 12
        self.assertEqual(12, self.triangle.calculate_perimeter())

    def test_str_method(self):
        expected = (
            "The shape color is red.\n"
            "This triangle has three sides with the lengths of "
            "3, 4 and 5 centimeters"
        )
        self.assertEqual(str(self.triangle), expected)


if __name__ == "__main__":
    unittest.main()
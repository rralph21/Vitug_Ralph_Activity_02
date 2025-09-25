"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = ""
__version__ = ""

import unittest
from shape import *


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle("red", 7, 8, 9)

        



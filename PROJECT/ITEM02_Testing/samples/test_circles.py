# To run 
# python3 -m unittest test_circles.py
# python3 -m unittest


import unittest
from circles import get_circle_area
from math import pi


class TestCircleArea( unittest.TestCase ):
    def test_area(self):
        # Test areas when radius is  >= 0
        self.assertAlmostEqual( get_circle_area(1) , pi  )
        self.assertAlmostEqual( get_circle_area(0),  0 )
        self.assertAlmostEqual( get_circle_area(2.1), ( pi * pow(2.1, 2)  ) )


    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises( ValueError, get_circle_area, -2 )


    def test_types(self):
        #Make sure type errors are raised when necessary
        self.assertRaises( ValueError, get_circle_area,  3+5j )
        self.assertRaises( ValueError, get_circle_area,  True )
        self.assertRaises( ValueError, get_circle_area,  "radius" )
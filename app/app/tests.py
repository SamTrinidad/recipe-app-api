"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(3, 8), 11)


    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        value = calc.subtract(11, 5)
        self.assertEqual(value, 6)
#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """"Unitest for max_integer([..])."""
    def test_max_integer_basic(self):
        """Test basic list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        """Test a siingle element"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_mixed_list(self):
        """Test a mixed list of integers"""
        self.assertEqual(max_integer([5, -3, 10, 0, -20]), 10)

    def test_max_integer_duplicate_elements(self):
        """Test a duplicate elements in a list"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_integer_float_list(self):
        """Test a list of floats"""
        self.assertAlmostEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_max_integer_strings(self):
        """Test a string"""
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_max_integer_mixed_types(self):
        """Test a list containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, "apple", 3])

    def test_max_integer_invalid_input(self):
        """Test invalid inputs"""
        with self.assertRaises(TypeError):
            max_integer("not a list")


if __name__ == '__main__':
    unittest.main()

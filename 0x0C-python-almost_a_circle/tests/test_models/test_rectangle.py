#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init_with_valid_params(self):
        """Test initialization of Rectangle with valid parameters."""
        rect = Rectangle(5, 10, 1, 2, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

    def test_init_with_invalid_params(self):
        """Test initialization of Rectangle with invalid parameters."""
        with self.assertRaises(TypeError):
            Rectangle("5", 10, 1, 2, 10)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 1, 2, 10)

    def test_area(self):
        """Test calculation of area."""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test display method."""
        rect = Rectangle(3, 2, 1, 1)
        expected_output = "\n###\n###"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_str(self):
        """Test string representation."""
        rect = Rectangle(5, 10, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        """Test update method."""
        rect = Rectangle(5, 10, 1, 2, 10)
        rect.update(20, 8, 15, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()

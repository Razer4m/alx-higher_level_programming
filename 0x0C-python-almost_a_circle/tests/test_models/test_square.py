#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_init_with_valid_params(self):
        """Test initialization of Square with valid parameters."""
        square = Square(5, 1, 2, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_init_with_invalid_params(self):
        """Test initialization of Square with invalid parameters."""
        with self.assertRaises(TypeError):
            Square("5", 1, 2, 10)
        with self.assertRaises(ValueError):
            Square(-5, 1, 2, 10)

    def test_area(self):
        """Test calculation of area."""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """Test display method."""
        square = Square(3, 1, 1)
        expected_output = "\n ###\n ###\n ###"
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        square.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_str(self):
        """Test string representation."""
        square = Square(5, 1, 2, 10)
        expected_str = "[Square] (10) 1/2 - 5"
        self.assertEqual(str(square), expected_str)

    def test_update(self):
        """Test update method."""
        square = Square(5, 1, 2, 10)
        square.update(20, 8, 3, 4)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        square = Square(5, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

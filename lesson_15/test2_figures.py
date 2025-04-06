import unittest
from homeworks_15 import Square, Rectangle, Circle 

class TestSquare(unittest.TestCase):
    def test_01_square_area(self):
        """Test if Square with side 4 returns correct area (16)."""
        square = Square(4)
        actual = square.get_area()
        expected = 16
        self.assertEqual(actual, expected)

    def test_02_square_perimeter(self):
        """Test that Square with side 4 returns correct perimeter (16)."""
        square = Square(4)
        actual = square.get_perimeter()
        expected = 16
        self.assertEqual(actual, expected)

    def test_03_square_negative_side(self):
        """Verify that ValueError is raised when side is negative."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_04_square_text_input(self):
        """Check that TypeError is raised when side is not a number (e.g. string)."""
        with self.assertRaises(TypeError):
            Square("abc")

class TestRectangle(unittest.TestCase):
    def test_01_rectangle_area(self):
        """Test that Rectangle with width 4 and height 6 returns correct area (24)."""
        rect = Rectangle(4, 6)
        actual = rect.get_area()
        expected = 24
        self.assertEqual(actual, expected)

    def test_02_rectangle_perimeter(self):
        """Test that Rectangle with width 4 and height 6 returns correct perimeter (20)."""
        rect = Rectangle(4, 6)
        actual = rect.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected)

    def test_03_rectangle_equal_sides(self):
        """Verify that ValueError is raised when width and height are equal."""
        with self.assertRaises(ValueError):
            Rectangle(5, 5)

    def test_04_rectangle_negative_value(self):
        """Check that ValueError is raised when any side is negative."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_05_rectangle_invalid_type(self):
        """Check that TypeError is raised when sides are not numbers."""
        with self.assertRaises(TypeError):
            Rectangle("three", 5)

class TestCircle(unittest.TestCase):
    def test_01_circle_area(self):
      """Test that Circle with radius 3 returns correct area (28.26)."""
      radius = 3
      circle = Circle(radius)
      expected = 3.14 * radius ** 2
      actual = circle.get_area()
      self.assertEqual(actual, expected)

    def test_02_circle_perimeter(self):
        """Test that Circle with radius 3 returns correct perimeter (18.84)."""
        circle = Circle(3)
        actual = circle.get_perimeter()
        expected = 2 * 3.14 * 3
        self.assertAlmostEqual(actual, expected, places=2)

    def test_03_circle_negative(self):
        """Verify that ValueError is raised when radius is negative."""
        with self.assertRaises(ValueError):
            Circle(-2)

    def test_04_circle_invalid_type(self):
        """Check that TypeError is raised when radius is not a number."""
        with self.assertRaises(TypeError):
            Circle([1, 2, 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)

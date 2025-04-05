import unittest
from homework14 import Rhombus

class TestRhombus(unittest.TestCase):

    def test_valid_rhombus(self):
        rhombus = Rhombus(10, 60)
        self.assertEqual(rhombus.side_a, 10)
        self.assertEqual(rhombus.angle_a, 60)
        self.assertEqual(rhombus.angle_b, 120)

    def test_valid_rhombus_with_different_angles(self):
        rhombus = Rhombus(5, 45)
        self.assertEqual(rhombus.angle_b, 135)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Rhombus(0, 60)

    def test_invalid_angle_too_small(self):
        with self.assertRaises(ValueError):
            Rhombus(10, -10)

    def test_invalid_angle_too_large(self):
        with self.assertRaises(ValueError):
            Rhombus(10, 180)

    def test_angle_b_cannot_be_set(self):
        rhombus = Rhombus(10, 70)
        with self.assertRaises(AttributeError):
            rhombus.angle_b = 110

    def test_none_values(self):
        with self.assertRaises(TypeError):  
            Rhombus(None, 60)

        with self.assertRaises(TypeError):
            Rhombus(10, None)

if __name__ == "__main__":
    unittest.main()
import unittest
from homework_14 import Rhomb

class RhombTest(unittest.TestCase):

    def test_01(self):
        """Verify if Rhomb with valid values is created"""
        rhomb = Rhomb(89, 100, 80)
        expected = 'Rhomb(side_a=89, angle_a=100, angle_b=80)'
        actual = repr(rhomb)
        self.assertEqual(actual, expected)

    def test_02(self):
        """Verify if angle B is calculated when not provided"""
        rhomb = Rhomb(89, 50)
        expected = 'Rhomb(side_a=89, angle_a=50, angle_b=130)'
        actual = repr(rhomb)
        self.assertEqual(actual, expected)

    def test_03(self):
        """Verify if Value error is raised when sum of angle A and angle B != 180"""
        with self.assertRaises(ValueError):
            Rhomb(89, 120, 80)

    def test_04(self):
        """Verify if Value error is raised when angle A <= 0"""
        with self.assertRaises(ValueError):
            Rhomb(89, -1, 80)

    def test_05(self):
        """Verify if Value error is raised when angle A >= 180"""
        with self.assertRaises(ValueError):
            Rhomb(89, 180, 80)

    def test_06(self):
        """Verify if Value error is raised when angle B <= 0"""
        with self.assertRaises(ValueError):
            Rhomb(89, 90, 0)

    def test_07(self):
        """Verify if Value error is raised when angle B >= 180"""
        with self.assertRaises(ValueError):
            Rhomb(89, 10, 180)

    def test_08(self):
        """Verify if Value error is raised when side a <= 0"""
        with self.assertRaises(ValueError):
            Rhomb(0, 100, 80)    

    def test_09(self):
        """Verify if angle B is recalculated when angle A changed"""
        rhomb = Rhomb(89, 100, 80)
        rhomb._angle_a = 20
        expected = 'Rhomb(side_a=89, angle_a=20, angle_b=160)'
        actual = repr(rhomb)
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)

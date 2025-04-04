import unittest
from homework_14 import Rhomb

class RhombTest(unittest.TestCase):

    def test_01(self):
        """Verify if Rhomb with valid values is created"""
        rhomb = Rhomb(89, 100)
        expected = 'Rhomb(side_a=89, angle_a=100, angle_b=80)'
        actual = repr(rhomb)
        self.assertEqual(actual, expected)

    def test_02(self):
        """Verify if Value error is raised when angle A <= 0"""
        with self.assertRaises(ValueError):
            Rhomb(89, -1)

    def test_03(self):
        """Verify if Value error is raised when angle A >= 180"""
        with self.assertRaises(ValueError):
            Rhomb(89, 180)

    def test_04(self):
        """Verify if Value error is raised when side a <= 0"""
        with self.assertRaises(ValueError):
            Rhomb(0, 100)    

    def test_05(self):
        """Verify if angle B is recalculated when angle A changed"""
        rhomb = Rhomb(89, 100)
        rhomb._angle_a = 20
        expected = 'Rhomb(side_a=89, angle_a=20, angle_b=160)'
        actual = repr(rhomb)
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)

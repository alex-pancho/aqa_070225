import unittest
from homework_14 import Romb 

class RhombusAnglesTest(unittest.TestCase):

    def test_01_valid_values(self):
        """Test if angle_b is correctly calculated from angle_a."""
        rhomb = Romb(10, 70)
        actual = rhomb.angle_b
        expected = 110
        self.assertEqual(actual, expected)
        
    def test_02_invalid_angle_zero(self):
        """Test ValueError when angle_a is 0."""
        with self.assertRaises(ValueError):
            Romb(10, 0)

    def test_03_invalid_side_length(self):
     """Test ValueError when side length is zero or less."""
     with self.assertRaises(ValueError):
         Romb(0, 90)
    
    def test_04_change_angle_a_updates_angle_b(self):
        """Test that changing angle_a updates angle_b correctly."""
        rhomb = Romb(12, 90)
        rhomb.angle_a = 75
        actual = rhomb.angle_b
        expected = 105
        self.assertEqual(actual, expected)


    def test_05_check_repr_output(self):
        """Test the string representation using repr()."""
        rh = Romb(7.5, 45)
        actual = repr(rh)
        expected = "Romb(side_length=7.5, angle_a=45, angle_b=135)"
        self.assertEqual(actual, expected)

    def test_06_setting_angle_b_manually_not_allowed(self):
        """Test that setting angle_b manually raises AttributeError."""
        rhomb = Romb(10, 80)
        with self.assertRaises(AttributeError):
            rhomb.angle_b = 50

if __name__ == "__main__":
    unittest.main(verbosity=2)
import math
import unittest


class Rhombus:
    def __init__ (self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
 
    def __setattr__ (self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Length cann't be less than 0")
            self.__dict__['side_a'] = value
        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Angle have to be 0 < angle < 180")
            self.__dict__['angle_a'] = value
            self.__dict__['angle_b'] = 180 - value
        elif name == "angle_b":
            raise AttributeError ("You cann't change angle B to manual. This is calculated automatically")
        else:
            self.__dict__[name] = value
        
    def __str__(self):
        return f"Rhombus: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"

Rhombus1 = Rhombus(5, 60)
print(Rhombus1)


class TestRhombus(unittest.TestCase):
    def test_valid_creation(self):
        Rhombus1 = Rhombus(10, 45)
        self.assertEqual(Rhombus1.side_a, 10)
        self.assertEqual(Rhombus1.angle_a, 45)
        self.assertEqual(Rhombus1.angle_b, 135)
    
    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Rhombus(0, 60)
        with self.assertRaises(ValueError):
            Rhombus(-6, 60)
    
    def test_invalid_angle(self):
        with self.assertRaises(ValueError):
            Rhombus(5, 0)
        with self.assertRaises(ValueError):
            Rhombus(5, 190)
        with self.assertRaises(ValueError):
            Rhombus(5, -40)
    
    def test_angle_assignment_updates_second_angle(self):
        Rhombus1 = Rhombus(7, 70)
        self.assertEqual(Rhombus1.angle_b, 110)
        Rhombus1.angle_a = 50
        self.assertEqual(Rhombus1.angle_a, 50)
        self.assertEqual(Rhombus1.angle_b, 130)

    def test_direct_assignment_of_angle_b_fails(self):
        Rhombus1 = Rhombus(8, 60)
        with self.assertRaises(AttributeError):
            Rhombus1.angle_b = 90


if __name__ == '__main__':
    unittest.main()
"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, 
    значення кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""
import unittest

class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        
    @property
    def angle_b(self):
        return 180 - self.angle_a
    

    def __str__(self):
        return f"Rhombus: side_a - {self.side_a}, angle_a - {self.angle_a}, angle_b - {self.angle_b}"

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side A must be > 0")
            super().__setattr__(name, value)
        elif name == "angle_a":
            if value <= 0 or  value >= 180:
                raise ValueError("Angle must be > 0 and <180")
            super().__setattr__(name, value)
        else:
            raise ValueError("Incorrect attribute. side_a or angle_a allowed only")

class TestRhombus(unittest.TestCase):

    def test_1_set_rhombus(self):
        test_romb = Rhombus(5,50)
        self.assertEqual(test_romb.side_a, 5)
        self.assertEqual(test_romb.angle_a, 50)
        self.assertEqual(test_romb.angle_b, 130)
    
    def test_2_str_rhombus(self):
        test_romb = Rhombus(5,50)
        self.assertEqual(str(test_romb), "Rhombus: side_a - 5, angle_a - 50, angle_b - 130")

    def test_3_setatr_rhombus_valid(self):
        test_romb = Rhombus(10,50)
        setattr(test_romb,"side_a",15)
        setattr(test_romb,"angle_a",60)
        self.assertEqual(test_romb.side_a, 15)
        self.assertEqual(test_romb.angle_a, 60)
        self.assertEqual(test_romb.angle_b, 120)

    def test_4_setatr_rhombus_side_a_below_0(self):
        test_romb = Rhombus(15,60)
        with self.assertRaises(ValueError) as context:
            setattr(test_romb,"side_a",-15)
            self.assertEqual(str(context.exception),"Side A must be > 0")
    
    def test_5_setatr_rhombus_angle_a_below_0(self):
        test_romb = Rhombus(15,60)
        with self.assertRaises(ValueError) as context:
            setattr(test_romb,"angle_a",-45)
            self.assertEqual(str(context.exception), "Angle must be > 0 and <180" )

    def test_6_setatr_rhombus_angle_a_over_180(self):
        test_romb = Rhombus(15,60)
        with self.assertRaises(ValueError) as context:
            setattr(test_romb,"angle_a",190)
            self.assertEqual(str(context.exception), "Angle must be > 0 and <180" )
        
    def test_7_setatr_incorrect_atribute(self):
        test_romb = Rhombus(15,60)
        with self.assertRaises(ValueError) as context:
            setattr(test_romb,"test",190)
            self.assertEqual(str(context.exception), "Incorrect attribute. side_a or angle_a allowed only" )

if __name__ == "__main__":
    romb = Rhombus(15,60)
    print(romb)
    setattr(romb,"side_a",50)
    setattr(romb,"angle_a",100)
    print(romb)
    print("___________Tests____________")
    unittest.main(verbosity=2)



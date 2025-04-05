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

class Romb:

    """
This code validates and sets the value of angle_a.
It first checks whether the input value is within the valid range (0 to 180).
If not, it raises a ValueError to prevent invalid geometry.
If the value is valid, it sets angle_a using super().__setattr__.
Then, it automatically calculates the adjacent angle (angle_b)
as 180 minus angle_a, and sets it as well.
This ensures that the sum of two adjacent angles in a rhombus
is always 180 degrees.

    """

    def __init__(self, side_length, angle_a):
        self.side_length = side_length
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_length":
            if value <= 0:
                raise ValueError("Side length must be greater than 0.")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if value <= 0 or value >= 180:
               raise ValueError("Angle must be between 0 and 180 degrees.")
            super().__setattr__("angle_a", value)
            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("angle_b is calculated automatically and cannot be set manually.")

        else:
            super().__setattr__(name, value)

    def __repr__(self):
        return f"Romb(side_length={self.side_length}, angle_a={self.angle_a}, angle_b={self.angle_b})"
    
if __name__ == "__main__":
    my_romb = Romb(12, 75)
    print(my_romb)

    another_romb = Romb(9.5, 65)
    print(another_romb)
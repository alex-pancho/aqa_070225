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
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    @staticmethod
    def val_side(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значення повинно бути цілим або дробним числом!")
        if value <= 0:
            raise ValueError("Сторона 'а' повина бути більше 0")

    @staticmethod
    def val_angles(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значення повинно бути цілим або дробним числом!")
        if not 0 < value < 180:
            raise ValueError("Кут не може бути меншим або дорівнювати 0 та дорівнювати або бути більшим 180")

    def __setattr__(self, name, value):
        if name == "side_a":
            self.val_side(value)
        elif name == "angle_a":
            self.val_angles(value)
        elif name == "angle_b":
            raise AttributeError("Кут 'b' розраховується автоматично і не може бути заданий напряму")
        super().__setattr__(name, value)

    @property
    def angle_b(self):
        return 180 - self.angle_a


if __name__ == "__main__":
    my_romb = Romb(1, 179)
    print(my_romb.side_a, my_romb.angle_a, my_romb.angle_b)

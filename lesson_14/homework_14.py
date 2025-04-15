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


class Rhombus:
    def __init__(self, side_a=None, angle_a=None):
        self.side_a = side_a
        self.angle_a = angle_a
        # angle_b буде розраховано автоматично

    def __setattr__(self, name, value):
        if name == "side_a":
            if value is not None:
                if not isinstance(value, (int, float)):
                    raise ValueError("Side must be a number")
                if value <= 0:
                    raise ValueError("Side must be greater than 0")

        elif name == "angle_a":
            if value is not None:
                if not isinstance(value, (int, float)):
                    raise ValueError("Angle must be a number")
                if not (0 < value < 180):
                    raise ValueError("angle_a must be in range 1–179 degrees")
                super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            if value is not None:
                if not isinstance(value, (int, float)):
                    raise ValueError("Angle must be a number")
                if not (0 < value < 180):
                    raise ValueError("angle_b must be in range 1–179 degrees")
                super().__setattr__("angle_a", 180 - value)

        super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus: side = {self.side_a}, angle A = {self.angle_a}, angle B = {self.angle_b}"


if __name__ == "__main__":
    rhombus = Rhombus(10, 60)
    # rhombus.side_a=0 #Side can't be 0 or shorter, your side: 0
    # rhombus.side_a="str" #ValueError: Side must be int, your side type: <class 'str'>
    rhombus.side_a = 1
    print(rhombus)
    # rhombus.angle_a = 0 #ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 0
    # rhombus.angle_a = 180 #ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 180
    # rhombus.angle_a="Hello" #ValueError: Angle must be int, your side type: <class 'str'>
    rhombus.angle_a = 100
    print(rhombus)
    # rhombus.angle_b = 0 # ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 0
    # rhombus.angle_b = 180 # ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 180
    # rhombus.angle_a="Hello" #ValueError: Angle must be int, your side type: <class 'str'>
    rhombus.__setattr__( "angle_a", 10)
    print(rhombus)
    setattr(rhombus, "angle_a", 20)
    print(rhombus)
    
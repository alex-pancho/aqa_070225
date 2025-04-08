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
    def __init__(self, side_a: int = None, angle_a: int = None, angle_b: int = None):
        self.__side_a = side_a
        self.__angle_a = angle_a
        self.__angle_b = angle_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, side_a: int):
        if not isinstance(side_a, int):
            raise ValueError(f"Side must be int, your side type: {type(side_a)}")
        if side_a > 0:
            self.__side_a = side_a
        else:
            raise ValueError(f"Side can't be 0 or shorter, your side: {side_a}")

    @property
    def angle_a(self):
        return self.__angle_a

    @angle_a.setter
    def angle_a(self, angle_a: int):
        if not isinstance(angle_a, int):
            raise ValueError(f"Angle must be int, your side type: {type(angle_a)}")
        if 0 < angle_a < 180:
            self.__angle_a = angle_a
            self.__angle_b = 180 - angle_a
        else:
            raise ValueError(f"Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: {angle_a}")

    @property
    def angle_b(self):
        return self.__angle_b

    @angle_b.setter
    def angle_b(self, angle_b: int):
        if not isinstance(angle_b, int):
            raise ValueError(f"Angle must be int, your side type: {type(angle_b)}")
        if 0 < angle_b < 180:
            self.__angle_a = 180 - angle_b
            self.__angle_b = angle_b
        else:
            raise ValueError(f"Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: {angle_b}")


if __name__ == "__main__":
    rhombus = Rhombus()
    # rhombus.side_a=0 #Side can't be 0 or shorter, your side: 0
    # rhombus.side_a="str" #ValueError: Side must be int, your side type: <class 'str'>
    rhombus.side_a = 1
    print(f"side_a = {rhombus.side_a}")
    # rhombus.angle_a = 0 #ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 0
    # rhombus.angle_a = 180 #ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 180
    # rhombus.angle_a="Hello" #ValueError: Angle must be int, your side type: <class 'str'>
    rhombus.angle_a = 1
    print(f"angle_a = {rhombus.angle_a}, angle_b = {rhombus.angle_b}")
    # rhombus.angle_b = 0 # ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 0
    # rhombus.angle_b = 180 # ValueError: Angle can't be 180 degrees or bigger, and 0 or lower degrees your angle: 180
    # rhombus.angle_a="Hello" #ValueError: Angle must be int, your side type: <class 'str'>
    rhombus.angle_b = 30
    print(f"angle_a = {rhombus.angle_a}, angle_b = {rhombus.angle_b}")

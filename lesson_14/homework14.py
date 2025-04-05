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
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if not isinstance(value, (int, float)):
                raise TypeError("Side 'a' must be a number.")
            if value <= 0:
                raise ValueError("Side 'a' must be greater than 0.")
            object.__setattr__(self, "_side_a", value)

        elif name == "angle_a":
            if not isinstance(value, (int, float)):
                raise TypeError("Angle 'a' must be a number.")
            if not (0 < value < 180):
                raise ValueError("Angle 'a' must be between 0 and 180 degrees (exclusive).")
            object.__setattr__(self, "_angle_a", value)
            object.__setattr__(self, "_angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Angle 'b' is automatically calculated and cannot be set.")

        else:
            object.__setattr__(self, name, value)

    @property
    def side_a(self):
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        self.__setattr__("side_a", value)

    @property
    def angle_a(self):
        return self._angle_a

    @angle_a.setter
    def angle_a(self, value):
        self.__setattr__("angle_a", value)

    @property
    def angle_b(self):
        return self._angle_b

if __name__ == "__main__":
    rhomb = Rhombus(5, 60)
    print(f"Side a: {rhomb.side_a}")
    print(f"Angle α: {rhomb.angle_a}")
    print(f"Angle β: {rhomb.angle_b}")
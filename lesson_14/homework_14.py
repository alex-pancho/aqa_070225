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
    def __init__(self, side_a, angle_a):

        self.side_a = side_a
        self.angle_a = angle_a  # це автоматично встановлює і кут angle_b

    @property
    def side_a(self):
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        if value <= 0:
            raise ValueError("Значення сторони сторона_а повинно бути більше 0.")
        self._side_a = value

    @property
    def angle_a(self):
        return self._angle_a

    @angle_a.setter
    def angle_a(self, value):
        if not (0 < value < 180):
            raise ValueError("Кут повинен бути в межах від 0 до 180 градусів і кути повинні задовольняти умову: кут_а "
                             "+ кут_б = 180")
        self._angle_a = value

    @property
    def angle_b(self):
        return 180 - self._angle_a

    def __repr__(self):
        return f"Ромб: (сторона_а={self.side_a}, кут_a={self.angle_a}, кут_б={self.angle_b})"


if __name__ == "__main__":
    romb = Rhombus(side_a=22, angle_a=22)
    print(romb)

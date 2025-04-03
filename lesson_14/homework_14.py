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

class Rhomb:
    def __init__(self, side_a: float, angle_a: float, angle_b: float = None):
        self._side_a = side_a
        self._angle_a = angle_a
        if angle_b is None: #при заданому значенні кут_а, значення кут_б обчислюється автоматично
            self._angle_b = 180 - angle_a
        else:
            if angle_a + angle_b != 180: # повинні задовольняти умову: кут_а + кут_б = 180
                raise ValueError('Sum of angle A and angle B must be 180')
            self._angle_b = angle_b

    def __setattr__(self, name, value):    
        if name == '_side_a':
            if value <= 0: # сторона_а повинна бути більше 0
                raise ValueError ("Expected value more than 1.")
            super().__setattr__(name, value)
        elif name == '_angle_a':
            if value <= 0 or value >= 180:
                raise ValueError ("Invalid angle A value: must be more than 0 and less than 180.")
            super().__setattr__(name, value)
            self._angle_b = 180 - value # recalculates angle B after angle A changed
        elif name == "_angle_b":
            if value <= 0 or value >= 180:
                raise ValueError ("Invalid angle B value: must be more than 0 and less than 180.")
            super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)

    def __repr__(self):
            return f"Rhomb(side_a={self._side_a}, angle_a={self._angle_a}, angle_b={self._angle_b})"

if __name__ == "__main__":
    rhomb = Rhomb(89, 100, 80) # valid check - PASS
    print(rhomb)

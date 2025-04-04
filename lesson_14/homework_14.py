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
        if name == "side_a" and value <= 0:
            raise ValueError("Довжина сторони має бути більше 0.")
        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут має бути між 0 і 180 градусами.")
            object.__setattr__(self, "angle_b", 180 - value)  
        object.__setattr__(self, name, value)
    
    def __str__(self):
        return f"Ромб зі стороною {self.side_a}, кут A {self.angle_a}°, кут B {self.angle_b}°"
    
    def __repr__(self):
        return f"Rhombus({self.side_a}, {self.angle_a})"
    
    def area(self):
        from math import sin, radians
        return self.side_a ** 2 * sin(radians(self.angle_a))
    
    def perimeter(self):
        return 4 * self.side_a


if __name__ == "__main__":
    rhombus = Rhombus(5, 60)
    print(rhombus)
    print("Площа:", rhombus.area())
    print("Периметр:", rhombus.perimeter())
class Rhombus:
    def __init__(self, side_a: float, angle_a: float):
        self._side_a = None
        self._angle_a = None
        self._angle_b = None
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0.")
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах (0, 180) градусів.")
            object.__setattr__(self, "_angle_b", 180 - value)  # Обчислюємо angle_b

        object.__setattr__(self, f"_{name}", value)  # Зберігаємо значення в _атрибут

    @property
    def side_a(self):
        return self._side_a

    @property
    def angle_a(self):
        return self._angle_a

    @property
    def angle_b(self):
        return self._angle_b

    def __repr__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"


if __name__ == "__main__":
    my_rhombus = Rhombus(10.58, 80.7)
    print(my_rhombus)

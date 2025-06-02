class Rhombus:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а  # кут_б встановиться автоматично через __setattr__

    def __setattr__(self, name, value):
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Довжина сторони має бути більше 0")
            super().__setattr__(name, value)

        elif name == "кут_а":
            if not (0 < value < 180):
                raise ValueError("Кут_а повинен бути між 0 та 180 градусами")
            super().__setattr__("кут_а", value)
            # автоматично обчислюємо суміжний кут_б
            super().__setattr__("кут_б", 180 - value)

        elif name == "кут_б":
            # кут_б не встановлюємо явно, він задається автоматично через кут_а
            # якщо хтось намагається встановити кут_б вручну, перевіримо правильність
            if abs(value + getattr(self, "кут_а", 0) - 180) > 1e-5:
                raise ValueError("Суміжний кут кут_б повинен бути 180 - кут_а")
            super().__setattr__(name, value)

        else:
            # для інших атрибутів звичайне встановлення
            super().__setattr__(name, value)

# Приклад використання:
try:
    r = Rhombus(5, 60)
    print(f"Сторона: {r.сторона_а}, кут_а: {r.кут_а}, кут_б: {r.кут_б}")
    r.кут_а = 120
    print(f"Після зміни кут_а: кут_а = {r.кут_а}, кут_б = {r.кут_б}")
    # r.сторона_а = -1  # викличе помилку
except ValueError as e:
    print("Помилка:", e)

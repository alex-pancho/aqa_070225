from abc import ABC, abstractmethod
import math

# --- ЗАДАНИЕ 1 ---

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

# Создаем объект TeamLead с передачей всех параметров через kwargs
tl = TeamLead(
    name="Іван",
    salary=100000,
    department="Розробка",
    programming_language="Python",
    team_size=5
)

print("Проверка атрибутов TeamLead:")
print(f"name: {tl.name}")
print(f"salary: {tl.salary}")
print(f"department: {tl.department}")
print(f"programming_language: {tl.programming_language}")
print(f"team_size: {tl.team_size}")


# --- ЗАДАНИЕ 2 ---

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

# Создаем объекты фигур
figures = [
    Square(4),
    Circle(3),
    Rectangle(5, 7)
]

print("ЗАДАНИЕ 2 — Площадь и периметр фигур:")
for fig in figures:
    print(f"{fig.__class__.__name__}: Площадь = {fig.area():.2f}, Периметр = {fig.perimeter():.2f}")

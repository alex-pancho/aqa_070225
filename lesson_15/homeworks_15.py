from abc import ABC, abstractmethod
import math


"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, 
Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати 
додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі 
атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує 
на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі
TeamLead
"""


class Employee:
    def __init__(self, name: str, salary: float, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department: str, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language: str, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(
        self,
        name: str,
        salary: float,
        department: str,
        programming_language: str,
        team_size: int,
    ):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language,
        )
        self.team_size = team_size


def test_team_lead():
    team_lead = TeamLead("Alice", 100000, "Development", "Python", 5)

    # Перевірка атрибутів з Manager
    assert team_lead.name == "Alice"
    assert team_lead.salary == 100000
    assert team_lead.department == "Development"

    # Перевірка атрибутів з Developer
    assert team_lead.programming_language == "Python"

    # Перевірка атрибута team_size
    assert team_lead.team_size == 5


"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius

    def area(self) -> float:
        return math.pi * self.__radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def area(self) -> float:
        return self.__length * self.__width

    def perimeter(self) -> float:
        return 2 * (self.__length + self.__width)


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self) -> float:
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c


if __name__ == "__main__":
    # Test for TeamLead
    test_team_lead()

    # Test for Shape classes
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print()

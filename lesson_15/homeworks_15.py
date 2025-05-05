"""Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи,
Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати
додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі
атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує
на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі
TeamLead"""


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

    def __str__(self):
        return f"My name is {self.name}, i have salary {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        self.department = department
        super().__init__(name=name, salary=salary, **kwargs)

    def __str__(self):
        return f"My name is {self.name}, i have salary {self.salary} and works in {self.department} department"


class Developer(Employee):
    def __init__(self, name, salary, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(name=name, salary=salary, **kwargs)

    def __str__(self):
        return f"My name is {self.name}, i have salary {self.salary}. My programming_language is {self.programming_language}"


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )

    def __str__(self):
        return (f"My name is {self.name}, i have salary {self.salary}. Works in {self.department} department. My "
                f"programming_language is {self.programming_language}. My team_size is {self.team_size}")


"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length  # приватний атрибут

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


if __name__ == "__main__":
    # task 1
    employee = Employee("Tatiana", "1000")
    manager = Manager("Oleksandr", "2000", "Analytics")
    developer = Developer("Vira", "3000", "Python")
    teamlead = TeamLead("Mike", "4000", "Analytics", "Python", 10)
    print(employee)
    print(manager)
    print(developer)
    print(teamlead)
    # task 2
    figures = [
        Square(4),
        Circle(3),
        Rectangle(5, 2)
    ]

    for figure in figures:
        print(f"{figure.__class__.__name__}:")
        print(f"Площа: {figure.area():.2f}")
        print(f"Периметр: {figure.perimeter():.2f}")

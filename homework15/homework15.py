from abc import ABC, abstractmethod
from math import pi
"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, 
Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати 
додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі 
атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує 
на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department
        
class Developer(Employee):
    def __init__(self, name, salary, pr_language):
        Employee.__init__(self, name, salary)
        self.pr_language = pr_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size, pr_language):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, pr_language)
        self.team_size = team_size

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
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Area: {self.area()}, Perimeter: {self.perimeter()}"

class Square(Shape):

    def __init__(self, side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Side must be a positive number.")
        self.__side = side

    @property
    def side(self):
        return self.__side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side  

class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        if (not isinstance(side_a, (int, float)) or side_a <= 0 or
            not isinstance(side_b, (int, float)) or side_b <= 0):
            raise ValueError("Sides must be positive numbers.")
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @property
    def side_b(self):
        return self.__side_b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

class Circle(Shape):

    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)

class Triangle(Shape):

    def __init__(self, side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Side must be a positive number.")
        self.__side = side

    @property
    def side(self):
        return self.__side

    def area(self):
        return round((3 ** 0.5 / 4) * self.side ** 2, 2)

    def perimeter(self):
        return 3 * self.side
    
if __name__ == "__main__":
    figures = [
        Square(4),
        Rectangle(4, 7),
        Circle(5),
        Triangle(6)
    ]

    for figure in figures:
        print(figure)
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
import math
from curses.textpad import rectangle


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print(f"Programming Language: {self.programming_language}")
        print(f"Team Size: {self.team_size}\n")


"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def set_radius(self, radius: float):
        self.__radius = radius

    def get_area(self):
        return round(math.pi * pow(self.__radius, 2), 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.__radius, 2)

    def display_info(self):
        print(f"Circle radius: {self.__radius}")
        print(f"Circle ares: {self.get_area()}")
        print(f"Circle perimeter: {self.get_perimeter()}\n")


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        self.__side_a = side_a
        self.__side_b = side_b

    def set_sides(self, side_a: float, side_b: float):
        self.__side_a = side_a
        self.__side_b = side_b

    def get_area(self):
        return round(self.__side_a * self.__side_b, 2)

    def get_perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def display_info(self):
        print(f"Rectangle sides: side_a = {self.__side_a}, side_b = {self.__side_b}")
        print(f"Rectangle area: {self.get_area()}")
        print(f"Rectangle perimeter: {self.get_perimeter()}\n")


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, angle: float):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__angle = angle

    def set_sides(self, side_a: float, side_b: float):
        self.__side_a = side_a
        self.__side_b = side_b

    def set_angle(self, angle):
        self.__angle = angle

    def get_area(self):
        return round(self.__side_a * self.__side_b * math.sin(math.radians(self.__angle)) / 2, 2)

    def get_perimeter(self):
        return round(math.sqrt(pow(self.__side_a, 2) + pow(self.__side_b, 2) - (
                2 * self.__side_a * self.__side_b) * math.cos(
            math.radians(self.__angle))) + self.__side_a + self.__side_b, 2)

    def display_info(self):
        print(f"Triangle sides and angle: side_a = {self.__side_a}, side_b = {self.__side_b}, angle = {self.__angle}")
        print(f"Triangle area: {self.get_area()}")
        print(f"Triangle perimeter: {self.get_perimeter()}\n")


if __name__ == "__main__":
    lead = TeamLead("Вадим", 40000, "QA", "Python", 5)
    lead.display_info()
    circle = Circle(1)
    rectangle = Rectangle(3, 4)
    triangle = Triangle(3, 4, 90)
    list_of_figures = [circle, rectangle, triangle]
    for figure in list_of_figures:
        figure.display_info()

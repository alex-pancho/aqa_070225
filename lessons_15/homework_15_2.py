#Task2
"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

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


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c


figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for fig in figures:
    print(f"{fig.__class__.__name__}: Area = {fig.area():.2f}, Perimeter = {fig.perimeter():.2f}")

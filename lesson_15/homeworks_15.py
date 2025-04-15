from abc import ABC, abstractmethod

"""Завдання 1
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
    def __init__(
        self,
        name,
        salary,
        department,
        programming_language,
        team_size
        ):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        
        
"""Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

class Figure(ABC):
    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.__radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_square(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_square(self):
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5  # без math.sqrt

    def get_perimeter(self):
        return self.__a + self.__b + self.__c


if __name__ == "__main__":
    figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for i, fig in enumerate(figures, 1):
    print(f"Фігура {i}: Площа = {fig.get_square():.2f}, Периметр = {fig.get_perimeter():.2f}")
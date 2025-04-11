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
TeamLead"""

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
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )



def test_team_lead():
    lead = TeamLead("Olena", 120000, "Development", "Python", 7)

    assert hasattr(lead, "name"), "Відсутній атрибут name"
    assert hasattr(lead, "salary"), "Відсутній атрибут salary"
    assert hasattr(lead, "department"), "Відсутній атрибут department"
    assert hasattr(lead, "programming_language"), "Відсутній атрибут programming_language"
    assert hasattr(lead, "team_size"), "Відсутній атрибут team_size"

    print("✅ Усі атрибути успішно перевірені.")


if __name__ == "__main__":
    test_team_lead()
    
"""Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod
import math



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

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius



class Rectangle(Figure):
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)



class Triangle(Figure):
    def __init__(self, side: float):
        self.__side = side

    def get_area(self):
        return (math.sqrt(3) / 4) * self.__side ** 2

    def get_perimeter(self):
        return 3 * self.__side


if __name__ == "__main__":
    figures = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3),
        Circle(2.5),
        Rectangle(10, 2)
    ]

    for i, fig in enumerate(figures, 1):
        print(f"   Фігура {i}: {fig.__class__.__name__}")
        print(f"   Площа: {fig.get_area():.2f}")
        print(f"   Периметр: {fig.get_perimeter():.2f}")
        print("-" * 30)
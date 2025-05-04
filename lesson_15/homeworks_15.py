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

Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

# ============================== Task 1 =====================================

"""
This module defines a simple employee hierarchy using class inheritance.

Classes:
- Employee: Base class with name and salary.
- Manager: Inherits from Employee and adds a department attribute.
- Developer: Inherits from Employee and adds a programming_language attribute.
- TeamLead: Inherits from both Manager and Developer. Represents a lead developer and adds a team_size attribute.

An example TeamLead object is created and its attributes are printed.
"""

class Employee:
    def __init__(self, name, salary):
        if not isinstance(salary, (int, float)):
            raise TypeError("Salary must be a number")
        if salary <= 0:
            raise ValueError("Salary must be greater than 0")
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        if not isinstance(department, str):
            raise TypeError("Department must be a string")
        self.department = department
        
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        if not isinstance(programming_language, str):
            raise TypeError("Programming language must be a string")
        self.programming_language = programming_language
        
class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        if not isinstance(team_size, int) or team_size <= 0:
            raise ValueError("Team size must be a positive integer")
        self.team_size = team_size

if __name__ == "__main__":
    lead = TeamLead("Ilonka", 3000, "Development", "Python", 5)

    print("Name:", lead.name)
    print("Salary:", lead.salary)
    print("Department:", lead.department)
    print("Programming Language:", lead.programming_language)
    print("Team Size:", lead.team_size)

# ============================== Task 2 =====================================

from abc import ABC, abstractmethod

"""
The class Figure is an abstract base class that defines methods to calculate area and perimeter.
It is inherited by:
- Square
- Rectangle
- Circle
Each shape validates input and implements its own area and perimeter calculations.
At the end, shape objects are created and their values are printed in a loop.
"""

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
       pass

class Square(Figure):
    def __init__(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("Side must be a number")
        if side <= 0:
            raise ValueError("Side must be greater than 0")       
        self.__side = side
    
    def get_area(self):
        square = self.__side * self.__side
        return square
         
    def get_perimeter(self):
        square_perimeter = self.__side * 4
        return square_perimeter

class Rectangle(Figure):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
           raise TypeError("Width and height must be numbers")   
        if width <= 0 or height <= 0:
           raise ValueError("Width and height must be greater than 0") 
        if width == height:
           raise ValueError("Rectangle must have different width and height")
       
        self.__width = width
        self.__height = height

    def get_area(self):
        rectangle_area = self.__width * self.__height
        return rectangle_area

    def get_perimeter(self):
        rectangle_perimeter = 2 * (self.__width + self.__height)
        return rectangle_perimeter

class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        
        self.__radius = radius

    def get_area(self):
        circle_area = 3.14 * self.__radius ** 2
        return circle_area

    def get_perimeter(self):
        circle_perimeter = 2 * 3.14 * self.__radius
        return circle_perimeter
  
if __name__ == "__main__":
    square1 = Square(4)
    rectangle1 = Rectangle(5, 8)
    circle1 = Circle(5)

    for figure in [square1, rectangle1, circle1]:
        print("Area:", figure.get_area(), "Perimeter:", figure.get_perimeter())

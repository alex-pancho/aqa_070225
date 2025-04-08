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
import unittest
from abc import ABC, abstractmethod


class Emploee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"Emploee {self.name}, earns ${self.salary}"

class Manager(Emploee):

    def __init__(self, name, salary, department):
        self.department = department
        Emploee.__init__(self, name, salary)

    def __str__(self):
        return f"Emploee {self.name}, earns ${self.salary} and works in {self.department} department"    
            
class Developer(Emploee):

    def __init__(self,  name, salary, programming_language):
        self.programming_language = programming_language
        Emploee.__init__(self, name, salary)

    def __str__(self):
        return f"Emploee {self.name} earns {self.salary}, skilled in {self.programming_language}"
        
class TeamLead(Manager, Developer):

    def __init__(self,name, salary, programming_language, department, team_size):
        self.team_size = team_size
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)

    def __str__(self):
        return  (f"Emploee {self.name} earns {self.salary}, "
        f"skilled in {self.programming_language}, "
        f"works in {self.department} department, team size {self.team_size} ")
    
class TestTeamLead(unittest.TestCase):

    def test_1_manag_atributes_in_team_lead(self):
        #verifies Manager and Developer atributes in TeamLead
        emploee_1 = Emploee("test-1", 100)
        manager = Manager( emploee_1.name, emploee_1.salary, "IT")
        lead = TeamLead(manager.name, manager.salary, "python", manager.department, 5)
        self.assertEqual(lead.department, "IT")
        self.assertEqual(lead.name, "test-1")
        self.assertEqual(lead.salary, 100)
        
    def test_2_dev_atributes_in_team_lead(self):
        #verifies Manager and Developer atributes in TeamLead
        emploee_2 = Emploee("test-2", 200)
        dev = Developer(emploee_2.name, emploee_2.salary, "python")
        lead = TeamLead(dev.name, dev.salary, dev.programming_language, "IT", 5)
        self.assertEqual(lead.programming_language, "python")
        self.assertEqual(lead.name, "test-2")
        self.assertEqual(lead.salary, 200)
      
"""Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from math import pi, sqrt

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

    def __str__(self):
        return f"Площа фігури {self.__class__.__name__} - {self.area()}, периметр - {self.perimeter()}"

class Square(Shape):

    def __init__(self, side):
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Side must be number and > 0")
        else:
            self.__side = side

    @property
    def side(self):
        return self.__side
    
    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side * 4  
    
class Rectangle(Shape):

    def __init__(self,side_a, side_b):
        if (not isinstance(side_a, (int, float)) 
        or not isinstance(side_b, (int, float))
        or side_a <= 0 or side_b <=0):
            raise ValueError("Sides must be number > 0")
        else:
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
        return (self.side_a + self.side_b) * 2
    
class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be number  > 0")
        else:
            self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return round(self.radius**2 * pi, 2)

    def perimeter(self):
        return round(self.radius*2 * pi, 2)

class RightAngelTriangle(Shape):

    def __init__(self, leg_a, leg_b):
        if (not isinstance(leg_a, (int, float)) 
        or not isinstance(leg_b, (int, float))
        or leg_a <= 0 or leg_b <=0):
            raise ValueError("Legs must be number > 0")
        else:
            self.__leg_a = leg_a
            self.__leg_b = leg_b

    @property
    def leg_a(self):
        return self.__leg_a
    
    @property
    def leg_b(self):
        return self.__leg_b

    def area(self):
        return (self.leg_a * self.leg_b)/2

    def perimeter(self):
        hypotenuse = sqrt(self.leg_a**2 + self.leg_b**2)
        return round((self.leg_a + self.leg_b + hypotenuse), 2)

if __name__ == "__main__":

    triangle_1 = RightAngelTriangle(3,4)
    triangle_2 = RightAngelTriangle(5,6)
    square_1 = Square(2)
    rectangle_1 = Rectangle(2, 3)
    circle_1 = Circle(3)

    print("_____Завдання 2 вивід через __str__")
    for element in [triangle_1, triangle_2, square_1, rectangle_1, circle_1]:
        print(element)
    
    print("_____Завдання 2 вивід через виклик в циклі")
    for element in [triangle_1, triangle_2, square_1, rectangle_1, circle_1]:
        print(f"Площа фігури - {element.area()}, переиметр - {element.perimeter()}")
    
    #triangle_3 = RightAngelTriangle(0,4)
    #triangle_4 = RightAngelTriangle(5,-6)
    #triangle_5 = RightAngelTriangle("a",4)
    #triangle_6 = RightAngelTriangle(5, [6])
    #square_2 = Square(-2)
    #square_3 = Square({2})
    #rectangle_2 = Rectangle(-2, 3)
    #rectangle_3 = Rectangle(2, -3)
    #rectangle_4 = Rectangle("2", 3)
    #rectangle_5 = Rectangle(2, "3")
    #circle_2 = Circle(0)
    #ircle_3 = Circle("3")
    print("_____Завдання 1")
    unittest.main(verbosity=2)
    
    
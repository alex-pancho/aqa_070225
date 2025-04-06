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
from abc import ABC, abstractmethod
import math

class Employee:
    def __init__(self, name: str, salary:float):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name:str, salary:float, department:str):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name:str, salary:float, programming_language:str):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name:str, salary: int|float, department:str, programming_language:str, team_size:int):
        if not isinstance (name, str):
            raise TypeError ("'Str' type is expected as 'name'")
        if not isinstance (salary, (int, float)):
            raise TypeError ("'Int' or 'float' type is expected as 'salary'")
        if not isinstance (department, str):
            raise TypeError ("'Str' type is expected as 'department'")
        if not isinstance (programming_language, str):
            raise TypeError ("'Str' type is expected as 'programming_language'")
        if not isinstance (team_size, int):
            raise TypeError ("'Int' is expected as 'team_size'")
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
            return f"TeamLead: {self.name}, Salary: {self.salary}, Department: {self.department}, " \
                f"Programming Language: {self.programming_language}, Team Size: {self.team_size}"
"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної. 
"""
class Figure(ABC):

    @abstractmethod
    def square_calc(self):
        pass

    @abstractmethod
    def perimeter_calc(self):
        pass

class Square(Figure):
    def __init__(self, side:float):
        self.__side = side

    def square_calc(self):
        return pow(self.__side, 2)
    
    def perimeter_calc(self):
        return self.__side * 4
    
    def __str__(self):
        return f'Class "Square", side value - {self.__side}. Square: {self.square_calc()}, perimeter: {self.perimeter_calc()}.'
    
class Rhomb(Figure):
    def __init__(self, side: float, height:float):
        self.__side = side
        self.__height = height

    def square_calc(self):
        return self.__side * self.__height
    
    def perimeter_calc(self):
        return self.__side * 4
    
    def __str__(self):
        return f'Class "Rhomb", side value - {self.__side}, height value - {self.__height}. Square: {self.square_calc()}, perimeter: {self.perimeter_calc()}.'

class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def square_calc(self):
        return round(math.pi * pow(self.__radius, 2))
    
    def perimeter_calc(self):
        return round(2 * math.pi * self.__radius)
    
    def __str__(self):
        return f'Class "Circle", radius value - {self.__radius}. Square: {self.square_calc()}, perimeter: {self.perimeter_calc()}.'            

if __name__ == "__main__":
    # emploee = Employee("Ivan", 5000)
    # print(emploee.name, emploee.salary)
    # manager = Manager("Ivan", 5000, "IT")
    # print(manager.name, manager.salary, manager.department)
    # developer = Developer("Ivan", 5000, "Python")
    # print(developer.name, developer.salary, developer.programming_language)
    team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8)
    print(team_lead)
    # print(TeamLead.mro()) #[<class '__main__.TeamLead'>, <class '__main__.Manager'>, <class '__main__.Developer'>, <class '__main__.Employee'>, <class 'object'>]
    my_square = Square(5)
    print(my_square)
    my_rhomb = Rhomb(25, 10)
    print(my_rhomb)
    my_circle = Circle(5)
    print(my_circle)
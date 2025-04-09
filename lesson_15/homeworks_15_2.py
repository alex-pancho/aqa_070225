"""Завдання 
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі 
та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично 
вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. 
повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних 
об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
    """
from abc import ABC, abstractmethod

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
    
    @property
    def radius(self):
        return self.__radius 
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Радіус повинен бути додатнім")
        self.__radius = value
        
    def area(self):
        return 3.14 * self.__radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.__radius
    
class Square(Figure):
    
    def __init__(self, side_lenght):
        self.__side_lenght = side_lenght
    
    @property
    def side_lenght(self):
        return self.__side_lenght
    
    @side_lenght.setter
    def side_lenght(self, value):
        if value < 0:
            raise ValueError("Сторона квадрата повиненна бути додатньою.")
        self.__side_lenght = value
    
        
    def area(self):
        return self.__side_lenght ** 2     
    
    def perimeter(self):
        return 4 * self.__side_lenght 
    
class Triangle(Figure):
    
    def __init__(self, side_lenght_a, side_lenght_b, side_lenght_c, height):
        self.__side_lenght_a = side_lenght_a
        self.__side_lenght_b = side_lenght_b
        self.__side_lenght_c = side_lenght_c
        self.__height = height
        
    @property
    def side_lenght_a(self):
        return self.__side_lenght_a
    
    @property
    def side_lenght_b(self):
        return self.__side_lenght_b
    
    @property
    def side_lenght_c(self):
        return self.__side_lenght_c
    
    @property
    def height(self):
        return self.__height
    
    def area(self):
        return 0.5 * self.__side_lenght_a * self.__height
    
    def perimeter(self):
        return self.__side_lenght_a + self.__side_lenght_b + self.__side_lenght_c 

if __name__ == "__main__":  
    
    c = Circle(4)
    s = Square(10)
    t = Triangle(5, 10, 7, 4)
    figures = [c, s, t]
    for f in figures:
        print(f"{f.__class__.__name__}: площа = {f.area()}, периметр = {f.perimeter()}")
    

  
     
    
    
    
        
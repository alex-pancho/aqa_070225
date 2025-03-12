"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:
    def __init__(self, name, surname, age, average_point):
        self.name = name
        self.surname = surname
        self.age = age
        self.__points = average_point

    def get_average_point(self):
        return self.__points
    
    def set_average_point(self, value):
        if isinstance (value, (int, float)):
                       self.__points = value
        else:
              raise ValueError ('Expected int or float value.')

if __name__ == "__main__":

    student_1 = Student(name = 'Ivan', surname = 'Ukrainets', age = 19, average_point = 75)

    print('Initial attributes:')
    print(f'Name: {student_1.name}, Surname: {student_1.surname}, Age: {student_1.age}, Average point: {student_1.get_average_point()}')

    student_1.set_average_point(95.7)
    print('Changed points attribute:')
    print(f'Name: {student_1.name}, Surname: {student_1.surname}, Age: {student_1.age}, Average point: {student_1.get_average_point()}')
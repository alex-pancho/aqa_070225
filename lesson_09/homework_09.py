"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:
        
    def __init__(self, name, surname, age, avr_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.avr_grade = avr_grade
        
    def grade(self, new_grade):
        self.avr_grade = new_grade
    
    def stud_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.avr_grade}")
        
    
stud = Student("Віталій", "Дорохін", 35, 95)
stud.stud_info()
stud.grade(99)
print("Оновленний бал:")
stud.stud_info()        
                
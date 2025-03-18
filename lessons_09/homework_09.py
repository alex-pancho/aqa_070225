"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""
class Student:

    def __init__(self, firstname, surname, age, avr_grade):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.avr_grade = avr_grade
    
    def change_grade(self, new_grade):
        self.avr_grade = new_grade

    
    def student_inf(self):
        print(f'Name: {self.firstname}')
        print(f'Surname: {self.surname}')
        print(f'Age: {self.age}')
        print(f'Average grade: {self.avr_grade}')



student = Student("Ярослав", "Биков", 24, 89)
student.student_inf()
student.change_grade(91)
print("Update:")
student.student_inf()

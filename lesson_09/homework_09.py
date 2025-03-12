"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""
class Student:

    def __init__(self, first_name, last_name, age, avarage_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.avarage_score = avarage_score
    
    def change_score(self, avarage_score):
        self.avarage_score = avarage_score + avarage_score * 0.1
        return self.avarage_score
""" 
if __name__ == "__name__":
    student_1 = Student("Petro", "Onsienko", 19, 4.5)
    #result = student_1.change_score()
    print(student_1.first_name, student_1.last_name, student_1.age, student_1.avarage_score)

"""
student_1 = Student("Petro", "Onsienko", 19, 4.5)
print(student_1.first_name, student_1.last_name, student_1.age, student_1.avarage_score)
result = student_1.change_score(3)
print(student_1.first_name, student_1.last_name, student_1.age, result)
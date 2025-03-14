"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""
class Student:
    def __init__(self,first_name, last_name, age, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa
 
    def change_gpa(self, new_gpa):
        self.gpa = new_gpa

    def print_info(self):
        print(f"Name: {self.first_name} {self.last_name} age: {self.age} gpa: {self.gpa}")

if __name__ == "__main__":
    student_one = Student("Willa", "Brown", 19, 10)
    student_one.print_info()
    student_one.change_gpa(12)
    student_one.print_info()    

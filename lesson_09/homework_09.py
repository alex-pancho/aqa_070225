"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:
    def __init__(self, first_name, last_name, age, grade_point_averge):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade_point_averge = grade_point_averge

    def update_grade_point_averge(self, new_geade_point_averge):
        self.grade_point_averge = new_geade_point_averge
        
student = Student("Rostyslav", "Lysytsia", 25, 90.0)

print(f"Імʼя студента:", student.first_name, "\nПрізвище студента:", student.last_name, "\nВік студента:", student.age, "\nСередній бал студента:", student.grade_point_averge)

student.update_grade_point_averge(100)

print(f"\nОновлений середній бал студента", "\nІмʼя студента:", student.first_name, "\nПрізвище студента:", student.last_name, "\nВік студента:", student.age, "\nСередній бал студента:", student.grade_point_averge)

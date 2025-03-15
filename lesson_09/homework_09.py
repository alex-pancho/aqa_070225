"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""


class Student:
    def __init__(self, first_name, last_name, age, avarage_point):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avarage_point = avarage_point

    def change_avarege(self, new_avarage_point):
        self.avarage_point = new_avarage_point

    def student_info(self):
        print(f"Ім’я студента: {self.first_name}")
        print(f"Прізвище студента: {self.last_name}")
        print(f"Вік студента: {self.age}")
        print(f"Середній бал студента: {self.avarage_point}")


if __name__ == "__main__":
    # Створили об’єкт Тетяна
    tetiana = Student("Tetiana", "Lypnyk", 30, "90")
    # вивели інформацю про тетяну
    tetiana.student_info()
    print("________________")
    # підвищили Тетяні бал
    tetiana.change_avarege("100")
    # показали нову інформацію про Тетяну
    tetiana.student_info()

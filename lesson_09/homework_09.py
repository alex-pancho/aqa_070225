"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""


class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, score):
        self.average_score = score


if __name__ == "__main__":
    vadym = Student("Vadym", "Hello", 23, 95)
    print(f"{vadym.name}'s average score is {vadym.average_score}\n")
    vadym.set_average_score(100)
    print(F"Name:{vadym.name}, surname:{vadym.surname}, age: {vadym.age}, average_score: {vadym.average_score}")

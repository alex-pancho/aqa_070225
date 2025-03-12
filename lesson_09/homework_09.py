"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:
    def __init__(self, name, surname, age, avscore):
        self.name = name
        self.surname = surname
        self.age = age
        self.avscore = avscore 

    def set_avscore(self, new_avscore):
       
        if 0 <= new_avscore <= 5:
            self.avscore = new_avscore
        else:
            print("Invalid average score. Please provide a score between 0 and 5.")

    def get_avscore(self):
        
        return self.avscore 

    def display_info(self):
        
        print(f"Student: {self.name} {self.surname}, Age: {self.age}, Average Score: {self.avscore}")


student1 = Student("Ivan", "Kropivnyckyj", 20, 4.5)


student1.display_info()

student1.set_avscore(4.8) 

student1.display_info()

student1.set_avscore(6) 

student1.display_info()
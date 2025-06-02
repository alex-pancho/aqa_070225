import math

class Romb:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а

    def __setattr__(self, name, value):
        if name == 'сторона_а':
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0")
        elif name == 'кут_а':
            if not (0 < value < 180):
                raise ValueError("Кут ромба повинен бути в межах від 0 до 180 (не включаючи)")
            # автоматично обчислюємо кут_б
            object.__setattr__(self, 'кут_б', 180 - value)

        object.__setattr__(self, name, value)

    def __str__(self):
        return f"Ромб зі стороною a = {self.сторона_а}, кут α = {self.кут_а}, кут β = {self.кут_б}"

# Приклад використання:
ромб = Romb(10, 60)
print(ромб)

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.average_grade = new_grade
        else:
            raise ValueError("Average grade must be between 0 and 100")

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Average Grade: {self.average_grade}"

# Create a student object
student1 = Student("Ivan", "Petrenko", 20, 85)

# Print student info
print("Before grade update:")
print(student1)

# Update average grade
student1.update_average_grade(92)

# Print updated student info
print("After grade update:")
print(student1)



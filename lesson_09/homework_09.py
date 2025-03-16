"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""
class Student:
    def __init__(self,first_name: str, last_name:str, age:float, gpa:float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

        #type/value check
        if not isinstance(first_name, str):
            raise ValueError("String is expected for first name") 
        if not isinstance(last_name, str):
            raise ValueError("String is expected for last name") 
        if not isinstance(age, (int, float)) or not (16 <= age <= 100):
            raise ValueError("Int or float in range 16-100 is expected for age") 
        if not isinstance(gpa, (int, float)) or not (0 <= gpa <= 100):
            raise ValueError("Int or float in range 0-100 is expected for GPA") 
        
         
    def change_gpa(self, new_gpa:float):
        if isinstance(new_gpa, (int, float)) and (0 <= new_gpa <= 100):
            self.gpa = new_gpa
        else:
            raise ValueError("Int or float in range 0-100 is expected for new GPA") 

    def print_info(self):
        print(f"Name: {self.first_name} {self.last_name} age: {self.age} gpa: {self.gpa}")

if __name__ == "__main__":
    student_one = Student("Willa", "Brown", 18, 90)
    student_one.print_info()
    student_one.change_gpa(92)
    student_one.print_info()    

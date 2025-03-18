class Student:
    def __init__(self, name: str, surname: str, age: int, grades: float):
        self.__name = None
        self.set_name(name)
        self.__surname = None
        self.set_surname(surname)
        self.__age = None
        self.set_age(age)
        self.__grades = None
        self.set_grades(grades)

    def set_name(self, new_name: str):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a string and not empty")
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_surname(self, new_surname: str):
        if not isinstance(new_surname, str) or not new_surname.strip():
            raise ValueError("Surname must be a string and not empty")
        self.__surname = new_surname

    def get_surname(self):
        return self.__surname

    def set_age(self, new_age: int):
        if not isinstance(new_age, int) or not 1 <= new_age <= 100:
            raise ValueError("Age must be an integer and between 1 and 100")
        self.__age = new_age

    def get_age(self):
        return self.__age

    def set_grades(self, new_grades: float):
        if isinstance(new_grades, int):
            new_grades = float(new_grades)
        if not isinstance(new_grades, float) or not 0 <= new_grades <= 12:
            raise ValueError("Grades must be a float and between 0 and 12")
        self.__grades = new_grades

    def get_grades(self):
        return self.__grades


"""  Функція розрахує середнє арифметичне списку чисел.
"""


def average_of_list(lst: list[int | float]) -> int | float | str:
    if not lst:
        raise ValueError("List is empty")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise TypeError("List must contain only numbers")
    return sum(lst) / len(lst)

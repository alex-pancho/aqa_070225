"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

from aqa_070225.lesson_10.homeworks import Student, average_of_list
import unittest


class StudentTest(unittest.TestCase):
    """
    Клас для тестування класу Student.

    Містить позитивні та негативні тести для перевірки правильності створення об'єкта Student
    та обробки винятків у випадках неправильних аргументів.
    """

    def test_01_student(self):
        """
        Перевіряє коректне створення об'єкта Student.

        Перевіряються значення атрибутів name, surname, age, grades.
        """
        student = Student("John", "Doe", 20, 10.0)
        self.assertEqual(student.get_name(), "John")
        self.assertEqual(student.get_surname(), "Doe")
        self.assertEqual(student.get_age(), 20)
        self.assertEqual(student.get_grades(), 10.0)

    def test_02_student(self):
        """
        Перевіряє виняток ValueError, коли name є порожнім рядком.
        """
        with self.assertRaises(ValueError) as e:
            Student("", "Doe", 20, 10)
        self.assertEqual(str(e.exception), "Name must be a string and not empty")

    def test_03_student(self):
        """
        Перевіряє виняток ValueError, коли name не є рядком.
        """
        with self.assertRaises(ValueError) as e:
            Student(123, "Doe", 20, 10)
        self.assertEqual(str(e.exception), "Name must be a string and not empty")

    def test_04_student(self):
        """
        Перевіряє виняток ValueError, коли surname є порожнім рядком.
        """
        with self.assertRaises(ValueError) as e:
            Student("John", "", 20, 10)
        self.assertEqual(str(e.exception), "Surname must be a string and not empty")

    def test_05_student(self):
        """
        Перевіряє виняток ValueError, коли surname не є рядком.
        """
        with self.assertRaises(ValueError) as e:
            Student("John", 123, 20, 10)
        self.assertEqual(str(e.exception), "Surname must be a string and not empty")

    def test_06_student(self):
        """
        Перевіряє виняток ValueError, коли age не є цілим числом.
        """
        with self.assertRaises(ValueError) as e:
            Student("John", "Doe", 20.5, 10)
        self.assertEqual(
            str(e.exception), "Age must be an integer and between 1 and 100"
        )

    def test_07_student(self):
        """
        Перевіряє виняток ValueError, коли age виходить за межі допустимого діапазону (1–100).
        """
        with self.assertRaises(ValueError) as e:
            Student("John", "Doe", 101, 10)
        self.assertEqual(
            str(e.exception), "Age must be an integer and between 1 and 100"
        )

    def test_08_student(self):
        """
        Перевіряє виняток ValueError, коли grades не є float.
        """
        with self.assertRaises(ValueError) as e:
            Student("John", "Doe", 20, "10")
        self.assertEqual(
            str(e.exception), "Grades must be a float and between 0 and 12"
        )

    def test_09_student(self):
        """
        Перевіряє виняток ValueError, коли grades виходять за межі допустимого діапазону (0–12).
        """
        with self.assertRaises(ValueError) as e:
            Student("John", "Doe", 20, 12.5)
        self.assertEqual(
            str(e.exception), "Grades must be a float and between 0 and 12"
        )

    def test_10_student(self):
        """
        Перевіряє випадок, коли grades передається як ціле число.
        """
        student = Student("John", "Doe", 20, 10)
        self.assertEqual(student.get_grades(), 10.0)

    def test_11_student(self):
        """
        Перевіряє TypeError при надлишковій кількості аргументів під час створення об'єкта Student.
        """
        with self.assertRaises(TypeError) as e:
            student = Student("John", "Doe", 20, 10.5, 10)
        self.assertEqual(
            str(e.exception),
            "Student.__init__() takes 5 positional arguments but 6 were given",
        )

    def test_12_student(self):
        """
        Перевіряє TypeError при недостатній кількості аргументів під час створення об'єкта Student.
        """
        with self.assertRaises(TypeError) as e:
            Student("Doe", 20, 10.5)
        self.assertEqual(
            str(e.exception),
            "Student.__init__() missing 1 required positional argument: 'grades'",
        )


class AverageTest(unittest.TestCase):
    """
    Клас для тестування функції average_of_list.

    Містить позитивні та негативні тести на коректне обчислення середнього значення та обробку помилок.
    """

    def test_01_average(self):
        """
        Перевіряє обчислення середнього значення для списку з одним елементом.
        """
        avg = average_of_list([0])
        self.assertEqual(avg, 0)

    def test_02_average(self):
        """
        Перевіряє обчислення середнього значення для списку з кількох елементів.
        """
        avg = average_of_list([3, 4])
        self.assertEqual(avg, 3.5)

    def test_03_average(self):
        """
        Перевіряє виняток ValueError, коли список порожній.
        """
        with self.assertRaises(ValueError) as e:
            average_of_list("")
        self.assertEqual(str(e.exception), "List is empty")

    def test_04_average(self):
        """
        Перевіряє виняток TypeError, коли в списку є нечислові значення.
        """
        with self.assertRaises(TypeError) as e:
            average_of_list([1, 2, 5, "as"])
        self.assertEqual(str(e.exception), "List must contain only numbers")


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import reversed_string, sum_numbers_in_list, math_average, Student
import unittest




class HomeworksTest(unittest.TestCase):


   def test_01_reverse(self):
       """ Позитивний тест на роботу методу, шо перекручує строку задом наперед """
       str = "Its Unittest!"
       actual = reversed_string(str)
       expected = str[::-1]
       self.assertEqual(actual, expected), "Строка повертаєтсья не перекрученою"


   def test_02_empty_list(self):
       """ Тест на порожній список """
       with self.assertRaises(ValueError):
           sum_numbers_in_list([]), "Порожній список"


   def test_03_types(self):
       """Перевірка, що передача неправильного формату списку з строками викликає TypeError"""
       small_list = [1, 2, 3, 4, "іваіва", 6, 7, 8, 9, 10]
       with self.assertRaises(TypeError):
           math_average(small_list), "Неправильний тип"


   def test_04_type(self):
       """Перевірка, що у самій помилці TypeError при використанні різних типів даних має текст: unsupported operand type(s) for +: 'int' and 'str'"""
       small_list = [1, 2, 3, 4, "іваіва", 6, 7, 8, 9, 10]
       with self.assertRaises(TypeError) as context:
           math_average(small_list)
       self.assertTrue("unsupported operand type(s) for +: 'int' and 'str'" in str(context.exception))


   def test_05_zero(self):
       """Перевірка, що дідення на нуль викликає ZeroDivisionError"""
       small_list = []
       with self.assertRaises(ZeroDivisionError):
           math_average(small_list), "Ділення на нуль"


   def test_06_change_avarege(self):
       """Тест на коректну зміну балів"""
       self.student = Student("Tetiana", "Lypnyk", 30, 10000)
       self.student.change_avarege(90)
       self.assertEqual(self.student.avarage_point, 90)


   def test_07_change_avarege_invalid(self):
       """Тест на зміну балів неправильного типу"""
       self.student = Student("Tetiana", "Lypnyk", 30, 10000)
       with self.assertRaises(TypeError):
           self.student.change_avarege("invalid")


   def test_08_attributes(self):
       """Тест на типи атрибутів класа"""
       self.student = Student("Tetiana", "Lypnyk", 30, 90)
       self.assertIsInstance(self.student.first_name, str)
       self.assertIsInstance(self.student.last_name, str)
       self.assertIsInstance(self.student.age, int)
       self.assertIsInstance(self.student.avarage_point, int)


   def test_09_invalid_avarege_type(self):
       """Тест перевіряє тип даних при зміні оцінки"""
       self.student = Student("Tetiana", "Lypnyk", 30, 90)
       with self.assertRaises(TypeError):
           self.student.change_avarege("90"), "Type Error при зміні оцінки"


   def test_10_age_is_zero(self):
       """Перевірка на вік студента, що йому не нуль"""
       with self.assertRaises(ValueError):
           self.student = Student("Tetiana", "Lypnyk", 0, 90), "Перевірка віку студента"


   def test_11_negative_age(self):
       """Перевірка на вік студента, що при відємному значенні ValueError"""
       with self.assertRaises(ValueError):
           self.student = Student("Tetiana", "Lypnyk", -55, 90), "Перевірка віку студента"




if __name__ == "__main__":
   unittest.main(verbosity=2)




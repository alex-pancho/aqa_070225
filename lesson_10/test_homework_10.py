"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import sum_numbers_in_list
import unittest

class NazvaTest(unittest.TestCase):

    def test_01(self):
        """ Test NazvaTest with strings of numbers """
        my_list = ["1,2,3", "4,0,6"]
        actual = sum_numbers_in_list(my_list)
        expected = [6, 10]
        self.assertEqual(actual, expected)

    def test_02(self):
        """ Test NazvaTest with list with 1 element"""
        my_list = [1]
        with self.assertRaises(ValueError):
            sum_numbers_in_list(my_list)

    
    def test_03(self):
        """ Test NazvaTest with empty list"""
        my_list = []
        with self.assertRaises(ValueError):
            sum_numbers_in_list(my_list)

    def test_04(self):
        """ Test NazvaTest with non-number strings"""
        my_list = ["1,2,3", "asas7,8,9", "4,0,6"]
        actual = sum_numbers_in_list(my_list)
        expected = [6, "Не можу це зробити!", 10]
        self.assertEqual(actual,expected)

if __name__ == "__main__":
    unittest.main(verbosity=3)

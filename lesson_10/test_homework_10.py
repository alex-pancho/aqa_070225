"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import func
import unittest

class NazvaTest(unittest.TestCase):

    def test_01(self):
        """ Doc here """
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)

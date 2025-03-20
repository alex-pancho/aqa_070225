"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import unittest
from homeworks import sum_two_numbers, sum_of_digits, swap_dict_keys_and_values, clean_string


class TestHomeworks(unittest.TestCase):

    def test_sum_two_numbers_valid(self):
        numbers = (1, 3)
        expected = 4
        actual = sum_two_numbers(*numbers)
        self.assertEqual(actual, expected)

    def test_sum_two_numbers_invalid(self):
        values = (1, "a")
        expected = "Для вводу доступні тільки числа!"
        actual = sum_two_numbers(*values)
        self.assertEqual(actual, expected)

    def test_sum_two_numbers_negative(self):
        numbers = (-1, -3)
        expected = -4
        actual = sum_two_numbers(*numbers)
        self.assertEqual(actual, expected)

    def test_sum_two_numbers_invalid_type(self):
        values = ([1, 2], 3)
        expected = "Для вводу доступні тільки числа!"
        actual = sum_two_numbers(*values)
        self.assertEqual(actual, expected)

    def test_sum_of_digits(self):
        number = (445,)
        expected = 13
        actual = sum_of_digits(*number)
        self.assertEqual(actual, expected)

    def test_sum_of_digits_single_digit(self):
        number = (7,)
        expected = 7
        actual = sum_of_digits(*number)
        self.assertEqual(actual, expected)

    def test_sum_of_digits_large_number(self):
        number = (123456789,)
        expected = 45
        actual = sum_of_digits(*number)
        self.assertEqual(actual, expected)

    def test_sum_of_digits_invalid_type(self):
        values = ("hello",)
        with self.assertRaises(ValueError):
            sum_of_digits(*values)
   
    def test_swap_dict_keys_and_values(self):
        input_dict = ({"Key_Key": "Key_Value", "Value_Key": "Value_Value"},)
        expected = {"Key_Value": "Key_Key", "Value_Value": "Value_Key"}
        actual = swap_dict_keys_and_values(*input_dict)
        self.assertEqual(actual, expected)

    def test_swap_dict_keys_and_values_empty(self):
        empty_dict = ({},)
        expected = {}
        actual = swap_dict_keys_and_values(*empty_dict)
        self.assertEqual(actual, expected)

    def test_clean_string(self):
        input_string = ("  Hello     world!  Привіт    Свіііт!. ",)
        expected = "Hello world! Привіт Свіііт!."
        actual = clean_string(*input_string)
        self.assertEqual(actual, expected)

    def test_clean_string_single_space(self):
        input_string = ("Hello world!",)
        expected = "Hello world!"
        actual = clean_string(*input_string)
        self.assertEqual(actual, expected)

    def test_clean_string_empty(self):
        input_string = ("     ",)
        expected = ""
        actual = clean_string(*input_string)
        self.assertEqual(actual, expected)

    def test_clean_string_invalid_type(self):
        input_string = (12345,)
        expected = "12345"
        actual = clean_string(*input_string)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

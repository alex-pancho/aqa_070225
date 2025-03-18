"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import sum_numbers_in_list, multiplication_table, list_sum
import unittest


class SumNumbersInList(unittest.TestCase):

    def test_01_valid_data(self):
        """ Positive test sum_numbers_in_list with correct data"""
        my_list = ["1,2,5", "3,0,5"]
        actual = sum_numbers_in_list(my_list)
        expected = [8, 8]
        self.assertEqual(actual, expected)
        my_list_2 = ["2,3", "5,0", "7,-2"]
        self.assertEqual(sum_numbers_in_list(my_list_2), [5, 5, 5])

    def test_02_empty_list(self):
        """ Negative test sum_numbers_in_list with empty list"""
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])

    def test_03_chars_in_list(self):
        """ Negative test sum_numbers_in_list with chars in list"""
        my_list = ["1,2,abc", "abc", "3,0,5"]
        self.assertEqual(sum_numbers_in_list(my_list), ["Не можу це зробити!", "Не можу це зробити!", 8])
        my_list_2 = ["0,2", "1,3,7", "o,1,2", "__,:"]
        self.assertEqual(sum_numbers_in_list(my_list_2), [2, 11, "Не можу це зробити!", "Не можу це зробити!"])

    def test_04_int_in_list(self):
        """ Negative test sum_numbers_in_list with int in list"""
        my_list = [7, "2, 10"]
        self.assertEqual(sum_numbers_in_list(my_list), ["Не можу це зробити! AttributeError", 12])

    def test_05_not_list_data(self):
        """ Negative test sum_numbers_in_list with not list data"""
        my_string = "12345"
        with self.assertRaises(ValueError):
            sum_numbers_in_list(my_string)
        my_int = 12345
        with self.assertRaises(ValueError):
            sum_numbers_in_list(my_int)


class MultiplicationTable(unittest.TestCase):
    def test_01_valid_data(self):
        """ Positive test multiplication_table with int input number and max_value"""
        number_1 = 5
        max_value_1 = 30
        actual = multiplication_table(number_1, max_value_1)
        expected = ['1 * 5 = 5', '2 * 5 = 10', '3 * 5 = 15', '4 * 5 = 20', '5 * 5 = 25', '6 * 5 = 30']
        self.assertEqual(actual, expected)
        number_2 = 0
        max_value_2 = 10
        actual = multiplication_table(number_2, max_value_2)
        expected = ['1 * 0 = 0', '2 * 0 = 0', '3 * 0 = 0', '4 * 0 = 0', '5 * 0 = 0',
                    '6 * 0 = 0', '7 * 0 = 0', '8 * 0 = 0', '9 * 0 = 0', '10 * 0 = 0']
        self.assertEqual(actual, expected)
        number_3 = 3
        max_value_3 = 0
        actual = multiplication_table(number_3, max_value_3)
        expected = []
        self.assertEqual(actual, expected)
        number_4 = 0
        max_value_4 = 0
        actual = multiplication_table(number_4, max_value_4)
        expected = ['1 * 0 = 0', '2 * 0 = 0', '3 * 0 = 0', '4 * 0 = 0', '5 * 0 = 0',
                    '6 * 0 = 0', '7 * 0 = 0', '8 * 0 = 0', '9 * 0 = 0', '10 * 0 = 0']
        self.assertEqual(actual, expected)

    def test_02_empty_data(self):
        """ Negative test multiplication_table with empty number or/and max_value input"""
        with self.assertRaises(TypeError):
            multiplication_table()
        with self.assertRaises(TypeError):
            multiplication_table(5, )
        with self.assertRaises(TypeError):
            multiplication_table(5)

    def test_03_string_data(self):
        """ Negative test multiplication_table with string number or/and max_value input"""
        with self.assertRaises(TypeError):
            multiplication_table("5", "3")
        with self.assertRaises(TypeError):
            multiplication_table(5, "3")
        with self.assertRaises(TypeError):
            multiplication_table("5", 3)
        with self.assertRaises(TypeError):
            multiplication_table("a", "b")


class ListSum(unittest.TestCase):
    def test_01_int_list(self):
        """ Positive test list_sum with list of int input"""
        my_list_1 = [1, 2, 3, 4]
        actual = list_sum(my_list_1)
        expected = 10
        self.assertEqual(actual, expected)
        my_list_2 = [0, 0, -3, 4]
        actual = list_sum(my_list_2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_02_empty_list(self):
        """ Negative test list_sum with empty input"""
        with self.assertRaises(TypeError):
            list_sum([])
        with self.assertRaises(TypeError):
            list_sum()

    def test_03_list_with_string(self):
        """ Negative test list_sum with string in list input"""
        my_list_1 = ["1", "2"]
        with self.assertRaises(TypeError):
            list_sum(my_list_1)
        my_list_2 = [10, 8, "bc"]


if __name__ == "__main__":
    unittest.main(verbosity=2)

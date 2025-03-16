"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import count_unique_characters, find_substring, pow_even_number_list
import unittest

class UniqueCharactersFunctionTest(unittest.TestCase):

    def test_count_unique_characters_01(self):
        """Check if TRUE returned for > 10 unique characters."""
        str_for_count = '123456789qw'
        actual = count_unique_characters(str_for_count)
        self.assertTrue(actual)

    def test_count_unique_characters_02(self):
        """Check if FALSE returned for <= 10 unique characters."""
        str_for_count = '1234567890'
        actual = count_unique_characters(str_for_count)
        self.assertFalse(actual)

    def test_count_unique_characters_03(self):
        """Check if ValueError is raised for empty string input."""
        str_for_count = ''
        with self.assertRaises(ValueError):
            count_unique_characters(str_for_count)

    def test_count_unique_characters_04(self):
        """Check if TypeError is raised when input is not \'str\' type."""
        str_for_count = 0
        with self.assertRaises(TypeError):
            count_unique_characters(str_for_count)
        str_for_count = [1, 2, 3]
        with self.assertRaises(TypeError):
            count_unique_characters(str_for_count)
        str_for_count = (1, 2, 3)
        with self.assertRaises(TypeError):
            count_unique_characters(str_for_count)

class FindSubstringFunctionTest(unittest.TestCase):

    def test_find_substring_01(self):
        """Check if '-1' is returned when str1 does not contain str2."""
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "cat"
        actual = find_substring(str1, str2)
        expected = -1
        self.assertEqual(actual, expected)

    def test_find_substring_02(self):
        """Check if index is returned if str1 contains str2."""
        str1 = "Hello, world!"
        str2 = "world"
        actual = find_substring(str1, str2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_find_substring_03(self):
        """Check if ValueError is raised when str2 is longer than str1."""
        str1 = "world"
        str2 = "Hello, world!"
        with self.assertRaises(ValueError):
            find_substring(str1, str2)

    def test_find_substring_04(self):
        """Check if TypeError is raised when str1 is not \'str\' type."""
        str1 = 0
        str2 = "Hello, world!"
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = [1, 2, 3]
        str2 = "Hello, world!"
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = (1, 2, 3)
        str2 = "Hello, world!"
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = {1, 2, 3}
        str2 = "Hello, world!"
        with self.assertRaises(TypeError):
            find_substring(str1, str2)

    def test_find_substring_05(self):
        """Check if TypeError is raised when str2 is not \'str\' type."""
        str1 = "world"
        str2 = 1.23
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = "world"
        str2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = "world"
        str2 = (1, 2, 3)
        with self.assertRaises(TypeError):
            find_substring(str1, str2)
        str1 = "world"
        str2 = {1, 2, 3}
        with self.assertRaises(TypeError):
            find_substring(str1, str2)

    def test_find_substring_06(self):
        """Check if '0' index is returned when str2 is empty """
        str1 = "Hello, world!"
        str2 = ""
        actual = find_substring(str1, str2)
        expected = 0
        self.assertEqual(actual, expected)

class PowEvenNumberListFunctionTest(unittest.TestCase):

    def test_pow_even_number_list_01(self):
         """Check for list with odd and even numbers"""
         number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
         actual = pow_even_number_list(number_list)
         expected = [4, 16, 36, 64, 100]
         self.assertEqual(actual, expected)
    
    def test_pow_even_number_list_02(self):
         """Check for list only with odd numbers"""
         number_list = [1, 3, 5, 7, 9]
         actual = pow_even_number_list(number_list)
         expected = []
         self.assertEqual(actual, expected)
    
    def test_pow_even_number_list_03(self):
         """Check for empty list"""
         number_list = []
         actual = pow_even_number_list(number_list)
         expected = []
         self.assertEqual(actual, expected)
    
    def test_pow_even_number_list_04(self):
         """Check for list with odd and even negative numbers"""
         number_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
         actual = pow_even_number_list(number_list)
         expected = [4, 16, 36, 64, 100]
         self.assertEqual(actual, expected)

    def test_pow_even_number_list_05(self):
         """Check if '0' is included in result with even numbers"""
         number_list = [0, 2, 4, 6]
         actual = pow_even_number_list(number_list)
         expected = [0, 4, 16, 36]
         self.assertEqual(actual, expected)

    def test_pow_even_number_list_06(self):
        """Check if TypeError is raised for non list type"""
        number_list = 2
        with self.assertRaises(TypeError):
            pow_even_number_list(number_list)
        number_list = "2"
        with self.assertRaises(TypeError):
            pow_even_number_list(number_list)
        number_list = (0, 2, 4, 6)
        with self.assertRaises(TypeError):
            pow_even_number_list(number_list)
        number_list = {0, 2, 4, 6}
        with self.assertRaises(TypeError):
            pow_even_number_list(number_list)

if __name__ == "__main__":
    unittest.main(verbosity=2)

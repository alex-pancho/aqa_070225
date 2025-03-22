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
from homeworks import add_numbers, reverse_string, long_word, find_substring, new_average

class TestHomeworkFunctions(unittest.TestCase):

    def test_add_numbers_1(self):
        """Tests for the add_numbers function."""
        actual = add_numbers(3, 2)
        expected = 5
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
        
    def test_add_numbers_2(self):
        actual = add_numbers(-1, 1)
        expected = 0
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
        
    def test_add_numbers_3(self):
        actual = add_numbers(1.5, 2.5)
        expected = 4.0
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_add_numbers_4(self):
        with self.assertRaises(TypeError):
            add_numbers("3", 2)  

    def test_new_average_1(self):
        """Tests for the new_average function."""
        actual = new_average([1, 2, 3, 4, 5])
        expected = 3.0
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
        
    def test_new_average_2(self):
        actual = new_average([10, 20, 30])
        expected = 20.0
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_new_average_3(self):
        actual = new_average([2])
        expected = 2.0
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
        
    def test_new_average_4(self):
        with self.assertRaises(ValueError):
            new_average([])        

    def test_reverse_string_1(self):
        """Tests for the reverse_string function."""
        actual = reverse_string("hello")
        expected = "olleh"
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
   
    def test_reverse_string_2(self):
        actual = reverse_string("Python")
        expected = "nohtyP"
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_reverse_string_3(self):
        actual = reverse_string("")
        expected = ""
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
        
    def test_reverse_string_4(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_long_word_1(self):
        actual = long_word(["Apple", "Banana", "Orange", "Pineapple"])
        expected = "Pineapple"
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_long_word_2(self):
        actual = long_word(["one", "two", "three"])
        expected = "three"
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")
       
    def test_long_word_3(self):
        with self.assertRaises(ValueError):
            long_word([])  

    def test_find_substring(self):
        """Tests for the find_substring function."""
        actual = find_substring("hello world", "world")
        expected = 6
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_find_substring_2(self):
        actual = find_substring("hello world", "hi")
        expected = -1
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_find_substring_3(self):
        actual = find_substring("banana", "na")
        expected = 2  
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_find_substring_4(self):
        actual = find_substring("The quick brown fox jumps over the lazy dog", "cat")
        expected = -1  
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}")

    def test_find_substring_5(self):
        with self.assertRaises(ValueError):
            find_substring("hello world", "")  


if __name__ == "__main__":
    unittest.main(verbosity=2)


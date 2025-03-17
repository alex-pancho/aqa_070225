"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homework_10.py
На оцінку впливає як якість тестів так і розмір тестового покриття. 
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from homeworks import sum_numbers_in_list, reverse, add_numbers
import unittest

class TestHW10(unittest.TestCase):

    def test_valid_input(self):
        """Тест правильного розрахунку"""
        output = sum_numbers_in_list(["1,2,3", "4,0,6"])
        expected = [6, 10]
        self.assertEqual(output, expected)
    
    def test_invalid_format(self):
        """Test не валідного формату"""
        output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
        expected = [6, "Не можу це зробити!", "Не можу це зробити!"]
        self.assertEqual(output, expected)

    def test_non_string_elements(self):
        """Тест з нерядковими елементами"""
        output = sum_numbers_in_list(["1,2,3,4", 7])
        expected = [10, "Не можу це зробити! AttributeError"]
        self.assertEqual(output, expected)

    def test_empty_list(self):
        """Тест з порожнім списком"""
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])

    def test_non_list_input(self):
        """Тест із введенням без списку"""
        with self.assertRaises(ValueError):
            sum_numbers_in_list("21")

    def test_mixed_valid_invalid(self):
        """Тест із змішаним дійсним і недійсним введеннямt"""
        output = sum_numbers_in_list(["1,2,3", "4,0,6", "invalid"])
        expected = [6, 10, "Не можу це зробити!"]
        self.assertEqual(output, expected)

    def test_single_valid_string(self):
        """Тест з одним дійсним рядком"""
        output = sum_numbers_in_list(["1,2,3"])
        expected = [6]
        self.assertEqual(output, expected)

    def test_single_invalid_string(self):
        """Тест з одним недійсним рядком"""
        output = sum_numbers_in_list(["invalid"])
        expected = ["Не можу це зробити!"]
        self.assertEqual(output, expected)

    def test_large_numbers(self):
        """Тест з великими числами"""
        output = sum_numbers_in_list(["1000000,2000000,3000000"])
        expected = [6000000]
        self.assertEqual(output, expected)

    def test_negative_numbers(self):
        """Test з відєемними числами"""
        output = sum_numbers_in_list(["-1,-2,-3", "4,-5,6"])
        expected = [-6, 5]
        self.assertEqual(output, expected)

    def test_reverse(self):
        """Перевіряємо, чи правильно перевертається слово"""
        actual = reverse("hello")
        excepted = "olleh"
        self.assertEqual (actual,excepted)

    def test_reverse_sentence(self):
        """Перевіряємо перевертання речення"""
        actual = reverse("reverse sentence")
        excepted = "ecnetnes esrever"
        self.assertEqual (actual,excepted)

    def test_reverse_empty_string(self):
        """Перевіряємо, що порожній рядок залишається порожнім"""
        actual = reverse("")
        excepted = ""
        self.assertEqual (actual,excepted)

    def test_reverse_palindrome(self):
        """Перевіряємо паліндром (повинен залишитися таким самим)"""
        actual = reverse("madam")
        excepted = "madam"
        self.assertEqual (actual,excepted)

    def test_reverse_numbers_as_string(self):
        """Перевіряємо, чи правильно перевертаються цифри у рядку"""
        actual = reverse("12345")
        excepted = "54321"
        self.assertEqual (actual,excepted)

    def test_reverse_special_characters(self):
        """Перевіряємо, чи працює функція з символами"""
        actual = reverse("!№;%:")
        excepted = ":%;№!"
        self.assertEqual (actual,excepted)
    
    def test_add_number(self):
        """Перевіряємо чи працює функція"""
        actual = add_numbers(1,3)
        excepted = 4
        self.assertEqual(actual,excepted)

    def test_add_nubmer_tree(self):
        """Перевіряємо функцію з 3ма цифрами та більше"""
        with self.assertRaises(TypeError):
            add_numbers(1,1,1)
        with self.assertRaises(TypeError):
            add_numbers(1,1,1,1,1,1,1,1,)
    
    def test_str_add_number(self):
        """Перевірка при додаванні str"""
        actual = add_numbers("TEST1", "TEST2")
        excepted = "TEST1TEST2"
        self.assertEqual(actual,excepted)

    def test_str_plus_nubmer(self):
        """Перевірка додавання str+int"""
        with self.assertRaises(TypeError):
            add_numbers("TEST1", 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)

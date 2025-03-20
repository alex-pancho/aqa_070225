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
from homeworks import Student
from homeworks import average_of_list
from homeworks import longest_word
import unittest

class SumNumbersInList(unittest.TestCase):
    def test_1_valid_input(self):
        # перевіряє список сум чисел зі списку строк,які складаються з чисел, розділених комою
        string_list = ["1,2,3", " 0,0", "-1, -4, 0.6" ]
        actual = sum_numbers_in_list(string_list)
        excepted = [6, 0, -4.4]
        self.assertEqual(actual, excepted)
        
    def test_2_invalid_input_not_number_element(self):
        #первіряє випадок коли рядковий елемент списоку містить не число
        string_list = ["1,2,3", "4/0,6", "asas7,8,9", ""]
        actual = sum_numbers_in_list(string_list)
        excepted = [6, "Не можу це зробити!", "Не можу це зробити!", "Не можу це зробити!"]
        self.assertEqual(actual, excepted)
    
    def test_3_invalid_input_not_str_element(self):
        #первіряє випадок коли елемент списку не str
        string_list = ["1,2,3,4", 7]
        actual = sum_numbers_in_list(string_list)
        excepted = [10, "Не можу це зробити! AttributeError"]
        self.assertEqual(actual, excepted)

    def test_4_empty_list(self):
        #первіряє випадок коли передано порожній список
        string_list = []
        with self.assertRaises(ValueError):
            sum_numbers_in_list(string_list)

    def test_5_not_list(self):
        #первіряє випадок коли передано не список
        string_list = "test"
        with self.assertRaises(ValueError):
            sum_numbers_in_list(string_list)    

class ChangeGpa(unittest.TestCase):
    def test_1_valid_input_gpa_float(self):
        #перевірка зміни середнього балу, якщо бал задовільняє умову float in range 0-100
        student_1 = Student("John","Dou", 18, 85.5)
        student_1.change_gpa(81.5)
        actual = student_1.gpa
        excepted = 81.5
        self.assertEqual(actual, excepted)

    def test_2_valid_input_gpa_int(self):
        #перевірка зміни середнього балу, якщо бал задовільняє умову int in range 0-100
        student_1 = Student("John","Dou", 18, 90)
        student_1.change_gpa(89)
        actual = student_1.gpa
        excepted = 89
        self.assertEqual(actual, excepted)  

    def test_3_invalid_input_gpa_not_number(self):
        #перевірка випадку виклику помилки якщо середній бал не число
        student_1 = Student("John","Dou", 18, 90)
        with self.assertRaises(ValueError):
            student_1.change_gpa({89})
       

    def test_4_invalid_input_gpa_below_zero(self):
        #перевірка випадку виклику помилки якщо середній бал < 0
        student_1 = Student("John","Dou", 18, 90)
        with self.assertRaises(ValueError):
            student_1.change_gpa(-1)
        
    def test_5_invalid_input_gpa_over_100(self):
        #перевірка випадку виклику помилки якщо середній бал >100
        student_1 = Student("John","Dou", 18, 90)
        with self.assertRaises(ValueError):
            student_1.change_gpa(101)
            

class AvarageOfList(unittest.TestCase):
    def test_01_valid_input(self):
        #перевіряє середнє арифметичне списку чисел
        my_list = [3, 2, 3, 4]
        actual = average_of_list(my_list)
        expected = 3
        self.assertEqual(actual, expected)

    def test_02_mixed_input_number_and_not_number(self):
        #перевіряє середнє арифметичне списку де крім чисел є інші типи
        my_list = [1, "a", -1, [1], 6]
        actual = average_of_list(my_list)
        expected = 2
        self.assertEqual(actual, expected)

    def test_03_invalid_input_all_elements_not_number(self):
        #перевіряє випадок коли передано список всі елементи не числа
        my_list = ["a", [1],{1}]
        with self.assertRaises(ValueError):
            average_of_list(my_list)

    def test_04_invalid_input_empty_list(self):
        #первіряє випадок коли передано порожній список
        my_list = []
        with self.assertRaises(ValueError):
            average_of_list(my_list)

    def test_05_invalid_input_not_list(self):
        #первіряє чи випадок коли передано не список
        my_list = ("a", [1],{1})
        with self.assertRaises(ValueError):
            average_of_list(my_list)

class LongestWord(unittest.TestCase):

    def test_1_valid_input(self):
        #перевіряє чи повертається перше найдовше слово у списку з валідними даними
       list_of_words = ["test","testLong", "testLongest", "test" ]
       actual = longest_word (list_of_words)
       self.assertEqual(actual, "testLongest")

    def test_2_valid_input_with_other_types(self):
        #перевіряє чи повертається перше найдовше слово у списку з валідними даними та даними іншого типу
        list_of_words = ["test", 2, "testLong", ["veryLongWord"], "testLongest", "test"]
        actual = longest_word(list_of_words)
        excepted = "testLongest"
        self.assertEqual(actual, excepted)

    def test_3_only_empty_string_in_list(self):
        #перевіряємо випадок коли в списку тільки порожні рядки
        list_of_words = ["", 2, "", ["veryLongWord"]]
        with self.assertRaises(ValueError) as context:
            longest_word(list_of_words)
            self.assertEqual(str(context.exception), "There are no words")

    def test_4_no_string_in_list(self):
        #перевіряємо випадок коли в списку немає рядка
        list_of_words = [1, 2, ["veryLongWord"]]
        with self.assertRaises(ValueError) as context:
            longest_word(list_of_words)
            self.assertEqual(str(context.exception), "There are no string elements in list")

    def test_5_empty_list(self):
        #перевіряємо випадок коли список порожній
        list_of_words = []
        with self.assertRaises(ValueError) as context:
            longest_word(list_of_words)
            self.assertEqual(str(context.exception), "List is empty")

    def test_6_not_a_list(self):
        #перевіряємо випадок коли передано не список
        list_of_words = []
        with self.assertRaises(ValueError):
            longest_word(list_of_words)

if __name__ == "__main__":
    unittest.main(verbosity=2)

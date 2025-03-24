from homeworks import average, longest_word, find_substring
import unittest

class TestHW10(unittest.TestCase):
#func 1 
    def test_01_valid(self):
        """Перевірка обчислення середнього арифметичного для коректних даних"""
        output = average([1,2,3,4,5])
        ex = 3
        self.assertEqual(output, ex)

    def test_02(self):
        """Перевірка виклику ValueError "Список порожній"""
        with self.assertRaises(ValueError):
            average([])

    def test_03(self):
        """Перевірка виклику ValueError "Не всі елементи є числами"""
        with self.assertRaises(ValueError):
            average(["test", 1])
#func 2
    def test_04(self):
        """Перевірка функції на роботу"""
        out = longest_word(["Повертає", "найдовше", "слово", "у", "списку"])
        ex = "Повертає"
        self.assertEqual(out, ex)
    
    def test_05(self):
        """Виклик ValueError "Не всі елементи є рядками"""
        with self.assertRaises(ValueError):
            longest_word(["test", 1])
    
    def test_06(self):
        """Виклик ValueError, перевірка, порожнього списку"""
        with self.assertRaises(ValueError):
            longest_word([])
# func 3
    def test_07(self):
        """Виклик ValueError, "Обидва параметри мають бути рядками"""
        with self.assertRaises(TypeError):
            find_substring([1,2])
    
    def test_08(self):
        """Перевірка роботи функції"""
        out = find_substring("Перевірка функції", "ф")
        ex = 10
        self.assertEqual(out, ex)

    def test_09(self):
        """не знаходження індексу"""
        out = find_substring("Перевірка функції", "ґ")
        ex = -1
        self.assertEqual(out, ex)

    def test_10(self):
        """Перевірка індексу з некоректними типами даних"""
        with self.assertRaises(TypeError):
            find_substring(["Перевірка функції",123])
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
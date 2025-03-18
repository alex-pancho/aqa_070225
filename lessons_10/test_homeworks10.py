import unittest
from homework_10 import factorial, is_prime, count_vowels, unique_elements, fibonacci, sum_numbers_in_list

class TestHomeworks(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(10), 3628800)
        with self.assertRaises(ValueError):
            factorial(-10)
        self.assertEqual(factorial(1), 1)
    
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(37))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(57))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(91))
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("abracadabra"), 5)
        self.assertEqual(count_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 5)
        self.assertEqual(count_vowels("1234567890"), 0)
        self.assertEqual(count_vowels("Why so serious?"), 5)
        self.assertEqual(count_vowels("gym"), 0)
    
    def test_unique_elements(self):
        self.assertEqual(set(unique_elements([1, 3, 3, 7, 8, 8, 9, 9, 9])), {1, 3, 7, 8, 9})
        self.assertEqual(unique_elements([42, 42, 42, 42]), [42])
        self.assertEqual(unique_elements(["apple", "banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
        self.assertEqual(unique_elements([]), [])
        self.assertEqual(unique_elements([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
        with self.assertRaises(ValueError):
            fibonacci(-5)
    
    def test_sum_numbers_in_list(self):
        self.assertEqual(sum_numbers_in_list(["1,2,3", "4,0,6"]), [6, 10])
        self.assertEqual(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]), [6, "Не можу це зробити!", 10])
        self.assertEqual(sum_numbers_in_list(["1,2,3,4", 7]), [10, "Не можу це зробити!"])
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])
        with self.assertRaises(ValueError):
            sum_numbers_in_list("21")

if __name__ == "__main__":
    unittest.main()

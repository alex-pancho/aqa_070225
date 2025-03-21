import unittest
from homework10 import multiplication_table, longest_in_list, list_of_squares, sum_numbers_in_list


class MultiplicationTable(unittest.TestCase):
    
    # Check maximum returned result
    def test_multiplication_table_10(self):
        actual = multiplication_table(10)
        expected = "Task 1 --> 10 x 1 = 10\nTask 1 --> 10 x 2 = 20\n"
        self.assertEqual(actual, expected)

    # Check that returned result is a string
    def test_multiplication_table_result_type(self):
        actual = multiplication_table(3)
        self.assertIsInstance(actual, str)
    
    # Check that resukt not empty 
    def test_multiplication_table_non_empty(self):
        actual = multiplication_table(7)
        self.assertTrue(len(actual) > 0)


class LongestInList(unittest.TestCase):

    def test_single_word(self):
        words = ["apple"]
        actual = longest_in_list(words)
        self.assertEqual(actual, "apple")
    
    def test_words_with_spaces(self):
        words = ["   ", "hello", "   world   "]
        actual = longest_in_list(words)
        self.assertEqual(actual, "   world   ")

    def test_long_word(self):
        words = ["short", "medium", "longer", "a" * 1000]  # Слово с 1000 символами
        actual = longest_in_list(words)
        self.assertEqual(actual, "a" * 1000)
    

class SumNumbersInList(unittest.TestCase):

    # Check error with num value 
    def test_invalid_values(self):
        string_list = ["1,2,3", "4,5,6", "7,a,b"]
        actual = sum_numbers_in_list(string_list)
        self.assertEqual(actual, [6, 15, "Не можу це зробити!"])
    
    # Check correct input
    def test_valid_input(self):
        string_list = ["1,2,3", "4,5,6", "7,8"]
        actual = sum_numbers_in_list(string_list)
        self.assertIsNotNone(actual)  
        self.assertIsInstance(actual, list)  
        self.assertEqual(actual, [6, 15, 15])  
    

class ListOfSquares(unittest.TestCase):

    def test_list_of_squares(self):
        data = [1, 2, 3, 4, 5, 6]
        actual = list_of_squares(data)
        self.assertTrue(len(actual) > 0)  
        self.assertIn(16, actual)  
        self.assertLess(actual[0], actual[1])

    def test_odd_numbers_only(self):
        data = [1, 3, 5, 7, 9]
        actual = list_of_squares(data)
        self.assertEqual(actual, [])
    
     
if __name__ == "__main__":
    unittest.main()



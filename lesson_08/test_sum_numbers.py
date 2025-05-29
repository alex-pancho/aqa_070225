import unittest
from sum_numbers import sum_numbers_in_list

class TestSumNumbersInList(unittest.TestCase):
    def test_correct_input(self):
        self.assertEqual(sum_numbers_in_list(["1,2,3", "4,0,6"]), [6, 10])
        self.assertEqual(sum_numbers_in_list(["10", "5,5", "0,0,0"]), [10, 10, 0])
        self.assertEqual(sum_numbers_in_list(["100"]), [100])

    def test_invalid_strings(self):
        self.assertEqual(
            sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]),
            [6, "Не можу це зробити!", 10]
        )
        self.assertEqual(
            sum_numbers_in_list(["4/0,6", "1,2,three"]),
            ["Не можу це зробити!", "Не можу це зробити!"]
        )
        self.assertEqual(
            sum_numbers_in_list(["1,,3", ",2,3"]),
            ["Не можу це зробити!", "Не можу це зробити!"]
        )

    def test_invalid_types_in_list(self):
        self.assertEqual(
            sum_numbers_in_list(["1,2,3,4", 7]),
            [10, "Не можу це зробити! AttributeError"]
        )
        self.assertEqual(
            sum_numbers_in_list([None, {"a":1}, ["1,2"]]),
            ["Не можу це зробити! AttributeError",
             "Не можу це зробити! AttributeError",
             "Не можу це зробити! AttributeError"]
        )

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])

    def test_non_list_input(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list("21")
        with self.assertRaises(ValueError):
            sum_numbers_in_list(3)
        with self.assertRaises(ValueError):
            sum_numbers_in_list({"a": 1})

    def test_whitespace_and_formatting(self):
        self.assertEqual(
            sum_numbers_in_list([" 1 , 2 , 3 ", " 4,5, 6"]),
            [6, 15]
        )
        self.assertEqual(
            sum_numbers_in_list(["\t1,2", "3 , 4\n"]),
            [3, 7]
        )

if __name__ == '__main__':
    unittest.main()

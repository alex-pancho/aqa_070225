import unittest
from homework_06 import (
    get_alien_points,
    sum_of_digits,
    calculate_total,
    fruits_without_orange,
    even_squares,
    even_sum,
    check_guess,
)

class TestHomework08(unittest.TestCase):

    def test_get_alien_points(self):
        self.assertEqual(get_alien_points("green"), 5)
        self.assertEqual(get_alien_points("yellow"), 10)
        self.assertEqual(get_alien_points("red"), 15)
        self.assertEqual(get_alien_points("blue"), 0)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("12345"), 15)
        self.assertEqual(sum_of_digits("0"), 0)
        self.assertEqual(sum_of_digits("999"), 27)

    def test_calculate_total(self):
        self.assertEqual(calculate_total([1, 2, 3]), 6)
        self.assertEqual(calculate_total([]), 0)
        self.assertEqual(calculate_total([-5, 5]), 0)

    def test_fruits_without_orange(self):
        self.assertEqual(
            fruits_without_orange(["apple", "orange", "banana"]),
            ["apple", "banana"]
        )
        self.assertEqual(fruits_without_orange(["orange", "orange"]), [])
        self.assertEqual(fruits_without_orange(["mango"]), ["mango"])

    def test_even_squares(self):
        self.assertEqual(even_squares([1, 2, 3, 4]), [4, 16])
        self.assertEqual(even_squares([]), [])
        self.assertEqual(even_squares([1, 3, 5]), [])

    def test_even_sum(self):
        self.assertEqual(even_sum([1, 2, 3, 4, 5]), 6)
        self.assertEqual(even_sum([]), 0)
        self.assertEqual(even_sum([2, 4, 6]), 12)

    def test_check_guess_correct(self):
        self.assertEqual(check_guess(10, [5, 7, 10]), "correct")

    def test_check_guess_lost(self):
        self.assertEqual(check_guess(15, [10, 12, 14]), "lost:15")

if __name__ == "__main__":
    unittest.main()

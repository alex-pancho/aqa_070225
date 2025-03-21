import unittest
from our_function import sum_list_last_first, is_data_list_type


class SumListTest(unittest.TestCase):

    def test_01_three(self):
        """Test sum_list_last_first with a list of three elements."""
        my_list = [1, 2, 3]
        actual = sum_list_last_first(my_list)
        expected = 1.5
        self.assertEqual(actual, expected)
    
    def test_02_two(self):
        my_list = [1, 2]
        actual = sum_list_last_first(my_list)
        expected = 1.0
        self.assertEqual(actual, expected)
    
    def test_02_one(self):
        my_list = [1]
        actual = sum_list_last_first(my_list)
        self.assertIsNone(actual)
    
    # def test_02_empty(self):
    #     my_list = [0, -0]
    #     #self.assertNotEqual(sum([my_list[0], my_list[-1]]), 0,
    #                     #f"Get val1: {my_list[0]} and val2: {my_list[-1]}, sum expected non-zero but gettting:{my_list[0]+my_list[-1]} ")
    #     #self.assertTrue(my_list[0])
    #     #self.assertTrue(my_list[-1])
    #     actual = sum_list_last_first(my_list)
    #     self.assertIsNone(actual)
    
    def test_03_data_type(self):
        my_list = [1, 2]
        actual = is_data_list_type(my_list)
        self.assertTrue(actual,
                        msg=f"Повідомлення у випадку помилки куди можна додати все що хоч через {actual} ф-стрнгу")
    
    def test_04_data_type(self):
        my_list = 1
        actual = is_data_list_type(my_list)
        self.assertFalse(actual)
    
    def test_05_zeros(self):
        my_list = "[0, -0]"
        with self.assertRaises(ValueError):
            sum_list_last_first(my_list)
        # my_list = (0, 0)
        # with self.assertRaises(ValueError):
        #     sum_list_last_first(my_list) 
        my_list = 0
        with self.assertRaises(ValueError):
            sum_list_last_first(my_list)
    
    def test_06_zeros(self):
        my_list = [0, -0]
        with self.assertRaises(ZeroDivisionError):
            sum_list_last_first(my_list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # Can be false-positive
    # self.assertTrue
    # self.assertNotEqual
    # self.assertIsNotNone


import unittest
from homework09 import Student  # або просто імпортуйте, якщо файл в тому ж каталозі

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Ivan", "Petrenko", 20, 85)

    def test_initial_values(self):
        self.assertEqual(self.student.first_name, "Ivan")
        self.assertEqual(self.student.last_name, "Petrenko")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.average_grade, 85)

    def test_update_average_grade_valid(self):
        self.student.update_average_grade(92)
        self.assertEqual(self.student.average_grade, 92)

    def test_update_average_grade_zero(self):
        self.student.update_average_grade(0)
        self.assertEqual(self.student.average_grade, 0)

    def test_update_average_grade_max(self):
        self.student.update_average_grade(100)
        self.assertEqual(self.student.average_grade, 100)

    def test_update_average_grade_below_zero(self):
        with self.assertRaises(ValueError):
            self.student.update_average_grade(-1)

    def test_update_average_grade_above_100(self):
        with self.assertRaises(ValueError):
            self.student.update_average_grade(101)

    def test_str_representation(self):
        expected = "Student: Ivan Petrenko, Age: 20, Average Grade: 85"
        self.assertEqual(str(self.student), expected)

if __name__ == '__main__':
    unittest.main()

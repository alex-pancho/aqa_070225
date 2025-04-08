import unittest

from lesson_15.homeworks_15 import TeamLead


class TestHomework15(unittest.TestCase):
    def setUp(self):
        self.teamlead = TeamLead("Mike", "4000", "Analytics", "Python", 10)

    def test_department_attribute(self):
        self.assertTrue(hasattr(self.teamlead, "department"), "TeamLead має мати атрибут 'department' від Manager")

    def test_programming_language_attribute(self):
        self.assertTrue(hasattr(self.teamlead, "programming_language"),
                        "TeamLead має мати атрибут 'programming_language' від Developer")

    def test_all_attributes(self):
        expected_attributes = ["name", "salary", "department", "programming_language", "team_size"]
        for atr in expected_attributes:
            with self.subTest(attr=atr):
                self.assertTrue(hasattr(self.teamlead, atr), f"TeamLead має мати атрибут '{atr}'")


if __name__ == "__main__":
    unittest.main()

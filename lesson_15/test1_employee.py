import unittest
from homeworks_15 import TeamLead

class TeamLeadAttributesTest(unittest.TestCase):
    def test_01_teamlead_has_all_required_attributes(self):
        """Test if TeamLead has all attributes and correct values."""
        lead = TeamLead("Ilonka", 3000, "Development", "Python", 5)
        actual = (lead.name, lead.salary, lead.department, lead.programming_language, lead.team_size)
        expected = ("Ilonka", 3000, "Development", "Python", 5)
        self.assertEqual(actual, expected)

    def test_02_missing_argument_raises_typeerror(self):
        """Test that missing required arguments raises TypeError."""
        with self.assertRaises(TypeError):
            TeamLead("Dima", 3500, "QA", "Java")
    
    def test_03_can_update_teamlead_attributes(self):
        """Test if TeamLead attributes can be updated after object creation."""
        lead = TeamLead("Ilonka", 3000, "Development", "Python", 5)
        lead.department = "HR"
        lead.team_size = 8
        actual = (lead.department, lead.team_size)
        expected = ("HR", 8)
        self.assertEqual(actual, expected)

    def test_04_teamlead_invalid_department_type(self):
        """Test that TypeError is raised when department is not a string."""
        with self.assertRaises(TypeError):
             TeamLead("Viktor", 3500, 123, "Python", 4)

    def test_05_teamlead_invalid_programming_language_type(self):
       """Test that TypeError is raised when programming_language is not a string."""
       with self.assertRaises(TypeError):
            TeamLead("Anna", 3200, "QA", 9876, 3)

    def test_06_teamlead_invalid_team_size(self):
        """Test that ValueError is raised when team_size is zero or negative."""
        with self.assertRaises(ValueError):
             TeamLead("Leo", 4000, "DevOps", "Go", 0)  
        with self.assertRaises(ValueError):
            TeamLead("Leo", 4000, "DevOps", "Go", -2)

    def test_07_teamlead_invalid_salary_type(self):
        """Test that TypeError is raised when salary is not a number."""
        with self.assertRaises(TypeError):
             TeamLead("Milan", "three thousand", "Dev", "Python", 4)

    def test_08_teamlead_negative_salary(self):
        """Test that ValueError is raised when salary is negative."""
        with self.assertRaises(ValueError):
             TeamLead("Solomija", -5000, "Dev", "Python", 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)


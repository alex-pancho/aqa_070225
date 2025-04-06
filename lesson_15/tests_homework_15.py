import unittest
from homeworks_15 import TeamLead

class TeamLeadTest(unittest.TestCase):
    def test_01_check_name_attribute(self):
        """Verify if 'name' attribute is available"""
        team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8)
        self.assertTrue(hasattr(team_lead, "name"), msg="'name' attribute is missing")

    def test_02_check_salary_attribute(self):
        """Verify if 'salary' attribute is available"""
        team_lead = TeamLead("Ivan", 5000.0, "IT", "Python", 8)
        self.assertTrue(hasattr(team_lead, "salary"), msg="'salary' attribute is missing")

    def test_03_check_department_attribute(self):
        """Verify if 'department' attribute is available"""
        team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8)
        self.assertTrue(hasattr(team_lead, "department"), msg="'department' attribute is missing")

    def test_04_check_programming_language_attribute(self):
        """Verify if 'programming_language' attribute is available"""
        team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8)
        self.assertTrue(hasattr(team_lead, "programming_language"), msg="'programming_language' attribute is missing")

    def test_05_check_team_size_attribute(self):
        """Verify if 'team_size' attribute is available"""
        team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8)    
        self.assertTrue(hasattr(team_lead, "team_size"), msg="'team_size' attribute is missing")

    def test_07_check_error_for_name_attribute(self):
        """Verify if 'TypeError' raised for 'name' attribute"""          
        with self.assertRaises(TypeError):
            team_lead = TeamLead(10, 5000, "IT", "Python", 8)

    def test_08_check_error_for_salary_attribute(self):
        """Verify if 'TypeError' raised for 'salary' attribute"""   
        with self.assertRaises(TypeError):
            team_lead = TeamLead("Ivan", '5000', "IT", "Python", 8) 

    def test_09_check_error_for_department_attribute(self):
        """Verify if 'TypeError' raised for 'department' attribute"""  
        with self.assertRaises(TypeError):
            team_lead = TeamLead("Ivan", 5000, ["IT"], "Python", 8) 

    def test_10_check_error_for_programming_language_attribute(self):
        """Verify if 'TypeError' raised for 'programming_language' attribute"""  
        with self.assertRaises(TypeError):
            team_lead = TeamLead("Ivan", 5000, "IT", ("Python",), 8) 

    def test_11_check_error_for_team_size_attribute(self):
        """Verify if 'TypeError' raised for 'team_size' attribute"""  
        with self.assertRaises(TypeError):
            team_lead = TeamLead("Ivan", 5000, "IT", "Python", 8.0)   

if __name__ == "__main__":
    unittest.main(verbosity=2)

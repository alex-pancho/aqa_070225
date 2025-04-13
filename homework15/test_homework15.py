import unittest
from homework15 import Employee, Manager, Developer, TeamLead

class TestTeamLeadCustomData(unittest.TestCase):
    def setUp(self):
        self.lead = TeamLead(
            name="Kostya",
            salary=10000,
            department="CS",
            pr_language="Python",
            team_size=10
        )

    def test_manager_attributes(self):
        self.assertTrue(hasattr(self.lead, "department"))
        self.assertEqual(self.lead.department, "CS")

    def test_developer_attributes(self):
        self.assertTrue(hasattr(self.lead, "pr_language"))
        self.assertEqual(self.lead.pr_language, "Python")

    def test_employee_attributes(self):
        self.assertTrue(hasattr(self.lead, "name"))
        self.assertTrue(hasattr(self.lead, "salary"))
        self.assertEqual(self.lead.name, "Kostya")
        self.assertEqual(self.lead.salary, 10000)

    def test_teamlead_attribute(self):
        self.assertTrue(hasattr(self.lead, "team_size"))
        self.assertEqual(self.lead.team_size, 10)

if __name__ == '__main__':
    unittest.main()
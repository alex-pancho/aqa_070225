import unittest
from homeworks_15 import TeamLead


class TestUserCreation(unittest.TestCase):

    def test_TL(self):
        team_lead = TeamLead("Vitalii", 12000, "QA", "Python", 1)
        self.assertEqual(team_lead.name, "Vitalii")
        self.assertEqual(team_lead.salary, 12000)
        self.assertEqual(team_lead.department, "QA")
        self.assertEqual(team_lead.programming_language, "Python")
        self.assertEqual(team_lead.team_size, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
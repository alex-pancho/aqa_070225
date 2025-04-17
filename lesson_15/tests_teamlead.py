import unittest
from homeworks_15 import TeamLead


def get_data():
    data = {"name": "Вадим",
            "salary": 40000,
            "department": "QA",
            "programming_language": "Python",
            "team_size": 5}
    return data


class TstTeamLead(unittest.TestCase):
    def setUp(self):
        data = get_data()
        self.lead = TeamLead(data["name"],
                             data["salary"],
                             data["department"],
                             data["programming_language"],
                             data["team_size"])

    def test_01_manager_attributes(self):
        data = get_data()
        self.assertTrue(hasattr(self.lead, 'department'))
        self.assertEqual(self.lead.department, data["department"])

    def test_02_developer_attributes(self):
        data = get_data()
        self.assertTrue(hasattr(self.lead, 'programming_language'))
        self.assertEqual(self.lead.programming_language, data["programming_language"])

    def test_03_employee_attributes(self):
        data = get_data()
        self.assertTrue(hasattr(self.lead, 'name'))
        self.assertTrue(hasattr(self.lead, 'salary'))
        self.assertEqual(self.lead.name, data["name"])
        self.assertEqual(self.lead.salary, data["salary"])

    def test_04_team_size_attribute(self):
        data = get_data()
        self.assertTrue(hasattr(self.lead, 'team_size'))
        self.assertEqual(self.lead.team_size, data["team_size"])

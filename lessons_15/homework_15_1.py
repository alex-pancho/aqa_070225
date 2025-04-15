#Task1
"""Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. 
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead 
"""

import unittest

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size
        
class TestTeamLead(unittest.TestCase):
    def test_attributes_from_parents(self):
        tl = TeamLead("Yaroslav", 6200, "R&D", "Python", 11)
        self.assertEqual(tl.name, "Yaroslav")
        self.assertEqual(tl.salary, 6200)
        self.assertEqual(tl.department, "R&D")
        self.assertEqual(tl.programming_language, "Python")
        self.assertEqual(tl.team_size, 11)

if __name__ == '__main__':

    unittest.main(verbosity=2)
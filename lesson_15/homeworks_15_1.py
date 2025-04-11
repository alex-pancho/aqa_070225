"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, 
Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати 
додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі 
атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує 
на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі
TeamLead
"""
import unittest

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    
     def __init__(self, name, salary, department):
         self.department = department
        # super().__init__(self, name, salary)
         Employee.__init__(self, name, salary)
         
class Developer(Employee):
    
    def __init__(self, name, salary, programming_language):
         self.programming_language = programming_language
         #super().__init__(self, name, salary)
         Employee.__init__(self, name, salary)
         
class TeamLead(Manager, Developer):
    
    def __init__(self, name, salary, department, team_size, programming_language):
         self.team_size = team_size
         Manager.__init__(self, name, salary, department)
         Developer.__init__(self, name, salary, programming_language)
         
class TestAttributes(unittest.TestCase):
    
    def setUp(self):
        self.tl = TeamLead("Vera", "1000", "QA", "5", "python")
    
    def test_name_attribute_from_manager(self):
        self.assertEqual(self.tl.name, "Vera")
        
    def test_salary_attribute_from_manager(self):
        self.assertEqual(self.tl.salary, "1000")
        
    def test_department_attribute_from_manager(self):
        self.assertEqual(self.tl.department, "QA")
        
    def test_programming_language_attribute_from_manager(self):
        self.assertEqual(self.tl.programming_language, "python")
        
    
                
if __name__ == '__main__':
    unittest.main(verbosity=2)

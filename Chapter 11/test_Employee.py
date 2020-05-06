import unittest
from Employee import Employee

class test_Employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("xp", "liao", 100000)
        
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(105000, self.employee.annualSalary)
    def test_give_custom_raise(self):
        self.employee.give_raise(7000)
        self.assertEqual(107000, self.employee.annualSalary)
unittest.main()
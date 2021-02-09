class Employee:
    def __init__(self, givename, familyname, annualSalary):
        self.givename = givename
        self.familyname = familyname
        self.annualSalary = annualSalary
    
    def give_raise(self, salaryIncrease = 5000):
        self.annualSalary += salaryIncrease

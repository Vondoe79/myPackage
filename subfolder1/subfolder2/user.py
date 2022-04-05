# import files, modules, packages, libraries, etc.


# import subfolder3.accounts  # abs import
# from subfolder3 import accounts  # abs import
#
# import myPackage.subfolder3.accounts # abs import?
# from subfolder3 import accounts # abs import
# from ... subfolder3 import accounts  # for relative import

class Employee:
    """To document characteristics & activities of employees"""
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@companyEmail.com'

        # increment counter
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise_amt(self):
        return int(self.pay) * self.raise_amount

    def __repr__(self):
        return f"Employee('{self.fname}', '{self.lname}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, str_value):
        fname, lname, pay = str_value.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# import statements

import datetime

from subfolder1.subfolder2.user import Employee
from subfolder1.item import Developer
from subfolder3.accounts import Manager


if __name__ == '__main__':
    # create class instance (employee) objects
    emp_1 = Employee('Kophi', 'Von', 50000)
    emp_2 = Employee('Khalid', 'Sam', 60000)

    # set new global annual "raise amount"
    Employee.set_raise_amt(1.05)

    # create datetime object
    mydate = datetime.date(2022, 3, 30)

    # How to create a new employee instance when you the form is a string value
    # by using our Employee class:-
    emp_str_1 = 'kofi-doe-70000'
    emp_str_2 = 'samar-alhihi-80000'

    # call the class method to process the string value & create 'new_emp' class instance/object
    new_emp_1 = Employee.from_string(emp_str_1)

    # create a developer class instance/object
    dev_1 = Developer('Georgina', 'Dogbe', 85000, 'JavaScript')

    # create a Manager class instance/object
    mgr_1 = Manager('EmmanuelKK', 'Adjasco', 98000, [dev_1])

    # access the instance and/or class attributes/data/variables/information, etc
    print(emp_1.fullname())
    print(emp_1.email)
    print(emp_1.pay)
    print(emp_1.raise_amount)
    print(emp_1.apply_raise_amt())

    print(emp_1.raise_amount)

    print()

    print(new_emp_1.fullname())
    print(new_emp_1.email)
    print(new_emp_1.pay)
    print(new_emp_1.raise_amount)
    print(new_emp_1.apply_raise_amt())

    print()

    print(Employee.num_of_emps)

    print()

    print(new_emp_1.is_weekday(mydate))

    print()

    print(dev_1.fullname())
    print(dev_1.email)
    print(dev_1.pay)
    print(dev_1.raise_amount)
    print(dev_1.apply_raise_amt())

    print()

    print(mgr_1.fullname())
    print(mgr_1.email)
    print(mgr_1.pay)
    print(mgr_1.raise_amount)
    print(mgr_1.apply_raise_amt())
    print(mgr_1.print_emp())

    print()

    print(new_emp_1)



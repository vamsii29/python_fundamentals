# Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so
# you don’t have to create a new employee instance in each test method. Run
# your test case, and make sure both tests pass.

print('\nAnswer')

import unittest
from employee import Employee

class Testing_Employee(unittest.TestCase):

    def setUp(self):
        self.employee_test = Employee('sai','vamsi', 100000)
        # amount_default = employee_test.give_raise()
        # amount_dynamic = employee_test.give_raise(10000)

    
    def test_default_raise(self):
        '''Testing that there is default raise given'''
        amount_default = self.employee_test.give_raise()
        self.assertEqual(amount_default, 105000)
    
    def test_custom_raise(self):
        '''Testing that there is a custom raise given'''
        amount_dynamic = self.employee_test.give_raise(10000)
        self.assertEqual(amount_dynamic, 110000)

    

unittest.main()



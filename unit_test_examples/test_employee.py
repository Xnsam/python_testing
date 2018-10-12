"""Unit test file for employee class."""

import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test case for testing employee."""

    @classmethod
    def setUpClass(cls):
        """Run only once before the test. E.g. database fecthing setup."""
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """Run only once after the test."""
        print('tearDownClass')

    def setUp(self):
        """Will run before every single test."""
        print('setUp')
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """Will run after every single test."""
        print('tearDown')

    def test_email(self):
        """Test the email of two emp objects."""
        print('test email')
        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')
        self.emp1.first = 'John'
        self.emp2.first = 'Jane'
        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        """Test the fullname of two emp objects."""
        print('test fullname')
        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Sue Smith')
        self.emp1.first = 'John'
        self.emp2.first = 'Jane'
        self.assertEqual(self.emp1.fullname, 'John Schafer')
        self.assertEqual(self.emp2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        """Test the fullname of two emp objects."""
        print('test apply raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        """Test the monthly schedule of two emp objects."""
        print('test monthly schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

if __name__ == "__main__":
    unittest.main()

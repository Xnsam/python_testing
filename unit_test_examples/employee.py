"""Employee Class for Unit Testing."""
import requests


class Employee:
    """A sample Employee class."""

    def __init__(self, first, last, pay):
        """Initializer for the class."""
        self.first = first
        self.last = last
        self.pay = pay
        self.raise_amt = 1.05

    @property
    def email(self):
        """Email property."""
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """Fullname property."""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Apply Raise."""
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        """Monthly schedule."""
        response = requests.get('http://company.com/Schafer/May')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

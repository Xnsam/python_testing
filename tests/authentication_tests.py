"""Authentication tests for testing."""

from unittest import TestCase
from mock import patch
import prj1.authentication as auth


class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    @patch('__builtin__.open')
    def test_login(self, mock_open):
        """Test the login function."""
        mock_open.return_value.read.return_value = "george|bosco\n"
        self.assertTrue(auth.login('george', 'bosco'))

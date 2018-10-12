"""Basic Example for unittest."""


import unittest


class TestStringMethods(unittest.TestCase):
    """Class for testing the string methods."""

    def test_upper(self):
        """Test upper."""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Test is upper."""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Test split."""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

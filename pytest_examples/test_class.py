"""Test with class."""


class TestClass(object):
    """Test class definitions."""

    def test_one(self):
        """Test one."""
        x = 'this'
        assert 'h' in x

    def test_two(self):
        """Test two."""
        x = 'hello'
        assert hasattr(x, 'check')

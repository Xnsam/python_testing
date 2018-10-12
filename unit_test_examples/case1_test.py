"""Use cases test."""


import unittest


class WidgetTestCase(self):
    """Widget for test case."""

    def setUp(self):
        """Override setup method."""
        self.widget = Widget('The widget')

    def tearDown(self):
        """Teardown for widget."""
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong size after resize')


defaultSizeTestCase = WidgetTestCase('test_default_size')
resizeTestCase = WidgetTestCase('test_resize')


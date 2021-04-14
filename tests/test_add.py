import unittest

from example_python_proj import add


class AddTests(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(1+2, add(1, 2))

    def test_add_2(self):
        self.assertEqual(1+10, add(1, 10))


import unittest

from mojave import workingmojave

class TestStringifyBool(unittest.TestCase):
    def test_zero_zero_returns_true(self):
        self.assertEquals("true", workingmojave.stringify_bool(0, 0))

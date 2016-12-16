import unittest
import workingmojave




class TestStringifyBool(unittest.TestCase):

	def test_zero_zero_returns_true(self):

		self.assertEqual("true", workingmojave.stringify_bool(0, 0))

import unittest

from mojave import workingmojave


class TestStringifyBool(unittest.TestCase):
    def test_zero_zero_returns_true(self):
        self.assertEqual("true", workingmojave.stringify_bool(0, 0))

class Det_2x2_Tests(unittest.TestCase):
    def testing_det2x2_valid(self):
        self.assertEqual(-2, workingmojave.det2x2([3, 2, 4, 2]))
        self.assertEqual(0, workingmojave.det2x2([0, 0, 0, 0]))
        self.assertEqual(0, workingmojave.det2x2([-1, -1, -1, -1]))

    def testing_det2x2_invalid(self):
        self.assertEqual(None, workingmojave.det2x2(["carrot", "waffles", "donuts", "parrots"]))
        self.assertEqual(None, workingmojave.det2x2([2, 5, 2]))
        self.assertEqual(None, workingmojave.det2x2([2, 5,]))
        self.assertEqual(None, workingmojave.det2x2([2, ]))

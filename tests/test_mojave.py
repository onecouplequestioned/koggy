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


class Det_3x3_Tests(unittest.TestCase):
    def testing_det3x3_valid(self):
        self.assertEqual(44, workingmojave.det3x3([4, 2, 9, 2, 4, 4, 8, 4, 1]))
        self.assertEqual(0, workingmojave.det3x3([0, 0, 0, 0, 0, 0, 0, 0,0]))
        self.assertEqual(-24, workingmojave.det3x3([-2, -4, -7, -2, -3, -3, -6, -2, - 9]))


    def testing_det3x3_valid(self):
        self.assertEqual(None, workingmojave.det3x3(["barf", "tads", "shoes", "sonix", "fear", "beers", "wako", "loops", "shade"]))
        self.assertEqual(None, workingmojave.det3x3([0, 0, 0, 0, 0, 0, 0,]))
        self.assertEqual(None, workingmojave.det3x3([-2]))

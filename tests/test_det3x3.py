import unittest

from mojave import workingmojave


class Det_3x3_Tests(unittest.TestCase):
    def testing_det3x3_valid(self):
        self.assertEqual(44, workingmojave.det3x3([4, 2, 9, 2, 4, 4, 8, 4, 1]))
        self.assertEqual(0, workingmojave.det3x3([0, 0, 0, 0, 0, 0, 0, 0,0]))
        self.assertEqual(-24, workingmojave.det3x3([-2, -4, -7, -2, -3, -3, -6, -2, - 9]))


    def testing_det3x3_valid(self):
        self.assertEqual(None, workingmojave.det3x3(["barf", "tads", "shoes", "sonix", "fear", "beers", "wako", "loops", "shade"]))
        self.assertEqual(None, workingmojave.det3x3([0, 0, 0, 0, 0, 0, 0,]))
        self.assertEqual(None, workingmojave.det3x3([-2]))

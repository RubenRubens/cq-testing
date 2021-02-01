import unittest
from math import pi

class TestCutThruAll(unittest.TestCase):

    def test_C1(self):
        import src.cutThruAll.C1
        R = src.cutThruAll.C1.result
        self.assertTrue(R.val().isValid())

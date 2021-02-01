import unittest
from math import pi

class TestCutThruAll(unittest.TestCase):

    def test_C1(self):
        import cutThruAll.C1
        R = cutThruAll.C1.result
        self.assertTrue(R.val().isValid())

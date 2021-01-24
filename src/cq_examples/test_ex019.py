import unittest
import src.cq_examples.Ex018_Making_Lofts as ex

class TestExample018(unittest.TestCase):
    def test_Ex018(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

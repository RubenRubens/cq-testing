import unittest
import src.cq_examples.Ex007_Using_Point_Lists as ex

class TestExample007(unittest.TestCase):
    def test_Ex007(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

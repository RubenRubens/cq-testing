import unittest
import src.cq_examples.Ex010_Defining_an_Edge_with_a_Spline as ex

class TestExample010(unittest.TestCase):
    def test_Ex010(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

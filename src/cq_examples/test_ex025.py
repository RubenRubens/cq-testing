import unittest
import src.cq_examples.Ex024_Sweep_With_Multiple_Sections as ex

class TestExample024(unittest.TestCase):
    def test_Ex024(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

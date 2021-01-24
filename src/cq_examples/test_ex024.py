import unittest
import src.cq_examples.Ex023_Sweep as ex

class TestExample023(unittest.TestCase):
    def test_Ex023(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

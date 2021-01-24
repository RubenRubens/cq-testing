import unittest
import src.cq_examples.Ex022_Revolution as ex

class TestExample022(unittest.TestCase):
    def test_Ex022(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

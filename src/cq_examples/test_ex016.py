import unittest
import src.cq_examples.Ex016_Using_Construction_Geometry as ex

class TestExample016(unittest.TestCase):
    def test_Ex016(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

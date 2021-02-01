import unittest
import cq_examples.Ex008_Polygon_Creation as ex

class TestExample008(unittest.TestCase):
    def test_Ex008(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())

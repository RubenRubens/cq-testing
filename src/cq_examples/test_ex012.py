import unittest
import src.cq_examples.Ex011_Mirroring_Symmetric_Geometry as ex

class TestExample011(unittest.TestCase):
    def test_Ex011(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
